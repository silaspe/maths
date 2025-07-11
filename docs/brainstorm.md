The equations below are the beginning of pages that may or may not get added to my website. All pages after Modular arithmetic and this one started here in the brainstorm page. I got (almost none of) these from copying things from a piece of paper (actually, just the one below) that had potential to become a digital page. And finally, the titles have a question mark if they are my best guess for the titles of the page, no question mark if I made the page and know the title, a question mark if I never published the page, but still want the world to see it, and extra small if is just one puzzle, but didn't fit anywhere and/or was worth making a dedicated page. Also, happy eclipse day! The eclipse was worth the $10$ (total) hours of driving.

### galois theory/group theory/ring theory?

A field of numbers is a collection of numbers where you can add, subtract, multiply, and even sometimes divide two numbers (as long as you don't divide by zero) in that field to get another number in that field. For example, the rationals, the reals and the complex numbers are all fields that are infinite and you can divide them. The complex lattice points (which are complex numbers of the form $integer + integer \cdot i$ ), the matrices (insert joke here), and the integers, are all infinite but can not always be divided. I know what you might be thinking: "what the stand-in-for-a-curse-word is a non-infinite field?". A non-infinite field (or finite field) is something like the [modulo numbers](https://silaspe.github.io/maths/mod.html). You might not be able to divide in a non-prime base, but you can do it in a prime base. So that completes the venn diagram!

Today, I want to show you an infinite field where you can not divide, I'm talking (well, typing) about numbers of the form

$$ a + b \sqrt{7} $$

for integers $a$ and $b$.

Side note! A number of this form can only be written in one way. Not because $\sqrt{7}$ is an imaginary number, but because $\sqrt{7}$ is irrational. End of side note.

You can probably take my word for it that you can add, subtract, and multiply these numbers to get another one, but here's a proof (which was the only* thing on that was on the paper that inspired this (digital) page. *Other than division and square roots).

$$ (a + b \sqrt{7}) + (c + d \sqrt{7}) = a + b \sqrt{7} + c + d \sqrt{7} $$

$$ (a + b \sqrt{7}) - (c + d \sqrt{7}) = a + b \sqrt{7} - c - d \sqrt{7} $$

$$ (a + b \sqrt{7}) \cdot (c + d \sqrt{7}) = ac + ad \sqrt{7} + b \sqrt{7} c + b \sqrt{7} d \sqrt{7} $$

.

$$ (a + b \sqrt{7}) + (c + d \sqrt{7}) = (a + c) + (b + d) \sqrt{7} $$

$$ (a + b \sqrt{7}) - (c + d \sqrt{7}) = (a - c) + (b - d) \sqrt{7} $$

$$ (a + b \sqrt{7}) \cdot (c + d \sqrt{7}) = (ac + 7bd) + (ad + bc) \sqrt{7} $$

$$ \text{And all of these are a number of this form. The end! Yeah, that was my whole* idea.} $$

### why can't you multiply two vectors? (all endings)?

$$ \vec{u} = \begin{bmatrix} u_x \\
u_y \\
u_z \\ \end{bmatrix} = u_x \hat{i} + u_y \hat{j} + u_z \hat{k} $$

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\
v_z \\ \end{bmatrix} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k} $$

$$ \vec{u} \vec{v} = (u_x \hat{i} + u_y \hat{j} + u_z \hat{k}) (v_x \hat{i} + v_y \hat{j} + v_z \hat{k}) = u_x \hat{i} v_x \hat{i} + u_x \hat{i} v_y \hat{j} + u_x \hat{i} v_z \hat{k} + u_y \hat{j} v_x \hat{i} + u_y \hat{j} v_y \hat{j} + u_y \hat{j} v_z \hat{k} + u_z \hat{k} v_x \hat{i} + u_z \hat{k} v_y \hat{j} + u_z \hat{k} v_z \hat{k} $$

$$ \text{For lack of a better way to display this, } \vec{u} \vec{v} \text{ equals the thing below:} $$

$$ (\hat{i} \hat{i})(u_x v_x) + (\hat{i} \hat{j})(u_x v_y) + (\hat{i} \hat{k})(u_x v_z) $$

$$ (\hat{j} \hat{i})(u_y v_x) + (\hat{j} \hat{j})(u_y v_y) + (\hat{j} \hat{k})(u_y v_z) $$

$$ (\hat{k} \hat{i})(u_z v_x) + (\hat{k} \hat{j})(u_z v_y) + (\hat{k} \hat{k})(u_z v_z) $$

$$ \text{Ending } 1 \text{, I give up.} $$

$$ \text{Because there is no way that this is a vector. Anyways, ending 2, } $$

### geometric algebra

Yeah, I forgot all the endings to multiplying vectors, so I came up with the previous one. Well, I guess I had this one, but I would rather make it into its own page. After watching [A Swift Introduction to Geometric Algebra](https://www.youtube.com/watch?v=60z_hpEAtD8) (literally, that was the name), I thought that (if it is a scalar plus a bivector), than it is just a scalar plus a vector times $i$ (or $-i$, I am not sure yet), but I will call it $U$ instead. But first, here's the definition of multiplying two basis vectors (all the alternative endings probably just had alternative definitions for this. I think that I remember the definition that multiplication was anticommutative, which would lead me to the cross product): The product of a basis vector $e_1$ and it self is $0$, and the product of two basis vectors $e_1$ and $e_2$ equals $-e_2 e_1$ equals $e_3$. This means that you can do this at any point in the product of basis vectors.

$$ \hat{i} = x $$

$$ \hat{j} = y $$

$$ \hat{k} = z $$

$$ \text{Now is about as good of a time as any to simplify the product.} $$

$$ \vec{u} \vec{v} = \begin{pmatrix} (xx)(u_x v_x) + (xy)(u_x v_y) + (xz)(u_x v_z) +  \\
(yx)(u_y v_x) + (yy)(u_y v_y) + (yz)(u_y v_z) + \\
(zx)(u_z v_x) + (zy)(u_z v_y) + (zz)(u_z v_z) \\ \end{pmatrix} = \begin{pmatrix} (xx)(u_x v_x) + (xy)(u_x v_y) - (zx)(u_x v_z) -  \\
(xy)(u_y v_x) + (yy)(u_y v_y) + (yz)(u_y v_z) + \\
(zx)(u_z v_x) - (yz)(u_z v_y) + (zz)(u_z v_z) \\ \end{pmatrix} = \begin{pmatrix} u_x v_x + (xy)(u_x v_y) - (zx)(u_x v_z) -  \\
(xy)(u_y v_x) + u_y v_y + (yz)(u_y v_z) + \\
(zx)(u_z v_x) - (yz)(u_z v_y) + u_z v_z \\ \end{pmatrix} = u_x v_x +  u_y v_y + u_z v_z + \begin{pmatrix} (xy)(u_x v_y - u_y v_x) +  \\
(yz)(u_y v_z - u_z v_y) + \\
(zx)(u_z v_x - u_x v_z) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + \begin{pmatrix} (xy)(u_x v_y - u_y v_x) +  \\
(yz)(u_y v_z - u_z v_y) + \\
(zx)(u_z v_x - u_x v_z) \\ \end{pmatrix} $$

$$ \text{But now, I need to turn a bivector into a vector, I'll use that } U \text{ thing for that.} $$

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)


$100$ Lines btw.

$$ U = xyz $$

Puzzle time! Prove that $U \vec{v} = \vec{v} U$.

$$ U^2 = xyzxyz = -xyzxzy = xyzzxy = xyxy = -xxyy $$

$$ U^2 = -1 $$

$$ \text{Yes, your suspicions are confirmed, it was called } i \text{ for that reason.} $$

$$ U^3 = xyzxyzxyz = -xyxzyzxyz = xxyzyzxyz = yzyzxyz = -yyzzxyz = -xyz = -U = xzy = -zxy = zyx $$

$$ U^4 = U^2 U^2 = (-1) (-1) = 1 $$

$$ U^4 = U^3 U = (-U) U = -U^2 = -(-1) = 1 $$

.

$$ U^1 = U = xyz $$

$$ U^2 = 1 $$

$$ U^3 = -U = zyx = -xyz $$

$$ U^4 = (-U) U  = 1 $$

$2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ lines!

.

$$ xy = xyzz = Uz $$

$$ yz = yzxx = -yxzx = xyzx = Ux $$

$$ zx = zxyy = -zyxy = -(-U)y = Uy $$

$$ \text{Yes! Now I can finally solve the puzzle.} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \begin{pmatrix} (Uz)(u_x v_y - u_y v_x) +  \\
(Ux)(u_y v_z - u_z v_y) + \\
(Uy)(u_z v_x - u_x v_z) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + U \begin{pmatrix} x(u_y v_z - u_z v_y) +  \\
y(u_z v_x - u_x v_z) + \\
z(u_x v_y - u_y v_x) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + U \begin{bmatrix} u_y v_z - u_z v_y \\
u_z v_x - u_x v_z \\
u_x v_y - u_y v_x \\ \end{bmatrix} $$

.

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + U \text{ } \vec{u} \times \vec{v} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \hat{i} \hat{j} \hat{k} \text{ } \vec{u} \times \vec{v} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \vec{u} \times \vec{v} \text{ } i $$

Also, the cross product only works in $3d$ while this $\hat{i} \hat{j} \hat{k} \text{ } \vec{u} \times \vec{v}$ thing works in any dimension. This operator actually has a name (well, two names), the outer product (as opposed to the dot product sometimes referred to as the inner product) or wedge product for its appearance as a wedge unicode character. This more general cross product is written $\vec{u} ∧ \vec{v}$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \vec{u} ∧ \vec{v} $$

#### Maxwell's equation (singular)

$$ \nabla F = J $$

$$ \text{Actually,} $$

$$ \nabla F = \frac{J}{c \epsilon_0} $$

[.](https://www.youtube.com/watch?v=60z_hpEAtD8)

### $\frac{1}{\vec{v}}$

$$ \vec{v} \frac{1}{\vec{v}} = \vec{v} \cdot \frac{1}{\vec{v}} + \hat{i} \hat{j} \hat{k} \text{ } \vec{v} \times \frac{1}{\vec{v}} = 1 + \hat{i} \hat{j} \hat{k} \text{ } 0 $$

$$ \vec{v} \cdot \frac{1}{\vec{v}} = 1 $$

$$ \vec{v} \times \frac{1}{\vec{v}} = 0 $$

$$ \text{if } \vec{v} \times \frac{1}{\vec{v}} = 0 \text{, than they are on the same axis, so } \frac{1}{\vec{v}} = c \vec{v} \text{, and the puzzle now is to solve for } c \text{ in terms of } \vec{v} $$

$$ \vec{v} \cdot c \vec{v} = || \vec{v} || \cdot || c \vec{v} || \cdot cos(\text{The angle between them}) = 1 $$

$$ \text{But the angle between them is } 0 \text{, so} $$

$$ \vec{v} \cdot c \vec{v} = || \vec{v} || \cdot || c \vec{v} || =  c || \vec{v} || \cdot || \vec{v} || = 1 $$

$$ c = \frac{1}{|| \vec{v} ||^2} $$

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

$$ \frac{1}{\vec{v}} = \frac{\vec{v}}{|| \vec{v} ||^2} $$

And perfect timing, it is exactly $200$ lines.

$$ \frac{1}{\frac{1}{\vec{v}}} = \frac{\frac{1}{\vec{v}}}{|| \frac{1}{\vec{v}} ||^2} = \frac{\frac{1}{\vec{v}}}{|| \vec{v} \frac{1}{|| \vec{v} ||^2} ||^2} = \frac{\frac{1}{\vec{v}}}{\frac{1}{|| \vec{v} ||^4} || \vec{v}||^2} = \frac{\frac{\vec{v}}{|| \vec{v} ||^2}}{\frac{1}{|| \vec{v}||^2}} = \vec{v} $$

$$ \text{But that is only in } 3d \text{, what about } 4d \text{ and beyond? I remember telling my sister the other day "what happens when you multiply two vectors? In } 4 \text{ dimensions!" (Both gasp).} $$

$$ \text{Let's say that we are in dimension } d \text{. First, basis vectors} $$

$$ e_1 = \hat{i} = x $$

$$ e_2 = \hat{j} = y $$

$$ e_3 = \hat{k} = z $$

$$ e_4 = \hat{l} = w $$

$$ \vdots $$

$$ \vec{u} = \begin{bmatrix} u_1 \\
u_2 \\
u_3 \\
\vdots \\
u_d\\ \end{bmatrix} = \sum\limits_{n = 1}^{d} u_n e_n $$

$$ \vec{v} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_d \\ \end{bmatrix} = \sum\limits_{n = 1}^{d} v_n e_n $$

$$ \vec{u} \vec{v} = \begin{bmatrix} (xx) u_1 v_1 & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
(yx) u_2 v_1 & (yy) u_2 v_2 & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
(zx) u_3 v_1 & (zy) u_3 v_2 & (zz) u_3 v_3 & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
(wx) u_4 v_1 & (wy) u_4 v_2 & (wz) u_4 v_3 & (ww) u_4 v_4 & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(e_d x) u_d v_1 & (e_d y) u_d v_2 & (e_d z) u_d v_3 & (e_d w) u_d v_4 & \dots & (e_d e_d) u_d v_d \\ \end{bmatrix} = \begin{bmatrix} u_1 v_1 & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
(yx) u_2 v_1 & u_2 v_2 & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
(zx) u_3 v_1 & (zy) u_3 v_2 & u_3 v_3 & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
(wx) u_4 v_1 & (wy) u_4 v_2 & (wz) u_4 v_3 & u_4 v_4 & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(e_d x) u_d v_1 & (e_d y) u_d v_2 & (e_d z) u_d v_3 & (e_d w) u_d v_4 & \dots & u_d v_d \\ \end{bmatrix} = (u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d) + \begin{bmatrix}  & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
(yx) u_2 v_1 &  & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
(zx) u_3 v_1 & (zy) u_3 v_2 &  & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
(wx) u_4 v_1 & (wy) u_4 v_2 & (wz) u_4 v_3 &  & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
(e_d x) u_d v_1 & (e_d y) u_d v_2 & (e_d z) u_d v_3 & (e_d w) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \text{It was really frustrating to write a plus in between, so I just gave up. Just assume that the result above is summed together.} $$

$$ \vdots $$

$$ \text{I actually have no idea how to prove this, but} $$

$$ \frac{1}{\vec{v}} = \frac{\vec{v}}{|| \vec{v} ||^2} $$

#### mini quadratic

How this page works is that I count up in binary such that if the last digit is one, it has a constant term, if the second to last digit is one, it has a linear term, if the third to last digit is one, it has a quadratic term. Starting at $0$ with the number above.

.

000

$$  = 0 $$

$$ x = \frac{0}{0} $$

001

$$ a = 0 $$

$$ x = \frac{a}{0} $$

010

$$ ax = 0 $$

$$ x = \frac{0}{a} $$

011

$$ ax + b = 0 $$

$$ x + \frac{b}{a} = 0 $$

$$ x = -\frac{b}{a} $$

100

$$ ax^2 = 0 $$

$$ x^2 = \frac{0}{a} $$

$$ x = \sqrt{\frac{0}{a}} $$

$$ \text{if } a = 0 \text{, then the square root of } \frac{0}{0} \text{ is still } \frac{0}{0} \text{, and if } a \ne 0 \text{ then the square root of } 0 \text{ is still } 0 \text{! (Not } 0 \text{ factorial)} $$

$$ x = \frac{0}{a} $$


$300$ Lines.

101

$$ ax^2 + b = 0 $$

$$ x^2 = -\frac{b}{a} $$

$$ x = \sqrt{-\frac{b}{a}} $$

110

$$ ax^2 + bx = 0 $$

$$ x(ax + b) = 0 $$

$$ x = 0, x = -\frac{b}{a} $$

$$ x = -\frac{b}{2a} \mp \frac{b}{2a} $$

111

$$ ax^2 + bx + c = 0 $$

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

### line through two points?

$$ f(a_x) = a_y $$

$$ f(b_x) = b_y $$

$$ f(x) \text{ Is a linear function.} $$

$$ \text{So, } f(x) \text{ is the line that passes thru } (a_x, a_y) \text{ and } (b_x, b_y) $$

$$ \text{there are many ways to solve this puzzle, but I only have time to show you one.} $$

$$ f(x) = cx + d $$

$$ c a_x + d = a_y $$

$$ c b_x + d = b_y $$

$$ c a_x + d - c b_x - d = a_y - b_y $$

$$ c(a_x - b_x) = a_y - b_y $$

$$ c = \frac{a_y - b_y}{a_x - b_x} $$

$$ \frac{a_y - b_y}{a_x - b_x} a_x + d = a_y $$

$$ \frac{a_y - b_y}{a_x - b_x} a_x - a_y = d $$

$$ (a_y - b_y) a_x - a_y (a_x - b_x) = d (a_x - b_x) $$

$$ a_x a_y - a_x b_y - a_y a_x + a_y b_x = d (a_x - b_x) $$

$$ a_x a_y - a_x a_y + a_y b_x - a_x b_y = d (a_x - b_x) $$

$$ d = \frac{a_y b_x - a_x b_y}{a_x - b_x} $$

$$ f(x) = \frac{a_y - b_y}{a_x - b_x} x + \frac{a_y b_x - a_x b_y}{a_x - b_x} = \frac{b_y - a_y}{b_x - a_x} x + \frac{a_x b_y - a_y b_x}{b_x - a_x} = \frac{(a_y - b_y) x + a_y b_x - a_x b_y}{a_x - b_x} = \frac{(b_y - a_y) x + a_x b_y - a_y b_x}{b_x - a_x} $$

$$ \text{Personally, my favorite is:} $$

$$ f(x) = \frac{a_y - b_y}{a_x - b_x} x + \frac{a_x b_y - a_y b_x}{b_x - a_x} $$

#### multivector times tables

$0$ d

$$ (u_1)(v_1) = (u_1 v_1) = (u_1 v_1) $$

$1$ d

$$ (u_1 + u_2 x)(v_1 + v_2 x) = (u_1 v_1 + u_2 v_2) + (u_1 v_2 + u_2 v_1)x $$

$2$ d

$$ (u_1 + u_2 x + u_3 y + u_4 xy)(v_1 + v_2 x + v_3 y + v_4 xy) = (u_1 v_1 + u_2 v_2 + u_3 v_3 - u_4 v_4) + (u_1 v_2 + u_2 v_1 - u_3 v_4 + u_4 v_3)x + (u_1 v_3 + u_2 v_4 + u_3 v_1 - u_4 v_2)y + (u_1 v_4 + u_2 v_3 - u_3 v_2 + u_4 v_1)xy $$

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

$400$ lines.

$3$ d

$$ (u_1 + u_2 x + u_3 y + u_4 xy + u_5 z + u_6 xz + u_7 yz + u_8 xyz)(v_1 + v_2 x + v_3 y + v_4 xy + v_5 z + v_6 xz + v_7 yz + v_8 xyz) = u_1 v_1 + u_1 v_2 x + u_1 v_3 y + u_1 v_4 xy + u_1 v_5 z + u_1 v_6 xz + u_1 v_7 yz + u_1 v_8 xyz + u_2 v_1 x + u_2 v_2 + u_2 v_3 xy + u_2 v_4 y + u_2 v_5 xz + u_2 v_6 z + u_2 v_7 xyz + u_2 v_8 yz + u_3 v_1 y - u_3 v_2 xy + u_3 v_3 - u_3 v_4 x + u_3 v_5 yz - u_3 v_6 xyz + u_3 v_7 z - u_3 v_8 xz + u_4 v_1 xy - u_4 v_2 y + u_4 v_3 x - u_4 v_4 + u_4 v_5 xyz - u_4 v_6 yz + u_4 v_7 xz - u_4 v_8 z + u_5 v_1 z - u_5 v_2 xz - u_5 v_3 yz + u_5 v_4 xyz + u_5 v_5 - u_5 v_6 x - u_5 v_7 y + u_5 v_8 xy $$

$$ \text{I think I'm too lazy to finish this.} $$

### set theory/logic (definitions)

$$ \text{A set is a well defined collection of objects, a set could contain the two shoes on you feet, or the } 5 \text{ pieces of cheese on this cutting board (that I'm going to pretend exists), sets can even contain other sets, but sets can not contain themselves, because it would lead to a paradox: would the set that contains every set that doesn't contain itself contain itself?" this also means that there isn't a set that contains everything.} $$

$$ \text{But the thing is, using some symbols, you can describe almost all of math. These symbols can just be pronounced as words, and it would make a sentence, such as "} ¬ \exists (x): |x| < 0 \text{" as "there does not exist } x \text{ such that the absolute value of } x \text{ is strictly less than } 0 \text{". Time to rapidfire through each one's pronunciation and meaning.} $$

.

$$ ∀ \text{ Is pronounced "for any" or "for all" (but I prefer "for any") and means what it says. It than has an open parentheses, a thing (} x, y, z, \text{ or a set) that I will call } x \text{ for now, a closed parentheses (parenthese is not a word), a } \cdot \text{, a statement that implies something about } x \text{, a colon, and finish it off with a statement including } x. $$

$$ ( \text{ and } ) \text{ are not pronounced.} $$

$$ \cdot \text{ Is pronounced "such that" and it's only used in two contexts: "for any } x \text{ such that..." and "there exists } x \text{ such that...".} $$

$$ : \text{ Is pronounced however a colon is pronounced.} $$

$$ \exists \text{ Is pronounced "there exists" and I don't think I need to explain that.} $$

$$ ¬ \text{ Is pronounced "is not" or "does not" as in "there does not exist } x \text{".} $$

$$ \in \text{ Is pronounced "is an element of" where an element of a set is a singular object that is contained in that set.} $$

$$ Ø \text{ Is pronounced "the empty set" and means "the set of which is empty inside".} $$

$$ x, y, \text{ And } z \text{ are pronounced "} x, y, \text{ And } z \text{" and they all mean "a thing that could  be an element of a set".} $$

$$ ⊆ \text{ Is pronounced "is a subset of" and I'll get to the meaning of that in the next chapter.} $$

$$ \text{capital letters are sets.} $$

$$ \iff \text{ Is pronounced "if and only if" as in "if statement } a \text{ is true, statement } b \text{ is true, and if statement } a \text{ is false, statement } b \text{ is false".} $$

$$ pow \text{ Is pronounced "the power set of" as in "} pow(S) \text{" and I'll get to the meaning in the next chapter.} $$

$$ ∩ \text{ Is pronounced "and" and means "} a ∩ b \text{ is true if and only if statement } a \text{ is true and } b \text{ is true".} $$

$$ = : \text{ Is pronounced "equals by definition" and means "define the thing on the left as the thing on the right", or was it the other way around?} $$

$$ = \text{ Is pronounced "is the same as" and I'll get to its formal meaning in the next chapter.} $$

$$ \in^S \text{ Is pronounced "is a super element of" (} S \text{ for super) and I'll get to its meaning in the next chapter.} $$

$$ ∨ \text{ Is pronounced "or" and means "} a ∨ b \text{ is true if statement } a \text{ is true or } b \text{ is true... Or both!", it can also mean the union of two sets, in that case, it is pronounced "unioned with", but I'll get to its formal meaning in the next chapter.} $$

$$ \text{succ Is pronounced "the immediate successor of" and means "that number } + 1 \text{".} $$

$$ set \text{ Is pronounced "the set containing" as in "} set(S) \text{" and I'll get to its formal meaning in the next chapter.} $$

### set theory (definitions from those definitions)?

$$ ¬ \exists (x) \cdot x \in Ø $$

$$ A ⊆ B \iff ∀(x) \cdot x \in A: x \in B $$

$$ ∀(P) \cdot ∀(U) \cdot U ⊆ S: U \in P ∩ ∀(T) \cdot T ¬ ⊆ S: T ¬ \in P: P = : pow(S) $$

$$ A = B \iff A ⊆ B ∩ B ⊆ A $$

$$ ¬ \exists (S) \cdot S \in S $$

$$ x \in \in S \iff \exists (U) \cdot U \in S ∩ x \in U $$

$$ x \in \in S \text{ can also be written as } \in^2 $$

$$ x \in \in \in S \iff \exists (U) \cdot U \in S ∩ x \in^2 U $$

$$ x \in \in \in S \text{ can also be written as } \in^3 $$

$$ x \in \in \in \in S \iff \exists (U) \cdot U \in S ∩ x \in^3 U $$

$$ x \in \in \in \in S \text{ can also be written as } \in^4 $$

$$ \vdots $$

$$ x \in^{a + b} S \iff \exists (U) \cdot U \in^a S ∩ x \in^b U $$

$$ x \in^{a + b} S \text{ can also be written as } x \in^a \in^b S $$

$$ x \in^S S \iff x \in S ∨ \exists (U) \cdot U \in S ∩ x \in^S U $$

###### .

Was [recursion](https://silaspe.github.io/maths/brainstorm.html#_1) in the rule book? I guess so.

### set theory (numbers)

$$ 0 = Ø $$

$$ \text{succ} (n) \text{ (Which mathematically equals } n + 1 \text{) Is how you would usually define numbers, so I'll define numbers that way, I'll say that succ} (n) \text{ is the set that contains all numbers } 0 \text{-} n \text{. But first: the union of two sets, denoted as an } ∨ \text{ sign.} $$

$$ x \in A ∨ B \iff x \in A ∨ x \in B $$

$$ \text{Around } 500 \text{ lines?? (I might add another definition, but at the time of typing this, this is on } 500 \text{ lines.)} $$

$$ ∀(S) \cdot E \in S ∩ ∀(T) \cdot T ¬ = E: T ¬ \in S: S = : set(E) $$

$$ \text{succ} (n) = : set(n) ∨ n $$

### set theory proofs?

No.

### bayes'?

<iframe src="https://www.desmos.com/calculator/1midapkbbr?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

[.](https://www.youtube.com/watch?v=HZGCoVF3YvM)

### counting in binary

Binary is a way to count where instead of the places: $1$, $10$, $100$, $1,000$, and so on, you use the $1$, $2$, $4$, $8$, $16$, $32$, $64$, $128$, $256$, $512$, $1,024$, $2,048$, $4,096$, $8,192$, $16,384$, $32,768$, $65,536$, $131,072$,  $262,144$, and so on for place names. (Also, if you were using binary to begin with, those would be $1$, $10$, $100$ and so on.) So the numbers $1-10$ would be $|$, $|.$, $||$, $|..$, $|.|$, $||.$, $|||$, $|...$, $|..|$, $|.|.$ (Period.) But how would you pronounce this?

$$ | = \text{ One} $$

$$ |. = \text{ Two} $$

$$ |.. = \text{ Four} $$

$$ |.... = \text{ Hex} $$

$$ |.^{|...} = \text{ Byte} $$

$$ |.^{|....} = \text{ Short} $$

$$ |.^{|.....} = \text{ Int} $$

$$ |.^{|......} = \text{ Long} $$

$$ |.^{|.......} = \text{ Overlong} $$

$$ \text{And finally,} $$

$$ |.^{|........} = |.^{Byte} = \text{ Byteplex or sha (for sha } 256 \text{)} $$

$$ \text{And then, for the other powers of two, combine the names, so } |... = |.. \text{ } \cdot \text{ } |. = \text{ Four } + \text{ Two } = \text{ Four Two. Then, to get things that are other than powers of two, combine the names of all of the powers of two that sum to it, largest to smallest. (Also, } . = \text{Zero.)} $$

$$ \text{So, } |..| = |... + | = \text{ Four two } + \text{ One } = \text{ Four Two One. But the thing is, } ||| \text{ is also pronounced "Four Two One". Okay, so, if something like that happens where the first part of the next digit is smaller than the last part of the previous digit, then... Um...} $$

#### here's a thing that I worked on for hours, but did not want to delete

$$ (\frac{D}{Dt} + \vec{\nabla}) \text{ } (\vec{E} + B) = \frac{\rho + \vec{J}}{c \epsilon_0} $$

$$ \frac{D \vec{E}}{Dt} + \vec{\nabla} \vec{E} + \frac{DB}{Dt} + \vec{\nabla} B = \frac{\rho + \vec{J}}{c \epsilon_0} $$

$$ \frac{D \vec{E}}{Dt} + \vec{\nabla} \cdot \vec{E} + \vec{\nabla} ∧ \vec{E} + \frac{DB}{Dt} + \vec{\nabla} \cdot B + \vec{\nabla} ∧ B = \frac{\rho + \vec{J}}{c \epsilon_0} $$

$$ \vec{\nabla} \cdot \vec{E} + \frac{D \vec{E}}{Dt} + \vec{\nabla} ∧ B + \vec{\nabla} ∧ \vec{E} + \frac{DB}{Dt} + \vec{\nabla} \cdot B = \frac{\rho}{c \epsilon_0} + \frac{\vec{J}}{c \epsilon_0} $$

$$ \vec{\nabla} \cdot \vec{E} = \text{A scalar} $$

$$ \frac{D \vec{E}}{Dt} + \vec{\nabla} ∧ B = \text{a vector} $$

$$ \vec{\nabla} ∧ \vec{E} + \frac{DB}{Dt} = \text{a bivector} $$

$$ \vec{\nabla} \cdot B = \text{a trivector} $$

$$ \text{And on the right hand side:} $$

$$ \frac{\rho}{c \epsilon_0} = \text{A scalar} $$

$$ \frac{\vec{J}}{c \epsilon_0} = \text{a vector.} $$

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{c \epsilon_0} $$

$$ \frac{D \vec{E}}{Dt} + \vec{\nabla} ∧ B = \frac{\vec{J}}{c \epsilon_0} $$

$$ \vec{\nabla} ∧ \vec{E} + \frac{DB}{Dt} = 0 $$

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

(insert text here)

$600$ lines.

$$ \vec{\nabla} \cdot B = 0 $$

#### ncuomdbee rr etphoe#o#r#y#

$$ \text{This chapter is about writing numbers as infinite dimensional vectors (if the vector components are } 3 \text{, } 4 \text{, } 5 \text{ and then infinite } 0 \text{'s, than it would be written as } [3 \text{, } 4 \text{, } 5 \text{, } 0 \text{, } 0 \text{, } 0...] \text{), this is how:} $$

$$ 2025000 = 2^3 \cdot 3^4 \cdot 5^5 \cdot 7^0 \cdot 11^0 \cdot 13^0 \cdot ... \rightarrow \vec{2025000} = [3 \text{, } 4 \text{, } 5 \text{, } 0 \text{, } 0 \text{, } 0...] $$

$$ \text{Before we do vector addition and scalar multiplication, here's some code:} $$

```py
def SmallestPrimeDivisor(n):
  k = 2
  while n % k != 0:
    k += 1
  return k
```

```py
def vec(n):
  primes = []
  for i in range(2, n + 1):
    if SmallestPrimeDivisor(i) = i:
      primes.append(i)
  AlmostResult = []
  for i in range(len(L)):
    p = l[i]
    power = 0
    k = n
    while k % p = 0:
      k /= p
      power += 1
    AlmostResult.append(power)
  k = 1
  while AlmostResult[len(AlmostResult) - k] = [0]:
    k += 1
  result = []
  for i in range(len(AlmostResult) - k + 1):
    result += AlmostResult[i]
  return result
```

$$ \vec{u} + \vec{v} = \vec{u \cdot v} $$

$$ c \cdot \vec{v} = \vec{v^c} $$

#### lambda simplification

$$ f(x) = g(x) → f = g $$

$$ (f ∘ g)(x) = f(g(x)) $$

$$ C(f)(a)(b) = f(b)(a) $$

$$ T_h (x)(f) = f(x) $$

$$ T_h = C(I) $$

$$ I = C ∘ C $$

$$ V(a)(b)(c) = c(a)(b) = T_h (b)(c(a)) = T_h (b)(T_h (a)(c)) = T_h (b)(T_h (a)(c)) = B(T_h (b))(T_h (a))(c) $$

$$ V(a)(b)(c) = B(T_h (b))(T_h (a))(c) $$

$$ V(a)(b) = B(T_h (b))(T_h (a)) = C(B)(T_h (a))(T_h (b)) = B(C(B)(T_h (a)))(T_h)(b) $$

$$ V(a)(b) = B(C(B)(T_h (a)))(T_h)(b) $$

$$ V(a) = B(C(B)(T_h (a)))(T_h) = C(B)(T_h)(C(B)(T_h (a))) = (C(B)(T_h) ∘ C(B) ∘ T_h)(a) $$

$$ V(a) = (C(B)(T_h) ∘ C(B) ∘ T_h)(a) $$

$$ V = (C(B)(T_h) ∘ C(B) ∘ T_h) $$

$$ V = (C(B)(C(I)) ∘ C(B) ∘ C(I)) $$

$$ V = (C(B)(C(C ∘ C)) ∘ C(B) ∘ C(C ∘ C)) $$

$$ e(a)(b) = a(b(a)) = B(a)(b)(a) = C(B(a))(a)(b) $$

$$ e(a)(b) = C(B(a))(a)(b) $$

$$ e(a) = C(B(a))(a) = (C ∘ B)(a)(a) $$

$$ W(f)(x) = f(x)(x) $$

$$ e(a) = W(C ∘ B)(a) $$

$$ e = W(C ∘ B) $$

$$ \text{Different approach!} $$

$$ e(a)(b) = a(b(a)) = a(T_h (a)(b)) = B(a)(T_h (a))(b) $$

$$ e(a)(b) = B(a)(T_h (a))(b) $$

$$ e(a) = B(a)(T_h (a)) = B(B(a))(T_h)(a) = C(B)(T_h)(B(a))(a) = (C(B)(T_h) ∘ B)(a)(a) = W(C(B)(T_h) ∘ B)(a) $$

$700$ lines, this page might beat the code repo page and become the new longest page on the website.

$$ e(a) = W(C(B)(T_h) ∘ B)(a) $$

$$ e = W(C(B)(T_h) ∘ B) $$

$$ e = W(C(B)(C(C ∘ C)) ∘ B) $$

#### (unfinished) cogputer

[finished cogputer](https://www.youtube.com/watch?v=e1Kw3yJoNxw)

| $0 \to $ | $1 \to 0$ | $2 \to 1$ | $3 \to 7$ | $4 \to 2$ | $5 \to $ | $6 \to 8$ | $7 \to $ | $8 \to 3$ | $9 \to 14$ |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------------|
|    | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
| 00 | 01 | 02 | 04 | 08 | 16 | 32 | 64 | 03 | 06 | 12 |
| 10 | 24 | 00 | 00 | 00 | 09 | 00 | 00 | 00 | 00 | 00 |
| 20 | 00 | 27 | 00 | 00 | 00 | 00 | 00 | 00 | 81 | 00 |
| 30 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 40 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 50 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 60 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 70 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 80 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| 90 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |

### logic to set theory

$$ \text{T} $$

$$ \text{F} $$

$$ \text{F} ∩ \text{F} = \text{F} $$

$$ \text{F} ∩ \text{T} = \text{F} $$

$$ \text{T} ∩ \text{F} = \text{F} $$

$$ \text{T} ∩ \text{T} = \text{T} $$

$$ p ∩ q ∩ r = p ∩ (q ∩ r) $$

$$ \text{F} ∨ \text{F} = \text{F} $$

$$ \text{F} ∨ \text{T} = \text{T} $$

$$ \text{T} ∨ \text{F} = \text{T} $$

$$ \text{T} ∨ \text{T} = \text{T} $$

$$ p ∨ q ∨ r = p ∨ (q ∨ r) $$

$$ ¬ \text{F} = \text{T} $$

$$ ¬ \text{T} = \text{F} $$

$$ \text{F} → \text{F} = \text{T} $$

$$ \text{F} → \text{T} = \text{T} $$

$$ \text{T} → \text{F} = \text{F} $$

$$ \text{T} → \text{T} = \text{T} $$

$$ (p = q = r) = (p = q) ∩ (q = r) $$

$$ (p \iff q) = (p = q) = (p → q) ∩ (q → p) $$

$$ \text{Order of operations: } ¬ > ∩ > ∨ > = > → > \iff \text{.} $$

$$ \text{E} (x; p(x)) = \text{ The extension of } p(x) \text{, the set of all } x \text{ such that } p(x) \text{ (is true) (the function } p(x) \text{ inputs, well, anything, and outputs a boolean (true or false) (e.g. is } x \text{ an odd number?)), and this is how I'm going to define sets.} $$

$$ \text{The extension of that particular function is the set of all odd numbers.} $$

$$ x \in \text{E} (y; p(y)) \iff p(x) \text{ (} = \text{T)} $$


$777$ Lines.

$$ ∀(x) \cdot p(x) \text{ (} = \text{T)}: q(x) \text{ (} = \text{T)} \iff p(x) → q(x) $$

$$ \exists (x) \cdot p(x) \text{ (} = \text{T)} \iff ¬(p(x) = \text{F}) $$

$$ 0 = Ø = \text{E} (x; \text{F}) $$

$$ \text{succ} (x) = \text{E} (y; y = x) $$

$$ \text{succ} (0) = 1 $$

$$ \text{succ} (1) = 2 $$

$$ \text{succ} (2) = 3 $$

$$ 0 \in ℕ $$

$$ x \in ℕ → \text{succ} (x) \in ℕ $$

$$ ℕ = \text{E} (x; (x = 0) ∨ \exists (y) \cdot (\text{succ} (y) = x) ∩ y \in ℕ) = \text{E} (x; (x = 0) ∨ ¬(((\text{succ} (y) = x) ∩ y \in ℕ) = \text{F})) $$


$800$ Lines.

$$ R = \text{E} (x; ¬(x \in x)) $$

$$ \text{Now, the question is, is } R \in R \text{? Because if } ¬(R \in R) \text{, than } ¬(x \in x) \text{ would be true (for } x \text{ equal to } R \text{), but then, } R \text{ would be an element of } R \text{, but if } R \in R \text{, than } ¬(x \in x) \text{ would be false (for } x \text{ equal to } R \text{), but then, } R \text{ wouldn't be an element of } R \text{, paradox! (Actually, one of the most popular paradoxes, russell's paradox.)} $$

$$ x \in \text{E} (y; p(y)) = \text{N (} \ne ℕ \text{)} \iff (¬(x \in \text{E} (y; p(y))) → p(x) = \text{T}) ∩ ((x \in \text{E} (y; p(y))) → p(x) = \text{F}) $$

$$ R \in R = \text{N} $$

$$ p(a, b, c,...) = p(a) ∩ (p(b) ∩ (p(c) ∩ (... $$

$$ x1, x2, x3, x4, x5,... \in \text{E} (x; \text{T}) $$

$$ x1 = x $$

$$ x2 = y $$

$$ x3 = z $$

$$ a, b \in ℕ $$

$$ \overline{d} $$

### projective geometry

Credit (even if it is very small): [The two points that lie on every circle (???) #SoME3](https://www.youtube.com/watch?v=iUUm0sKLoiE), [Putting Algebraic Curves in Perspective](https://www.youtube.com/watch?v=XXzhqStLG-4), and [Extraordinary Conics: The Most Difficult Math Problem I Ever Solved](https://www.youtube.com/watch?v=X83vac2uTUs).

Yes, I know, the last one was added literally $4$ days ago, but I thougt of something else to talk about.

Let's say that a point $(a: b)$ (as opposed to $(a, b)$) is equal to $(ca: cb)$ $(c \ne 0)$, so every* (and that's a big asterisk) point $(a: b)$ can be scaled onto $(\frac{a}{b}: 1)$, a kind of number line.

*unless $b = 0$, then we add this kind of "point at infinity" to our number line (it's a single point because the point $(a: 0)$ can be scaled to $(1: 0)$ (aka the point at infinity), that is, of coarse, unless $a = 0$, but that point isn't really aloud for the same reason as $\frac{0}{0}$) making it the real projective line or $ℝ \text{P}^1$.

The reason why it's at infinity is because, if you consider the point $(1: 1)$, it falls onto $1$ on the number line, the point $(1: \frac{1}{2})$ falls onto $2$, the point $(1: \frac{1}{4})$ falls onto $4$, the point $(1: \frac{1}{8})$ falls onto $8$, and as the second number gets smaller, the point on the number line gets bigger approaching infinity, hence the name "point at infinity". But, if you instead do this from the other direction, it approaches negative infinity. You can imagine a number line that curves down as it goes along, consecutive integers getting closer and closer, and an unsigned infinity at the bottom where the line meets itself.

Stepping a dimension up, you get the real projective plane or $ℝ \text{P}^2$, $(a: b: c) = (da: db: dc)$, most numbers going to $(\frac{a}{c}: \frac{b}{c}: 1)$, some becoming $(\frac{a}{b}: 1: 0)$, less becoming $(1: 0: 0)$, the point at infinity becomes a line at infinity (more of a circle, but $1$ degree of freedom, so it's a line), and the number line becomes a space of all points.

There is a problem though (that is big enough to be explained on a line by itself), you could imagine the same process that I used to prove the unsigned infinity thing but in $ℝ \text{P}^2$ to get the unsurprising result of $(a: b: 0) = (-a: -b: 0)$. This does mean that, when drawing the regular or affine plane, and drawing a circle around it (to represent the line at infinity of coarse), if you wanted to draw, say, the point $(1: 1: 0)$, it would need to be at both the very top right, and the very bottom left of the circle.

To see why this double counting thing makes sense, I'll project onto a unit sphere, so, if $r = \sqrt{a^2 + b^2 + c^2}$, the point $(a: b: c)$ maps to $(\frac{a}{r}: \frac{b}{r}: \frac{c}{r})$. You might see the problem though, it also maps to $(-\frac{a}{r}: -\frac{b}{r}: -\frac{c}{r})$, because it's also on the unit sphere. So, if you just consider the top half of the sphere (including the equator so that points at infinity are accounted for), it counts almost every point once, and points at infinity twice, kinda like the one where we projected onto the plane parallel to and one unit above the $xy$ plane. So, to fix this problem, and give every point the same treatment, you (counterintuitively) count every point twice by using the entire sphere, kinda like giving every line in $2d$ an angle instead of a slope to fix the vertical lines problem, at the cost of there being two angles for every line.

[Here's a desmos graph](https://www.desmos.com/3d/zzoajkphnn).

Yes, I know, the plane is placed one unit below the sphere instead of one above, but it's only like that for the sake of demonstration.

### duality

It's hard to explain how points are dual to lines, but an example would be the origin and the line at infinity, or on the sphere, the equator and the north and south poles (remember, two solutions). The more general definition would be something like this: the two points on a sphere, a point on the dual line, and the point $90°$ away but still on the dual line are all mutually perpendicular. By the way, points on the plane project to antipodal points on the sphere, and lines on the plane project to great circles on the sphere.

Also fun fact: the duals of every point on a line would all pass through the dual point, and the duals of every line that passes through a point would all lie on the dual line.

### linear algebra, complex numbers, and higher dimensional complex numbers?

$$ \text{Let's say that a vector } \vec{v} \text{ is an ordered set of numbers } \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} \text{, or } v_x \hat{x} + v_y \hat{y} \text{, or a point } (v_x, v_y) \text{, or an arrow with it's tip at } (v_x, v_y) \text{, and tail at } (0, 0) \text{. They can be scaled (that is, multiplied by a scalar or real number) (} c \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = c(v_x \hat{x} + v_y \hat{y} = c v_x \hat{x} + c v_y \hat{y}) = \begin{bmatrix} c v_x \\
c v_y \\ \end{bmatrix} \text{), added (} \begin{bmatrix} u_x \\
u_y \\ \end{bmatrix} + \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = u_x \hat{x} + u_y \hat{y} + v_x \hat{x} + v_y \hat{y} = (u_x + v_x) \hat{x} + (u_y + v_y) \hat{y} = \begin{bmatrix} u_x + v_x \\
u_y + v_y \\ \end{bmatrix} \text{), and with just those two, any vector can be made from } \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} \text{ and } \begin{bmatrix} 0 \\
1 \\ \end{bmatrix} \text{ (that is, } 1 \hat{x} + 0 \hat{y} \text{ and } 0 \hat{x} + 1 \hat{y} \text{ (that is, } \hat{x} \text{ and } \hat{y} \text{)), and that's pretty much it.} $$

You can also multiply vectors, but that's a [story for another day](https://silaspe.github.io/maths/geometric_algebra.html).

$$ \text{Let's say that a matrix } A \text{ is also an ordered set of numbers arranged in a square: } \begin{bmatrix} a_{11} & a_{21} \\
a_{12} & a_{22} \\ \end{bmatrix} \text{ that denotes a linear transformation (every linear transformation has a corrasponding matrix, and every matrix has a corrasponding linear transformation), a type of function that, among other things, acts on vectors. ( A matrix } A \text{ applied to a vector } \vec{v} \text{ is denoted as }  A \vec{v} \text{ btw.) Matrix operations are linear (the linear part of linear algebra), that is, } A(c \vec{v}) = c(A \vec{v}) \text{, and } A(\vec{u} + \vec{v}) = A \vec{u} + A \vec{v} \text{. So all you need to describe a linear transformation is how it affects the basis vectors (} \hat{x} \text{ and } \hat{y} \text{), thankfully, it's right there in the columns, } \begin{bmatrix} a_{11} & a_{21} \\
a_{12} & a_{22} \\ \end{bmatrix} \hat{x} = \begin{bmatrix} a_{11} \\
a_{12} \\ \end{bmatrix} \text{, and } \begin{bmatrix} a_{11} & a_{21} \\
a_{12} & a_{22} \\ \end{bmatrix} \hat{y} = \begin{bmatrix} a_{21} \\
a_{22} \\ \end{bmatrix} \text{.} $$

$$ \text{Now, I can derive a formula for matrix vector multiplication!} $$

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} v_x \\
v_x \\ \end{bmatrix} = \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (v_x \hat{x} + v_y \hat{y}) = \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (v_x \hat{x}) + \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (v_y \hat{y}) = v_x \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \hat{x} + v_y \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \hat{y} = v_x \begin{bmatrix} a \\
c \\ \end{bmatrix} + v_y \begin{bmatrix} b \\
d \\ \end{bmatrix} \hat{y} = \begin{bmatrix} v_x a \\
v_x c \\ \end{bmatrix} + \begin{bmatrix} v_y b \\
v_y d \\ \end{bmatrix} $$

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = \begin{bmatrix} v_x a + v_y b \\
v_x c + v_y d \\ \end{bmatrix} $$

$$ \text{Next, matrix multiplication!} $$

$$ \text{I'll define } AB \text{ like this: } (AB) \vec{v} = A(B \vec{v}) \text{, and I'll derive the formula like this:} $$

$$ \text{Actually, too hard.} $$


$900$ Lines.

$$ \text{And if you were wondering, this also works in } 3d \text{ or higher, with } \hat{z} \text{, } \hat{w} \text{, and so on.} $$

$$ \text{Next, complex numbers!} $$

Complex numbers are, if I'm gonna quote Morphocular in [this video](https://www.youtube.com/watch?v=4KlvI_uK9zs&t=470s), the language of $2d$ rotation. I'll describe them in an unusual way:

$$ \text{Let's say that I want to rotate a vector } \vec{v} \text{ or } \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} \text{ by an angle } \theta \text{ in the plane, well, there's only one plane, and from } \hat{x} \text{ to } \hat{y} \text{, the result is } \begin{bmatrix} v_x cos(\theta) - v_y sin(\theta) \\
v_x sin(\theta) + v_y cos(\theta) \\ \end{bmatrix} \text{, which happens to equal } \begin{bmatrix} cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta) \\ \end{bmatrix} \vec{v} \text{.} $$

$$ \text{I'll take a simple rotation like } \theta = 90° \text{, and give it a name: } i \text{ (yes, complex numbers } i \text{), so } i = \begin{bmatrix} cos(90°) & - sin(90°) \\
sin(90°) & cos(90°) \\ \end{bmatrix} = \begin{bmatrix} 0 & -1 \\
1 & 0 \\ \end{bmatrix} \text{, let's see what happens if we square } i $$

$$ i^2 \vec{v} = (ii) \vec{v} = i(i \vec{v}) = i(i \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix}) = i \begin{bmatrix} -v_y \\
v_x \\ \end{bmatrix} = \begin{bmatrix} -v_x \\
-v_y \\ \end{bmatrix} $$

$$ i^2 \vec{v} = -\vec{v} $$

$$ i^2 = -1 ?!?!?! $$

$$ \text{Ok, you might have seen that one coming.} $$

$$ \text{Time for euler's identity!} $$

$$ e^{i \theta} = cos(\theta) + isin(\theta) $$

$$ \text{I know what you're thinking: Why? And how? Well, first, if you have two matrices } A \text{ and } B \text{, } A + B \text{ is equal to the termwise sum of } A \text{ and } B \text{. And, you'll have to trust me on this, but } (A + B) \vec{v} = A \vec{v} + B \vec{v} \text{. And second, the matrix } \begin{bmatrix} 1 & 0 \\
0 & 1 \\ \end{bmatrix} \text{ (aka } I \text{) is equal to } 1 \text{ (} 1 \text{ times anything is that thing, and } I \text{ times anything is that thing, hence, } I = 1 \text{). Now time to figure out what } e^{i \theta} \text{ is.} $$

$$ cos(\theta) + isin(\theta) = \begin{bmatrix} 1 & 0 \\
0 & 1 \\ \end{bmatrix} cos(\theta) + \begin{bmatrix} 0 & -1 \\
1 & 0 \\ \end{bmatrix} sin(\theta) = \begin{bmatrix} cos(\theta) & 0 \\
0 & cos(\theta) \\ \end{bmatrix} + \begin{bmatrix} 0 & -sin(\theta) \\
sin(\theta) & 0 \\ \end{bmatrix} = \begin{bmatrix} cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta) \\ \end{bmatrix} $$

$$ e^{i \theta} = \begin{bmatrix} cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta) \\ \end{bmatrix} $$

$$ \text{So, if you want to rotate a vector } \vec{v} \text{ with an angle } \theta \text{ from } \hat{x} \text{ to } \hat{y} \text{, it's just } e^{i \theta} \vec{v} \text{!} $$

$$ \text{And this would technically also work in } 3d \text{ or higher. You could say that } i = \begin{bmatrix} 0 & -1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1 \\ \end{bmatrix} \text{, } j = \begin{bmatrix} 0 & 0 & -1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\ \end{bmatrix} \text{, } k = \begin{bmatrix} 1 & 0 & 0 \\
0 & 0 & -1 \\
0 & 1 & 0 \\ \end{bmatrix} \text{, then you would have } e^{i \theta} \text{, } e^{j \theta} \text{, and } e^{k \theta} \text{ for the } xy \text{, } xz \text{, and } yz \text{ planes respectively.} $$

If you want a better rotation formula, [here](https://www.youtube.com/watch?v=Y1gOYtQYRXo) [it is!](https://www.youtube.com/watch?v=i0cp3iQXSk8)

### homogenization

Homogenization is a method of interpolation from equations on the affine plane (non-projective plane) to equations on the projective plane (so, adding the line at infinity), but I think it would be better if I just showed how to do it.

Let's say that I have these equations for describing my line:

$$ y = mx + b $$

$$ z = 1 $$

so, we have this equation:

$$ (x: y: z) = (x: mx + b: 1) $$

$$ (x, y, z) = (cx, cmx + cb, c) $$

and from those, I have this new equation for describing my line:

$$ y = mx + bz $$

Now, the equation is homogeneous $^1$.

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


$1000$ Lines, wow.

Y'know how any two distinct points on the affine plane have a line through them? And how (almost) any two distinct lines on the affine plane have a point on both? That is, of course, unless the lines are parallel. Solution: homogenization. A homogenized line with slope $m$ has the point $(1: m: 0)$ (and $(0: 1: 0)$ if the line is vertical). So, if two lines have the same slope $m$ (and are distinct), then they don't meet normally, and they intersect at $(1: m: 0)$. If they have different slopes, then they do meet normally, and they don't intersect at the line at infinity. But what about the "any two distinct points have a line through them" rule? If you have a normal point and a point at infinity $(1: m: 0)$, they have the line with slope $m$ going through the first one. But what if you have two points on the line at infinity? This (among other things) is why it's called the line at infinity, a line that all points at infinity lie on.

#### greek letters

| Alpha | Beta | Gamma | Delta | Epsilon | Zeta | Eta | Theta | Iota | Kappa | Lambda | Mu | Nu | Xi | Omicron | Pi | Rho | Sigma (yes, actualy) | Tau | Upsilon | Phi | Chi | Psi | Omega |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| $\alpha$ | $\beta$ | $\gamma$ | $\delta$ | $\epsilon$ | $\zeta$ | $\eta$ | $\theta$ | $\iota$ | $\kappa$ | $\lambda$ | $\mu$ | $\nu$ | $\xi$ | $\omicron$ | $\pi$ | $\rho$ | $\sigma$ | $\tau$ | $\upsilon$ | $\phi$ | $\chi$ | $\psi$ | $\omega$ |
| $\Alpha$ | $\Beta$ | $\Gamma$ | $\Delta$ | $\Epsilon$ | $\Zeta$ | $\Eta$ | $\Theta$ | $\Iota$ | $\Kappa$ | $\Lambda$ | $\Mu$ | $\Nu$ | $\Xi$ | $\Omicron$ | $\Pi$ | $\Rho$ | $\Sigma$ | $\Tau$ | $\Upsilon$ | $\Phi$ | $\Chi$ | $\Psi$ | $\Omega$ |
| A | B |  |  | E | Z | H |  | I | K |  | M | N |  | O |  | P |  | T |  |  | X |  |  |

#### cursed math

$$ \int i \text{ } dt = \iota $$

#### fixed point combinators

When I say "fixed point combinator", what I really mean is a combinator $p$ such that $f(p(f)) = p(f)$. The term "fixed point" just means: $x$ is a fixed point of $f$ if and only if $f(x) = x$. The puzzle of constructing your own fixed point combinator is a puzzle found in the lambda paper after showing you the $\text{Y}$ combinator and the older turing fixed point combinator $\Theta$. In both of them, $p(f)$ reduces to $f(p(f))$. Here's a proof:

$$ \text{Y} = \lambda f. (\lambda x. f(x(x)))(\lambda x. f(x(x))) $$

$$ \text{Y} (f) = (\lambda f. (\lambda x. f(x(x)))(\lambda x. f(x(x))))(f) = (\lambda x. f(x(x)))(\lambda x. f(x(x))) = f((\lambda x. f(x(x)))(\lambda x. f(x(x)))) = f((\lambda f. (\lambda x. f(x(x)))(\lambda x. f(x(x))))(f)) = f(\text{Y} (f)) $$

$$ \text{Y} (f) = f(\text{Y} (f)) $$

$$ \Theta = A(A) $$

$$ A = \lambda xy. y(x(x)(y)) $$

$$ \Theta (f) = A(A)(f) = (\lambda xy. y(x(x)(y)))(A)(f) = f(A(A)(f)) = f(\Theta (f)) $$

$$ \Theta (f) = f(\Theta (f)) $$

But this challenge of making your own fixed point combinator is really easy (I'll use the Theta combinator as an example): first, we need a combinator that reduces to itself, a self referential combinator (such as $\Omega$ or $\text{M} (\text{M})$ or $(\lambda x. x(x))(\lambda x. x(x))$, they're all the same thing. Actually, I'm gonna re derive The Omega). And for that, we need a form, where a form has some $f$s, maybe $x$s and $y$s where it is $f$ of single things (so no $f(x(y))$s), one of which is another $f$. The one that I'm gonna use (and the simplest one) is $f(f)$. To make a self referential combinator out of this, we're gonna need to make a combinator $A$ where $A(A)$ reduces to itself. That is, $A$ of all the given inputs (just $A$) returns $A(A)$. So $A$, if you exaluate it on $A$, you get $A(A)$. So $A$ must be the self application combinator $\lambda x. x(x)$. To turn this self referential combinator into a fixed point combinator, you just need to make $A(A)(f)$ equal to $A(A)(f)$. But, to avoid confusion with the original $A$ (not the one in the turing fixed point combinator), I'll call it $B$. First, as a starting point, $B$ should equal $A$ but with one more input (so $B = \lambda xy. x(x)(y)$). And, now that $B$ can factor in $f$, we can make $B$ of $B$ and $f$ output $f(B(B)(f))$. But this is easy, just change the definition of $B$ to $\lambda xy. y(x(x)(y))$. And we now have $\Theta$.

#### linear systems of equations

$$ A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\ \end{bmatrix} $$

$$ \vec{x} = \begin{bmatrix} x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_n \\ \end{bmatrix} $$

$$ \vec{v} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_n \\ \end{bmatrix} $$

$$ A \vec{x} = \vec{v} $$

$$ \vec{x} = ? $$

$$ A \vec{x} = A \begin{bmatrix} x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_n \\ \end{bmatrix} = A (x_1 \hat{x} + x_2 \hat{y} + x_3 \hat{z} + \dots + x_n \hat{\omega}) = A x_1 \hat{x} + A x_2 \hat{y} + A x_3 \hat{z} + \dots + A x_n \hat{\omega} = x_1 A \hat{x} + x_2 A \hat{y} + x_3 A \hat{z} + \dots + x_n A \hat{\omega} : = x_1 \begin{bmatrix} a_{11} \\
a_{21} \\
a_{31} \\
\vdots \\
a_{n1} \\ \end{bmatrix} + x_2 \begin{bmatrix} a_{12} \\
a_{22} \\
a_{32} \\
\vdots \\
a_{n2} \\ \end{bmatrix} + x_3 \begin{bmatrix} a_{13} \\
a_{23} \\
a_{33} \\
\vdots \\
a_{n3} \\ \end{bmatrix} + \dots + x_n \begin{bmatrix} a_{1n} \\
a_{2n} \\
a_{3n} \\
\vdots \\
a_{nn} \\ \end{bmatrix} = \begin{bmatrix} x_1 a_{11} \\
x_1 a_{21} \\
x_1 a_{31} \\
\vdots \\
x_1 a_{n1} \\ \end{bmatrix} + \begin{bmatrix} x_2 a_{12} \\
x_2 a_{22} \\
x_2 a_{32} \\
\vdots \\
x_2 a_{n2} \\ \end{bmatrix} + \begin{bmatrix} x_3 a_{13} \\
x_3 a_{23} \\
x_3 a_{33} \\
\vdots \\
x_3 a_{n3} \\ \end{bmatrix} + \dots + \begin{bmatrix} x_n a_{1n} \\
x_n a_{2n} \\
x_n a_{3n} \\
\vdots \\
x_n a_{nn} \\ \end{bmatrix} = \begin{bmatrix} x_1 a_{11} + x_2 a_{12} + x_3 a_{13} + \dots + x_n a_{1n} \\
x_1 a_{21} + x_2 a_{22} + x_3 a_{23} + \dots + x_n a_{2n} \\
x_1 a_{31} + x_2 a_{32} + x_3 a_{33} + \dots + x_n a_{3n} \\
\vdots \\
x_1 a_{n1} + x_2 a_{n2} + x_3 a_{n3} + \dots + x_n a_{nn} \\ \end{bmatrix} $$

$1102$ Lines.

$$ \begin{bmatrix} x_1 a_{11} + x_2 a_{12} + x_3 a_{13} + \dots + x_n a_{1n} \\
x_1 a_{21} + x_2 a_{22} + x_3 a_{23} + \dots + x_n a_{2n} \\
x_1 a_{31} + x_2 a_{32} + x_3 a_{33} + \dots + x_n a_{3n} \\
\vdots \\
x_1 a_{n1} + x_2 a_{n2} + x_3 a_{n3} + \dots + x_n a_{nn} \\ \end{bmatrix} = \vec{v} $$

$$ \begin{bmatrix} x_1 a_{11} + x_2 a_{12} + x_3 a_{13} + \dots + x_n a_{1n} \\
x_1 a_{21} + x_2 a_{22} + x_3 a_{23} + \dots + x_n a_{2n} \\
x_1 a_{31} + x_2 a_{32} + x_3 a_{33} + \dots + x_n a_{3n} \\
\vdots \\
x_1 a_{n1} + x_2 a_{n2} + x_3 a_{n3} + \dots + x_n a_{nn} \\ \end{bmatrix} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_n \\ \end{bmatrix} $$

$$ x_1 a_{11} + x_2 a_{12} + x_3 a_{13} + \dots + x_n a_{1n} = v_1 $$

$$ x_1 a_{21} + x_2 a_{22} + x_3 a_{23} + \dots + x_n a_{2n} = v_2 $$

$$ x_1 a_{31} + x_2 a_{32} + x_3 a_{33} + \dots + x_n a_{3n} = v_3 $$

$$ \vdots $$

$$ x_1 a_{n1} + x_2 a_{n2} + x_3 a_{n3} + \dots + x_n a_{nn} = v_n $$

### linear algebra

This will be a series of subchapters about linear algebra. In particular, the more general mathmetician's version. But if you want some more intuition about how it works, each subchapter will have a corrasponding part in [this playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab). The first thing to do in linear algebra is to...

### part $1$: choose your fighte- vector space!

As you might know, the main thing in linear algebra is the vector. so, to make this as general as possible, I'm gonna let you make your own vector space (space in which vectors live). Something important that defines a vector is that there's a sense of vector $\vec{u} + \vec{v}$ (for vectors $\vec{u}$ and $\vec{v}$) and there's a sense of vector $c \vec{v}$ (for vector $\vec{v}$ and scalar (real number) $c$). But, you cannot (necessarily) multiply vectors or add vectors and scalars (unless you use geometric algebra). But, for something to quallify as a vector space, there are some more rules/axioms it has to follow: (assume that your vector space is denoted as $\text{V}$ with vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ and scalars $x$, $y$, and $z$)

Rule #$1$:

$\vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}$

Rule #$2$:

$\vec{u} + \vec{v} = \vec{v} + \vec{u}$

Rule #$3$ with words:

There is a vector $\vec{0}$ aka "the zero vector" such that $\vec{v} + \vec{0} = \vec{v}$ for all $\vec{v}$

Rule #$3$ with set theory:

$\exists \vec{0} \in \text{V}. ∀ \vec{v} \in \text{V}. \vec{v} + \vec{0} = \vec{v}$

Rule #$4$ with words:

For any $\vec{v}$ there is a $-\vec{v}$ such that $\vec{v} + (-\vec{v}) = \vec{0}$ for all $\vec{v}$

Rule #$4$ with set theory:

$∀ \vec{v} \in \text{V}. \exists -\vec{v} \in \text{V}. \vec{v} + (-\vec{v}) = \vec{0}$

Rule #$5$:

$x(y \vec{v}) = (xy) \vec{v}$

Rule #$6$:

$1 \vec{v} = \vec{v}$

Rule #$7$:

$x(\vec{u} + \vec{v}) = x \vec{u} + x \vec{v}$

Rule #$8$:

$(x + y) \vec{v} = x \vec{v} + y \vec{v}$

The vector space that (at least to me) makes all of the intuition click is arrows in space where it's the same if it has the same length and direction (hence the little arrow over every vector). The result of adding two of them is putting the base of the second on the tip of the first and drawing a new arrow from the base of the first to the tip of the second. The result of multiplying one of these by a number is scaling the length by a factor of the number (hence the name) and flipping the vector and scaling the length by a factor of the absolute value of the number if it is negative. You can convince yourself that this is a vector space. Also, these sorts of vectors are usually rooted at the origin.

another commonly used definition of a vector is that of lists of numbers. The result of adding two of them is adding them term by term and the result of multiplying one of these by a number is multiplying each term by said number. You can convince yourself that this is a vector space.

You can convert from the first definition to the second by making a list of the vector's coordinates and doing the opposite to convert from a list of numbers to an arrow.

Now that you have chosen a vector space, we can now move on to...

### part $2$: linear combinations, span, and basis vectors

In $2d$ (arrows of length $1$ or list of two numbers) there are vectors that will prove to be very important. The first being called $\hat{x}$ (x hat), the unit vector pointing to the right (in the direction in the $x$ axis) or the list of numbers $\begin{bmatrix} 1 \\
0 \\ \end{bmatrix}$ (vectors that are of length $1$ are denoted with a hat) and $\hat{y}$ (y hat) the unit vector pointing up (in the direction in the $y$ axis). AKA the list of numbers $\begin{bmatrix} 0 \\
1 \\ \end{bmatrix}$.

If you think about it, any $2d$ vector $\begin{bmatrix} x \\
y \\ \end{bmatrix}$ can be written in terms of $\hat{x}$ and $\hat{y}$ (i.e. $x \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} = \begin{bmatrix} x \\
0 \\ \end{bmatrix}$, $y \begin{bmatrix} 0 \\
1 \\ \end{bmatrix} = \begin{bmatrix} 0 \\
y \\ \end{bmatrix}$, $\begin{bmatrix} x \\
0 \\ \end{bmatrix} + \begin{bmatrix} 0 \\
y \\ \end{bmatrix} = \begin{bmatrix} x \\
y \\ \end{bmatrix}$).

$1200$ Lines.

Alternatively (and you might need a grid for this), you can take the unit vector in the x direction and scale it until it's tip is on the same vertical line as the tip of your vector and the same thing with the y direction. And, when you add them up, (you can deduce that) you get your original vector. This can be used as another way to go back and forth between the two definitions of a vector.

By the way, this is called a linear combination of $\hat{x}$ and $\hat{y}$ (linear because if you fix one and vary the other, it traces out a line if you look at the tip of the result).

For this reason that every $2d$ vector can be made out of $\hat{x}$ and $\hat{y}$, they are called the basis vectors.

Also, Every Vector that can be formed by adding and scaling $\hat{x}$, $\hat{y}, and any other vector formed in this way is of the form $a \hat{x} + b \hat{y}$, and the reason why is because $(a \hat{x} + b \hat{y}) + c \hat{x} + d \hat{y} = (a + c) \hat{x} + (b + d) \hat{y}$ and $c(a \hat{x} + b \hat{y}) = (a) \hat{x} + (cb) \hat{y}$.

Also by the way, $a \vec{u} + b \vec{v}$ is called a linear combination of $\vec{u}$ and $\vec{v}$.

But this begs the question: we could've used any other two basis vectors and we would've gotten another completely sensible way of going back and forth between the two definitions of a vector. That is, of course, unless the two vectors that are aligned with each other (or are both the zero vector).

By the way, the set of all the vectors that can be made with a linear combination of two vectors is called the span of those two vectors. This idea of using different basis vectors, aka a different basis, is something that I'll go much more in detail about later.

Also, if you have just one vector, think of it as an arrow, but if you have many vectors, think of each of them as a point where the point lies at the tip of the vector.

But, things get more interesting in $3d$, now it's $a \vec{u} + b \vec{v} + c \vec{w}$ for scalars $a$, $b$, $c$. And if the third is in the span of the other two, it doesn't change the span and it's still a flat sheet cutting through the origin.

You can imagine the first two forming a plane and then the third one moving the plane around sweeping it through space. Another intuition is that you're using all three scalars to your advantage, you can't replace one of them with the other two.

Whenever you can remove a vector without changing its span it is also known as linearly dependent, but $\hat{z}$ signed the declaration of independence ~$250$ years ago, so they span all of $3d$ space.

So, the more formal definition of a basis is a set of linearly independent vectors that span all of space.

### part $3$: matrices and linear transformations


Let's start off this part with a quote:


$1234$ lines.

No one really understands The Matrix, you just have to see for yourself

-Morpheus

Jokes Aside, for this part I'm going to be talking about linear transformations. Transformation is just a fancy word for function (In this context, it's a function that inputs and outputs vectors), but what makes it linear is that it preserves the two operations of vector addition and scalar multiplication, that is, $L(\vec{u} + \vec{v}) = L(\vec{u}) + L(\vec{v})$ and $L(c \vec{v}) = c L(\vec{v})$ (I'll explain why the word linear is used later).

But, if you were given one of these guys, how would you describe it numerically? What is $L(\vec{v})$?

Well, describe $\vec{v}$ as a linear combination of $\hat{x}$ and $\hat{y}$, so $v_x \hat{x} + v_y \hat{y}$

$$ L(\vec{v}) = L(v_x \hat{x} + v_y \hat{y}) = L(v_x \hat{x}) + L(v_y \hat{y}) = v_x L(\hat{x}) + v_y L(\hat{y}) $$

This is why it's called a linear transformation, $L(\vec{v})$ is a linear combination of $L(\hat{x})$ and $L(\hat{y})$

So, literally all you need to define a ($2d$) linear transformation is where $\hat{x}$ and $\hat{y}$ each go.

Here's a concrete example: let's say that the transformation applied to $\hat{x}$ is $\begin{bmatrix} 1 \\
-2 \\ \end{bmatrix}$ and the transformation applied to $\hat{y}$ is $\begin{bmatrix} 3 \\
0 \\ \end{bmatrix}$, then the transformation applied to $-1 \hat{x} + 2 \hat{y}$ should be $-1 \begin{bmatrix} 1 \\
-2 \\ \end{bmatrix} + 2 \begin{bmatrix} 3 \\
0 \\ \end{bmatrix} = \begin{bmatrix} (-1)(1) + (2)(3) \\
(-1)(-2) + (2)(0) \\ \end{bmatrix} = \begin{bmatrix} 5 \\
2 \\ \end{bmatrix}$

Ok, got all that?

In general, this transformation applied to $\begin{bmatrix} x \\
y \\ \end{bmatrix}$ is $\begin{bmatrix} 1x + 3y \\
-2x + 0y$. You give me any vector and I tell you the output vector.

What I'm saying is that the linear transformation $L$ is completely determined by four numbers: the $x$ coordinate of the transformed $\hat{x}$, the y coordinate of the transformed $\hat{x}$, the $x$ coordinate of the transformed $\hat{y}$, and the y coordinate of the transformed $\hat{y}$.

Usually how you write a linear transformation is with a $2x2$ group of numbers, also called a called a $2x2$ matrix. You can read off the first column as where $\hat{x}$ goes and the second as where $\hat{y}$ goes.

By the way, a matrix $A$ times a vector $\vec{v}$

If you're given a matrix describing a linear transformation and you're also given some specific vector and you want to compute the linear transformation evaluated on said vector, you multiply the coordinates of the vector by the columns of the matrix and adding up the results.

Here's a concrete example:

$$ \begin{bmatrix} 3 & 2 \\
-2 & 1 \\ \end{bmatrix} \begin{bmatrix} 5 \\
7 \\ \end{bmatrix} = 5 \begin{bmatrix} 3 \\
-2 \\ \end{bmatrix} + 7 \begin{bmatrix} 2 \\
1 \\ \end{bmatrix} = 5 \begin{bmatrix} 3 \\
-2 \\ \end{bmatrix} + 7 \begin{bmatrix} 2 \\
1 \\ \end{bmatrix} = \dots = \begin{bmatrix} 29 \\
-3 \\ \end{bmatrix} $$

What about the most general possible example of matrix vector multiplication:

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} x \\
y \\ \end{bmatrix} = x \begin{bmatrix} a \\
c \\ \end{bmatrix} + y \begin{bmatrix} b \\
d \\ \end{bmatrix} = \begin{bmatrix} ax \\
cx \\ \end{bmatrix} + \begin{bmatrix} by \\
dy \\ \end{bmatrix} $$

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} x \\
y \\ \end{bmatrix} = \begin{bmatrix} ax + by \\
cx + dy \\ \end{bmatrix} $$

$1300$ Lines.

You could even use this formula as a definition. And then you could teach it to high schoolers worldwide and not teach them the key intuition that makes it intuitive ($x \begin{bmatrix} a \\
c \\ \end{bmatrix} + y \begin{bmatrix} b \\
d \\ \end{bmatrix}$)

Isn't it better to think of the columns of the matrix as where $\hat{x}$ and $\hat{y}$ each go and the result of multiplying a matrix by a vector as the appropriate linear combination?

How would you describe a linear transformation like a 90° counterclockwise rotation? (Yes, that is a linear transformation.) Well, $\hat{x}$ gets shifted up towards $\begin{bmatrix} 0 \\
1 \\ \end{bmatrix}$ ($\hat{y}$) and $\hat{y}$ gets rotated down towards $\begin{bmatrix} -1 \\
0 \\ \end{bmatrix}$ ($-\hat{x}$). So the result should be the matrix $\begin{bmatrix} 0 & -1 \\
1 & 0$, and if you want to rotate any vector clockwise by 90 degrees, just multiply it by the matrix $\begin{bmatrix} 0 & -1 \\
1 & 0$.

On the other hand, if the two columns are linearly dependent, the transformation squishes all of space onto one line, the span of the two linearly dependent columns.

Summary:

linear transformations are those that preserve the operations of vector addition and scalar multiplication, of which you can think of as transformations of space that keep the grid lines parallel and evenly spaced with the origin remaining fixed. But to describe your linear transformation, you only need a handful of numbers: the coordinates of where the basis vectors land. matrices give us a language for linear transformations: just read off the columns and you'll know where the basis vectors land. And matrix vector multiplication just tells you what the linear transformation does to a given vector.

#### linear systems of equations (but with sum notation)

$$ A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1k} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2k} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3k} & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots &  & \vdots \\
a_{k1} & a_{k2} & a_{k3} & \dots & a_{kk} & \dots & a_{kn} \\
\vdots & \vdots & \vdots &  & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nk} & \dots & a_{nn} \\ \end{bmatrix} $$

$$ \vec{x} = \begin{bmatrix} x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_k \\
\vdots \\
x_n \\ \end{bmatrix} $$

$$ \vec{v} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_k \\
\vdots \\
v_n \\ \end{bmatrix} $$

$$ A \vec{x} = \vec{v} $$

$$ \vec{x} = ? $$

$$ A \vec{x} = A \begin{bmatrix} x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_k \\
\vdots \\
x_n \\ \end{bmatrix} = A(\sum\limits_{k = 1}^{n} x_k e_k) = \sum\limits_{k = 1}^{n} A x_k e_k = \sum\limits_{k = 1}^{n} x_k A e_k : = \sum\limits_{k = 1}^{n} x_k \begin{bmatrix} a_{1k} \\
a_{2k} \\
a_{3k} \\
\vdots \\
a_{mk} \\
\vdots \\
a_{nk} \\ \end{bmatrix} = \sum\limits_{k = 1}^{n} \begin{bmatrix} x_k a_{1k} \\
x_k a_{2k} \\
x_k a_{3k} \\
\vdots \\
x_k a_{mk} \\
\vdots \\
x_k a_{nk} \\ \end{bmatrix} = \begin{bmatrix} \sum\limits_{k = 1}^{n} x_k a_{1k} \\
\sum\limits_{k = 1}^{n} x_k a_{2k} \\
\sum\limits_{k = 1}^{n} x_k a_{3k} \\
\vdots \\
\sum\limits_{k = 1}^{n} x_k a_{mk} \\
\vdots \\
\sum\limits_{k = 1}^{n} x_k a_{nk} \\ \end{bmatrix} $$

$$ \begin{bmatrix} \sum\limits_{k = 1}^{n} x_k a_{1k} \\
\sum\limits_{k = 1}^{n} x_k a_{2k} \\
\sum\limits_{k = 1}^{n} x_k a_{3k} \\
\vdots \\
\sum\limits_{k = 1}^{n} x_k a_{mk} \\
\vdots \\
\sum\limits_{k = 1}^{n} x_k a_{nk} \\ \end{bmatrix} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_k \\
\vdots \\
v_n \\ \end{bmatrix} $$

$$ \sum\limits_{k = 1}^{n} a_{1k} x_k = v_1 $$

$$ \sum\limits_{k = 1}^{n} a_{2k} x_k = v_2 $$

$$ \sum\limits_{k = 1}^{n} a_{3k} x_k = v_3 $$

$$ \vdots $$

$$ \sum\limits_{k = 1}^{n} a_{mk} x_k = v_m $$

$1400$ lines.

$$ \vdots $$

$$ \sum\limits_{k = 1}^{n} a_{nk} x_k = v_n $$

#### solutions to said linear systems of equations

$$ \sum\limits_{k = 1}^{n} a_{1k} x_k = v_1 $$

$$ x_1 a_{11} + \sum\limits_{k = 2}^{n} a_{1k} x_k = v_1 $$

$$ x_1 a_{11} = v_1 - \sum\limits_{k = 2}^{n} a_{1k} x_k $$

$$ x_1 = \frac{v_1 - \sum\limits_{k = 2}^{n} a_{1k} x_k}{a_{11}} = \frac{v_1}{a_{11}} - \frac{\sum\limits_{k = 2}^{n} a_{1k} x_k}{a_{11}} = \frac{v_1}{a_{11}} - \sum\limits_{k = 2}^{n} \frac{a_{1k} x_k}{a_{11}} $$

$$ x_1 = \frac{v_1}{a_{11}} - \sum\limits_{k = 2}^{n} \frac{a_{1k}}{a_{11}} x_k $$

$$ \sum\limits_{k = 1}^{n} a_{mk} x_k = v_m $$

$$ a_{m1} x_1 + \sum\limits_{k = 2}^{n} a_{mk} x_k = v_m $$

$$ a_{m1} (\frac{v_1}{a_{11}} - \sum\limits_{k = 2}^{n} \frac{a_{1k}}{a_{11}} x_k) + \sum\limits_{k = 2}^{n} a_{mk} x_k = v_m $$

$$ a_{m1} \frac{v_1}{a_{11}} - a_{m1} \sum\limits_{k = 2}^{n} \frac{a_{1k}}{a_{11}} x_k + \sum\limits_{k = 2}^{n} a_{mk} x_k = v_m $$

$$ \frac{a_{m1} v_1}{a_{11}} - \sum\limits_{k = 2}^{n} \frac{a_{m1} a_{1k}}{a_{11}} x_k + \sum\limits_{k = 2}^{n} a_{mk} x_k = v_m $$

$$ -\sum\limits_{k = 2}^{n} \frac{a_{m1} a_{1k}}{a_{11}} x_k + \sum\limits_{k = 2}^{n} a_{mk} x_k = v_m - \frac{a_{m1} v_1}{a_{11}} $$

$$ \sum\limits_{k = 2}^{n} \frac{a_{m1} a_{1k}}{a_{11}} x_k + \sum\limits_{k = 2}^{n} a_{mk} x_k = \frac{a_{m1} v_1}{a_{11}} - v_m $$

$$ \sum\limits_{k = 2}^{n} \frac{a_{m1} a_{1k}}{a_{11}} x_k + a_{mk} x_k = \frac{a_{m1} v_1}{a_{11}} - \frac{a_{11} v_m}{a_{11}} $$

$$ \sum\limits_{k = 2}^{n} (\frac{a_{m1} a_{1k}}{a_{11}} + a_{mk}) x_k = \frac{a_{m1} v_1 - a_{11} v_m}{a_{11}} $$

$$ \sum\limits_{k = 2}^{n} (\frac{a_{m1} a_{1k}}{a_{11}} + \frac{a_{11} a_{mk}}{a_{11}}) x_k = \frac{a_{m1} v_1 - a_{11} v_m}{a_{11}} $$

$$ \sum\limits_{k = 2}^{n} (\frac{a_{m1} a_{1k} + a_{11} a_{mk}}{a_{11}}) x_k = \frac{a_{m1} v_1 - a_{11} v_m}{a_{11}} $$

$$ \sum\limits_{k = 2}^{n} (a_{m1} a_{1k} + a_{11} a_{mk}) x_k = a_{m1} v_1 - a_{11} v_m $$

$$ \sum\limits_{k = 2}^{n} (a_{21} a_{1k} + a_{11} a_{2k}) x_k = a_{21} v_1 - a_{11} v_2 $$

$$ \sum\limits_{k = 2}^{n} (a_{31} a_{1k} + a_{11} a_{3k}) x_k = a_{31} v_1 - a_{11} v_3 $$

$$ \vdots $$

$$ \sum\limits_{k = 2}^{n} (a_{m1} a_{1k} + a_{11} a_{mk}) x_k = a_{m1} v_1 - a_{11} v_m $$

$$ \vdots $$

$$ \sum\limits_{k = 2}^{n} (a_{n1} a_{1k} + a_{11} a_{nk}) x_k = a_{n1} v_1 - a_{11} v_n $$

$$ \begin{bmatrix} a_{21} a_{12} + a_{11} a_{22} & a_{21} a_{12} + a_{11} a_{22} & \dots & a_{21} a_{1k} + a_{11} a_{2k} & \dots & a_{21} a_{1n} + a_{11} a_{2n} \\
a_{31} a_{12} + a_{11} a_{32} & a_{31} a_{13} + a_{11} a_{33} & \dots & a_{31} a_{1k} + a_{11} a_{3k} & \dots & a_{31} a_{1n} + a_{11} a_{3n} \\
\vdots & \vdots & \ddots & \vdots &  & \vdots \\
a_{21} a_{1k} + a_{11} a_{k2} & a_{31} a_{1k} + a_{11} a_{k3} & \dots & a_{k1} a_{1k} + a_{11} a_{kk} & \dots & a_{n1} a_{1k} + a_{11} a_{kn} \\
\vdots & \vdots &  & \vdots & \ddots & \vdots \\
a_{n1} a_{12} + a_{11} a_{n2} & a_{n1} a_{13} + a_{11} a_{n3} & \dots & a_{n1} a_{1k} + a_{11} a_{nk} & \dots & a_{n1} a_{1n} + a_{11} a_{nn} \\ \end{bmatrix} \begin{bmatrix} x_2 \\
x_3 \\
\vdots \\
x_k \\
\vdots \\
x_n \\ \end{bmatrix} = \begin{bmatrix} a_{21} v_1 - a_{11} v_2 \\
a_{31} v_1 - a_{11} v_3 \\
\vdots \\
a_{k1} v_1 - a_{11} v_k \\
\vdots \\
a_{n1} v_1 - a_{11} v_n \\ \end{bmatrix} $$

#### conclutions

conclution #1:

$$ \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1k} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2k} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3k} & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots &  & \vdots \\
a_{k1} & a_{k2} & a_{k3} & \dots & a_{kk} & \dots & a_{kn} \\
\vdots & \vdots & \vdots &  & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nk} & \dots & a_{nn} \\ \end{bmatrix} \begin{bmatrix} x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_k \\
\vdots \\
x_n \\ \end{bmatrix} = \begin{bmatrix} v_1 \\
v_2 \\
v_3 \\
\vdots \\
v_k \\
\vdots \\
v_n \\ \end{bmatrix} $$

$$ \Downarrow $$

$$ x_1 = \frac{v_1}{a_{11}} - \sum\limits_{k = 2}^{n} \frac{a_{1k}}{a_{11}} x_k $$

$$ \begin{bmatrix} a_{21} a_{12} + a_{11} a_{22} & a_{21} a_{12} + a_{11} a_{22} & \dots & a_{21} a_{1k} + a_{11} a_{2k} & \dots & a_{21} a_{1n} + a_{11} a_{2n} \\
a_{31} a_{12} + a_{11} a_{32} & a_{31} a_{13} + a_{11} a_{33} & \dots & a_{31} a_{1k} + a_{11} a_{3k} & \dots & a_{31} a_{1n} + a_{11} a_{3n} \\
\vdots & \vdots & \ddots & \vdots &  & \vdots \\
a_{21} a_{1k} + a_{11} a_{k2} & a_{31} a_{1k} + a_{11} a_{k3} & \dots & a_{k1} a_{1k} + a_{11} a_{kk} & \dots & a_{n1} a_{1k} + a_{11} a_{kn} \\
\vdots & \vdots &  & \vdots & \ddots & \vdots \\
a_{n1} a_{12} + a_{11} a_{n2} & a_{n1} a_{13} + a_{11} a_{n3} & \dots & a_{n1} a_{1k} + a_{11} a_{nk} & \dots & a_{n1} a_{1n} + a_{11} a_{nn} \\ \end{bmatrix} \begin{bmatrix} x_2 \\
x_3 \\
\vdots \\
x_k \\
\vdots \\
x_n \\ \end{bmatrix} = \begin{bmatrix} a_{21} v_1 - a_{11} v_2 \\
a_{31} v_1 - a_{11} v_3 \\
\vdots \\
a_{k1} v_1 - a_{11} v_k \\
\vdots \\
a_{n1} v_1 - a_{11} v_n \\ \end{bmatrix} $$

$1516$ Lines

conclution #2:

$$ \begin{bmatrix} a_{11} \\ \end{bmatrix} \begin{bmatrix} x_1 \\ \end{bmatrix} = \begin{bmatrix} v_1 \\ \end{bmatrix} $$

$$ \Downarrow $$

$$ x_1 = \frac{v_1}{a_{11}} $$

#### general matrix multiplication

$$ A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\ \end{bmatrix} $$

$$ B = \begin{bmatrix} b_{11} & b_{12} & b_{13} & \dots & b_{1n} \\
b_{21} & b_{22} & b_{23} & \dots & b_{2n} \\
b_{31} & b_{32} & b_{33} & \dots & b_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & b_{n3} & \dots & b_{nn} \\ \end{bmatrix} $$

$$ AB = \begin{bmatrix} ? & ? & ? & \dots & ? \\
? & ? & ? & \dots & ? \\
? & ? & ? & \dots & ? \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
? & ? & ? & \dots & ? \\ \end{bmatrix} $$

$$ (AB) e_x = A(B e_x) $$

$$ B e_x : = \begin{bmatrix} b_{1x} \\
b_{2x} \\
b_{3x} \\
\vdots \\
b_{nx} \\ \end{bmatrix} $$

$$ A(B e_x) = A \begin{bmatrix} b_{1x} \\
b_{2x} \\
b_{3x} \\
\vdots \\
b_{nx} \\ \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\ \end{bmatrix} \begin{bmatrix} b_{1x} \\
b_{2x} \\
b_{3x} \\
\vdots \\
b_{nx} \\ \end{bmatrix} = \begin{bmatrix} \sum\limits_{i = 1}^{n} b_{ix} a_{1i} \\
\sum\limits_{i = 1}^{n} b_{ix} a_{2i} \\
\sum\limits_{i = 1}^{n} b_{ix} a_{3i} \\
\vdots \\
\sum\limits_{i = 1}^{n} b_{ix} a_{ni} \\ \end{bmatrix} $$

$$ AB = \begin{bmatrix} \sum\limits_{i = 1}^{n} b_{i1} a_{1i} & \sum\limits_{i = 1}^{n} b_{i2} a_{1i} & \sum\limits_{i = 1}^{n} b_{i3} a_{1i} & \dots & \sum\limits_{i = 1}^{n} b_{in} a_{1i} \\
\sum\limits_{i = 1}^{n} b_{i1} a_{2i} & \sum\limits_{i = 1}^{n} b_{i2} a_{2i} & \sum\limits_{i = 1}^{n} b_{i3} a_{2i} & \dots & \sum\limits_{i = 1}^{n} b_{in} a_{2i} \\
\sum\limits_{i = 1}^{n} b_{i1} a_{3i} & \sum\limits_{i = 1}^{n} b_{i2} a_{3i} & \sum\limits_{i = 1}^{n} b_{i3} a_{3i} & \dots & \sum\limits_{i = 1}^{n} b_{in} a_{3i} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\sum\limits_{i = 1}^{n} b_{i1} a_{ni} & \sum\limits_{i = 1}^{n} b_{i2} a_{ni} & \sum\limits_{i = 1}^{n} b_{i3} a_{ni} & \dots & \sum\limits_{i = 1}^{n} b_{in} a_{ni} \\ \end{bmatrix} $$

$$ \sum\limits_{i = 1}^{n} b_{iy} a_{xi} = \begin{bmatrix} b_{1y} \\
b_{2y} \\
b_{3y} \\
\vdots \\
b_{ny} \\ \end{bmatrix} \cdot \begin{bmatrix} a_{x1} \\
a_{x2} \\
a_{x3} \\
\vdots \\
a_{xn} \\ \end{bmatrix} = B e_y \cdot A^T e_x $$

$$ AB = \begin{bmatrix} B \hat{x} \cdot A^T \hat{x} & B \hat{y} \cdot A^T \hat{x} & B \hat{z} \cdot A^T \hat{x} & \dots & B \hat{\omega} \cdot A^T \hat{x} \\
B \hat{x} \cdot A^T \hat{y} & B \hat{y} \cdot A^T \hat{y} & B \hat{z} \cdot A^T \hat{y} & \dots & B \hat{\omega} \cdot A^T \hat{y} \\
B \hat{x} \cdot A^T \hat{z} & B \hat{y} \cdot A^T \hat{z} & B \hat{z} \cdot A^T \hat{z} & \dots & B\hat{\omega} \cdot A^T \hat{z} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
B \hat{x} \cdot A^T \hat{\omega} & B \hat{y} \cdot A^T \hat{\omega} & B \hat{\omega} \cdot A^T \hat{z} & \dots & B \hat{\omega} \cdot A^T \hat{\omega} \\ \end{bmatrix} $$

### $1 + 1$ and the foundations of modern mathematics

Before I start, none of this was scripted.

What I want to do here is prove that $1 + 1 = 2$. But most of the time, you find yourself in a loop of defining things. For example: what is $1$? $1$ is the successor of $0$. What is the successor operation? The successor operation is the function that-

$1600$ Lines.

"Stop right there!" Said person #$2$, "What is a function?".

"Okay, fine!" Said person #$1$, "I'll instead say that $1$ is the set that contains $0$." (written $\{ 0 \}$.)

"That's better, but can you express $\{ 0 \}$ more formally?" Said person #$2$.

"Well, what I mean by that is: $∀x.x \in \{ 0 \} \iff x = 0$." Said person #$1$. (For any/all $x$, $x$ is within $\{ 0 \}$ precisely when $x = 0$.)

"But what is $=$?" Said person #$2$.

"Axiom #$1$ of ZFC: the axiom of extensionality" said person #$1$, "it states that $S = T$ precisely when for any $s \in S$, $s \in T$, and for any $t \in T$, $t \in S$"

"Okay, so what you're saying is that $∀x.x \in 1 \iff (∀y.y \in x → y \in 0) ∧ (∀y.y \in 0 → y \in x)$." Said person #$2$.

"Yes. Is there anything else left undefined?" Said person #$1$.

"Yes, always!" Said person #$2$. "What is $0$?"

"Are you really gonna make me answer that?" Said person #$1$.

"Yes!" Said person #$2$.

"Okay, fine!" Person #$1$ said with frustration. "$0$ is Ø" (the empty set) "is the set with nothing in it, so $¬∃x.x \in Ø$."

"So, what you really meant by $∀x.x \in 1 \iff (∀y.y \in x → y \in 0) ∧ (∀y.y \in 0 → y \in x)$ was $∀x.x \in 1 \iff ¬∃y.y \in x$." Said person #$2$

"Yes!" Said person #$1$.

"So $1$ is the set of all empty sets, of which there are only one" Said person #$2$ "am I understanding this correctly?" Said person #$2$

"Yes!" Said person #$1$.

I'm tired of this conversation between a mathematician and probably a mathematical snob who only accepts the truest logical statements crafted from pure mathematical set theory.

$$ ∀x_1.(∀x_2.x_2 \in x_1 \iff ¬∃x_3.x_3 \in x_2) → x_1 + x_1 = 2 $$

$$ \text{"For any variable (call it } x_1 \text{), that variable being } 1 \text{ implies that adding it to itself results in } 2 \text{, that is, there is not an } x_3 \in x_2 \text{"} $$

$$ ∀x_1.x_1 \in 2 \iff (∀x_2.x_2 \in x_1 \iff ¬∃x_3.x_3 \in x_2) $$

$$ \text{"For any variable (call it } x_1 \text{), } x_1 \in 2 \text{ implies that } x_1 = 1 \text{, that is, for any variable (call it } x_2 \text{), } x_2 \in 1 \text{ precisely when } x_2 = 0 \text{, that is, there is not an } x_3 \in x_2 \text{"} $$

$$ ∀x_1.∀x_2.(∀x_3.x_3 \in x_1 \iff ¬∃x_4.x_4 \in x_3) ∧ (∀x_3.x_3 \in x_2 \iff (∀x_4.x_4 \in x_3 \iff ¬∃x_5.x_5 \in x_4)) → ∀x_3.x_3 \in x_1 + x_1 \iff x_3 \in x_2 $$

$$ A(m, n) = m + n $$

$$ A(n, 0) = n $$

$$ S(n) = n + 1 $$

$$ A(m, S(n)) = S(A(m, n)) $$

$$ ∀m.∀n.n = S(m) \iff (∀x.x \in n \iff x = m) $$

$$ ∀m.∀n.n = S(m) \iff (∀x_1.x_1 \in n \iff (∀x_2.x_2 \in x_1 \iff x_2 \in m)) $$

I feel like doing something else, how about Russel's paradox? It states that there is no set that conain only sets that don't contain themselves.

$$ ¬∃x_1.∀x_2.x_2 \in x_1 \iff ¬x_2 \in x_2 $$

Next: the first axiom of set theory (The Axiom of Extensionality). It states that two sets are equal if they have the same elements, but I think it actually means that if two sets are equal (i.e. they have the same elements), a set cannot contain just one of them, it has to contain either both or neither of the sets.

$$ ∀x_1.∀x_2.x_1 = x_2 → ∀x_3.x_1 \in x_3 \iff x_2 \in x_3 $$

$$ ∀x_1.∀x_2.(∀x_3.x_3 \in x_1 \iff x_3 \in x_2) → ∀x_3.x_1 \in x_3 \iff x_2 \in x_3 $$

Next: the second axiom of set theory (The Axiom of Foundation). It states that every set must have an element disjoint from itself (i.e. an element where the union of that element and the original set is empty (i.e. they don't have any common elements)).

$$ ∀x_1.x_1 \ne Ø → ∃x_2.x_2 \in x_1 ∧ x_2 ∩ x_1 = Ø $$

$$ ∀x_1.¬x_1 = Ø → ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

$$ ∀x_1.x_1 = Ø ∨ ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

$$ ∀x_1.¬(∃x_2.x_2 \in x_1) ∨ ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

Next: the third axiom of set theory (The Axiom of Pairing). Actually, I'm not going to use the axiom of pairing, I'm going to use the closely related singleton axiom, It states that if you have a set then there exists the set containing that set, as opposed to the axiom of pairing which says that if you have two sets then there is a set containing both of them. These two statements are equivalent, but I prefer the first one.

Also I realized that this axiom makes the axiom a regularity redundant. Let's say that $S = \{ S \}$. then you would say that $S$ is a set because it is equal to the set containing $S$. So we would also need to assume that $S$ is a set for that to work, so that would mean that we need to prove that $S$ is a set, so that would mean that we need to prove that $S$ is a set, you just never get to the bottom of it and you can never declare that $S$ is a set.

Also this is a weird kind of axiom because it doesn't always make the set containing a set into a set, you still have to prove it with the other rules. So we just knocked out two axioms of set theory with one stone.

#### $\text{Symm}_4$

I'm going to use a notation and this is how it works: I will notate $(1, 2, 3)(4, 5)$ as the function on a string that brings the first term to the second place in the string, the second term to the third place in the string, and the third thing back to the first term in the string. And then also swapping the fourth and fifth terms. And also I'm going to do composition from left to right instead of from right to left, so the composition of $f$ and $g$ does $f$ first then $g$.

Here's a chart of each permutation multiplied by each other permutation of four elements:

| $\times$  | () | (1, 2) | (2, 3) | (1, 2, 3) | (1, 3, 2) | (1, 3) | (3, 4) | (1, 2)(3, 4) | (2, 3, 4) | (1, 2, 3, 4) | (1, 3, 4, 2) | (1, 3, 4) | (2, 4, 3) | (1, 2, 4, 3) | (2, 4) | (1, 2, 4) | (1, 3)(2, 4) | (1, 3, 2, 4) | (1, 4, 3, 2) | (1, 4, 3) | (1, 4, 2) | (1, 4) | (1, 4, 2, 3) | (1, 4)(2, 3) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| () | () | (1, 2)  | (2, 3)  | (1, 2, 3) | (1, 3, 2) | (1, 3) | (3, 4) | (1, 2)(3, 4) | (2, 3, 4) | (1, 2, 3, 4) | (1, 3, 4, 2) | (1, 3, 4) | (2, 4, 3) | (1, 2, 4, 3) | (2, 4) | (1, 2, 4) | (1, 3)(2, 4) | (1, 3, 2, 4) | (1, 4, 3, 2) | (1, 4, 3) | (1, 4, 2) | (1, 4) | (1, 4, 2, 3) | (1, 4)(2, 3) |
| (1, 2)  | (1, 2)  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2, 3)  | (2, 3)  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 2, 3) | (1, 2, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3, 2) | (1, 3, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3) | (1, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (3, 4) | (3, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 2)(3, 4) | (1, 2)(3, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2, 3, 4) | (2, 3, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 2, 3, 4) | (1, 2, 3, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3, 4, 2) | (1, 3, 4, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3, 4) | (1, 3, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2, 4, 3) | (2, 4, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 2, 4, 3) | (1, 2, 4, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2, 4) | (2, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 2, 4) | (1, 2, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3)(2, 4) | (1, 3)(2, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 3, 2, 4) | (1, 3, 2, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4, 3, 2) | (1, 4, 3, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4, 3) | (1, 4, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4, 2) | (1, 4, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4) | (1, 4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4, 2, 3) | (1, 4, 2, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1, 4)(2, 3) | (1, 4)(2, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

$1717$ Lines.

I don't feel like filling out the rest of the $529$ entries of this table. Instead I'll ask my dad to write some code to do it for me, and then use that information to create a new times table.

#### magic squares

If you don't know, a magic square is a square of numbers, typically $3x3$, where the sum, for the sum of each row, each column, and the two diagonals are all equal. Particularly, what I would like to do here is find how many numbers it takes to define an affine magic square. That is, one without the diagonal requirement, because then if you rotate it, or move the first column to the end, or the first row to the end, or swap to rows or two columns, then it will still work.

$$ \begin{bmatrix} a & b & c \\
d & e & f \\
g & h & i \\ \end{bmatrix} $$

$$ a + b + c = d + e + f = g + h + i = a + d + g = b + e + h = c + f + i = m $$

$$ a + b + c = m $$

$$ a = m - b - c $$

$$ a + b + c = a + d + g $$

$$ b + c = d + g $$

$$ d + e + f = g + h + i = b + e + h = c + f + i = m $$

$$ b + c = d + g $$

#### a puzzle

Okay, here's the puzzle: you are greeted by $10$ boxes that contain a random number from $0$ to $1$ and you want to get the biggest one. So what you can do is you open the first box and you can either choose to take it or leave it, and if you leave it, then you can never come back to it. What is your strategy for getting the highest number? And how does that strategy scale for more or fewer boxes?

According to a veritasium video about the number $37$, the answer is to check the first $37$%, rejects all of those, and then after that you choose one that's bigger than the biggest one in those first $37$%, choose that one, and if those first $37$% contained the biggest one (which happens 37% of the time), then tough luck!

I thought: what if you didn't choose some boxes to reject always and then choose the best one after that? Then I was thinking: what is the perfect strategy?

Well, for one box it's really obvious: just choose that box. For two boxes, it also seems kind of obvious: if the first one is more than one half, then do it, and if it's less than one half, pass it.

What about three boxes? Well, I know that if I somehow get down to two, then I know a strategy. So at what threshold $t$ should I keep it? Well, what's the expected value for two of them? Half of the time it's less than $\frac{1}{2}$ and you have to skip it, with an average value for the other one being $\frac{1}{2}$, but half of the time it's more than $\frac{1}{2}$ and the average is $\frac{3}{4}$. So if you compute $\frac{1}{2} \frac{1}{2} + \frac{1}{2} \frac{3}{4} = \frac{1}{4} + \frac{3}{8} = \frac{2}{8} + \frac{3}{8} = \frac{5}{8}$. So if the value in the first box is more than $\frac{5}{8}$, then keep it, and if it's less, skip it.

But what about a more general case? If I have $n$ boxes then what is the threshold (call it $f(n)$) where if it's more than that, I should keep it, and if it's less than that, I should leave it, and if it's exactly that, then either one.

Well, I know that it's equal to the expected score for $n - 1$ boxes (denoted $\text{ES} (n - 1)$), and $\text{ES} (n)$ must be equal to the probability that a random number from $0$ to $1$ is less than $f(n)$ (that is, $f(n)$ itself), multiplied by $\text{ES} (n - 1)$, plus the probability that it is more than $f(n)$ (that is, $1 - f(n)$), and in that case, the expected value is $\frac{1 + f(n)}{2} = \frac{1}{2} + \frac{f(n)}{2}$. So the expected score (and hence $f(n + 1)$) is given by:

$$ f(n + 1) = f(n) \text{ES} (n - 1) + (1 - f(n)) (\frac{1}{2} + \frac{f(n)}{2}) = f(n) f(n) + 1 \frac{1}{2} + 1 \frac{f(n)}{2} - f(n) \frac{1}{2} - f(n) \frac{f(n)}{2} = f(n)^2 + \frac{1}{2} + \frac{f(n)}{2} - \frac{f(n)}{2} - \frac{f(n)^2}{2} $$

$$ f(n + 1) = \frac{f(n)^2}{2} + \frac{1}{2} $$

And coupled with the results that there is no threshold for one box (i.e. the threshold is $0$), we now have an inductive formula for the perfect strategy.

So, the answer to the original question for $n = 10$ is: If the first one is more than about $0.849$, then keep it, if not, then pass it. And if the second one is more than about $0.836$, then keep it, if not, then pass it. And if the third one is more than about $0.82$, then keep it, if not, then pass it. And if the fourth one is more than about $0.8$, then keep it, if not, then pass it. And if the fifth one is more than about $0.775$, then keep it, if not, then pass it. And if the sixth one is more than about $0.741$, then keep it, if not, then pass it. And if the seventh one is more than about $0.695$, then keep it, if not, then pass it. And if the eighth one is more than $0.625$, then keep it, if not, then pass it. And if the nineth one is more than $\frac{1}{2}$, then keep it, if not, then pass it.

#### $\text{Symm}_3$

Last time I tried this it was too much data and my dad still hasn't finished that code. So I'm going to make a multiplication table of a more manageable size, then find all of its symmetric beauty.

| $\times$  | ()        | (1, 2)    | (2, 3)    | (1, 2, 3) | (1, 3, 2) | (1, 3)    |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| ()        | ()        | (1, 2)    | (2, 3)    | (1, 2, 3) | (1, 3, 2) | (1, 3)    |
| (1, 2)    | (1, 2)    | ()        | (1, 3, 2) | (1, 3)    | (2, 3)    | (1, 2, 3) |
| (2, 3)    | (2, 3)    | (1, 2, 3) | ()        | (1, 2)    | (1, 3)    | (1, 3, 2) |
| (1, 2, 3) | (1, 2, 3) | (2, 3)    | (1, 3)    | (1, 3, 2) | ()        | (1, 2)    |
| (1, 3, 2) | (1, 3, 2) | (1, 3)    | (1, 2)    | ()        | (1, 2, 3) | (2, 3)    |
| (1, 3)    | (1, 3)    | (1, 3, 2) | (1, 2, 3) | (2, 3)    | (1, 2)    | ()        |

$1776 + 4$ Lines.

Process: swap around pieces of paper labeled $1$, $2$, and $3$, doing another swap, and looking at the table of what the answer should be based on the pieces of paper (see table below), and then repeating that $25$ times.

| $123$ | ()        |
| ----- | --------- |
| $213$ | (1, 2)    |
| $132$ | (2, 3)    |
| $312$ | (1, 2, 3) |
| $231$ | (1, 3, 2) |
| $321$ | (1, 3)    |

So now I'm going to swap out the swaps with letters of the alphabet, and remove the trivial first row and first column.

| $\times$  | $a$  | $b$  | $c$  | $d$  | $e$  |
| --------- | ---- | ---- | ---- | ---- | ---- |
| $a$       | $id$ | $d$  | $e$  | $b$  | $c$  |
| $b$       | $c$  | $id$ | $a$  | $e$  | $d$  |
| $c$       | $b$  | $e$  | $d$  | $id$ | $a$  |
| $d$       | $e$  | $a$  | $id$ | $c$  | $b$  |
| $e$       | $d$  | $c$  | $b$  | $a$  | $id$ |

$1802$ Lines.

If you were wondering, I'm not using $i$ for the identity, because in group theory, you use an $e$. But $e$ was already taken, so instead of using $i$, I used $id$, which is the standard category theory notation.

Notice any patterns? Well, the first thing that jumped out to me a few months ago was the string of $id$s across the diagonal, interrupted by $c$ and $d$.

The reason why was because my first encounter with this group was an equivalent group $D_3$ (the dihedral group of order $3$ or the group of all rotations and reflections of a triangle that leave the corners looking the same), as opposed to $\text{Symm}_3$, which is the group of all ways to arrange three objects. What I noticed was that $a$, $b$, and $e$ were reflections, so of course doing them twice would result in the same thing.

#### SIR model

$$ \text{S} (0) = 1 $$

$$ \frac{d \text{S}}{dt} = -ln(R_0) \text{I} (t) $$

$$ \text{I} (0) = dt $$

$$ \frac{d \text{I}}{dt} = (ln(R_0) - c) \text{I} (t) $$

$$ \text{R} (0) = 0 $$

$$ \frac{d \text{R}}{dt} = c \text{I} (t) $$

#### extreme SIR model

$$ f_1 (0) = 1 $$

$$ f_n (0) = 0 $$

$$ \frac{df_1}{dt} = -x_1 f_1 (t) $$

$$ \frac{df_n}{dt} = x_{n - 1} f_{n - 1} (t) - x_n f_n (t) $$

$$ f_1 (t) = C e^{-x_1 t} $$

$$ f_1 (0) = 1 = C e^{-x_1 0} = C e^0 = 1C = C $$

$$ C = 1 $$

$$ f_1 (t) = e^{-x_1 t} $$

$$ f_2 (0) = 0 $$

$$ \frac{df_2}{dt} = x_1 f_{1} (t) - x_2 f_2 (t) $$

$$ \frac{df_2}{dt} = x_1 e^{-x_1 t} - x_2 f_2 (t) $$

$$ \text{And after plugging this into a differential equation solver (shout out to Symbolab), I have a solution.} $$

$$ f_2 (t) = \frac{x_1}{(x_2 - x_1) e^{x_1 t}} + \frac{C}{e^{x_2 t}} $$

$$ f_2 (0) = 0 = \frac{x_1}{(x_2 - x_1) e^{x_1 0}} + \frac{C}{e^{x_2 0}} = \frac{x_1}{(x_2 - x_1) e^0} + \frac{C}{e^0} = \frac{x_1}{1 (x_2 - x_1)} + \frac{C}{1} = \frac{x_1}{x_2 - x_1} + C $$

$$ \frac{x_1}{x_2 - x_1} + C = 0 $$

$$ C = -\frac{x_1}{x_2 - x_1} $$

$$ f_2 (t) = \frac{x_1}{(x_2 - x_1) e^{x_1 t}} - \frac{\frac{x_1}{x_2 - x_1}}{e^{x_2 t}} = \frac{x_1}{(x_2 - x_1) e^{x_1 t}} - \frac{x_1}{(x_2 - x_1) e^{x_2 t}} = \frac{x_1}{(x_2 - x_1)} e^{-x_1 t} - \frac{x_1}{(x_2 - x_1)} e^{-x_2 t} $$

$$ f_2 (t) = \frac{x_1}{(x_2 - x_1)} (e^{-x_1 t} - e^{-x_2 t}) $$

#### $\text{Symm}_4$ attempt $2$

Status update: my dad still hasn't finished the code so I wrote my own code. The original output is:

|  | [0 1 2 3] | [1 0 2 3] | [0 2 1 3] | [2 0 1 3] | [1 2 0 3] | [2 1 0 3] | [0 1 3 2] | [1 0 3 2] | [0 3 1 2] | [3 0 1 2] | [1 3 0 2] | [3 1 0 2] | [0 2 3 1] | [2 0 3 1] | [0 3 2 1] | [3 0 2 1] | [2 3 0 1] | [3 2 0 1] | [1 2 3 0] | [2 1 3 0] | [1 3 2 0] | [3 1 2 0] | [2 3 1 0] | [3 2 1 0] |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [0 1 2 3] | [0 1 2 3] | [1 0 2 3] | [0 2 1 3] | [2 0 1 3] | [1 2 0 3] | [2 1 0 3] | [0 1 3 2] | [1 0 3 2] | [0 3 1 2] | [3 0 1 2] | [1 3 0 2] | [3 1 0 2] | [0 2 3 1] | [2 0 3 1] | [0 3 2 1] | [3 0 2 1] | [2 3 0 1] | [3 2 0 1] | [1 2 3 0] | [2 1 3 0] | [1 3 2 0] | [3 1 2 0] | [2 3 1 0] | [3 2 1 0] |
| [1 0 2 3] | [1 0 2 3] | [0 1 2 3] | [2 0 1 3] | [0 2 1 3] | [2 1 0 3] | [1 2 0 3] | [1 0 3 2] | [0 1 3 2] | [3 0 1 2] | [0 3 1 2] | [3 1 0 2] | [1 3 0 2] | [2 0 3 1] | [0 2 3 1] | [3 0 2 1] | [0 3 2 1] | [3 2 0 1] | [2 3 0 1] | [2 1 3 0] | [1 2 3 0] | [3 1 2 0] | [1 3 2 0] | [3 2 1 0] | [2 3 1 0] |
| [0 2 1 3] | [0 2 1 3] | [1 2 0 3] | [0 1 2 3] | [2 1 0 3] | [1 0 2 3] | [2 0 1 3] | [0 3 1 2] | [1 3 0 2] | [0 1 3 2] | [3 1 0 2] | [1 0 3 2] | [3 0 1 2] | [0 3 2 1] | [2 3 0 1] | [0 2 3 1] | [3 2 0 1] | [2 0 3 1] | [3 0 2 1] | [1 3 2 0] | [2 3 1 0] | [1 2 3 0] | [3 2 1 0] | [2 1 3 0] | [3 1 2 0] |
| [2 0 1 3] | [2 0 1 3] | [2 1 0 3] | [1 0 2 3] | [1 2 0 3] | [0 1 2 3] | [0 2 1 3] | [3 0 1 2] | [3 1 0 2] | [1 0 3 2] | [1 3 0 2] | [0 1 3 2] | [0 3 1 2] | [3 0 2 1] | [3 2 0 1] | [2 0 3 1] | [2 3 0 1] | [0 2 3 1] | [0 3 2 1] | [3 1 2 0] | [3 2 1 0] | [2 1 3 0] | [2 3 1 0] | [1 2 3 0] | [1 3 2 0] |
| [1 2 0 3] | [1 2 0 3] | [0 2 1 3] | [2 1 0 3] | [0 1 2 3] | [2 0 1 3] | [1 0 2 3] | [1 3 0 2] | [0 3 1 2] | [3 1 0 2] | [0 1 3 2] | [3 0 1 2] | [1 0 3 2] | [2 3 0 1] | [0 3 2 1] | [3 2 0 1] | [0 2 3 1] | [3 0 2 1] | [2 0 3 1] | [2 3 1 0] | [1 3 2 0] | [3 2 1 0] | [1 2 3 0] | [3 1 2 0] | [2 1 3 0] |
| [2 1 0 3] | [2 1 0 3] | [2 0 1 3] | [1 2 0 3] | [1 0 2 3] | [0 2 1 3] | [0 1 2 3] | [3 1 0 2] | [3 0 1 2] | [1 3 0 2] | [1 0 3 2] | [0 3 1 2] | [0 1 3 2] | [3 2 0 1] | [3 0 2 1] | [2 3 0 1] | [2 0 3 1] | [0 3 2 1] | [0 2 3 1] | [3 2 1 0] | [3 1 2 0] | [2 3 1 0] | [2 1 3 0] | [1 3 2 0] | [1 2 3 0] |
| [0 1 3 2] | [0 1 3 2] | [1 0 3 2] | [0 2 3 1] | [2 0 3 1] | [1 2 3 0] | [2 1 3 0] | [0 1 2 3] | [1 0 2 3] | [0 3 2 1] | [3 0 2 1] | [1 3 2 0] | [3 1 2 0] | [0 2 1 3] | [2 0 1 3] | [0 3 1 2] | [3 0 1 2] | [2 3 1 0] | [3 2 1 0] | [1 2 0 3] | [2 1 0 3] | [1 3 0 2] | [3 1 0 2] | [2 3 0 1] | [3 2 0 1] |
| [1 0 3 2] | [1 0 3 2] | [0 1 3 2] | [2 0 3 1] | [0 2 3 1] | [2 1 3 0] | [1 2 3 0] | [1 0 2 3] | [0 1 2 3] | [3 0 2 1] | [0 3 2 1] | [3 1 2 0] | [1 3 2 0] | [2 0 1 3] | [0 2 1 3] | [3 0 1 2] | [0 3 1 2] | [3 2 1 0] | [2 3 1 0] | [2 1 0 3] | [1 2 0 3] | [3 1 0 2] | [1 3 0 2] | [3 2 0 1] | [2 3 0 1] |
| [0 3 1 2] | [0 3 1 2] | [1 3 0 2] | [0 3 2 1] | [2 3 0 1] | [1 3 2 0] | [2 3 1 0] | [0 2 1 3] | [1 2 0 3] | [0 2 3 1] | [3 2 0 1] | [1 2 3 0] | [3 2 1 0] | [0 1 2 3] | [2 1 0 3] | [0 1 3 2] | [3 1 0 2] | [2 1 3 0] | [3 1 2 0] | [1 0 2 3] | [2 0 1 3] | [1 0 3 2] | [3 0 1 2] | [2 0 3 1] | [3 0 2 1] |
| [3 0 1 2] | [3 0 1 2] | [3 1 0 2] | [3 0 2 1] | [3 2 0 1] | [3 1 2 0] | [3 2 1 0] | [2 0 1 3] | [2 1 0 3] | [2 0 3 1] | [2 3 0 1] | [2 1 3 0] | [2 3 1 0] | [1 0 2 3] | [1 2 0 3] | [1 0 3 2] | [1 3 0 2] | [1 2 3 0] | [1 3 2 0] | [0 1 2 3] | [0 2 1 3] | [0 1 3 2] | [0 3 1 2] | [0 2 3 1] | [0 3 2 1] |
| [1 3 0 2] | [1 3 0 2] | [0 3 1 2] | [2 3 0 1] | [0 3 2 1] | [2 3 1 0] | [1 3 2 0] | [1 2 0 3] | [0 2 1 3] | [3 2 0 1] | [0 2 3 1] | [3 2 1 0] | [1 2 3 0] | [2 1 0 3] | [0 1 2 3] | [3 1 0 2] | [0 1 3 2] | [3 1 2 0] | [2 1 3 0] | [2 0 1 3] | [1 0 2 3] | [3 0 1 2] | [1 0 3 2] | [3 0 2 1] | [2 0 3 1] |
| [3 1 0 2] | [3 1 0 2] | [3 0 1 2] | [3 2 0 1] | [3 0 2 1] | [3 2 1 0] | [3 1 2 0] | [2 1 0 3] | [2 0 1 3] | [2 3 0 1] | [2 0 3 1] | [2 3 1 0] | [2 1 3 0] | [1 2 0 3] | [1 0 2 3] | [1 3 0 2] | [1 0 3 2] | [1 3 2 0] | [1 2 3 0] | [0 2 1 3] | [0 1 2 3] | [0 3 1 2] | [0 1 3 2] | [0 3 2 1] | [0 2 3 1] |
| [0 2 3 1] | [0 2 3 1] | [1 2 3 0] | [0 1 3 2] | [2 1 3 0] | [1 0 3 2] | [2 0 3 1] | [0 3 2 1] | [1 3 2 0] | [0 1 2 3] | [3 1 2 0] | [1 0 2 3] | [3 0 2 1] | [0 3 1 2] | [2 3 1 0] | [0 2 1 3] | [3 2 1 0] | [2 0 1 3] | [3 0 1 2] | [1 3 0 2] | [2 3 0 1] | [1 2 0 3] | [3 2 0 1] | [2 1 0 3] | [3 1 0 2] |
| [2 0 3 1] | [2 0 3 1] | [2 1 3 0] | [1 0 3 2] | [1 2 3 0] | [0 1 3 2] | [0 2 3 1] | [3 0 2 1] | [3 1 2 0] | [1 0 2 3] | [1 3 2 0] | [0 1 2 3] | [0 3 2 1] | [3 0 1 2] | [3 2 1 0] | [2 0 1 3] | [2 3 1 0] | [0 2 1 3] | [0 3 1 2] | [3 1 0 2] | [3 2 0 1] | [2 1 0 3] | [2 3 0 1] | [1 2 0 3] | [1 3 0 2] |
| [0 3 2 1] | [0 3 2 1] | [1 3 2 0] | [0 3 1 2] | [2 3 1 0] | [1 3 0 2] | [2 3 0 1] | [0 2 3 1] | [1 2 3 0] | [0 2 1 3] | [3 2 1 0] | [1 2 0 3] | [3 2 0 1] | [0 1 3 2] | [2 1 3 0] | [0 1 2 3] | [3 1 2 0] | [2 1 0 3] | [3 1 0 2] | [1 0 3 2] | [2 0 3 1] | [1 0 2 3] | [3 0 2 1] | [2 0 1 3] | [3 0 1 2] |
| [3 0 2 1] | [3 0 2 1] | [3 1 2 0] | [3 0 1 2] | [3 2 1 0] | [3 1 0 2] | [3 2 0 1] | [2 0 3 1] | [2 1 3 0] | [2 0 1 3] | [2 3 1 0] | [2 1 0 3] | [2 3 0 1] | [1 0 3 2] | [1 2 3 0] | [1 0 2 3] | [1 3 2 0] | [1 2 0 3] | [1 3 0 2] | [0 1 3 2] | [0 2 3 1] | [0 1 2 3] | [0 3 2 1] | [0 2 1 3] | [0 3 1 2] |
| [2 3 0 1] | [2 3 0 1] | [2 3 1 0] | [1 3 0 2] | [1 3 2 0] | [0 3 1 2] | [0 3 2 1] | [3 2 0 1] | [3 2 1 0] | [1 2 0 3] | [1 2 3 0] | [0 2 1 3] | [0 2 3 1] | [3 1 0 2] | [3 1 2 0] | [2 1 0 3] | [2 1 3 0] | [0 1 2 3] | [0 1 3 2] | [3 0 1 2] | [3 0 2 1] | [2 0 1 3] | [2 0 3 1] | [1 0 2 3] | [1 0 3 2] |
| [3 2 0 1] | [3 2 0 1] | [3 2 1 0] | [3 1 0 2] | [3 1 2 0] | [3 0 1 2] | [3 0 2 1] | [2 3 0 1] | [2 3 1 0] | [2 1 0 3] | [2 1 3 0] | [2 0 1 3] | [2 0 3 1] | [1 3 0 2] | [1 3 2 0] | [1 2 0 3] | [1 2 3 0] | [1 0 2 3] | [1 0 3 2] | [0 3 1 2] | [0 3 2 1] | [0 2 1 3] | [0 2 3 1] | [0 1 2 3] | [0 1 3 2] |
| [1 2 3 0] | [1 2 3 0] | [0 2 3 1] | [2 1 3 0] | [0 1 3 2] | [2 0 3 1] | [1 0 3 2] | [1 3 2 0] | [0 3 2 1] | [3 1 2 0] | [0 1 2 3] | [3 0 2 1] | [1 0 2 3] | [2 3 1 0] | [0 3 1 2] | [3 2 1 0] | [0 2 1 3] | [3 0 1 2] | [2 0 1 3] | [2 3 0 1] | [1 3 0 2] | [3 2 0 1] | [1 2 0 3] | [3 1 0 2] | [2 1 0 3] |
| [2 1 3 0] | [2 1 3 0] | [2 0 3 1] | [1 2 3 0] | [1 0 3 2] | [0 2 3 1] | [0 1 3 2] | [3 1 2 0] | [3 0 2 1] | [1 3 2 0] | [1 0 2 3] | [0 3 2 1] | [0 1 2 3] | [3 2 1 0] | [3 0 1 2] | [2 3 1 0] | [2 0 1 3] | [0 3 1 2] | [0 2 1 3] | [3 2 0 1] | [3 1 0 2] | [2 3 0 1] | [2 1 0 3] | [1 3 0 2] | [1 2 0 3] |
| [1 3 2 0] | [1 3 2 0] | [0 3 2 1] | [2 3 1 0] | [0 3 1 2] | [2 3 0 1] | [1 3 0 2] | [1 2 3 0] | [0 2 3 1] | [3 2 1 0] | [0 2 1 3] | [3 2 0 1] | [1 2 0 3] | [2 1 3 0] | [0 1 3 2] | [3 1 2 0] | [0 1 2 3] | [3 1 0 2] | [2 1 0 3] | [2 0 3 1] | [1 0 3 2] | [3 0 2 1] | [1 0 2 3] | [3 0 1 2] | [2 0 1 3] |
| [3 1 2 0] | [3 1 2 0] | [3 0 2 1] | [3 2 1 0] | [3 0 1 2] | [3 2 0 1] | [3 1 0 2] | [2 1 3 0] | [2 0 3 1] | [2 3 1 0] | [2 0 1 3] | [2 3 0 1] | [2 1 0 3] | [1 2 3 0] | [1 0 3 2] | [1 3 2 0] | [1 0 2 3] | [1 3 0 2] | [1 2 0 3] | [0 2 3 1] | [0 1 3 2] | [0 3 2 1] | [0 1 2 3] | [0 3 1 2] | [0 2 1 3] |
| [2 3 1 0] | [2 3 1 0] | [2 3 0 1] | [1 3 2 0] | [1 3 0 2] | [0 3 2 1] | [0 3 1 2] | [3 2 1 0] | [3 2 0 1] | [1 2 3 0] | [1 2 0 3] | [0 2 3 1] | [0 2 1 3] | [3 1 2 0] | [3 1 0 2] | [2 1 3 0] | [2 1 0 3] | [0 1 3 2] | [0 1 2 3] | [3 0 2 1] | [3 0 1 2] | [2 0 3 1] | [2 0 1 3] | [1 0 3 2] | [1 0 2 3] |
| [3 2 1 0] | [3 2 1 0] | [3 2 0 1] | [3 1 2 0] | [3 1 0 2] | [3 0 2 1] | [3 0 1 2] | [2 3 1 0] | [2 3 0 1] | [2 1 3 0] | [2 1 0 3] | [2 0 3 1] | [2 0 1 3] | [1 3 2 0] | [1 3 0 2] | [1 2 3 0] | [1 2 0 3] | [1 0 3 2] | [1 0 2 3] | [0 3 2 1] | [0 3 1 2] | [0 2 3 1] | [0 2 1 3] | [0 1 3 2] | [0 1 2 3] |

And then I'll use `ctrl + f` $24$ times to swap out the lists with letters.

|    | $id$ | $a$  | $b$  | $c$  | $d$  | $e$  | $f$  | $g$  | $h$  | $i$  | $j$  | $k$  | $l$  | $m$  | $n$  | $o$  | $p$  | $q$  | $r$  | $s$  | $t$  | $u$  | $v$  | $w$  |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| $id$ | $id$ | $a$  | $b$  | $c$  | $d$  | $e$  | $f$  | $g$  | $h$  | $i$  | $j$  | $k$  | $l$  | $m$  | $n$  | $o$  | $p$  | $q$  | $r$  | $s$  | $t$  | $u$  | $v$  | $w$  |
| $a$  | $a$  | $id$ | $c$  | $b$  | $e$  | $d$  | $g$  | $f$  | $i$  | $h$  | $k$  | $j$  | $m$  | $l$  | $o$  | $n$  | $q$  | $p$  | $s$  | $r$  | $u$  | $t$  | $w$  | $v$  |
| $b$  | $b$  | $d$  | $id$ | $e$  | $a$  | $c$  | $h$  | $j$  | $f$  | $k$  | $g$  | $i$  | $n$  | $p$  | $l$  | $q$  | $m$  | $o$  | $t$  | $v$  | $r$  | $w$  | $s$  | $u$  |
| $c$  | $c$  | $e$  | $a$  | $d$  | $id$ | $b$  | $i$  | $k$  | $g$  | $j$  | $f$  | $h$  | $o$  | $q$  | $m$  | $p$  | $l$  | $n$  | $u$  | $w$  | $s$  | $v$  | $r$  | $t$  |
| $d$  | $d$  | $b$  | $e$  | $id$ | $c$  | $a$  | $j$  | $h$  | $k$  | $f$  | $i$  | $g$  | $p$  | $n$  | $q$  | $l$  | $o$  | $m$  | $v$  | $t$  | $w$  | $r$  | $u$  | $s$  |
| $e$  | $e$  | $c$  | $d$  | $a$  | $b$  | $id$ | $k$  | $i$  | $j$  | $g$  | $h$  | $f$  | $q$  | $o$  | $p$  | $m$  | $n$  | $l$  | $w$  | $u$  | $v$  | $s$  | $t$  | $r$  |
| $f$  | $f$  | $g$  | $l$  | $m$  | $r$  | $s$  | $id$ | $a$  | $n$  | $o$  | $t$  | $u$  | $b$  | $c$  | $h$  | $i$  | $v$  | $w$  | $d$  | $e$  | $j$  | $k$  | $p$  | $q$  |
| $g$  | $g$  | $f$  | $m$  | $l$  | $s$  | $r$  | $a$  | $id$ | $o$  | $n$  | $u$  | $t$  | $c$  | $b$  | $i$  | $h$  | $w$  | $v$  | $e$  | $d$  | $k$  | $j$  | $q$  | $p$  |
| $h$  | $h$  | $j$  | $n$  | $p$  | $t$  | $v$  | $b$  | $d$  | $l$  | $q$  | $r$  | $w$  | $id$ | $e$  | $f$  | $k$  | $s$  | $u$  | $a$  | $c$  | $g$  | $i$  | $m$  | $o$  |
| $i$  | $i$  | $k$  | $o$  | $q$  | $u$  | $w$  | $c$  | $e$  | $m$  | $p$  | $s$  | $v$  | $a$  | $d$  | $g$  | $j$  | $r$  | $t$  | $id$ | $b$  | $f$  | $h$  | $l$  | $n$  |
| $j$  | $j$  | $h$  | $p$  | $n$  | $v$  | $t$  | $d$  | $b$  | $q$  | $l$  | $w$  | $r$  | $e$  | $id$ | $k$  | $f$  | $u$  | $s$  | $c$  | $a$  | $i$  | $g$  | $o$  | $m$  |
| $k$  | $k$  | $i$  | $q$  | $o$  | $w$  | $u$  | $e$  | $c$  | $p$  | $m$  | $v$  | $s$  | $d$  | $a$  | $j$  | $g$  | $t$  | $r$  | $b$  | $id$ | $h$  | $f$  | $n$  | $l$  |
| $l$  | $l$  | $r$  | $f$  | $s$  | $g$  | $m$  | $n$  | $t$  | $id$ | $u$  | $a$  | $o$  | $h$  | $v$  | $b$  | $w$  | $c$  | $i$  | $j$  | $p$  | $d$  | $q$  | $e$  | $k$  |
| $m$  | $m$  | $s$  | $g$  | $r$  | $f$  | $l$  | $o$  | $u$  | $a$  | $t$  | $id$ | $n$  | $i$  | $w$  | $c$  | $v$  | $b$  | $h$  | $k$  | $q$  | $e$  | $p$  | $d$  | $j$  |
| $n$  | $n$  | $t$  | $h$  | $v$  | $j$  | $p$  | $l$  | $r$  | $b$  | $w$  | $d$  | $q$  | $f$  | $s$  | $id$ | $u$  | $e$  | $k$  | $g$  | $m$  | $a$  | $o$  | $c$  | $i$  |
| $o$  | $o$  | $u$  | $i$  | $w$  | $k$  | $q$  | $m$  | $s$  | $c$  | $v$  | $e$  | $p$  | $g$  | $r$  | $a$  | $t$  | $d$  | $j$  | $f$  | $l$  | $id$ | $n$  | $b$  | $h$  |
| $p$  | $p$  | $v$  | $j$  | $t$  | $h$  | $n$  | $q$  | $w$  | $d$  | $r$  | $b$  | $l$  | $k$  | $u$  | $e$  | $s$  | $id$ | $f$  | $i$  | $o$  | $c$  | $m$  | $a$  | $g$  |
| $q$  | $q$  | $w$  | $k$  | $u$  | $i$  | $o$  | $p$  | $v$  | $e$  | $s$  | $c$  | $m$  | $j$  | $t$  | $d$  | $r$  | $a$  | $g$  | $h$  | $n$  | $b$  | $l$  | $id$ | $f$  |
| $r$  | $r$  | $l$  | $s$  | $f$  | $m$  | $g$  | $t$  | $n$  | $u$  | $id$ | $o$  | $a$  | $v$  | $h$  | $w$  | $b$  | $i$  | $c$  | $p$  | $j$  | $q$  | $d$  | $k$  | $e$  |
| $s$  | $s$  | $m$  | $r$  | $g$  | $l$  | $f$  | $u$  | $o$  | $t$  | $a$  | $n$  | $id$ | $w$  | $i$  | $v$  | $c$  | $h$  | $b$  | $q$  | $k$  | $p$  | $e$  | $j$  | $d$  |
| $t$  | $t$  | $n$  | $v$  | $h$  | $p$  | $j$  | $r$  | $l$  | $w$  | $b$  | $q$  | $d$  | $s$  | $f$  | $u$  | $id$ | $k$  | $e$  | $m$  | $g$  | $o$  | $a$  | $i$  | $c$  |
| $u$  | $u$  | $o$  | $w$  | $i$  | $q$  | $k$  | $s$  | $m$  | $v$  | $c$  | $p$  | $e$  | $r$  | $g$  | $t$  | $a$  | $j$  | $d$  | $l$  | $f$  | $n$  | $id$ | $h$  | $b$  |
| $v$  | $v$  | $p$  | $t$  | $j$  | $n$  | $h$  | $w$  | $q$  | $r$  | $d$  | $l$  | $b$  | $u$  | $k$  | $s$  | $e$  | $f$  | $id$ | $o$  | $i$  | $m$  | $c$  | $g$  | $a$  |
| $w$  | $w$  | $q$  | $u$  | $k$  | $o$  | $i$  | $v$  | $p$  | $s$  | $e$  | $m$  | $c$  | $t$  | $j$  | $r$  | $d$  | $g$  | $a$  | $n$  | $h$  | $l$  | $b$  | $f$  | $id$ |

$1922$ Lines.

Notice any patterns? Me neither.

### group theory?

I'm making this page to celebrate the up upcoming $2000$th line.

Here's some great videos about the subject that should get at least some credit: [Group theory, abstraction, and the 196,883-dimensional monster](https://www.youtube.com/watch?v=mH0oCDa74tE), [What is Group Theory? — Group Theory Ep. 1](https://www.youtube.com/watch?v=KufsL2VgELo) (Yes, I know, there's a part two. But I decided not to watch it because I was worried that if I watched it then I would just copy some of it), [This playlist by Another Roof](https://www.youtube.com/playlist?list=PLsdeQ7TnWVm_KATm7HjPoZ-q0UaQNjYrC) (I've only seen the third part).

I'll start off with the textbook definition of a group:

PS I don't have a group theory textbook.

It is a set or collection of things together with a binary operation (e.g. addition or multiplication because they input two things and output one thing) (this binary operation is usually denoted with a composition circle (this thing: ∘) so that is the notation that I will use) such that...

$1$. Closure: (this one is sometimes a given) If you have $a$ and $b$ in the group, then $a ∘ b$ is also within the group.

$2$. Associativity: If you have $a$, $b$ and $c$ in the group, then $(a ∘ b) ∘ c$ is equal to $a ∘ (b ∘ c)$. For this reason, I will be denoting both as $a ∘ b ∘ c$

$3$. Identity (or neutral depending on where you're from): There must always be a term in the group (call it $e$) where if you have $a$ in the group, then $a ∘ e$ is equal to $e ∘ a$ is equal to $a$.

$4$. Inverses: If you have $a$ in the group, then there is also $a^{-1}$ in the group where $a ∘ a^{-1}$ is equal to $e$.

Notice there is no point where I say that the operation is commutative (i.e. $a ∘ b = b ∘ a$). If it is commutative, it is also known as an Abelian group.

Also by the way, it is common to notate $a ∘ a ∘ a ∘ ... ∘ a$ $n$ times as $a^n$

A good way to think about what groups actually are is as symmetries. This is because these four rules are exactly what you would expect rotations and reflections to do with the operation of doing one after the other.

For example, now the inverses rule makes sense because if you rotate clockwise then of course you should also be able to rotate counterclockwise.

An example of a group is the integers with the operation of addition, but not the integers with an operation of multiplication because only $1$ and $-1$ have an inverse. The rational numbers under multiplication (excluding $0$) also form a group and so can the rationals under addition. Also of course, the real numbers with addition and multiplication (excluding $0$).

#### proofs

Proof number one: there's only one identity element.

This proof uses a proof by contradiction strategy. Let's say that there are more than one identity element. So I'm going to choose the first two being $e_1$ and $e_2$.

Now, I ask of you, what is $e_1 ∘ e_2$? Because on the one hand, it should equal $e_2$ because $e_1$ times anything is that thing. But on the other hand, it should equal $e_1$ because anything times $e_2$ is that thing.

Thus, because they are both equal to $e_1 ∘ e_2$, they must themselves be equal. Thus there is only one identity element.

And you can keep going with this logic, doing the same thing with the next one, and the next one, until there is only one left.

QED!

Proof number two: The inverse of the inverse is the original.

Every element has an inverse. So, by definition, the inverse has an inverse.

Let's operate all of these together and see what happens.

$$ a ∘ a^{-1} ∘ (a^{-1})^{-1} $$

This should of course equal $a$ because $a^{-1}$ times its inverse should cancel out. But also this should equal $(a^{-1})^{-1}$ because $a$ and its inverse should cancel out. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

Proof number three: The inverse can cancel out from either side.

The term $a^{-1} ∘ a$ can also be simplified. Because $a$ is equal to $(a^{-1})^{-1}$, I can cancel $a^{-1}$ with its inverse, resulting in the identity.

$$ a^{-1} ∘ a = a^{-1} ∘ (a^{-1})^{-1} = e $$

QED!

Proof number four: There's only one inverse for a given term.

This one uses the same general strategy as proof number one. Let's assume that there were multiple inverses, denoted $a^{-1}_1$ and $a^{-1}_2$. Then of course, $a ∘ a^{-1}_1 = e$.

Let's see what happens when you multiply both sides on the left by $a^{-1}_2$.

$$ a^{-1}_2 ∘ a ∘ a^{-1}_1 = a^{-1}_2 ∘ e $$

Then $a^{-1}_2$ and $a$ would cancel out resulting in $a^{-1}_1$ on the left. But on the other side, the identity element cancels out resulting in $a^{-1}_2$. Thus, because they are both equal to the same thing, they themselves must be equal.

$2000$ Lines, wow.

QED!

Proof number five: $(a^2)^{-1} = (a^{-1})^2$ and they can both be denoted as $a^{-2}$.

$$ a^2 ∘ (a^2)^{-1} = e $$

$$ a^2 ∘ (a^{-1})^2 = a ∘ a ∘ a^{-1} ∘ a^{-1} = a ∘ a^{-1} = e $$

Because these are both the inverse of $a^2$ and because of proof number four, they must both be the same.


$2013$ Lines (I was born in $2013$).

QED!

#### Newtonian physics

I tried to just write this down on paper, but I thought it would be much more convenient to write it down over here.

I'm going to try to use Newtonian physics to describe collision of spheres. Each sphere has an index $n$ with a center $c_n$, velocity $v_n$ acceleration $a_n$, and so on. If there's a property that doesn't have a subscript, then it works with any number.

$$ \text{V} = \frac{4}{3} \pi r^3 $$

$2025$ Lines.

$$ \text{V} = \frac{4 \pi}{3} r^3 $$

$$ \text{V} = \frac{2 \tau}{3} r^3 $$

$$ \text{V} = \frac{2}{3} \tau r^3 $$

$$ \text{D} = \frac{\text{M}}{\text{V}} $$

$$ \text{M} = \text{V} \text{D} $$

$$ \text{V} = \frac{\text{M}}{\text{D}} $$

#### the Fibonacci part of the eigen page, but better

Here's the obvious definition of the Fibonacci sequence:

$$ F_0 = 0 $$

$$ F_1 = 1 $$

$$ F_n = F_{n - 1} + F_{n - 2} $$

Yes, I know, it normally starts at $1$ and $2$, but there's a reason why I'm starting it at $0$ and $1$. But we still have the following:

$$ F_{n + 2} = F_{n + 1} + F_n $$

$$ F_{n + 1} = F_{n + 1} $$

$$ \begin{bmatrix} F_{n + 2} \\
F_{n + 1} \\ \end{bmatrix} = \begin{bmatrix} F_{n + 1} + F_n \\
F_{n + 1} \\ \end{bmatrix} = \begin{bmatrix} 1 F_{n + 1} + 1 F_n \\
1 F_{n + 1} + 0 F_n \\ \end{bmatrix} $$

$$ \begin{bmatrix} F_{n + 2} \\
F_{n + 1} \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_{n + 1} \\
F_n \\ \end{bmatrix} $$

$$ \begin{bmatrix} F_2 \\
F_1 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_1 \\
F_0 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$$ \begin{bmatrix} F_3 \\
F_2 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_2 \\
F_1 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^2 \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$$ \begin{bmatrix} F_4 \\
F_3 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_3 \\
F_2 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^2 \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^3 \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$$ \begin{bmatrix} F_5 \\
F_4 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_4 \\
F_3 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^3 \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^4 \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$2102$ Lines.

$$ \vdots $$

$$ \begin{bmatrix} F_{n + 1} \\
F_n \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^n \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

I know you're probably thinking: Yeah, that's a pretty nice formula. But still, how do I raise this matrix to the power of $n$? Well, to answer this question, we need a little bit of eigenvectors and eigenvalues.

That's enough work for one day.

The eigenvectors of a matrix $A$ are vectors where if you apply the matrix's operation, that just ends up scaling the vector by some constant $\lambda$ (a.k.a. the eigenvalue). In written form, it looks like this:

$$ A \vec{v} = \lambda \vec{v} $$

Also, an $n \times n$ matrix usually has $n$ eigenvectors*.

Side note!

$$ A (c \vec{v}) = \lambda (c \vec{v}) $$

*What this means is that the scaled copies of a given eigenvector are also eigenvectors and have the same eigenvalue. For this reason, scaled copies of an eigenvector are usually considered as just one.

But, assuming that there are two eigenvectors, I can do something special: I can change the basis.

$$ A(a \vec{u} + b \vec{v}) = A(a \vec{u}) + A(b \vec{v}) = a(A \vec{u}) + b(A \vec{v}) $$

$$ A(a \vec{u} + b \vec{v}) = a \lambda_1 \vec{u} + b \lambda_2 \vec{v} $$

$$ A(A(a \vec{u} + b \vec{v})) = A^2 (a \vec{u} + b \vec{v}) = A(a \lambda_1 \vec{u} + b \lambda_2 \vec{v}) = a \lambda_1^2 \vec{u} + b \lambda_2^2 \vec{v} $$

$$ A^2 (a \vec{u} + b \vec{v}) = a \lambda_1^2 \vec{u} + b \lambda_2^2 \vec{v} $$

$$ A(A^2 (a \vec{u} + b \vec{v})) = A^3 (a \vec{u} + b \vec{v}) = A(a \lambda_1^2 \vec{u} + b \lambda_2^2 \vec{v}) = a \lambda_1^3 \vec{u} + b \lambda_2^3 \vec{v} $$

$$ A^3 (a \vec{u} + b \vec{v}) = a \lambda_1^3 \vec{u} + b \lambda_2^3 \vec{v} $$

$$ \vdots $$

$$ A^n (a \vec{u} + b \vec{v}) = a \lambda_1^n \vec{u} + b \lambda_2^n \vec{v} $$

As you can see, this can be very useful for finding $\begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^n$. We just need to figure out the eigenvectors, eigenvalues, and how to combine them.

That's enough work for now.

It's been $3$ hours.

$$ \varphi^2 = \varphi + 1 $$

$$ \psi^2 = \psi + 1 $$

$$ \varphi = \frac{1 + \sqrt{5}}{2} = 1.618... $$

$$ \psi = \frac{1 - \sqrt{5}}{2} = -0.618... = -\frac{1}{\varphi} = 1 - \varphi $$

$$ \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} = \begin{bmatrix} 1 \cdot \varphi + 1 \cdot 1 \\
1 \cdot \varphi + 0 \cdot 1 \\ \end{bmatrix} = \begin{bmatrix} \varphi + 1 \\
\varphi \\ \end{bmatrix} = \begin{bmatrix} \varphi^2 \\
\varphi \\ \end{bmatrix} $$

$$ \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} = \varphi \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} $$

$$ \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} = \begin{bmatrix} 1 \cdot \psi + 1 \cdot 1 \\
1 \cdot \psi + 0 \cdot 1 \\ \end{bmatrix} = \begin{bmatrix} \psi + 1 \\
\psi \\ \end{bmatrix} = \begin{bmatrix} \psi^2 \\
\psi \\ \end{bmatrix} $$

$$ \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} = \psi \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} $$

$$ \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix}^n (a \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} + b \begin{bmatrix} \psi \\
1 \\ \end{bmatrix}) = a \varphi^n \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} + b \psi^n \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} $$

But, now the question becomes: how do I write $\begin{bmatrix} 1 \\
0 \\ \end{bmatrix}$ in terms of $\begin{bmatrix} \varphi \\
1 \\ \end{bmatrix}$ and $\begin{bmatrix} \psi \\
1 \\ \end{bmatrix}$?

$$ \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} = a \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} + b \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} $$

$2201$ Lines.

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} x \\
y \\ \end{bmatrix} = \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (x \hat{x} + y \hat{y}) = \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (x \hat{x}) + \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} (y \hat{y}) = x \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \hat{x} + y \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \hat{y} $$

$$ \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} \begin{bmatrix} x \\
y \\ \end{bmatrix} = x \begin{bmatrix} a \\
c \\ \end{bmatrix} + y \begin{bmatrix} b \\
d \\ \end{bmatrix} $$

$$ \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix} \begin{bmatrix} a \\
b \\ \end{bmatrix} = a \begin{bmatrix} \varphi \\
1 \\ \end{bmatrix} + b \begin{bmatrix} \psi \\
1 \\ \end{bmatrix} $$

$2222 + 2$ Lines.

$$ \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix} \begin{bmatrix} a \\
b \\ \end{bmatrix} = \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$$ \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix}^{-1} \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix} \begin{bmatrix} a \\
b \\ \end{bmatrix} = \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix}^{-1} \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

$$ \begin{bmatrix} a \\
b \\ \end{bmatrix} = \begin{bmatrix} \varphi & \psi \\
1 & 1 \\ \end{bmatrix}^{-1} \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} $$

#### an inductive set theoretic proof (unfinished)

This proof partially comes from [Another Roof](https://www.youtube.com/watch?v=rhhhUAAAh-g).

Also, before I start with how addition is set theoretically defined, I have the notation $\text{S} (n)$ pronounced "the successor of $n$" which means $n + 1$, which can easily be defined within set theory.

$$ n + 0 : = n $$

$$ a + \text{S} (b) : = \text{S} (a + b) $$

Here's an example:

$$ n + 3 = n + \text{S} (2) : = \text{S} (n + 2) = \text{S} (n + \text{S} (1)) : = \text{S} (\text{S} (n + 1)) = \text{S} (\text{S} (n + \text{S} (0))) : = \text{S} (\text{S} (\text{S} (n + 0))) $$

$$ n + 3 = \text{S} (\text{S} (\text{S} (n))) $$

Now, how do I inductively prove that the following is true?

$$ a + b = b + a $$

Obviously I use induction on $b$. First, base case, set $b$ to zero.

$$ a + 0 = 0 + a $$

$$ a + 0 : = a $$

$$ 0 + a = a $$

So, of course, to figure this out, just use induction on $a$!

Base case:

$$ 0 + 0 = 0 $$

This statement is true by definition.

Inductive reasoning:

$$ 0 + a = a $$

$$ 0 + \text{S} (a) : = \text{S} (0 + a) = \text{S} (a) = \text{S} (a) $$

### set theory 3?

#### what is a set?

A set is a collection of things...

... Okay, fine I'll be more specific. A set can contain a certain amount of objects, so for example, I could have the set containing this mouse that I'm holding and this chair that I'm sitting on.

So a set kind of means a collection or a group, but group theory is a [whole other page](https://silaspe.github.io/maths/group_theory.html).

Note: the elements (that is, the things part of the set, a.k.a. the members of it) are not ordered within a set, and a set having the same element twice doesn't change the set. When you ask the question "is this thing part of your set?" I can only answer with a yes or a no.

In other words, sets are only defined by their elements.


$2300$ Lines.

As for some notation, the set of all even numbers would be written as $\{ 2, 4, 6, 8 ... \}$, $\{$ numbers $n: n$ is even $\}$, or $\{ x: x$ is a number and is even $\}$. (Pronounced "the set containing $2$, $4$, $6$, $8$ and so on", "the set of all numbers $n$ where $n$ is even", and "the set of all $x$ where $x$ is a number, and furthermore, $x$ is even" respectively.)

Also, the symbol for "$x$ is a member of $S$" where $S$ is a set is $x \in S$.

But sets can contain more than just things, they can contain other sets.

But this leads to a paradox: would $\{S:$ not $S \in S \}$ (the set containing only the sets that don't contain themselves) contain itself? (P.S. there's [a great video on this](https://www.youtube.com/watch?v=xauCQpnbNAM).)

Clearly there's a problem with this. Let's take a step back.

#### what is a set, really?

Idk. I'd rather talk about...

#### ordinals

$$ 0 = Ø $$

$$ 1 = \{ 0 \} $$

$$ 2 = \{ 1 \} $$

$$ 3 = \{ 2 \} $$

$$ \omega = \{ 0, 1, 2, 3 ... \} $$

$$ \omega + 1 = \{ \omega \} $$

$$ \omega + 2 = \{ \omega + 1 \} $$

$$ \omega + 3 = \{ \omega + 2 \} $$

$$ \omega + \omega = 2 \omega = \{ \omega, \omega + 1, \omega + 2, \omega + 3 ... \} $$

$$ 2 \omega + 1 = \{ 2 \omega \} $$

$$ 2 \omega + 2 = \{ 2 \omega + 1 \} $$

$$ 2 \omega + 3 = \{ 2 \omega + 2 \} $$

$$ 2 \omega + \omega = 3 \omega = \{ 2 \omega, 2 \omega + 1, 2 \omega + 2, 2 \omega + 3 ... \} $$

$$ \omega \omega = \omega^2 = \{ \omega, 2 \omega, 3 \omega ... \} $$

$$ \omega^2 + 1 = \{ \omega^2 \} $$

$$ \omega^2 + 2 = \{ \omega^2 + 1 \} $$

$$ \omega^2 + 3 = \{ \omega^2 + 2 \} $$

$$ \omega^2 + \omega = \{ \omega^2, \omega^2 + 1, \omega^2 + 2, \omega^2 + 3 ... \} $$

$$ \omega^2 + \omega + 1 = \{ \omega^2 + \omega \} $$

$$ \omega^2 + \omega + 2 = \{ \omega^2 + \omega + 1 \} $$

$$ \omega^2 + \omega + 3 = \{ \omega^2 + \omega + 2 \} $$

$$ \omega^2 + \omega + \omega = \omega^2 + 2 \omega = \{ \omega^2 + \omega, \omega^2 + \omega + 1, \omega^2 + \omega + 2, \omega^2 + \omega + 3 ... \} $$

$$ \omega^2 + \omega \omega = \omega^2 + \omega^2 = 2 \omega^2 = \{ \omega^2, \omega^2 + \omega, \omega^2 + 2 \omega ... \} $$

$$ 2 \omega^2 + 1 = \{ 2 \omega^2 \} $$

$$ 2 \omega^2 + 2 = \{ 2 \omega^2 + 1 \} $$

$$ 2 \omega^2 + 3 = \{ 2 \omega^2 + 2 \} $$

$$ 2 \omega^2 + \omega = \{ 2 \omega^2, 2 \omega^2 + 1, 2 \omega^2 + 2, 2 \omega^2 + 3 ... \} $$

$$ 2 \omega^2 + \omega + 1 = \{ 2 \omega^2 + \omega \} $$

$$ 2 \omega^2 + \omega + 2 = \{ 2 \omega^2 + \omega + 1 \} $$

$$ 2 \omega^2 + \omega + 3 = \{ 2 \omega^2 + \omega + 2 \} $$

$$ 2 \omega^2 + \omega + \omega = 2 \omega^2 + 2 \omega = \{ 2 \omega^2 + \omega, 2 \omega^2 + \omega + 1, 2 \omega^2 + \omega + 2, 2 \omega^2 + \omega + 3 ... \} $$

$$ 2 \omega^2 + \omega \omega = 2 \omega^2 + \omega^2 = 3 \omega^2 = \{ 2 \omega^2, 2 \omega^2 + \omega, 2 \omega^2 + 2 \omega ... \} $$

$$ \omega \omega^2 = \omega^3 = \{ \omega^2, 2 \omega^2, 3 \omega^2 ... \} $$

$$ \omega^3 + \omega \omega^2 = \omega^3 + \omega^3 = 2 \omega^3 = \{ \omega^3, \omega^3 + \omega^2, \omega^3 + 2 \omega^2 ... \} $$

$$ 2 \omega^3 + \omega \omega^2 = 2 \omega^3 + \omega^3 = 3 \omega^3 = \{ 2 \omega^3, 2 \omega^3 + \omega^2, 2 \omega^3 + 2 \omega^2 ... \} $$

$$ \omega \omega^3 = \omega^4 = \{ \omega^3, 2 \omega^3, 3 \omega^3 ... \} $$

$$ \omega^{\omega} = \{ \omega, \omega^2, \omega^3, \omega^4 ... \} $$

$$ \omega \omega^{\omega} = \omega^{\omega + 1} = \{ \omega^{\omega}, 2 \omega^{\omega}, 3 \omega^{\omega} ... \} $$

$$ \omega \omega^{\omega + 1} = \omega^{\omega + 2} = \{ \omega^{\omega + 1}, 2 \omega^{\omega + 1}, 3 \omega^{\omega + 1} ... \} $$

Wait a minute! I can just do what I've already done, but in the exponents.

$$ \omega^{\omega^{\omega}} = \{ \omega^{\omega}, \omega^{\omega^2}, \omega^{\omega^3} ... \} $$

$2400$ Lines.

$$ \omega^{\omega^{\omega^{\omega}}} = \{ \omega^{\omega^{\omega}}, \omega^{\omega^{\omega^2}}, \omega^{\omega^{\omega^3}} ... \} $$

$$ \epsilon_0 = \{ \omega, \omega^{\omega}, \omega^{\omega^{\omega}}, \omega^{\omega^{\omega^{\omega}}} ... \} $$
