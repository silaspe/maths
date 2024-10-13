## Angle addition

<iframe src="https://www.desmos.com/calculator/qwqbirdsyw?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

By the way, the opposite is the sine times the hypotenuse, and the adjacent is the cosine times the hypotenuse

In other words, $opp = sin \cdot hyp$, and $adj = cos \cdot hyp$.

The black triangle in its bottom-left corner has angle $\alpha$ and the blue triangle in its bottom-left corner has angle $\beta$, they are both right triangles, and the length of the top of the blue triangle is 1, and of coarse the combined angle is $\alpha + \beta$.

The question is: what is the $sin(\alpha + \beta)$ and $cos(\alpha + \beta)$?

I'll start with the $sin$, which is the length of the purple line, which is the length of the purple line below the upper-black line plus the length of the purple line above the upper-black line.

The length below is the same as the height of the right of the black triangle with hypotenuse $cos(\beta)$ which is the $opp$ so $sin(\alpha)cos(\beta)$.

The length above is in the top right mini blue triangle with hypotenuse $sin(\beta)$, and I'll leave this as an exercise for the viewer, but the angle in the top-left is $\alpha$ and it's the $adj$ so $cos(\alpha)sin(\beta)$.

In total, $sin(\alpha + \beta) = cos(\alpha)sin(\beta) + sin(\alpha)cos(\beta)$.

Now with the $cos$, which is the length of the green line, which is the length of the upper-black line minus the length of the mini blue triangle bottom.

The first length is the same as the length of the bottom of the black triangle with hypotenuse $cos(\beta)$ which is the $adj$, so $cos(\alpha)cos(\beta)$

the length of second line is in the bottom of the mini blue triangle with hypotenuse $sin(\beta)$, and as you know, the angle in the top-left is $\alpha$ and it's the $opp$ so $sin(\alpha)sin(\beta)$

in total, $cos(\alpha + \beta) = cos(\alpha)cos(\beta) - sin(\alpha)sin(\beta)$

$$ cos(\alpha + \beta) = cos(\alpha)cos(\beta) - sin(\alpha)sin(\beta) $$

$$ sin(\alpha + \beta) = cos(\alpha)sin(\beta) + sin(\alpha)cos(\beta) $$
