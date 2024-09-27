Credit (even if it is very small): [The two points that lie on every circle (???) #SoME3](https://www.youtube.com/watch?v=iUUm0sKLoiE), [Putting Algebraic Curves in Perspective](https://www.youtube.com/watch?v=XXzhqStLG-4), and [Extraordinary Conics: The Most Difficult Math Problem I Ever Solved](https://www.youtube.com/watch?v=X83vac2uTUs).

Lets say that a point $(a: b)$ (as opposed to $(a, b)$) is equal to $(ca: cb)$ $(c \ne 0)$, so every* (and that's a big asterisk) point $(a: b)$ can be scaled onto $(\frac{a}{b}: 1)$, a kind of number line.

*unless $b = 0$, then we add this kind of "point at infinity" to our number line (it's a single point because the point $(a: 0)$ can be scaled to $(1: 0)$ (aka the point at infinity), that is, of coarse, unless $a = 0$, but that point isn't really aloud for the same reason as $\frac{0}{0}$) making it the real projective line or $ℝ \text{P}^1$.

The reason why it's at infinity is because, if you consider the point $(1: 1)$, it falls onto $1$ on the number line, the point $(1: \frac{1}{2})$ falls onto $2$, the point $(1: \frac{1}{4})$ falls onto $4$, the point $(1: \frac{1}{8})$ falls onto $8$, and as the second number gets smaller, the point on the number line gets bigger aproaching infinity, hence the name "point at infinity". But, if you instead do this from the other direction, it approaches negative infinity. You can imagine a number line that curves down as it goes along, consecutave integers getting closer and closer, and an unsigned infinity at the bottom where the line meets itself.

Stepping a dimension up, you get the real projective plane or $ℝ \text{P}^2$, $(a: b: c) = (da: db: dc)$, most numbers going to $(\frac{a}{c}: \frac{b}{c}: 1)$, some becoming $(\frac{a}{b}: 1: 0)$, less becoming $(1: 0: 0)$, the point at infinity becomes a line at infinity (more of a circle, but $1$ degree of freedom, so it's a line), and the number line becomes a space of all points.

There is a problem though (that is big enough to be explained on a line by itself), you could imagine the same process that I used to prove the unsigned infinity thing but in $ℝ \text{P}^2$ to get the unsuprising result of $(a: b: 0) = (-a: -b: 0)$. This does mean that, when drawing the regular or affine plane, and drawing a circle around it (to represent the line at infinity of coarse), if you wanted to draw, say, the point $(1: 1: 0)$, it would need to be at both the very top right, and the very bottom left of the circle.

To see why this double counting thing makes sense, I'll project onto a unit sphere, so, if $r = \sqrt{a^2 + b^2 + c^2}$, the point $(a: b: c)$ maps to $(\frac{a}{r}: \frac{b}{r}: \frac{c}{r})$. You might see the problem though, it also maps to $(-\frac{a}{r}: -\frac{b}{r}: -\frac{c}{r})$, because it's also on the unit sphere. So, if you just consider the top half of the sphere (includineg the equator so that points at infinity are acounted for), it counts almost every point once, and points at infinity twice, kinda like the one where we projected onto the plane paralel to and one unit above the $xy$ plane. So, to fix this problem, and give every point the same treatment, you (counterintuitavely) count every point twice by using the entire sphere, kinda like giving every line in $2d$ an angle instead of a slope to fix the vertical lines problem, at the cost of there being two angles for every line.

[Here's a desmos graph](https://www.desmos.com/3d/zzoajkphnn).

Yes, I know, the plane is placed one unit below the sphere instead of one above, but it's only like that for the sake of demonstration.

### homogenization

Homogenization is a method of interpolation from equations on the affine plane (non-projective plane) to equations on the projective plane (so, adding the line at infinity), but I think it would be better if I just showed how to do it.

Lets say that I have these equations for describing my line:

$$ y = mx + b $$

$$ z = 1 $$

so, we have this equation:

$$ (x: y: z) = (x: mx + b: 1) $$

$$ (x, y, z) = (cx, cmx + cb, c) $$

and from those, I have this new equation for describing my line:

$$ y = mx + bz $$

now, the equation is homogeneous $^1$.

In (this $(x, y, z) = (cx, cmx + cb, c)$) equation for a line, $z$ could not equal $0$, but now, $z$ can equal $0$, and if $z = 0$, then it's at the line at infinity, so these $z = 0$ solutions snuck in as a result of homogenization, mission success!

$^1$ That is, a polynomial where each term has the same degree. There is a much easier way of doing this called homogenization: you take each term whose degree is not the max, and add factors of $z$ to bring the degree up to the max.

But what are these solutions at the line at infinity?

$$ z = 0 $$

$$ y = mx + bz $$

$$ y = mx $$

$$ (x: y: z) = (x: mx: 0) $$

$$ (1: m: 0) $$

This has some pretty cool implications, but I'll do that tomorrow.

Oh, look, it's tomorrow, time to tell you the implications.

Y'know how any two distinct points on the affine plane have a line through them? And how (almost) any two distinct lines on the affine plane have a point on both? That is, of coarse, unless the lines are parallel. Solution: homogenization. A homogenized line with slope $m$ has the point $(1: m: 0)$ (and $(0: 1: 0)$ if the line is vertical). So, if two lines have the same slope $m$ (and are distinct), then they don't meet normally, and they intersect at $(1: m: 0)$. If they have different slopes, then they do meet normally, and they don't intersect at the line at infinity. But what about the "any two distinct points have a line through them" rule? If you have a normal point and a point at infinity $(1: m: 0)$, they have the line with slope $m$ going through the first one. But what if you have two points on the line at infinity? This (among other things) is why it's called the line at infinity, a line that all points at infinity lie on.

Also, I'm gonna swich from $y = mx + b$ to $ax + by + c = 0$, to deal with vertical lines, and because I'm gonna use a variation of this to describe quadratics.

### dualtity

It's hard to explain how points dual to lines, but an example would be that they are both defined by three numbers, they are considered the same if you scale all three by the same amount, throw an error if all three are zero, the origin and the line at infinity are duals, or on the sphere, the equator and the north and south poles (remember, two solutions). The more general definition would be something like this: the two points on a sphere, a point on the dual line, and the point $90°$ away but still on the dual line are all mutually perpindicular. By the way, points on the plane project to antipodal points on the sphere, and lines on the plane project to great circles on the sphere.

Also fun fact: the duals of every point on a line would all pass through the dual point, and the duals of every line that passes through a point would all lie on the dual line.

$$ \text{Formula: the dual of point } (a: b: c) \text{ is the homogenized line } $ax + by + cz = 0$ \text{.} $$

#### conics

surprisingly, every conic is a hyperbola or elipse (circles are just perfect elipses, and parabolas are right in between elipses and hyperbolas), and each one has this form:

$$ ax^2 + bxy + cy^2 + dx + ey + f = 0 $$

(Not calculus $dx$ and $e$)
