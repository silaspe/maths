## Harmonic

i'm going to start with the alternating harmonic seireis $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} ...$

then, for example $- \frac{1}{4} = \frac{1}{4} - \frac{1}{2}$

then, the original seireis is equal to $1 + \frac{1}{2} - 1 + \frac{1}{3} + \frac{1}{4} - \frac{1}{2} ...$

also, I will call the total sum "?"

now, let me define $f(n)$ as $f(1) = 1$ and $f(2) = 1 + \frac{1}{2} - 1 + \frac{1}{3} = \frac{1}{2} + \frac{1}{3}$ than $f(3)$ equals the next few terms, so $\frac{1}{3} + \frac{1}{4} + \frac{1}{5}$

in genaral, $f(n)$ = $\frac{1}{n} + \frac{1}{n + 1} + ...$ with n terms OR $\frac{1}{n} + \frac{1}{n} + ... + \frac{1}{2n - 1}$

but than $f(\infty) = ?$

$f(n,x) = \frac{1}{n} + \frac{1}{n + 1} + ... + \frac{1}{xn - 1}$ $x$ as $\frac{integer}{n}$ for integer n

$f(n,x + \frac{1}{n}) - f(n,x) = \frac{1}{xn}$

$n(f(n,x + \frac{1}{n}) - f(n,x)) = \frac{1}{x}$

as $n \to \infty$ $\frac{1}{n} \to 0$ and $x$ could be anything AND the previous expression equals $\frac{df(\infty,x)}{dx}$

but $ln \prime(x) = \frac{1}{x}$ and $ln(1) = 0$ AND $f(\infty,1) = \frac{1}{1 + \infty} = 0$

therefore $f(\infty,x) = ln(x)$

but $f(n,2) = f(n)$ and $? = f(\infty)$

so, $? = f(\infty,2) = ln(2)$

so $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5}$ FOREVER $ = ln(2)$

yay!

### regular harmonic

Now I'll start with a seiries like $1 + \frac{1}{2} + \frac{1}{3} - 1 + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} - \frac{1}{2}$ is $f(\infty, 3)$, so ln(3)

the simpler $1 + \frac{1}{2} + \frac{1}{3} - 1 - \frac{1}{2} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} - \frac{1}{3} - \frac{1}{4}$, if you don't get it, its 3 positave 2 negatave.

for the same reasons as before, this equals (remember that $n \to \infty$ in the following) $\frac{1}{2n} + \frac{1}{2n + 1} + ... + \frac{1}{3n - 1}$, so $(\frac{1}{n} + \frac{1}{n + 1} + ... + \frac{1}{3n - 1}) - (\frac{1}{n} + \frac{1}{n + 1} + ... + \frac{1}{2n - 1})$, so $f(n, 3) - f(n, 2)$, so $f(\infty, 3) - f(\infty, 2)$, so $ln(3) - ln(2)$, so $ln(\frac{3}{2})$, now I will define $g(m, n)$ as m posataves, n negataves, so $g(m, n) = ln(\frac{m}{n})$

now, with the power of $g$ on our side, we can solve for $1 + \frac{1}{2} + \frac{1}{3}...$ (which by the way is the point of this chapter) as 1 posatave, 0 negataves, so $ln(1) - ln(0)$, but $ln(0)$ is undefined, so time to define it!

### $ln(0)$

$ln(0) = u$ (u for undefined)

$e^u = 0$

$\frac{1}{e^{-u}} = 0$

$e^{\infty} = \infty$

$\frac{1}{\infty} = 0 \Rightarrow u = - \infty \quad \And \quad ln(1) = 0 \Rightarrow 1 + \frac{1}{2} + \frac{1}{3}... = \infty$

### $\frac{1}{\infty}$

well, I am not really saying that $\frac{1}{\infty} = 0$, but that $\frac{1}{\lim_{n \to \infty} n}$

so $\lim_{N \to \infty} \frac{1}{n}$
