## Complex numbers

$$ i = \sqrt{-1} $$

$$ a + bi = c + di \iff c = a, d = b $$

$$ (a + bi)(c + di) = ac + adi + bci + bdii = ac + adi + bci - bd = (ac - bd) + (ad + bc)i $$

$$ (a + bi)^2 = (aa - bb) + (ab + ab)i = (a^2 - b^2) + 2abi $$

$$ (a + bi)r = ar + bri $$

$$ ccong(a + bi) = a - bi $$

<iframe scrolling="no" title="sine_and_cosine" src="https://www.geogebra.org/material/iframe/id/qvcffjd6/width/1366/height/587/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1366px" height="587px" style="border:0px;"> </iframe>

f is the definition of $sin(\theta)$

g is the definition of $cos(\theta)$

$\theta$ is the angle from the right of the x axis to the line h

now, I will define $f(x)$ as a function that takes in a real number and outputs a complex number that is $x$ radians around the unit circle, so like the geogebra file above, but in the complex plane. using the file we can say that $f(x) = cos(x) + isin(x)$, and any complex number $z$ has an angle $\theta$ measured in radians and a distance $r$ from the origin, so $z$ equals $rf(\theta)$, eccept pepole don't use $f(\theta)$ because there are other complex functions $f(z)$, and $rcos(x) + irsin(x)$ dosen't reach the high bar for perfection set by mathmeticians 

so now, the question is: solve for f(x)

i'll start by multaplying (f(x) \cdot f(y))

and using angle addition derived in the trigonomitry section...

$$ f(x)f(y) = (cos(x) + isin(x))(cos(y) + isin(y)) = (cos(x)cos(y) - sin(x)sin(y)) + (cos(x)sin(y) + sin(x)cos(y))i = cos(x + y) + isin(x + y) = f(x + y) $$

hmmm $f(x)f(y) = f(x + y)$ sounds faniliar.. Oh ringt! This is an exponental, but what base?

while, a common proof that I once used that if the derivitave of $g(x)$ is $g(x)$ then $g(x) = e^x$, it has a method of:

$\frac{g(x + dx) - g(x)}{dx} = g(x)$, $g(x + dx) = g(x)(1 + dx)$, $g(x + 2dx) = g(x)(1 + dx)^2$, $g(x + ndx) = g(x)(1 + dx)^n$, $g(0 + \frac{x}{dx} dx) = g(x) = g(0)(1 + dx)^{\frac{x}{dx}}$

and then, using facts from calculas II, $g(x) = g(0)e^x$.

So I will use a proof like that
