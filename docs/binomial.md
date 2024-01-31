## $(1 + x)^n$

$$ (1 + x)^0 = 1 $$

$$ (1 + x)^1 = 1 + x $$

$$ (1 + x)^2 = 1 + 2x + x^2 $$

$$ (1 + x)^3 = 1 + 3x + 3x^2 +  x^3 $$

$$ (1 + x)^n = \sum\limits_{k = 0}^{n} f(n, k) x^k = \sum\limits_{k = -\infty}^{\infty} f(n, k) x^k $$

$$ f(n, 0) = 1 $$

$$ f(n, k) = 0 \quad for \quad k \quad bigger \quad than \quad n \quad or \quad smaller \quad than \quad 0 $$

$$ (1 + x)^n = (1 + x) (1 + x)^{n - 1} = (1 + x) \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k = \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k + \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^{k + 1} = \sum\limits_{k = -\infty}^{\infty} f(n - 1, k) x^k +\sum\limits_{k = -\infty}^{\infty} f(n - 1, k - 1) x^k $$

$$ \sum\limits_{k = -\infty}^{\infty} f(n, k) x^k = \sum\limits_{k = -\infty}^{\infty} (f(n - 1, k) + f(n - 1, k - 1)) x^k $$

$$ f(n, k) = f(n - 1, k) + f(n - 1, k - 1) $$

### discrete calculus

$$ f(n, k) - f(n - 1, k) = f(n - 1, k - 1) $$

$$ \Delta f(x) = : f(x + 1) - f(x) $$

$$ x^{\frac{n}{}} = : \prod\limits_{k = x - n + 1}^{x} k = x \cdot (x - 1) \cdot (x - 2) ... \quad n \quad times = \frac{x!}{(x - n)!} $$

$$ \Delta x^{\frac{n}{}} = \frac{(x + 1)!}{(x - n + 1)!} - \frac{x!}{(x - n)!} = (x + 1) \frac{x!}{(x - n + 1)!} - \frac{x!}{\frac{(x - n + 1)!}{x - n + 1}} = (x + 1) x^{\frac{n - 1}{}} - (x - n + 1) x^{\frac{n - 1}{}} = x^{\frac{n - 1}{}} ((x + 1) - (x - n + 1)) $$

$$ \Delta x^{\frac{n}{}} = n x^{\frac{n - 1}{}} $$

$$ \Delta f(x, k) = f(x + 1, k) - f(x, k) = f((x + 1), k) - f((x + 1) - 1, k) = f((x + 1) - 1, k - 1) $$

$$ \Delta f(x, k) = f(x, k - 1) $$

$$ \Delta \frac{x^{\frac{n}{}}}{n!} = \frac{x^{\frac{n - 1}{}}}{(n - 1)!} $$

$$ f(x, k) = \frac{x^{\frac{n}{}}}{n!} = \frac{x!}{n!(x - n)!} = \begin{pmatrix} n \\
k \\ \end{pmatrix} $$

$$ (1 + x)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k = \sum\limits_{k = 0}^{\infty} \frac{n! x^k}{k!(n - k)!} $$