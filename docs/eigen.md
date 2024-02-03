Learn more [here](https://www.youtube.com/watch?v=XkY2DOUCWMU), [here](https://www.youtube.com/watch?v=O85OWBJ2ayo&t=194s), [here](https://www.youtube.com/watch?v=uQhTuRlWMxw&t=592s), [here](https://www.youtube.com/watch?v=PFDu9oVAE-g&t=960s), [here](https://www.youtube.com/watch?v=uQhTuRlWMxw&t=283s), [and here](https://www.youtube.com/watch?v=P2LTAUO1TdA) in that order if you stop at 3:54 on the second, 10:44 on the third, 16:01 on the fourth, 4:53 on the fifth, and 12:21 on the sixth

by the way, any matrix to the power of zero is the identity matrix $I$

and you can add and subtract matrices term by term

### I want to take a matrix to a large power $n$

if the matrix (I'll call it $A$) is diagonal, in other words if it is of the form below

$$ \begin{bmatrix} a & 0 & 0 & \dots \\
0 & b & 0 & \dots \\
0 & 0 & c & \dots \\
\vdots & \vdots & \vdots & \ddots \\ \end{bmatrix} $$

or because I am assuming $A$ is a $2 \times 2$ matrix, its probably more like

$$ \begin{bmatrix} a & 0 \\
0 & b \\ \end{bmatrix}$$

than $A^n$ is the matrix below:

$$ \begin{bmatrix} a^n & 0 \\
0 & b^n \\ \end{bmatrix}$$

but if $A$ is not diagonal, than just switch to a basis (in particular, an eigenbasis that I will dedicate the rest of the page or)

an eigenbasis as it is called, is also just usefull in other cases lke when you need to find the next [fibbonacci number](https://www.youtube.com/watch?v=BMPa0FA65Fk), or find the flow in a population of foxes and rabbits (even if you need to see the entire second video) which I will do both of thoes at the end of the page

so the top question is...

### what even is an eigenvector?

an eigenvector is really a set of vectors (that I will refer to from now on as an eigenset) that are all multiples of each other can be defined as the slope of the line that connects the tips of vectors in said eigenset, and an eigenvector is defined as a vector within said eigenset, unfortunately the slope is not the corrasponding eigenvalue, but that this slope can also be $\frac{1}{0}$ if it is pointing straight up, also on the note of eigensets, there can be two (two slopes, not two vectors) with any given matrix, I'll give you an example

but you are probably just waiting for the definition, and here it is:

under multiplication by matrix $A$, most vectors are rotated and scaled, but any eigenvector (or vector within the eigenset) is just scaled, and it makes sense that $2$ times the eigenvector isn't scaled either, thus every vector within the eigenset is an eigenvector, and the eigenvalue? that corrasponds to how mutch each vector is scaled, and two differend eigensets usually have different eigenvalues.

But you are probably just waiting for the example, and here it is:

a matrix with a [determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk0) of $0$, and a [rank](https://www.youtube.com/watch?v=uQhTuRlWMxw) of $1$ has eigensets of the line that it squishes space onto, and the null space of the matrix.

Anyways, on to my favorate part! (And reason I made this page)

### how to find the eigenvetors and eigenvalues

$$ eigenvetor = \vec{v} = \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} $$

$$ eigenvalue = \lambda $$

$$ eigenset = r = \frac{v_y}{v_x} $$

$$ matrix = A $$

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

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = v_x \hat{i} + v_y \hat{j} \neq \vec{0} = \begin{bmatrix} 0 \\
0 \\ \end{bmatrix} = 0 \hat{i} + 0 \hat{j}  $$

$$ A^{\star} \vec{v} = A^{\star} (v_x \hat{i} + v_y \hat{j}) = v_x (A^{\star} \hat{i}) + v_y (A^{\star} \hat{j}) = 0 $$

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

$$ \lambda = -\frac{a + d}{2} \pm \frac{\sqrt{a^2 - 2ad + d^2 + 4bc}}{2} $$

$$ \lambda = \begin{Bmatrix} bd = 0 \to \lambda = a, \lambda = d \\
bd \neq 0 \to \lambda = \frac{\sqrt{a^2 - 2ad + d^2 + 4bc}}{2} -\frac{a + d}{2}, \lambda = -\frac{a + d}{2} - \frac{\sqrt{a^2 - 2ad + d^2 + 4bc}}{2} \\ \end{Bmatrix} $$

$$ -r = \frac{a^{\star}}{b^{\star}} = \frac{c^{\star}}{d^{\star}} $$

$$ r = -\frac{a^{\star}}{b^{\star}} = -\frac{c^{\star}}{d^{\star}} $$
