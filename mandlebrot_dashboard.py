try:
    import numpy as np
    from numba import njit
    import plotly.graph_objects as go
    from dash import Dash, dcc, html, Input, Output, State
except ImportError as e:
    missing_module = str(e).split("'")[1]
    print(f"Error: Missing module '{missing_module}'.")

    print("\nPlease install the required dependencies using pip or conda:")
    print("  Using pip:")
    print("    pip install numpy numba plotly dash")
    print("\n  Using conda:")
    print("    conda install -c conda-forge numpy numba plotly dash")
    
    # Exit the program if imports fail
    import sys
    sys.exit(1)


# Initialize the Dash app
app = Dash(__name__)

@njit
def compute_mandelbrot_numba(x_min, x_max, y_min, y_max, width, height, max_iterations, smooth_shading=False, start_at_one=False):
    x = np.empty(width, dtype=np.float64)
    y = np.empty(height, dtype=np.float64)
    for i in range(width):
        x[i] = x_min + i * (x_max - x_min) / (width - 1)
    for j in range(height):
        y[j] = y_min + j * (y_max - y_min) / (height - 1)

    mandelbrot_set = np.zeros((height, width), dtype=np.float64)

    for i in range(height):
        for j in range(width):
            real = x[j]
            imag = y[i]
            # Initialize based on the toggle
            z_real = 1.0 if start_at_one else 0.0
            z_imag = 0.0
            c_real = real
            c_imag = imag
            iteration = 0

            while z_real * z_real + z_imag * z_imag <= 4 and iteration < max_iterations:
                z_real_new = z_real * z_real - z_imag * z_imag + c_real
                z_imag = 2 * z_real * z_imag + c_imag
                z_real = z_real_new
                iteration += 1

            mandelbrot_set[i, j] = iteration

    if smooth_shading:
        mandelbrot_set = np.log(mandelbrot_set + 1) / np.log(max_iterations)

    return mandelbrot_set, x, y


default_x_min, default_x_max = -2, .7
default_y_min, default_y_max = -.9, .9
default_width, default_height = 400, 400
default_max_iterations = 100

binary_mandelbrot, x_values, y_values = compute_mandelbrot_numba(
    default_x_min, default_x_max, default_y_min, default_y_max,
    default_width, default_height, default_max_iterations
)

app.layout = html.Div([
    html.H1("Interactive Mandelbrot Set (Numba Optimized)", style={"text-align": "center"}),
    html.Div(
        style={
            "display": "flex",
            "flex-direction": "row",
            "align-items": "start",  # Align the top edges
            "gap": "10px"  # Reduce gap between the graph and tools
        },
        children=[
            # Graph in the left column
            dcc.Graph(
                id="mandelbrot-plot",
                config={"scrollZoom": True},
                style={"flex": "3", "margin-right": "0px"},  # Remove extra margin
                figure=go.Figure()
            ),
            # Controls in the right column
            html.Div(
                style={
                    "flex": "1",
                    "display": "flex",
                    "flex-direction": "column",
                    "gap": "5px",  # Minimize spacing between tools
                    "padding": "5px",  # Add slight padding for aesthetics
                    "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.1)",  # Add a subtle shadow
                    "background-color": "#f9f9f9",  # Light background for the tools
                    "border-radius": "5px"  # Slight border rounding for a polished look
                },
                children=[
                    html.Label("Resolution (Width x Height)"),
                    dcc.Slider(
                        id="resolution-slider",
                        min=100,
                        max=1000,
                        step=50,
                        value=400,
                        marks={i: f"{i}" for i in range(100, 1100, 100)},
                    ),
                    html.Label("Max Iterations"),
                    dcc.Slider(
                        id="iterations-slider",
                        min=10,
                        max=1000,
                        step=10,
                        value=default_max_iterations,
                        marks={i: str(i) for i in range(10, 1100, 100)},
                    ),
                    html.Label("Display Mode"),
                    dcc.Checklist(
                        id="display-mode",
                        options=[{"label": "Smooth Shading", "value": "smooth"}],
                        value=[],
                        inline=True
                    ),
                    html.Label("Start at 1"),
                    dcc.Checklist(
                        id="start-at-one",
                        options=[{"label": "Enable", "value": "start_one"}],
                        value=[],
                        inline=True
                    )
                ]
            )
        ]
    )
])



@app.callback(
    Output("mandelbrot-plot", "figure"),
    [Input("resolution-slider", "value"),
     Input("iterations-slider", "value"),
     Input("display-mode", "value"),
     Input("start-at-one", "value"),
     Input("mandelbrot-plot", "relayoutData")],
    [State("mandelbrot-plot", "figure")]
)
def update_mandelbrot(resolution, max_iterations, display_mode, start_at_one, relayout_data, figure):
    width, height = resolution, resolution  # Set width and height equal

    # Use default ranges if figure or relayoutData is uninitialized
    x_min = default_x_min
    x_max = default_x_max
    y_min = default_y_min
    y_max = default_y_max

    # Extract ranges from the figure layout if available
    if figure and "layout" in figure:
        x_min = figure.get("layout", {}).get("xaxis", {}).get("range", [default_x_min, default_x_max])[0]
        x_max = figure.get("layout", {}).get("xaxis", {}).get("range", [default_x_min, default_x_max])[1]
        y_min = figure.get("layout", {}).get("yaxis", {}).get("range", [default_y_min, default_y_max])[0]
        y_max = figure.get("layout", {}).get("yaxis", {}).get("range", [default_y_min, default_y_max])[1]

    # Update ranges if relayoutData is available
    if relayout_data:
        if "xaxis.range[0]" in relayout_data:
            x_min = relayout_data["xaxis.range[0]"]
            x_max = relayout_data["xaxis.range[1]"]
        if "yaxis.range[0]" in relayout_data:
            y_min = relayout_data["yaxis.range[0]"]
            y_max = relayout_data["yaxis.range[1]"]

    # Check the toggle for starting at 1
    start_at_one_flag = "start_one" in start_at_one
    smooth_shading = "smooth" in display_mode

    # Compute the Mandelbrot set
    updated_mandelbrot, x_values, y_values = compute_mandelbrot_numba(
        x_min, x_max, y_min, y_max, width, height, max_iterations, smooth_shading, start_at_one_flag
    )

    if not smooth_shading:
        updated_mandelbrot = (updated_mandelbrot < max_iterations).astype(int)


    figure = go.Figure(data=go.Heatmap(
        z=updated_mandelbrot,
        x=x_values,
        y=y_values,
        colorscale="Greys" if smooth_shading else [[0, "black"], [1, "white"]],
        showscale=False,
    )).update_layout(
        title=f"Mandelbrot Set (Max Iterations: {max_iterations})",
        margin=dict(l=10, r=10, t=30, b=10),  # Minimized margins
        xaxis=dict(
            scaleanchor="y",
            range=[x_min, x_max],
            showgrid=False,
            showticklabels=False,  # Remove tick labels
            ticks=""  # Remove ticks
        ),
        yaxis=dict(
            range=[y_min, y_max],
            showgrid=False,
            showticklabels=False,  # Remove tick labels
            ticks=""  # Remove ticks
        ),
        width=800,  # Reduced width
        height=500,  # Reduced height
        paper_bgcolor="white",
        plot_bgcolor="white",
        uirevision="constant"
    )
    return figure




if __name__ == "__main__":
    app.run_server(debug=True)

