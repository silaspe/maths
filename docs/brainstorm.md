The equations below are the beginning of pages that may or may not get added to my website. All pages after Modular arithmetic and this one started here in the brainstorm page. I got (almost all of) these from copying things from a piece of paper (actually, just the one below) that had potential to become a digital page. And finaly, the titles have a question mark if they are my best guss for the titles of the page, no question mark if I made the page and know the title, a question mark if I never published the page, but still want the world to see it, and extra small if is just one puzzle, but didn't fit anywhere and/or was worth making a dedicated page. Also, happy eclipse day! The eclipse was worth the $10$ (total) hours of driving.

### galois theory/field theory/group theory?

A field of numbers is a collection of numbers where you can add, subtract, multiply, and even sometimes divide two numbers (as long as you don't divide by zero) in that field to get another number in that field. For example, the rationals, the reals and the complex numbers ane all fields that are infinate and you can divide them. The complex lattice points (which are complex numbers of the form $integer + integer \cdot i$ ), the matrixes (insert joke here), and the integers, are all in the infinate but can not always be divided. I know what you might be thinking: "what the (abbreviation that I am allowed to say for a curse word that I am not allowed to say) is a non-infinate field?". A non-infinite field or finite field is something like the [modulo numbers](https://silaspe.github.io/maths/mod.html). You might not be able to divide in a non-prime base, but you can do it in a prime base. So that completes the venn diagram!

Today, I want to show you an infinate field where you can not divide, I'm talking (well, typing) about numbers of the form

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

Yeah, I forgot all endings to multiplying vectors, so I came up with the previous one. Well, I guss I had this one, but I would rather make it into it's own page. After waching [A Swift Introduction to Geometric Algebra](https://www.youtube.com/watch?v=60z_hpEAtD8) (litteraly, that was the name), I thought that (if it is a scalar plus a bivector), than it is just a scalar plus a vector times $i$ (or $-i$, I am not sure yet), but I will call it $U$ instead. But first, here's the definition of multiplying two basis vectors (all the alternitave endings probably just had alternitave definitions for this. I think that I remember the definition that multiplication was anticomutative, which would lead me to the cross product): The prodct of a basis vector $e_1$ and it self is $0$, and the product of two basis vectors $e_1$ and $e_2$ equals $-e_2 e_1$ equals $e_3$. This means that you can do this at any point in the product of basis vectors.

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

$$ \text{Yes! Now I can finaly solve the puzzle.} $$

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

Also, the cross product only works in $3d$ while this $\hat{i} \hat{j} \hat{k} \text{ } \vec{u} \times \vec{v}$ thing works in any dimention. This operator actually has a name (well, two names), the outer product (as oppose to the dot product sometimes refered to as the inner product) or wedge product for it's apperance as a wedge unicode character. This more genaral cross product is written $\vec{u} ∧ \vec{v}$

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

$$ \text{Lets say that we are in dimension } d \text{. First, basis vectors} $$

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

$$ \text{A set is a well defined collection of objects, a set could contain the two shoes on you feet, or the } 5 \text{ peices of chese on this cutting board (that I'm going to pretend exists), sets can even contain other sets, but sets can not contain themselfes, because tis would lead to a paradox: would the set that contains every set that doesn't contain itsef contain itself?" this also means that there isn't a set that contains everything.} $$

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

$$ = : \text{ Is pronounced "equals by definition" and means "define the thing on the left as the thing on the right", or was it the other wat around?} $$

$$ = \text{ Is pronounced "is the same as" and I'll get to it's formal meaning in the next chapter.} $$

$$ \in^S \text{ Is pronounced "is a super element of" (} S \text{ for super) and I'll get to it's meaning in the next chapter.} $$

$$ ∨ \text{ Is pronounced "or" and means "} a ∨ b \text{ is true if statement } a \text{ is true or } b \text{ is true... Or both!", it can also mean the union of two sets, in that case, it is pronounced "unioned with", but I'll get to it's formal meaning in the next chapter.} $$

$$ \text{succ Is pronounced "the immediate successor of" and means "that number } + 1 \text{".} $$

$$ set \text{ Is pronounced "the set containing" as in "} set(S) \text{" and I'll get to it's formal meaning in the next chapter.} $$

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

$$ \text{succ} (n) \text{ (Which mathematicly equals } n + 1 \text{) Is how you would usually define numbers, so I'll define numbers that way, I'll say that succ} (n) \text{ is the set that contains all numbers } 0 \text{-} n \text{. But first: the union of two sets, denoted as an } ∨ \text{ sign.} $$

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

$$ \text{And finaly,} $$

$$ |.^{|........} = |.^{Byte} = \text{ Byteplex or sha (for sha } 256 \text{)} $$

$$ \text{And then, for the other powers of two, combine the names, so } |... = |.. \text{ } \cdot \text{ } |. = \text{ Four } + \text{ Two } = \text{ Four Two. Then, to get things that are other than powers of two, combine the names of all of the powers of two that sum to it, largest to smallest. (Also, } . = \text{Zero.)} $$

$$ \text{So, } |..| = |... + | = \text{ Four two } + \text{ One } = \text{ Four Two One. But the thing is, } ||| \text{ is also pronounced "Four Two One". Okay, so, if something like that happens where the first part of the next digit is smaller that the last part of the previous digit, then... Um...} $$

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

$$ \text{This chapter is about writing numbers as infinate dimentional vectors (if the vector components are } 3 \text{, } 4 \text{, } 5 \text{ and then infinite } 0 \text{'s, than it would be written as } [3 \text{, } 4 \text{, } 5 \text{, } 0 \text{, } 0 \text{, } 0...] \text{), this is how:} $$

$$ 2025000 = 2^3 \cdot 3^4 \cdot 5^5 \cdot 7^0 \cdot 11^0 \cdot 13^0 \cdot ... \rightarrow \vec{2025000} = [3 \text{, } 4 \text{, } 5 \text{, } 0 \text{, } 0 \text{, } 0...] $$

$$ \text{Before we do vector addition and scalar multiplcation, here's some code:} $$

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

$$ \text{E} (x; p(x)) = \text{ The extention of } p(x) \text{, the set of all } x \text{ such that } p(x) \text{ (is true) (the function } p(x) \text{ inputs, well, anything, and outputs a boolean (true or false) (e.g. is } x \text{ an odd number?)), and this is how I'm going to define sets.} $$

$$ \text{The extention of that particular function is the set of all odd numbers.} $$

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

### projective geometry?

Credit (even if it is very small): [The two points that lie on every circle (???) #SoME3](https://www.youtube.com/watch?v=iUUm0sKLoiE), [Putting Algebraic Curves in Perspective](https://www.youtube.com/watch?v=XXzhqStLG-4), and [Extraordinary Conics: The Most Difficult Math Problem I Ever Solved](https://www.youtube.com/watch?v=X83vac2uTUs).

Yes, I know, the last one was added literally $4$ days ago, but I thougt of something else to talk about.

Lets say that a point $(a: b)$ (as opposed to $(a, b)$) is equal to $(ca: cb)$ $(c \ne 0)$, so every* (and that's a big asterisk) point $(a: b)$ can be scaled onto $(\frac{a}{b}: 1)$, a kind of number line.

*unless $b = 0$, then we add this kind of "point at infinity" to our number line (it's a single point because the point $(a: 0)$ can be scaled to $(1: 0)$ (aka the point at infinity), that is, of coarse, unless $a = 0$, but that point isn't really aloud for the same reason as $\frac{0}{0}$) making it the real projective line or $ℝ \text{P}^1$.

The reason why it's at infinity is because, if you consider the point $(1: 1)$, it falls onto $1$ on the number line, the point $(1: \frac{1}{2})$ falls onto $2$, the point $(1: \frac{1}{4})$ falls onto $4$, the point $(1: \frac{1}{8})$ falls onto $8$, and as the second number gets smaller, the point on the number line gets bigger aproaching infinity, hence the name "point at infinity". But, if you instead do this from the other direction, it approaches negative infinity. You can imagine a number line that curves down as it goes along, consecutave integers getting closer and closer, and an unsigned infinity at the bottom where the line meets itself.

Stepping a dimension up, you get the real projective plane or $ℝ \text{P}^2$, $(a: b: c) = (da: db: dc)$, most numbers going to $(\frac{a}{c}: \frac{b}{c}: 1)$, some becoming $(\frac{a}{b}: 1: 0)$, less becoming $(1: 0: 0)$, the point at infinity becomes a line at infinity (more of a circle, but $1$ degree of freedom, so it's a line), and the number line becomes a space of all points.

There is a problem though (that is big enough to be explained on a line by itself), you could imagine the same process that I used to prove the unsigned infinity thing but in $ℝ \text{P}^2$ to get the unsuprising result of $(a: b: 0) = (-a: -b: 0)$. This does mean that, when drawing the regular or affine plane, and drawing a circle around it (to represent the line at infinity of coarse), if you wanted to draw, say, the point $(1: 1: 0)$, it would need to be at both the very top right, and the very bottom left of the circle.

To see why this double counting thing makes sense, I'll project onto a unit sphere, so, if $r = \sqrt{a^2 + b^2 + c^2}$, the point $(a: b: c)$ maps to $(\frac{a}{r}: \frac{b}{r}: \frac{c}{r})$. You might see the problem though, it also maps to $(-\frac{a}{r}: -\frac{b}{r}: -\frac{c}{r})$, because it's also on the unit sphere. So, if you just consider the top half of the sphere (includineg the equator so that points at infinity are acounted for), it counts almost every point once, and points at infinity twice, kinda like the one where we projected onto the plane paralel to and one unit above the $xy$ plane. So, to fix this problem, and give every point the same treatment, you (counterintuitavely) count every point twice by using the entire sphere, kinda like giving every line in $2d$ an angle instead of a slope to fix the vertical lines problem, at the cost of there being two angles for every line.

[Here's a desmos graph](https://www.desmos.com/3d/zzoajkphnn).

Yes, I know, the plane is placed one unit below the sphere instead of one above, but it's only like that for the sake of demonstration.

### dualtity?

It's hard to explain how points dual to lines, but an example would be the origin and the line at infinity, or on the sphere, the equator and the north and south poles (remember, two solutions). the more general definition would be something like this: the two points on a sphere, a point on the dual line, and the point $90°$ away but still on the dual line are all mutually perpindicular. By the way, points on the plane project to antipodal points on the sphere, and lines on the plane project to great circles on the sphere.

Also fun fact: the duals of every point on a line would all pass through the dual point, and the duals of every line that passes through a point would all lie on the dual line.

### linear algebra, complex numbers, and higher dimensional complex numbers

$$ \text{Let's say that a vector } \vec{v} \text{ is an ordered set of numbers } \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} \text{, or } v_x \hat{x} + v_y \hat{y} \text{, or a point } (v_x, v_y) \text{, or an arrow with it's tip at } (v_x, v_y) \text{, and tail at } (0, 0) \text{. They can be scaled (that is, multiplied by a scalar or real number) (} c \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = c(v_x \hat{x} + v_y \hat{y} = c v_x \hat{x} + c v_y \hat{y}) = \begin{bmatrix} c v_x \\
c v_y \\ \end{bmatrix} \text{), added (} \begin{bmatrix} u_x \\
u_y \\ \end{bmatrix} + \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = u_x \hat{x} + u_y \hat{y} + v_x \hat{x} + v_y \hat{y} = (u_x + v_x) \hat{x} + (u_y + v_y) \hat{y} = \begin{bmatrix} u_x + v_x \\
u_y + v_y \\ \end{bmatrix} \text{), and with just those two, any vector can be made from } \begin{bmatrix} 1 \\
0 \\ \end{bmatrix} \text{ and } \begin{bmatrix} 0 \\
1 \\ \end{bmatrix} \text{ (that is, } 1 \hat{x} + 0 \hat{y} \text{ and } 0 \hat{x} + 1 \hat{y} \text{ (that is, } \hat{x} \text{ and } \hat{y} \text{)), and that's pprreeaattyy much it.} $$

You can also multiply vectors, but that's a [story for another day](https://silaspe.github.io/maths/geometric_algebra.html).

$$ \text{Let's say that a matrix } A \text{ is an ordered set of numbers arranged in a square: } \begin{bmatrix} a_{11} & a_{21} \\
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

$$ \text{And if you were wondering, this also works in } 3d \text{ or higher, with } \hat{z} \text{, } \hat{w} \text{, and so on.} $$

$$ \text{Next, complex numbers!} $$

Complex numbers are, if I'm gonna quote Morphocular in [this video](https://www.youtube.com/watch?v=4KlvI_uK9zs&t=470s), the language of $2d$ rotation. I'll desribe them in an unusual way:

$900$ Lines.

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

$$ \text{Ok, you might have seen that one comming.} $$
