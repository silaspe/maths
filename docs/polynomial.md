## disclaimer

this page uses terms like $dx$ and $e$, but these have nothing to do with calculas and are just notation, also in the $2nd$ and $4th$ chapters if this is the $1st$, I swapped $x$ for $x - \frac{b}{na}$ where $n$ is the degree of the polynomial so when pluging things in, make sure to add $\frac{b}{na}$, also I probably should have swapped the order I did this so that the quadratic came first, the last thing to warn you about is that I re-used letters like $a$, $b$, $c$, $p$, $q$, and $z$, anyways lets start strong with the...

### quartic

$$ ax^4 + bx^3 + cx^2 + dx + e = 0 $$

$$ x \to x - \frac{b}{4a} $$

$$ a (x - \frac{b}{4a})^4 + b (x - \frac{b}{4a})^3 + c (x - \frac{b}{4a})^2 + d (x - \frac{b}{4a}) + e = 0 $$

$$ ax^4 - 4ax^3 \frac{b}{4a} + 6ax^2 \frac{b^2}{16a^2} - 4ax \frac{b^3}{64a^3} + a \frac{b^4}{256a^4} + bx^3 - 3bx^2 \frac{b}{4a} + 3bx \frac{b^2}{16a^2} - b \frac{b^3}{64a^3} + cx^2 - 2cx \frac{b}{4a} + c \frac{b^2}{16a^2} + dx - d \frac{b}{4a} + e = 0 $$

$$ ax^4 - bx^3 + \frac{3b^2 x^2}{8a} - \frac{b^3 x}{16a^2} + \frac{b^4}{256a^3} + bx^3 - \frac{3b^2 x^2}{4a} + \frac{3b^3 x}{16a^2} - \frac{b^4}{64a^3} + cx^2 - \frac{bcx}{2a} + \frac{b^2c}{16a^2} + dx - \frac{bd}{4a} + e = 0 $$

$$ ax^4 - \frac{3b^2 x^2}{8a} - \frac{b^3 x}{16a^2} + \frac{b^4}{256a^3} + \frac{3b^3 x}{16a^2} - \frac{b^4}{64a^3} + cx^2 - \frac{bcx}{2a} + \frac{b^2c}{16a^2} + dx - \frac{bd}{4a} + e = 0 $$

$$ (a)x^4 + (c-\frac{3b^2}{8a})x^2 + (\frac{2b^3}{16a^2} - \frac{bc}{2a} + d)x + (\frac{b^4}{256a^3} - \frac{b^4}{64a^2} + \frac{b^2c}{16a^2} - \frac{bd}{4a} + e) = 0 $$

$$ x^4 + (c-\frac{3b^2}{8a^2})x^2 + (\frac{2b^3}{16a^3} - \frac{bc}{2a^2} + \frac{d}{a})x + (\frac{b^4}{256a^4} - \frac{b^4}{64a^3} + \frac{b^2c}{16a^3} - \frac{bd}{4a^2} + \frac{e}{a}) = 0 $$

$$ p = c-\frac{3b^2}{8a^2} $$

$$ q = \frac{2b^3}{16a^3} - \frac{bc}{2a^2} + \frac{d}{a} $$

$$ r = \frac{b^4}{256a^4} - \frac{b^4}{64a^3} + \frac{b^2c}{16a^3} - \frac{bd}{4a^2} + \frac{e}{a} $$

### depresed quartic

$$ x^4 + px^2 + qx + r = 0 $$

$$ x^4 + px^2 = -qx - r $$

$$ x^4 + 2px^2 + p^2 = px^2 - qx - r + p^2 $$

$$ (x^2 + p)^2 = px^2 - qx - r + p^2 $$

$$ (x^2 + p)^2 + 2(x^2 + p)z + z^2 = (x^2 + p + z)^2 = px^2 - qx - r + p^2 + 2zx^2 + 2pz + z^2 = (p + 2z)x^2 - qx + 2pz + z^2 - r + p^2 $$

now, define z so that the right side of this equation is a perfect square. But then a quadratic is of the form $c(x - ?)(x - ?)$ or $(\something x + \something)^2$, so if it is a perfect sqare, than there is only one solution, which means that the [discriminant](https://silaspe.github.io/maths/polynomial.html#depresed-quartic-again) equals zero, so

$$ (-q)^2 - 4(p + 2z)(2pz + z^2 - r + p^2) = 0 $$

expanding out, we get a cubic polynomial to solve for z. and once we do, we have that $(x^2 + p + z)^2 = (\something x + \something)^2$, so now we can solve for x with a quadratic

yay! but we still have to derive the quadratic discriminate and the cubic formula in the next few chapters.

### cubic

$$ ax^3 + bx^2 + cx + d = 0 $$

$$ x \to x - \frac{b}{3a} $$

$$ a (x - \frac{b}{3a})^3 + b (x - \frac{b}{3a})^2 + c (x - \frac{b}{3a}) + d = 0 $$

$$ ax^3 - 3ax^2 \frac{b}{3a} + 3ax \frac{b^2}{9a^2} - a \frac{b^3}{27a^3} + bx^2 - 2bx \frac{b}{3a} + b \frac{b^2}{9a^2} + cx - c \frac{b}{3a} + d = 0 $$

$$ ax^3 - bx^2 + \frac{b^2x}{3a} - \frac{b^3}{27a^2} + bx^2 - \frac{2b^2x}{3a} + \frac{b^3}{9a^2} + cx - \frac{bc}{3a} + d = 0 $$

$$ ax^3 - \frac{b^2x}{3a} + \frac{b^3}{6a^2} + cx - \frac{bc}{3a} + d = 0 $$

$$ (a)x^3 + (c - \frac{b^2}{3a})x + (\frac{b^3}{6a^2} - \frac{bc}{3a} + d) = 0 $$

$$ x^3 + (c - \frac{b^2}{3a^2})x + (\frac{b^3}{6a^3} - \frac{bc}{3a^2} + \frac{d}{a}) = 0 $$

$$ p = c - \frac{b^2}{3a^2} $$

$$ q = \frac{b^3}{6a^3} - \frac{bc}{3a^2} + \frac{d}{a} $$

### depresed cubic

$$ x^3 + px + q = 0 $$

$$ x + y = z $$

$$ z^3 = x^3 + 3x^2 y + 3x y^2 + y^3 = x^3 + 3xyz + y^3 $$

$$ 3xyz = px $$

$$ x^3 + 3xyz + q = 0 $$

$$ x^3 + 3xyz + y^3 = y^3 - q $$

$$ 3yz = p $$

$$ z^3 = y^3 - q $$

#### y

$$ z = \frac{p}{3y} $$

$$ y^3 - q = \frac{p^3}{27y^3} $$

$$ (y^3)^2 - qy^3 - (\frac{p}{3})^3 = 0 $$

#### z

$$ y = \frac{p}{3z} $$

$$ z^3 = \frac{p^3}{27z^3} - q $$

$$ (z^3)^2 + qz^3 - (\frac{p}{3})^3 = 0 $$

okay, so now we have to solve the quadratic, take the cube root, and subtract just to solve for x

### quadratic

either [this](https://silaspe.github.io/maths/quadratic.html)

or [that](https://silaspe.github.io/maths/polynomial.html# )

###  

$$ ax^2 + bx + c = 0 $$

$$ x^2 + \frac{b}{a} x = x^2 + 2 \frac{b}{2a} x = - \frac{c}{a} $$

$$ x^2 + 2 \frac{b}{2a} x + \frac{b^2}{4a^2} = (x + \frac{b}{2a})^2 = \frac{b^2}{4a^2} - \frac{c}{a} = \frac{b^2 - 4ac}{4a^2} $$

$$ x + \frac{b}{2a} = \pm  = \pm \frac{\sqrt{b^2 - 4ac}}{2a} $$

$$ x = -\frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = -\frac{b}{2a} \pm \sqrt{\frac{b^2 - 4ac}{4a^2}} $$

#### depresed cubic (again)

$$ y^3 = \frac{q}{2} \pm \sqrt{\frac{q^2 + 4(\frac{p}{3})^3}{4}} = \frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3} $$

$$ y = \sqrt[3]{\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} $$

$$ z^3 = -\frac{q}{2} \pm \sqrt{\frac{q^2 + 4(\frac{p}{3})^3}{4}} = -\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3} $$

$$ z = \sqrt[3]{-\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} $$

$$ x = z - y = \sqrt[3]{-\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} - \sqrt[3]{\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} = \sqrt[3]{-\frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} + \sqrt[3]{-\frac{q}{2} \mp \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} $$

but now, that $\pm$ is the only difference between $y$ and $z$, and if they are the same then $x$ equals zero, and if you saw [this mathologer video](https://www.youtube.com/watch?v=N-KXStupwsc&t=978s) and stop at timestamp and 19:55, than you know that we might as well say that they are different because we only need one solution, if $x \neq 0$ than they have to be different. In all cases, one has to be $+$ and one has to be $-$, you can choose which but I will just put the plus one first. In total:

$$ x = \sqrt[3]{-\frac{q}{2} + \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} + \sqrt[3]{-\frac{q}{2} - \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} $$

so just plug in for $p$ and $q$ and add $\frac{b}{3a}$ and you have the cubic formula!

#### z (quartic)

so finally, after reading the whole page, you can understand the quadratic discriminant, (either that or you just skipped to this part) but probably not. So this discriminant is the $b^2 - 4ac$ in the quadratic formula, because the square root of a positive number is positive and plus or minus a positive number has two solutions, the square root of a negatave number is undefined (unless complex numbers) and plus or minus an undefined number has zero solutions, the square root zero is zero and plus or minus zero has one solution. In total, the sign of the $b^2 - 4ac$ determins how many solutions exist, which is why it is called descriminant, so...

$$ (-q)^2 - 4(p + 2z)(2pz + z^2 - r + p^2) = 0 $$

$$ q^2 - 8p^2z - 16pz^2 - 4pz^2 - 8z^3 + 4pr + 8rz - 4p^3 - 8p^2z = 0 $$

$$ (-8)z^3 + (-20p)z^2 + (8(r - 2p^2))z + (q^2 + 4pr - 4p^3) = 0 $$

$$ (8)z^3 + (20p)z^2 + (16p^2 - 8r)z + (4p(p^2 - r) - q^2) = 0 $$

solve for z! (not $\Gamma$[ ](https://silaspe.github.io/maths/gamma.html)($z + 1$))
