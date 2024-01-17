## quartic

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

now, define z so that the right side of this equation is a perfect square. But then a quadratic is of the form $(x - ?)(x - ?)$, so if it is a perfect sqare, than there is only one solution, which means that the discriminant equals zero, so

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

$$ ax^2 + bx + c = 0 $$

$$ x^2 + \frac{b}{a} x = x^2 + 2 \frac{b}{2a} x = - \frac{c}{a} $$

$$ x^2 + 2 \frac{b}{2a} x + \frac{b^2}{4a^2} = (x + \frac{b}{2a})^2 = \frac{b^2}{4a^2} - \frac{c}{a} = \frac{b^2 - 4ac}{4a^2} $$

$$ x + \frac{b}{2a} = \pm \sqrt{\frac{b^2 - 4ac}{(2a)^2}} = \pm \frac{\sqrt{b^2 - 4ac}}{2a} $$

$$ x = -\frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
