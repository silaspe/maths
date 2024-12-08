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
def compute_mandelbrot_numba(u, v, x_min, x_max, y_min, y_max, width, height, max_iterations, smooth_shading, offset_values):
    # Ensure inputs are float64 for compatibility
    u = u.astype(np.float64)
    v = v.astype(np.float64)
    x_min = float(x_min)
    x_max = float(x_max)
    y_min = float(y_min)
    y_max = float(y_max)
    width = int(width)
    height = int(height)

    # Precompute x and y grid values
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    # Precompute components based on u and v
    umag = np.sqrt(np.sum(u ** 2))  # |u| as sqrt(sum(u_i^2))
    uhat = u / umag                 # û (unit vector)
    
    # Manually compute the dot product using a loop
    valg = 0.0
    for i in range(len(v)):
        valg += v[i] * uhat[i]      # projection of v onto û

    vperp = v - valg * uhat         # perpendicular component of v
    vperp_norm = np.sqrt(np.sum(vperp ** 2)) + 1e-12  # Norm of vperp plus epsilon to avoid noise?

    # Change of basis (cob) matrix
    cob = np.array([[umag, valg],
                    [0, vperp_norm]])

    # Manually compute the determinant of cob
    det_cob = cob[0, 0] * cob[1, 1] - cob[0, 1] * cob[1, 0]

    # Print warning if determinant is too small
    if abs(det_cob) < 1e-8:
        print("Warning: cob matrix is nearly singular. Determinant:", det_cob)

    cobinv = np.array([[cob[1, 1], -cob[0, 1]],
                       [-cob[1, 0], cob[0, 0]]]) / det_cob


    # Combine u and v into a 2x2 matrix for transformation
    thirdeye = np.zeros((len(u), 2), dtype=np.float64)
    for i in range(len(u)):
        thirdeye[i, 0] = u[i]
        thirdeye[i, 1] = v[i]

    # Prepare Mandelbrot set array
    mandelbrot_set = np.zeros((height, width), dtype=np.float64)

    for i in range(height):
        for j in range(width):
            # Map p to (x[j], y[i]) using the transformation
            p = np.array([x[j], y[i]], dtype=np.float64)
            # Replace np.dot with manual matrix multiplication
            p_transformed = np.zeros(4)
            for k in range(4):
                for l in range(4):
                    p_transformed[k] += thirdeye[k, l] * p[l]
            z_real, z_imag, c_real, c_imag = p_transformed + offset_values  # Apply offset values

            iteration = 0

            # Mandelbrot iteration
            while z_real * z_real + z_imag * z_imag <= 4 and iteration < max_iterations:
                z_real_new = z_real * z_real - z_imag * z_imag + c_real
                z_imag = 2 * z_real * z_imag + c_imag
                z_real = z_real_new
                iteration += 1

            mandelbrot_set[i, j] = iteration

    # Apply smooth shading if enabled
    if smooth_shading:
        mandelbrot_set = np.log(mandelbrot_set + 1) / np.log(max_iterations)

    return mandelbrot_set, x, y


default_x_min, default_x_max = -2, .7
default_y_min, default_y_max = -.9, .9
default_width, default_height = 400, 400
default_max_iterations = 100

default_u = np.array([0, 0, 1, 0])
default_v = np.array([0, 0, 0, 1])
default_offset = np.array([0.0, 0.0, 0.0, 0.0])


app.layout = html.Div([
    html.H1("Interactive Mandelbrot Set with Offset and Smoothing Toggles", style={"text-align": "center"}),
    html.Div(
        style={
            "display": "flex",
            "flex-direction": "row",
            "align-items": "flex-start",
            "gap": "10px"
        },
        children=[
            dcc.Graph(
                id="mandelbrot-plot",
                config={"scrollZoom": True},
                style={"flex": "3", "margin-right": "0px"},
                figure=go.Figure()
            ),
            html.Div(
                style={
                    "flex": "1",
                    "max-width": "300px",
                    "display": "flex",
                    "flex-direction": "column",
                    "gap": "10px",
                    "padding": "10px",
                    "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.1)",
                    "background-color": "#f9f9f9",
                    "border-radius": "5px",
                    "overflow": "hidden"
                },
                children=[
                    html.Label("Resolution (Width x Height)"),
                    dcc.Slider(
                        id="resolution-slider",
                        min=10,
                        max=1000,
                        step=50,
                        value=400,
                        marks={i: f"{i}" for i in range(100, 1100, 100)},
                    ),
                    html.Label("Max Iterations"),
                    dcc.Slider(
                        id="iterations-slider",
                        min=0,
                        max=1000,
                        step=10,
                        value=default_max_iterations,
                        marks={i: str(i) for i in range(0, 1000, 100)},
                    ),
                    html.Label("u Vector Components"),
                    html.Div([
                        dcc.Input(id="ux", type="number", placeholder="ux", value=default_u[0], style={"width": "70px"}),
                        dcc.Input(id="uy", type="number", placeholder="uy", value=default_u[1], style={"width": "70px"}),
                        dcc.Input(id="uz", type="number", placeholder="uz", value=default_u[2], style={"width": "70px"}),
                        dcc.Input(id="uw", type="number", placeholder="uw", value=default_u[3], style={"width": "70px"}),
                    ], style={"display": "flex", "gap": "5px"}),

                    html.Label("v Vector Components"),
                    html.Div([
                        dcc.Input(id="vx", type="number", placeholder="vx", value=default_v[0], style={"width": "70px"}),
                        dcc.Input(id="vy", type="number", placeholder="vy", value=default_v[1], style={"width": "70px"}),
                        dcc.Input(id="vz", type="number", placeholder="vz", value=default_v[2], style={"width": "70px"}),
                        dcc.Input(id="vw", type="number", placeholder="vw", value=default_v[3], style={"width": "70px"}),
                    ], style={"display": "flex", "gap": "5px"}),
                    dcc.Checklist(
                        id="toggle-offset",
                        options=[{"label": "Show Offset Inputs", "value": "show"}],
                        value=[],
                        inline=True
                    ),
                    html.Div(
                        id="offset-inputs",
                        style={"display": "none"},
                        children=[
                            html.Label("Offset Values"),
                            html.Div([
                                dcc.Input(id="offset-z-real", type="number", placeholder="z_real offset", value=0, style={"width": "70px"}),
                                dcc.Input(id="offset-z-imag", type="number", placeholder="z_imag offset", value=0, style={"width": "70px"}),
                                dcc.Input(id="offset-c-real", type="number", placeholder="c_real offset", value=0, style={"width": "70px"}),
                                dcc.Input(id="offset-c-imag", type="number", placeholder="c_imag offset", value=0, style={"width": "70px"}),
                            ], style={"display": "flex", "gap": "5px"})
                        ]
                    ),
                    dcc.Checklist(
                        id="smooth-shading-toggle",
                        options=[{"label": "Smooth Shading", "value": "smooth"}],
                        value=["smooth"],
                        inline=True
                    )
                ]
            )
        ]
    )
])

@app.callback(
    Output("offset-inputs", "style"),
    Input("toggle-offset", "value")
)
def toggle_offset_div(toggle_value):
    if "show" in toggle_value:
        return {"display": "block"}  # Show the div
    return {"display": "none"}  # Hide the div


@app.callback(
    Output("mandelbrot-plot", "figure"),
    [
        Input("resolution-slider", "value"),
        Input("iterations-slider", "value"),
        Input("ux", "value"),
        Input("uy", "value"),
        Input("uz", "value"),
        Input("uw", "value"),
        Input("vx", "value"),
        Input("vy", "value"),
        Input("vz", "value"),
        Input("vw", "value"),
        Input("toggle-offset", "value"),
        Input("offset-z-real", "value"),
        Input("offset-z-imag", "value"),
        Input("offset-c-real", "value"),
        Input("offset-c-imag", "value"),
        Input("smooth-shading-toggle", "value"),
        Input("mandelbrot-plot", "relayoutData")
    ]
)
def update_mandelbrot(resolution, max_iterations, ux, uy, uz, uw, vx, vy, vz, vw, toggle_offset, offset_z_real, offset_z_imag, offset_c_real, offset_c_imag, smooth_shading_toggle, relayout_data):
    width, height = resolution, resolution

    u = np.array([ux, uy, uz, uw])
    v = np.array([vx, vy, vz, vw])

    # Get offsets
    offset_values = np.array([offset_z_real, offset_z_imag, offset_c_real, offset_c_imag]) if "show" in toggle_offset else default_offset

    # Default ranges
    x_min, x_max = default_x_min, default_x_max
    y_min, y_max = default_y_min, default_y_max

    # Update ranges based on relayoutData
    if relayout_data:
        x_min = relayout_data.get("xaxis.range[0]", x_min)
        x_max = relayout_data.get("xaxis.range[1]", x_max)
        y_min = relayout_data.get("yaxis.range[0]", y_min)
        y_max = relayout_data.get("yaxis.range[1]", y_max)

    if np.all(u == 0) or np.all(v == 0):
        return go.Figure()

    smooth_shading = "smooth" in smooth_shading_toggle

    updated_mandelbrot, x_values, y_values = compute_mandelbrot_numba(
        u, v, x_min, x_max, y_min, y_max, width, height, max_iterations, smooth_shading, offset_values
    )

    figure = go.Figure(data=go.Heatmap(
        z=updated_mandelbrot,
        x=x_values,
        y=y_values,
        zmin=0,  # Set the colormap range to [0, 1]
        zmax=1,
        colorscale="Greys" if smooth_shading else [[0, "black"], [1, "white"]],
        showscale=False,
    )).update_layout(
        title=f"Mandelbrot Set (Max Iterations: {max_iterations})",
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis=dict(scaleanchor="y", range=[x_min, x_max], showgrid=False, showticklabels=False, ticks=""),
        yaxis=dict(range=[y_min, y_max], showgrid=False, showticklabels=False, ticks=""),
        width=800,  # Wider than height for a rectangular plot
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white",
        uirevision="constant"  # Prevent layout resetting on update
    )
    return figure



if __name__ == "__main__":
    app.run_server(debug=True)
