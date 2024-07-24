First, the things on the left of the screen are not part of the submission, because it said in the rules "you can't make your submission ahead of time", this page exists, I'll be summarizing the website as of today, and finally, I'll only show original math that I did.

## Calculus

$$ \frac{f(x + dx) - f(x)}{dx} = \frac{df}{dx} = f\prime (x) $$

### sum rule

$$ \vdots $$

$$ (f + g)\prime = f\prime + g\prime $$

### product rule

$$ \vdots $$

$$ (fg)\prime = fg\prime + f\prime g $$

### chain rule

$$ \vdots $$

$$ (f(g))\prime = f\prime(g) g\prime $$

### mbc rule

$$ \vdots $$

$$ (cf)\prime = c f\prime $$

### exponent rule

$$ \vdots $$

$$ \frac{d(a^x)}{dx} = a^x \frac{a^{dx} - 1}{dx} $$

$$ \text{(lets figure this out later!)} $$

### e

$$ \frac{de^x}{dx} = e^x $$

$$ \vdots $$

$$ e = (1 + dx)^{\frac{1}{dx}} $$

$$ log_e (x) = : ln(x) $$

### logarithmic derivitave

$$ \vdots $$

$$ (ln(f))\prime = \frac{f\prime}{f} $$

$$ f(x) = a^x $$

$$ \vdots $$

$$ (a^x)\prime = a^x ln(a) $$

### power rule

$$ f(x) = x^n $$

$$ \vdots $$

$$ (x^n)\prime = n x^{n - 1} $$

## Polynomial

Skipping this one, it's just [Mathologer](https://www.youtube.com/watch?v=N-KXStupwsc)

## Calculus II

### More about $e$

$$ e = \lim_{\Delta x \to 0} (1 + \Delta x)^{\frac{1}{\Delta x}} = \lim_{N \to \infty} (1 + \frac{1}{N})^N $$

$$ \vdots $$

$$ e^x = (1 + x dx)^{\frac{1}{dx}} $$

you will see why this is usefull [here](https://silaspe.github.io/maths/some4.html#proof).

### More about $e$ to the $x$

$$ \sum\limits_{n=0}^{\infty} C_n x^n = e^x $$

$$ \vdots $$

$$ \sum\limits_{n=0}^{\infty} C_n n x^{n - 1} = \sum\limits_{n=0}^{\infty} C_n x^n $$

$$ \vdots $$

$$ C_n = \frac{1}{n!} $$

$$ e^x = \sum\limits_{n=0}^{\infty}\frac{x^n}{n!} $$

$$ e = \sum\limits_{n=0}^{\infty}\frac{1}{n!} $$

### quoteint rule

$$ \vdots $$

$$ (\frac{f}{g})\prime = \frac{f\prime g - f g\prime}{g^2} $$

### L'Hopital's rule

$$ f(c) = 0 $$

$$ g(c) = 0 $$

$$ \lim_{x \to c} \frac{f(x)}{g(x)} = ? $$

$$ \vdots $$

$$ \lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{\frac{d}{dx} f(x)}{\frac{d}{dx} g(x)} $$
