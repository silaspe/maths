## Complex numbers

$$ i = \sqrt{-1} $$

$$ a + bi = c + di \iff c = a, d = b $$

$$ (a + bi)(c + di) = ac + adi + bci + bdii = ac + adi + bci - bd = (ac - bd) + (ad + bc)i $$

$$ (a + bi)^2 = (aa - bb) + (ab + ab)i = (a^2 - b^2) + 2abi $$

$$ (a + bi)r = ar + bri $$

$$ \text{ccong} (a + bi) = a - bi $$

<iframe scrolling="no" title="sine_and_cosine" src="https://www.geogebra.org/material/iframe/id/qvcffjd6/width/1366/height/587/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1366px" height="587px" style="border:0px;"> </iframe>

$f$ is the definition of $sin(\theta)$

$g$ is the definition of $cos(\theta)$

$\theta$ is the angle from the right of the $x$ axis to the line $h$

Now, I will define $f(x)$ as a function that takes in a real number and outputs a complex number that is $x$ radians around the unit circle, so like the geogebra file above, but in the complex plane. using the file, we can say that $f(x) = cos(x) + isin(x)$, and any complex number $z$ has an angle $\theta$ measured in radians and a distance $r$ from the origin, so $z$ equals $rf(\theta)$, except people don't use $f(\theta)$ because there are other complex functions $f(z)$, and $rcos(x) + irsin(x)$ doesn't reach the high bar for perfection set by mathematicians 

so now, the question is: solve for $f(x)$

i'll start by multiplying $f(x) \cdot f(y)$

and using angle addition derived in the [trigonometry section](https://silaspe.github.io/maths/trigonometry.html)...

$$ f(x)f(y) = (cos(x) + isin(x))(cos(y) + isin(y)) = (cos(x)cos(y) - sin(x)sin(y)) + (cos(x)sin(y) + sin(x)cos(y))i = cos(x + y) + isin(x + y) = f(x + y) $$

hmmm $f(x)f(y) = f(x + y)$ sounds familiar... Oh right! This is an exponential, but what's the base?

while, a common proof that I once used that if the derivative of $g(x)$ is $g(x)$, then $g(x) = ce^x$, it has a method of:

$\frac{g(x + dx) - g(x)}{dx} = g(x)$, $g(x + dx) = g(x)(1 + dx)$, $g(x + 2dx) = g(x)(1 + dx)^2$, $g(x + ndx) = g(x)(1 + dx)^n$, $g(0 + \frac{x}{dx} dx) = g(x) = g(0)(1 + dx)^{\frac{x}{dx}}$

and then, using facts from [Calculus part 2](https://silaspe.github.io/maths/calculus_2.html), $g(x) = g(0)e^x = ce^x$.

So I will use a proof like that, the proof will go like this:

### proof

$$ f(x + dx) = f(x)f(dx) $$

$$ f(dx) = cos(dx) + isin(dx) = cos(0 + dx) + isin(0 + dx) = (cos(0) + dx \text{ } cos'(0)) + (sin(0) + dx \text{ } sin'(0))i $$

$cos(x)$ reaches a peak at $0$, so $cos'(0) = 0$

while as you zoom into the right of the unit circle, the height is the distance traveled and the sine of a small angle is that angle, so $sin'(0) = 1$

$$ f(dx) = (1 + 0dx) + (0 + 1dx)i = 1 + dxi $$

$$ f(x + dx) = f(x)(1 + dxi)$$

$$ f(x + 2dx) = f(x)(1 + dxi)^2 $$

$$ f(x + ndx) = f(x)(1 + dxi)^n $$

and if you saw [Calculus part 2](https://silaspe.github.io/maths/calculus_2.html), you know that...

$$ f(0 + \frac{x}{dx}dx) = f(x) = f(0)((1 + dxi)^{\frac{1}{dx}})^x = f(0)(e^i)^x $$

so surprisingly, the base of the exponential is $e^i$, except many of you would've guessed that because of eueler's identity, which I was trying to derive, anyways there is one more step (more like three but you get the point)

$$ f(0) = 1 $$

$$ f(x) = e^{ix} $$

thus:

$$ cos(x) + isin(x) = e^{ix} $$

proof complete!

### now what?

well everything! Now complex multiplication is much easier, for example $z \cdot w = r e^{i \theta} \rho e^{i \psi} = r \rho e^{\theta + \psi}$

and if multiplying by a real number is scaling the distance from the origin, then complex multiplication has the much more intuitive interpretation that most people teach: multiplying the magnitudes and adding the angles.

another interpretation of complex multiplication is that if $w(z) = wz$ then $w(1) = w$ and scaling the input scales the output and then rotating the input rotates the output, in other words complex multiplication looks like scaling and rotating

Except I think that just saying things like "multiplying by a number on the unit circle rotates a point counterclockwise" which by the way is true, needs rigorous proof. And I wanted to add more cases, but this page only needs one more fact before saying "now everything" so that the right of the page makes sense, anyways the fact is that the only reason why mathematicians use $e^{i \theta}$ is either to show that $e^{i \theta} e^{i \psi} = e^{i(\theta + \psi)}$, to show that $\frac{d}{dx} e^{ix} = ie^{ix}$ which makes sense if you think about it, or to confuse complex number beginners possibly making them not want to learn about complex numbers in the first place

### now everything

quaternions!

jk

.

.

.

.

.

.

.

.

.

.

.

.

.

.

ok, if you want quaternions, then...

you have to find it!

..........

..[.](https://silaspe.github.io/maths/gamma.html#_1)........

..........

...........

...........

#### the Holy Grail of complex numbers, I forgot to do this $3$ months ago

$$ cos(\pi) + isin(\pi) = e^{i \pi} $$

$$ e^{i \pi} = -1 + i0 = -1 $$

$$ e^{i \pi} + 1 = 0 $$
