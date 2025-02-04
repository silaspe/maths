Learn more [here](https://www.youtube.com/watch?v=kYB8IZa5AuE), [here](https://www.youtube.com/watch?v=XkY2DOUCWMU), [here](https://www.youtube.com/watch?v=O85OWBJ2ayo&t=194s), [here](https://www.youtube.com/watch?v=uQhTuRlWMxw&t=592s), [here](https://www.youtube.com/watch?v=PFDu9oVAE-g&t=960s), [here](https://www.youtube.com/watch?v=uQhTuRlWMxw&t=283s), [and here](https://www.youtube.com/watch?v=P2LTAUO1TdA) in that order if you stop at 3:54 on the third, 10:44 on the fourth, 16:01 on the fifth, 4:53 on the sixth, and 12:21 on the seventh

by the way, any matrix to the power of zero is the identity matrix $I$

and you can add and subtract matrices term by term

### I want to take a matrix to a large power $n$

if the matrix (I'll call it $A$) is diagonal, in other words if it is of the form below

$$ \begin{bmatrix} a & 0 & 0 & \dots \\
0 & b & 0 & \dots \\
0 & 0 & c & \dots \\
\vdots & \vdots & \vdots & \ddots \\ \end{bmatrix} $$

or because I am assuming $A$ is a $2 \times 2$ matrix, it's probably more like

$$ \begin{bmatrix} a & 0 \\
0 & b \\ \end{bmatrix}$$

than $A^n$ is the matrix below:

$$ \begin{bmatrix} a^n & 0 \\
0 & b^n \\ \end{bmatrix}$$

but if $A$ is not diagonal, than just switch to a basis (in particular, an eigenbasis that I will dedicate the rest of the page or)
the eigenvector as it is called, is also just useful in other cases like when you need to find the next [fibonacci number](https://silaspe.github.io/maths/fibonacci.md), or find the flow in a population of foxes and rabbits (even if you need to see the entire second video) which I will do both of those at the end of the page

So the top question is...

### what even is an eigenvector?

an eigenvector is really a set of vectors (that I will refer to from now on as an eigenset) that are all multiples of each other can be defined as the slope of the line that connects the tips of vectors in said eigenset, and an eigenvector is defined as a vector within said eigenset, unfortunately the slope is not the corresponding eigenvalue, but that this slope can also be $\frac{1}{0}$ if it is pointing straight up, also on the note of eigensets, there can be two (two slopes, not two vectors) with any given matrix, I'll give you an example

but you are probably just waiting for the definition, and here it is:

under multiplication by matrix $A$, most vectors are rotated and scaled, but any eigenvector (or vector within the eigenset) is just scaled, and it makes sense that $2$ times the eigenvector isn't scaled either, thus every vector within the eigenset is an eigenvector, and the eigenvalue? that corresponds to how much each vector is scaled, and two different eigensets usually have different eigenvalues.

But you are probably just waiting for the example, and here it is:

a matrix with a [determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk0) of $0$, and a [rank](https://www.youtube.com/watch?v=uQhTuRlWMxw) of $1$ has eigensets of the line that it squishes space onto, and the null space of the matrix.

Anyways, on to my favorite part! (And reason I made this page)

### how to find the eigenvectors and eigenvalues

$$ \text{eigenvector} = \vec{v} = \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} $$

$$ \text{eigenvalue} = \lambda $$

$$ \text{eigenset} = r = \frac{v_y}{v_x} $$

$$ \text{matrix} = A $$

$$ A \vec{v} = \lambda \vec{v} $$

$$ I = \begin{bmatrix} 1 & 0 \\
0 & 1 \\ \end{bmatrix} $$

$$ I \vec{v} = \vec{v} $$

$$ A \vec{v} = \lambda (I \vec{v}) = (\lambda I) \vec{v} $$

$$ A \vec{v} - (\lambda I) \vec{v} = \vec{0} $$

$$ (A - \lambda I) \vec{v} = \vec{0} $$

$$ \lambda I = \begin{bmatrix} \lambda & 0 \\
0 & \lambda \\ \end{bmatrix} $$

$$ A = \begin{bmatrix} a & b \\
c & d \\ \end{bmatrix} $$

$$ \begin{bmatrix} a - \lambda & b \\
c & d - \lambda \\ \end{bmatrix} \vec{v} = \vec{0} $$

$$ \begin{bmatrix} a - \lambda & b \\
c & d - \lambda \\ \end{bmatrix} = A^{\star} $$

$$ a - \lambda = a^{\star} $$

$$ b = b^{\star} $$

$$ c = c^{\star} $$

$$ d - \lambda = d^{\star} $$

$$ A^{\star} = \begin{bmatrix} a^{\star} & b^{\star} \\
c^{\star} & d^{\star} \\ \end{bmatrix} $$

$$ A^{\star} \vec{v} = \vec{0} $$

$$ \vec{v} = v_x \hat{i} + v_y \hat{j} \neq \vec{0} = \begin{bmatrix} 0 \\
0 \\ \end{bmatrix} = 0 \hat{i} + 0 \hat{j}  $$

$$ A^{\star} \vec{v} = A^{\star} (v_x \hat{i} + v_y \hat{j}) = v_x (A^{\star} \hat{i}) + v_y (A^{\star} \hat{j}) = 0 $$


$100$ lines.

$$ v_x (A^{\star} \hat{i}) = - v_y (A^{\star} \hat{j}) $$

$$ -\frac{v_x}{v_y} A^{\star} \hat{i} = A^{\star} \hat{j} $$

$$ -\frac{v_x}{v_y} A^{\star}_x = A^{\star}_y $$

$$ -\frac{v_x}{v_y} \begin{bmatrix} a^{\star} \\
c^{\star} \\ \end{bmatrix} = \begin{bmatrix} b^{\star} \\
d^{\star} \\ \end{bmatrix} $$

$$ -\frac{1}{r} \begin{bmatrix} a^{\star} \\
c^{\star} \\ \end{bmatrix} = \begin{bmatrix} b^{\star} \\
d^{\star} \\ \end{bmatrix} $$

$$ \begin{bmatrix} a^{\star} \\
c^{\star} \\ \end{bmatrix} = \begin{bmatrix} -r b^{\star} \\
-r d^{\star} \\ \end{bmatrix} $$

$$ a^{\star} = -r b^{\star} $$

$$ c^{\star} = -r d^{\star} $$

$$ -r d^{\star} = c^{\star} $$

$$ -r a^{\star} d^{\star} = -b^{\star} r c^{\star} $$

$$ a^{\star} d^{\star} = b^{\star} c^{\star} $$

$$ a^{\star} d^{\star} - b^{\star} c^{\star} = 0 $$

$$ (a - \lambda)(d - \lambda) - bc = 0 $$

$$ ad - a \lambda - d \lambda + \lambda^2 - bc = 0 $$

$$ (1) \lambda^2 + (-(a + d)) \lambda + (ad - bc) = 0 $$

$$ \lambda = \frac{a + d}{2} \pm \frac{\sqrt{a^2 + 2ad + d^2 - 4ad+ 4bc}}{2} = \frac{a + d}{2} \pm \frac{\sqrt{a^2 - 2ad + d^2 + 4bc}}{2} $$

$$ \lambda = \begin{Bmatrix} bd = 0 \to \lambda = a, \lambda = d \\
bd \neq 0 \to \lambda = \frac{a + d + \sqrt{(a - d)^2 + 4bc}}{2}, \lambda = \frac{a + d - \sqrt{(a - d)^2 + 4bc}}{2} \\ \end{Bmatrix} $$

$$ -r = \frac{a^{\star}}{b^{\star}} = \frac{c^{\star}}{d^{\star}} $$

$$ r = -\frac{a^{\star}}{b^{\star}} = -\frac{c^{\star}}{d^{\star}} = -\frac{a - \lambda}{b} = -\frac{c}{d - \lambda} $$

Another thing that is important is that if an eigenset is stable equilibrium (sorry, I couldn't find a good video), the eigenvector is an equilibrium.

So if vectors will slowly drift towards the eigenset as you apply the transformation, then it is convergent, but if vectors will slowly drift away from the eigenset as you apply the transformation, then it is divergent.

I wanted to prove how to compute this, but then I had to find out the point to line distance formula, which requires the inverse pythagorean theorem, which requires the pythagorean theorem, and I don't know how to prove that without geometry

so I will just tell you if an eigenset is convergent or not in the next part which I said I would do eventually... 

### fibonacci

$$ F_n = F_{n - 1} + F_{n - 2} $$

$$ F_1 = 1 $$

$$ F_2 = 1 $$

$$ F_{n + 1} = ?(F_n) $$

$$ F_n = 1 F_{n - 1} + 1 F_{n - 2} $$

$$ F_{n - 1} = 1 F_{n - 1} + 0 F_{n - 2} $$

$$ \begin{bmatrix} F_n \\
F_{n - 1} \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_{n - 1} \\
F_{n - 2} \\ \end{bmatrix} $$

$$ \lambda = \frac{1 + \sqrt{5}}{2} = \phi, \lambda = \frac{1 - \sqrt{5}}{2} = \psi $$

$$ \phi = : 1 + \frac{1}{\phi} = \frac{1 + \sqrt{5}}{2} $$

$$ \psi = : 1 + \frac{1}{\psi} = \frac{1 - \sqrt{5}}{2} $$

The $\phi$ one is convergent, the $\psi$ one is not.

$$ r = \frac{1}{\phi}, r =\frac{1}{\psi}  $$

Once again, the $\phi$ one is convergent, the $\psi$ one is not.

but, if it is convergent when making the next fibonacci number, then all possible starting conditions* will eventually approach the $\frac{F_n}{F_{n - 1}} = \phi$, but if that is true then...

*Even if it is not stable, if the starting conditions lie directly on the alternative line, the ratio of terms doesn't approach, but always is $\psi$, but that is irrational, so an easy fix is to make both of the initial conditions integers. Anyways...

$$ \frac{F_{n + 1}}{F_n} \to \phi $$

$$ F_{n + 1} \approx \phi F_n $$

okay, I have the next fibonacci number, onto foxes and rabbits

### which one would win in a boxing match, the fox or the rabbit?



$200$ lines.

$$ \frac{d}{dt} \begin{bmatrix} f(t) \\
g(t) \\ \end{bmatrix} = \begin{bmatrix} f\prime (t) \\
g\prime (t) \\ \end{bmatrix} $$

$$ r(t) = \text{ The number of rabbits.} $$

$$ f(t) = \text{ The number of foxes.} $$

$$ r\prime (t) = \alpha r(t) - \beta f(t) $$

$$ f\prime (t) = \gamma f(t) + \delta r(t) $$

$$ \begin{bmatrix} r\prime (t) \\
f\prime (t) \\ \end{bmatrix} = \begin{bmatrix} \alpha & - \beta \\
\delta & \gamma \\ \end{bmatrix} \begin{bmatrix} r(t) \\
f(t) \\ \end{bmatrix} $$

$$ \lambda = \begin{Bmatrix} \beta \gamma = 0 \to \lambda = \alpha, \lambda = \gamma \\
\beta \gamma \neq 0 \to \lambda = \frac{\alpha + \gamma + \sqrt{(\alpha - \gamma)^2 - 4 \beta \delta}}{2}, \lambda = \frac{\alpha + \gamma - \sqrt{(\alpha - \gamma)^2 - 4 \beta \delta}}{2} \\ \end{Bmatrix} $$

$$ r = \frac{\alpha - \lambda}{\beta} $$
