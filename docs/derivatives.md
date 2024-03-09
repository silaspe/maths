## Derivatives

$$ \frac{f(x + dx) - f(x)}{dx} = \frac{df}{dx} = f\prime (x) $$

### sum rule

$$ \frac{d(f(x) + g(x))}{dx} = \frac{f(x + dx) + g(x + dx) - f(x) -g(x)}{dx} = \frac{f(x + dx) - f(x)}{dx} + \frac{g(x + dx) - g(x)}{dx} = \frac{df}{dx} + \frac{dg}{dx} $$

$$ \frac{d(f(x) + g(x))}{dx} = \frac{df}{dx} + \frac{dg}{dx} $$

$$ (f + g)\prime = f\prime + g\prime $$

### product rule

$$ f(x + dx) = f(x) + df $$

$$ \frac{d(f(x)g(x))}{dx} = \frac{(f(x) + df)(g(x) + dg) - f(x)g(x)}{dx} = \frac{f(x)g(x) + f(x)dg + dfg(x) + dfdg - f(x)g(x)}{dx} = f(x)\frac{dg}{dx} + \frac{df}{dx}g(x) + \frac{dfdg}{dx} $$

$$ \frac{dfdg}{dx} \to 0 $$

$$ \frac{d(f(x)g(x))}{dx} = f(x)\frac{dg}{dx} + \frac{df}{dx}g(x) $$

$$ (fg)\prime = fg\prime + f\prime g $$

### chain rule

$$ \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{df}{dx} (x) $$

$$ \Delta x \to 0 $$

$$ \frac{d(f(g(x)))}{dx} = \frac{f(g(x + dx)) - f(g(x))}{dx} = \frac{f(g(x) + dg) - f(g(x))}{dx} $$

$$ dg \to 0 $$

$$ \frac{f(g(x) + dg) - f(g(x))}{dg} = \frac{df}{dx}(g(x)) $$

$$ \frac{f(g(x) + dg) - f(g(x))}{dg}\frac{dg}{dx} $$

$$ = \frac{d(f(g(x)))}{dx} = \frac{df}{dx}(g(x))\frac{dg}{dx} $$

$$ (f(g))\prime = f\prime(g)g \prime $$

### mbc rule

$$ \frac{dcf(x)}{dx} = c f\prime(x) $$

$$ (cf)\prime = c f\prime $$

### exponent rule

$$ \frac{d(a^x)}{dx} = \frac{a^{x + dx} -a^x}{dx} = \frac{a^x a^{dx} - a^x}{dx} = a^x \frac{a^{dx} - 1}{dx} $$

$$ \frac{d(a^x)}{dx} = a^x \frac{a^{dx} - 1}{dx} $$

$$ \text{(lets figure this out later!)} $$

### e

$$ \frac{de^x}{dx} = e^x = e^x \frac{e^{dx} - 1}{dx} $$

$$ \frac{e^{dx} - 1}{dx} = 1 $$

$$ e^{dx} -1 = dx $$

$$ e^{dx} = 1 + dx $$

$$ e = (1 + dx)^{\frac{1}{dx}} $$

$$ log_e (x) = ln(x) $$

### logarithmic derivitave

$$ e^{ln(f(x))} = f(x) $$

$$ \frac{d(e^{ln(f(x)})}{dx} = (ln(f(x)))\prime e^{ln(f(x))} = f(x) (ln(f(x)))\prime = f\prime(x) $$

$$ (ln(f))\prime = \frac{f\prime}{f} $$

$$ f(x) = a^x $$

$$ ln(f(x)) = ln(a^x) = x ln(a) $$

$$ \frac{f\prime (x)}{f(x)} = ln(a) $$

$$ (a^x)\prime = a^x ln(a) $$

### power rule

$$ f(x) = x^n $$

$$ ln(f(x)) = ln(x^n) = n ln(x) $$

$$ ln\prime(x) = \frac{1}{x} $$

$$ \frac{f\prime(x)}{f(x)} = \frac{n}{x} $$

$$ (x^n)\prime = x^n \frac{n}{x} $$

$$ (x^n)\prime = n x^{n - 1} $$
