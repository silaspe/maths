## n!

$$ n! = ? $$

$$ n! = n(n - 1)(n - 2)... 1 $$

$$ \frac{d}{dx} x^n = n x^{n - 1} $$

$$ \frac{d^2}{dx^2} x^n = n(n - 1) x^{n - 2} $$

$$ \frac{d^a}{dx^a} x^n = \frac{n! x^{n - a}}{(n - a)!} $$

$$ \frac{d^n}{dx^n} x^n = \frac{n! x^{n - n}}{(n - n)!} = n! $$

$$ \frac{d^n}{dx^n} \frac{1}{x} = \frac{(-1)^n n!}{x^{n - 1}} $$

$$ \frac{d^n}{dx^n} (-\frac{1}{x}) = \frac{n!}{(-x)^{n + 1}} $$

$\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$  if $\frac{n!}{(-x)^{n + 1}}$ is a function of x and x can be a constant then $\frac{d^n}{dx^n} (-\frac{1}{x})$ is not. so $\frac{n!}{(-x)^{n + 1}}$ at $x = -1$ is $n!$

$\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ problem solved!... but that is a bit too many derivitaves...

$\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ $\quad$ so an example of something easy to differentiate is $e^x$

$$ \frac{d}{dx} e^x = e^x $$

$$ \frac{\partial}{\partial t} e^{xt} = x e^{xt} $$

$$ \frac{d}{dx} (\int f(x) dx) = : f(x) $$

$$ \int_{a}^{b} f(x) dx = : \int f(b) - \int f(a) $$

$$ \int{0}^{\infty} f(x) dx = : (\lim_{x \to \infty} f(x)) - f(0) $$

$$ \int e^{xt} dt = \frac{e^{xt}}{x} $$

$$ \int_{0}^{\infty} e^{xt} dt = \frac{e^{\infty x}}{x} - e^{0x} = -\frac{1}{x}, x<0 $$

$$ \frac{d^n}{dx^n} \int_{0}^{\infty} e^{xt} dt = \frac{d^n}{dx^n} (-\frac{1}{x}), x<0 $$

$$ \int_{0}^{\infty} \frac{\partial^n}{\partial x^n} e^{xt} dt = \frac{n!}{(-x)^{n + 1}}, x<0 $$

$$ \int_{0}^{\infty} t^n e^{xt} dt = \frac{n!}{(-x)^{n + 1}}, x<0 $$

$$ \int_{0}^{\infty} t^n e^{-t} dt = n! $$

$$ \Gamma (x) = : \int_{0}^{\infty} t^{n - 1} e^{-t} dt $$

problem solved! but this has no constraint that $n$ is an integer, so I will use $x$ now that it is freed up from the formula, and the factorial has its own definition so the formula has been demoted to $\Gamma (x + 1)$
