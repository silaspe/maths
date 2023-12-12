## Harmonic

i'm going to start with the alternating harmonic seireis $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} ...$

then, for example $- \frac{1}{4} = \frac{1}{4} - \frac{1}{2}$

then, the original seireis is equal to $1 + \frac{1}{2} - 1 + \frac{1}{3} + \frac{1}{4} - \frac{1}{2} ...$

also, I will call the total sum "?"

now, let me define $f(n)$ as $f(1) = 1$ and $f(2) = 1 + \frac{1}{2} - 1 + \frac{1}{3} = \frac{1}{2} + \frac{1}{3}$ than $f(3)$ equals the next few terms, so $\frac{1}{3} + \frac{1}{4} + \frac{1}{5}$

in genaral, $f(n)$ = $\frac{1}{n} + \frac{1}{n + 1} + ...$ with n terms OR $\frac{1}{n} + \frac{1}{n + 1} + ... + \frac{1}{2n - 1}$

but than $f(\infty) = ?$

$f(n,x) = \frac{1}{n} + \frac{1}{n + 1} + ... + \frac{1}{xn - 1}$ for integer n and $x$ as $\frac{integer}{n}

$f(n,x + \frac{1}{n}) - f(n,x) = \frac{1}{xn}$

$n(f(n,x + \frac{1}{n}) - f(n,x)) = \frac{1}{x}$

as $n \to \infty$ $\frac{1}{n} \to 0$ and $x$ could be anything AND the previous expression equals $\frac{df(\infty,x)}{dx}$

but $ln \prime(x) = \frac{1}{x}$ and $ln(1) = 0$ AND $f(\infty,1) = \frac{1}{1 + \infty} = 0$

therefore $f(\infty,x) = ln(x)$

but $f(n,2) = f(n)$ and $? = f(\infty)$

so, $? = f(\infty,2) = ln(2)$

so $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5}$ FOREVER $= ln(2)$

yay!

### regular harmonic
