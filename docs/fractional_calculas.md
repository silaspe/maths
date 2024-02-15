## $\frac{calculas}{2}$

$$ \frac{d^{\frac{1}{2}}}{dx^{\frac{1}{2}}} f(x) = ? $$

$$ f(x) = x^n $$

$$ \frac{d}{dx} x^n = n x^{n - 1} $$

$$ \frac{d^2}{dx^2} x^n = n (n - 1) x^{n - 2} $$

$$ \vdots $$

$$ \frac{d^k}{dx^k} x^n = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot (n - k + 1) x^{n - k} = \frac{n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 1 x^{n - k}}{(n - k) \cdot (n - k - 1) \cdot (n - k - 2) \cdot ... \cdot 1} $$

$$ \frac{d^k}{dx^k} x^n = \frac{n! x^{n - k}}{(n - k)!} $$

$$ \frac{d^p}{dx^p} x^n = \frac{n! x^{n - p}}{(n - p)!} $$

$$ where \quad (n - p)! = : \int_{0}^{\infty} t^{n - p} e^{-t} dt $$

### $\quad_p \int_{0}^{x}$

$$ \int f(x) dx = \int_{0}^{x} f(t) dt $$

$$ \int \int f(x) dx^2 = ? = \quad_2 \int f(x) dx $$

$$ ? = \int_{0}^{x} \int_{0}^{y} f(t) dt dy $$

$$ ! = \int_{0}^{x} (x - t) f(t) dt = \int_{0}^{x} (x f(t) - t f(t)) dt = \int_{0}^{x} \int_{t}^{x} f(t) dy dt $$
