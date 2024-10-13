## More about $e$

$$ e = (1 + dx)^{\frac{1}{dx}} = \lim_{\Delta x \to 0} (1 + \Delta x)^{\frac{1}{\Delta x}} = \lim_{N \to \infty} (1 + \frac{1}{N})^N $$

$$ e^x = \lim_{N \to \infty} (1 + \frac{1}{N})^{Nx} = \lim_{N \to \infty} (1 + \frac{x}{Nx})^{Nx} $$

$$ Nx \to \infty $$

$$ N \to \infty $$

$$ e^x = \lim_{N \to \infty} (1 + \frac{x}{N})^{N} $$

$$ e^x = (1 + x dx)^{\frac{1}{dx}} $$

you will see why this is useful [here](https://silaspe.github.io/maths/complex.html#proof)

$$ \sum\limits_{n=0}^{\infty}C_n x^n = e^x $$

$$ \sum\limits_{n=0}^{\infty}C_n n x^{n - 1} = e^x = \sum\limits_{n=0}^{\infty}C_n x^n $$

$$ \sum\limits_{n=0}^{\infty}C_n n x^{n - 1} = \sum\limits_{n=-1}^{\infty}C_{n + 1} (n + 1) x^n = c_0 0 x^{-1} + \sum\limits_{n=0}^{\infty}C_{n + 1} (n + 1) x^n = \sum\limits_{n=0}^{\infty}C_n x^n $$

### More about $e$ to the $x$

$$ C_{n + 1} (n + 1) = C_n $$

$$ C_{n + 1} = \frac{C_n}{n + 1} $$

$$ C_n = \frac{C_{n - 1}}{n} $$

$$ e^0 = 1 $$

$$ C_0 = 1 $$

$$ C_n = \frac{1}{n!} $$

$$ e^x = \sum\limits_{n=0}^{\infty}\frac{x^n}{n!} $$

$$ e = \sum\limits_{n=0}^{\infty}\frac{1}{n!} $$

$$ \sum\limits_{n=0}^{\infty}C_n x^n = e^x $$

$$ \sum\limits_{n=0}^{\infty}C_n n x^{n - 1} = e^x = \sum\limits_{n=0}^{\infty}C_n x^n $$

$$ \sum\limits_{n=0}^{\infty}C_n n x^{n - 1} = \sum\limits_{n=-1}^{\infty}C_{n + 1} (n + 1) x^n = c_0 0 x^{-1} + \sum\limits_{n=0}^{\infty}C_{n + 1} (n + 1) x^n = \sum\limits_{n=0}^{\infty}C_n x^n $$

$$ C_{n + 1} (n + 1) = C_n $$

$$ C_{n + 1} = \frac{C_n}{n + 1} $$

$$ C_n = \frac{C_{n - 1}}{n} $$

$$ e^0 = 1 $$

$$ C_0 = 1 $$

$$ C_n = \frac{1}{n!} $$

$$ e^x = \sum\limits_{n=0}^{\infty}\frac{x^n}{n!} $$

### quotient rule

$$ (\frac{f}{g})\prime = ? $$

$$ \frac{f(x)}{g(x)} = h(x) $$

$$ g(x) h(x) = f(x) $$

$$ (g(x) h(x))\prime = f\prime (x) $$

$$ g\prime (x) h(x) + g(x) h\prime (x) = f\prime (x) $$

$$ g(x) h\prime (x) = f\prime (x) - g\prime (x) h(x) $$

$$ g(x) h\prime (x) = f\prime (x) - g\prime (x) \frac{f(x)}{g(x)} $$

$$ g(x) h\prime (x) = f\prime (x) - \frac{f(x) g\prime(x)}{g(x)} $$

$$ g(x) h\prime (x) = \frac{f\prime (x) g(x)}{g(x)} - \frac{f(x) g\prime (x)}{g(x)} $$

$$ g(x) h\prime (x) = \frac{f\prime (x) g(x) - f(x) g\prime (x)}{g(x)} $$

$$ h\prime (x) = \frac{f\prime (x) g(x) - f(x) g\prime (x)}{g^2(x)} $$

$$ (\frac{f}{g})\prime = \frac{f\prime g - f g\prime}{g^2} $$

### L'Hopital's rule

$$ f(c) = 0 $$

$$ g(c) = 0 $$

$$ ? = \lim_{x \to c} \frac{f(x)}{g(x)} = \frac{f(c + dx)}{g(c + dx)} = \frac{f(c) + df_c}{g(c) + dg_c} = \frac{df_c}{dg_c} = \frac{\frac{df_c}{dc}}{\frac{dg_c}{dc}} $$

$$ \lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{\frac{d}{dx} f(x)}{\frac{d}{dx} g(x)} $$
