## $(1 + x)^n$

$$ (1 + x)^0 = 1 $$

$$ (1 + x)^1 = 1 + x $$

$$ (1 + x)^2 = 1 + 2x + x^2 $$

$$ (1 + x)^3 = 1 + 3x + 3x^2 + x^3 $$

$$ (1 + x)^n = \sum\limits_{k = 0}^{n} f(n, k) x^k = \sum\limits_{k = -\infty}^{\infty} f(n, k) x^k $$

$$ f(n, 0) = 1 $$

$$ f(n, k) = 0, $$

for $k$ bigger than $n$ or smaller than $0$

$$ (1 + x)^n = (1 + x) (1 + x)^{n - 1} = (1 + x) \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k = \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k + \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^{k + 1} = \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k +\sum\limits_{k = -\infty}^{\infty} f(n - 1, k - 1) x^k $$

$$ \sum\limits_{k = -\infty}^{\infty} f(n, k) x^k = \sum\limits_{k = -\infty}^{\infty} (f(n - 1, k) + f(n - 1, k - 1)) x^k $$

$$ f(n, k) = f(n - 1, k) + f(n - 1, k - 1) $$

### discrete calculus

$$ f(n, k) - f(n - 1, k) = f(n - 1, k - 1) $$

$$ \Delta f(x) = : f(x + 1) - f(x) $$

$$ x^{\frac{n}{}} = : \prod\limits_{k = x - n + 1}^{x} k = x \cdot (x - 1) \cdot (x - 2) ... \text{n times} = \frac{x!}{(x - n)!} $$

$$ \Delta x^{\frac{n}{}} = \frac{(x + 1)!}{(x - n + 1)!} - \frac{x!}{(x - n)!} = (x + 1) \frac{x!}{(x - n + 1)!} - \frac{x!}{\frac{(x - n + 1)!}{x - n + 1}} = (x + 1) x^{\frac{n - 1}{}} - (x - n + 1) x^{\frac{n - 1}{}} = x^{\frac{n - 1}{}} ((x + 1) - (x - n + 1)) $$

$$ \Delta x^{\frac{n}{}} = n x^{\frac{n - 1}{}} $$

$$ \Delta f(x, k) = f(x + 1, k) - f(x, k) = f((x + 1), k) - f((x + 1) - 1, k) = f((x + 1) - 1, k - 1) $$

$$ \Delta f(x, k) = f(x, k - 1) $$

$$ \Delta \frac{x^{\frac{n}{}}}{n!} = \frac{x^{\frac{n - 1}{}}}{(n - 1)!} $$

$$ f(x, k) = \frac{x^{\frac{k}{}}}{k!} = \frac{x!}{k!(x - k)!} = \begin{pmatrix} x \\
k \\ \end{pmatrix} $$

$$ (1 + x)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k = \sum\limits_{k = 0}^{\infty} \frac{n! x^k}{k!(n - k)!} $$

if $x$ is closer to $0$, than this will converge faster!

## $\pi$

$$ \pi = 2 \int_{-1}^{1} \sqrt{1 - x^2} dx = 4 \int_{0}^{1} \sqrt{1 - x^2} dx $$

but at $0$, this is $1$, and at $\frac{1}{2}$, this will converge really fast!

But

$$ \int_{0}^{\frac{1}{2}} \sqrt{1 - x^2} dx = \frac{\sqrt{3}}{8} + \frac{\pi}{12} $$

### $\sqrt{3}$

$$ \sqrt{3} = \sqrt{4 - 1} = \sqrt{4(1 - \frac{1}{4})} = 2 \sqrt{1 - \frac{1}{4}} = 2 (1 - \frac{1}{4})^{\frac{1}{2}} $$

which converges really fast!

thus...

$$ \pi = 12 ((\sum\limits_{k = 0}^{\infty} \frac{\begin{pmatrix} \frac{1}{2} \\
k \\ \end{pmatrix} (-\frac{1}{4})^{k + 1}}{k + 1}) - \frac{\sum\limits_{k = 0}^{\infty} \begin{pmatrix} \frac{1}{2} \\
k \\ \end{pmatrix} (-\frac{1}{4})^k}{4}) $$

where

$$ \begin{pmatrix} \frac{1}{2} \\
k \\ \end{pmatrix} = \frac{\prod\limits_{m = \frac{1}{2} - k + 1}^{\frac{1}{2}} m}{k!} = \frac{\prod\limits_{m = 1 - k}^{0} m + \frac{1}{2}}{k!} $$
