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

## Complex numbers

$$ i = \sqrt{-1} $$

$$ a + bi = c + di \iff c = a, d = b $$

$$ (a + bi)(c + di) = ac + adi + bci + bdii = ac + adi + bci - bd = (ac - bd) + (ad + bc)i $$

$$ (a + bi)^2 = (aa - bb) + (ab + ab)i = (a^2 - b^2) + 2abi $$

$$ (a + bi)r = ar + bri $$

$$ \text{ccong} (a + bi) = a - bi $$

<iframe src="https://www.desmos.com/calculator/6surjc6ubm?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

the vertical line is the definition of $sin(\theta)$

the horizontal line is the definition of $cos(\theta)$

$\alpha$ is the angle from the right of the $x$ axis to the point.

I will define $f(x)$ as a function that takes in a real number and outputs a complex number that is $x$ radians around the unit circle. Because of how circles work, $f(x) = cos(x) + isin(x)$. Fun fact! $z$ equals $rf(\theta)$ for any complex $z$. Eccept pepole don't use $f(\theta)$ because there are other complex functions $f(z)$, and $rcos(x) + irsin(x)$ dosen't reach the high bar for perfection set by mathematicians.

So, now the question is: solve for $f(x)$.

I'll start by multiplying $f(x) \cdot f(y)$

$$ \vdots $$



$$ \vdots $$

$$ f(x)f(y) = f(x + y) $$

hmmm $f(x)f(y) = f(x + y)$ sounds faniliar... Oh right! This is an exponential, but what's the base?

while, a common proof that I once used that if the derivitave of $g(x)$ is $g(x)$, then $g(x) = ce^x$, it has a method of:

$$ \vdots $$

$$ g(x) = g(0)(1 + dx)^{\frac{x}{dx}} $$

and then, using facts from [Calculus part 2](https://silaspe.github.io/maths/some4.html#calculus-ii), $g(x) = g(0)e^x = ce^x$.

So I will use a proof like that, the proof will go like this:

### proof

$$ f(x + dx) = f(x)f(dx) $$

$$ \vdots $$

$$ f(dx) = (cos(0) + dx \text{ } cos'(0)) + (sin(0) + dx \text{ } sin'(0))i $$

$cos(x)$ reaches a peak at $0$, so $cos'(0) = 0$

while as you zoom into the right of the unit circle, the hight is the distance travled and the sine of a small angle is that angle, so $sin'(0) = 1$

$$ \vdots $$

$$ f(x + ndx) = f(x)(1 + dxi)^n $$

and if you saw [Calculus part 2](https://silaspe.github.io/maths/some4.html#calculus-ii), you know that...

$$ f(0 + \frac{x}{dx}dx) = f(x) = f(0)((1 + dxi)^{\frac{1}{dx}})^x = f(0)(e^i)^x $$

so, surprisingly, the base of the exponential is $e^i$, eccept many of you would of guessed that because of eueler's identity, which I was trying to derive, anyways there is one more step (more like three but you get the point)

$$ f(0) = 1 $$

$$ f(x) = e^{ix} $$

thus:

$$ cos(x) + isin(x) = e^{ix} $$

proof complete!

### now what?

well, everything! Now complex multiplication is mutch easier, for example $z \cdot w = r e^{i \theta} \rho e^{i \psi} = r \rho e^{\theta + \psi}$

and if multiplying by a real number is scaling the distance from the origin, then complex multiplication has the mutch more intuitave interpritation that most pepole teach: multiplying the magnitudes and adding the angles.

another interpritation of complex multiplication is that if $w(z) = wz$ then $w(1) = w$ and scaling the input scales the output and then rotating the input rotates the output, in other words complex multiplication looks like scaling and rotating

Eccept I think that just saying things like "multiplying by a number on the unit circle rotates a point counterclockwise" which by the way is true, needs rigoris proof. And I wanted to add more cases, but this page only needs one more fact before saying "now everything" so that the right of the page makes sense, anywas the fact is that the only reason why mathematicians use $e^{i \theta}$ is either to show that $e^{i \theta} e^{i \psi} = e^{i(\theta + \psi)}$, to show that $\frac{d}{dx} e^{ix} = ie^{ix}$ which makes sense if you think about it, or to confuse complex number beginners possibly making them not want to learn about complex numbers in the first place

#### the Holy Grail of complex numbers (I forgot to do this $3$ months ago.)

$$ cos(\pi) + isin(\pi) = e^{i \pi} $$

$$ e^{i \pi} = -1 + i0 $$

$$ e^{i \pi} = -1 + i0 = -1 $$

$$ e^{i \pi} + 1 = 0 $$
