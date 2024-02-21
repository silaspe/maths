## $\frac{calculas}{2}$

$$ \frac{d^{\frac{1}{2}}}{dx^{\frac{1}{2}}} f(x) = ? $$

$$ f(x) = x^n $$

$$ \frac{d}{dx} x^n = n x^{n - 1} $$

$$ \frac{d^2}{dx^2} x^n = n (n - 1) x^{n - 2} $$

$$ \vdots $$

$$ \frac{d^k}{dx^k} x^n = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot (n - k + 1) x^{n - k} = \frac{n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 1 x^{n - k}}{(n - k) \cdot (n - k - 1) \cdot (n - k - 2) \cdot ... \cdot 1} $$

$$ \frac{d^k}{dx^k} x^n = \frac{n! x^{n - k}}{(n - k)!} $$

$$ \frac{d^p}{dx^p} x^n = \frac{n! x^{n - p}}{(n - p)!} $$

$$ \text{where } (n - p)! = : \int_{0}^{\infty} t^{n - p} e^{-t} dt $$

### $\quad_2 \int_{0}^{x}$

$$ \int f(x) dx = \int_{0}^{x} f(t) dt $$

$$ \int \int f(x) dx^2 = ? = \quad_2 \int_{0}^{x} f(t) dt^2 $$

$$ ? = \int_{0}^{x} \int_{0}^{y} f(t) dt dy $$

$$ \frac{d^2}{dx^2} ? = \frac{\partial^2}{\partial x^2} ? = : f(x) $$

$$ ! = \int_{0}^{x} (x - t) f(t) dt = \int_{0}^{x} g(x, t) dt $$

$$ g(x, t) = (x - t) f(t) $$

$$ \frac{\partial}{\partial x} ! = \frac{\partial}{\partial x} \int_{0}^{x} g(x, t) dt = \frac{\int_{0}^{x + dx} g(x + dx, t) dt - \int_{0}^{x} g(x, t) dt}{dx} = \frac{\int_{0}^{x} g(x + dx, t) dt - \int_{0}^{x} g(x, t) dt + g(x + dx, x + dx) dt}{dx} = \frac{\int_{0}^{x} g(x + dx, t) dt - \int_{0}^{x} g(x, t) dt}{dx} + \frac{g(x + dx, x + dx) dt}{dx} = \int_{0}^{x} \frac{g(x + dx, t) - g(x, t)}{dx} dt + \frac{(x + dx - x - dx) f(t) dt}{dx} = \int_{0}^{x} \frac{\partial}{\partial x} g(x, t) dt $$

$$ \frac{\partial}{\partial x} g(x, t) = \frac{\partial}{\partial x} (x - t) f(t) = f(t) $$

$$ \frac{\partial}{\partial x} ! = \int_{0}^{x} f(t) dt $$

$$ \frac{\partial^2}{\partial x^2} ! = f(x) $$

$$ ? = \text{ } !  $$

$$ \quad_2 \int_{0}^{x} f(t) dt^2 = \int_{0}^{x} (x - t) f(t) dt $$

$$ \quad_2 \int_{0}^{x} f(t) dt^2 - \quad_2 \int_{0}^{a} f(t) dt^2 = \int_{0}^{x} (x - t) f(t) dt - \int_{0}^{a} (x - t) f(t) dt $$

$$ \quad_2 \int_{a} f(x) dx^2 = \int_{a}^{x} (x - t) f(t) dt $$

### $\quad_3 \int_{a}^{x}$

$$ \quad_3 \int_{a}^{x} f(t) dt^3 = \quad_2 \int_{a}^{x} \int_{a}^{t} f(s) ds dt^2 = \int_{a}^{x} (x - t) \int_{a}^{t} f(s) ds dt $$

$$ (uv) \prime = u v \prime + u \prime v $$

$$ \int (uv) \prime dx = \int u v \prime dx + \int u \prime v dx $$

$$ uv = \int u \frac{dv}{dx} dx + \int \frac{du}{dx} v dx $$

$$ uv = \int u dv + \int du v $$

$$ \int u dv = uv - \int du v $$

$$ u = \int_{a}^{t} f(s) ds $$

$$ dv = (x - t) dt $$

$$ du = f(t) dt $$

$$ v = - \frac{1}{2} (x - t)^2 $$

$$ \quad_3 \int_{a}^{x} f(t) dt^3 = \int_{t=a}^{x} u dv = [uv]_ {t=a}^{x} - \int_{a}^{x} - \frac{1}{2} (x - t)^2 f(t) dt = [- \frac{1}{2} (x - t)^2 \int_{a}^{t} f(s) ds]_ {t=a}^{x} + \int_{a}^{x} - \frac{1}{2} (x - t)^2 f(t) dt = (- \frac{1}{2} (x - a)^2 \int_{a}^{a} f(s) ds) - (- \frac{1}{2} (x - x)^2 \int_{a}^{x} f(s) ds) + \int_{a}^{x} \frac{1}{2} (x - t)^2 f(t) dt $$

$$ \quad_3 \int_{a} f(x) dx^3 = \frac{1}{2} \int_{a}^{x} (x - t)^2 f(t) dt $$

### $\quad_p \int_{a}^{x}$

$$ \vdots $$

$$ \quad_n \int_{a}^{x} f(t) dt = \int_{a}^{x} g(x, t, n) f(t) dt $$

$$ \quad_{n + 1} \int_{a}^{x} f(t) dt^{n + 1} = \quad_n \int_{a}^{x} \int_{a}^{t} f(s) ds dt^n = \int_{a}^{x} g(x, t, n) \int_{a}^{t} f(s) ds dt $$

$$ u = \int_{a}^{t} f(s) ds $$

$$ dv = g(x, t, n) dt $$

$$ du = f(t) dt $$

$$ v \quad ? = ? \quad - g(x, t, n + 1) $$

$$ \quad_{n + 1} \int_{a}^{x} f(t) dt^{n + 1} = \int_{t=a}^{x} u dv = [uv]_ {t=a}^{x} - \int_{a}^{x} - g(x, t, n + 1) f(t) dt = [- g(x, t, n + 1) \int_{a}^{t} f(s) ds]_ {t=a}^{x} + \int_{a}^{x} g(x, t, n + 1) f(t) dt = (- g(x, a, n + 1) \int_{a}^{a} f(s) ds) - (- g(x, x, n + 1) \int_{a}^{x} f(s) ds) + \int_{a}^{x} g(x, t, n + 1) f(t) dt = \int_{a}^{x} g(x, t, n + 1) f(t) dt + g(x, x, n + 1) \int_{a}^{x} f(s) ds = \int_{a}^{x} g(x, t, n + 1) f(t) dt $$

$$ g(x, x, n + 1) = 0 \text{AND} \frac{d}{dt} g(x, t, n + 1) = - g(x, t, n) \Rightarrow v = - g(x, t, n + 1) $$

$$ \frac{1}{n!} (x - x)^n = 0 $$

$$ \frac{d}{dt} \frac{1}{n!} (x - t)^n = - \frac{1}{n} n (x - t)^{n - 1} = - \frac{1}{(n - 1)!} (x - t)^{n - 1} $$

$$ g(x, t, 2) = x - t $$

$$ \frac{1}{(2 - 1)!} (x - t)^{2 - 1} = x - t $$

$$ g(x, t, n) = \frac{1}{(n - 1)!} (x - t)^{n - 1} $$

$$ \quad_n \int_{a} f(x) dx^n = \frac{1}{(n - 1)!} \int_{a}^{x} (x - t)^{n - 1} f(t) dt $$

$$ \quad_n \int_{a} f(x) dx^n = \frac{1}{\Gamma (n)} \int_{a}^{x} (x - t)^{n - 1} f(t) dt $$

[(this is Gamma)](https://silaspe.github.io/maths/gamma.html)

$$ \quad_\frac{1}{2} \int_{a} f(x) dx^{\frac{1}{2}} = : \frac{1}{\Gamma (\frac{1}{2})} \int_{a}^{x} (x - t)^{n - 1} f(t) dt = \frac{1}{\sqrt{\pi}} \int_{a}^{x} (x - t)^{n - 1} f(t) dt $$

### differintegral (not derivigral)

$$ \frac{d^{\frac{1}{2}}}{dx^{\frac{1}{2}}} f(x) = : \frac{d}{dx} \frac{1}{\sqrt{\pi}} \int_{a}^{x} (x - t)^{n - 1} f(t) dt $$

$$ \frac{d^p}{dx^p} f(x) = : \begin{Bmatrix} p = 0 : f(x) \\
p \text{ is an integer and greater than } 0 : \frac{d^p}{dx^p} f(x) \\
p \text{ is an integer and less than } 0 : \frac{1}{(|p| - 1)!} \int_{a}^{x} (x - t)^{|p| - 1} f(t) dt \\
p < 0 : \frac{1}{\Gamma (|p|)} \int_{a}^{x} (x - t)^{|p| - 1} f(t) dt \\
p > 0 : \frac{d^k}{dx^k} (\frac{1}{\Gamma (\alpha)} \int_{a}^{x} (x - t)^{\alpha - 1} f(t) dt)  \\
\text{where } p + \alpha = \text{integer } k \\ \end{Bmatrix} $$

and here's a graph!

<iframe src="https://www.desmos.com/calculator/uypsj28ndo?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

the calculator could not take derivitaves of fractional integrals, so I used the limit definition of the derivitave and sadly, that is why  you can only go from $-1$ to $1$
