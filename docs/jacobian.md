## linear algebra

learn more [here](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), and [here](https://silaspe.github.io/maths/complex.html)

$$ \begin{bmatrix}  a \\
  b\end{bmatrix} = a + bi $$

$$ \hat{I} = \begin{bmatrix}  1 \\
  0\end{bmatrix} = 1 $$

$$ \hat{j} = \begin{bmatrix}  0 \\
  1\end{bmatrix} = i $$

$$ \begin{bmatrix}
a \quad b \\
c \quad d \\ \end{bmatrix}
\begin{bmatrix}  e \\
f \end{bmatrix} = \begin{bmatrix}  ae + bf \\
ce + df\end{bmatrix}$$

$$ A = \begin{bmatrix}  ? \quad ? \\
? \quad ?\end{bmatrix} $$

$$ A \hat{I} = \begin{bmatrix}  a \\
c\end{bmatrix} $$

$$ A \hat{j} = \begin{bmatrix}  b \\
d\end{bmatrix} $$

$$ A = \begin{bmatrix}  a \quad b \\
c \quad d\end{bmatrix} $$

$$ a + bi = \begin{bmatrix}  ? \quad ? \\
? \quad ?\end{bmatrix} $$

$$ (a + bi) \hat{I} = (a + bi) 1 = a + bi = \begin{bmatrix}  a \\
b\end{bmatrix} $$

$$ (a + bi) \hat{j} = (a + bi) i = -b + ai = \begin{bmatrix}  -b \\
a\end{bmatrix} $$

$$ a + bi = \begin{bmatrix} a & -b \\
b & a\end{bmatrix} $$

### complex functions

$$ z = x + yi =\begin{bmatrix}  x \\
y\end{bmatrix} $$

$$ f(z) = u + vi = \begin{bmatrix}  u \\
v\end{bmatrix} $$

$$ dz = dx + dyi = \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ df = du + dvi = \begin{bmatrix}  du \\
dv\end{bmatrix} $$

$$ f\prime (z) = \frac{df}{dz} $$

$$ df = f\prime (z) dz $$

$$ \begin{bmatrix}  du \\
dv\end{bmatrix} = f\prime (z) \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ df = f(z + dz) - f(z) $$

$$ \frac{\partial}{\partial x} f(x, t) = : \frac{f(x + dx, t) - f(x, t)}{dx} $$

$$ \partial f(x, t)_x = : f(x + dx, t) - f(x, t) $$

$$ f(z + dx \hat{I}) = f(z) + \begin{bmatrix}  \partial u_x \\
\partial v_x\end{bmatrix} $$

$$ f(z + dy \hat{j}) = f(z) + \begin{bmatrix}  \partial u_y \\
\partial v_y\end{bmatrix} $$

$$ f(z + dx + dyi) = f(z + dz) = f(z) + \begin{bmatrix}  \partial u_x \\
\partial v_x\end{bmatrix} + \begin{bmatrix}  \partial u_y \\
\partial v_y\end{bmatrix} $$

$$ f(z + dz) - f(z) = df = \begin{bmatrix}  \partial u_x \\
\partial v_x\end{bmatrix} + \begin{bmatrix}  \partial u_y \\
\partial v_y\end{bmatrix} = \partial u_x \hat{I} + \partial v_x \hat{j} + \partial u_y \hat{I} + \partial v_y \hat{j} = \frac{\partial u}{\partial x} dx \hat{I} + \frac{\partial v}{\partial x} dx \hat{j} + \frac{\partial u}{\partial y} dy \hat{I} + \frac{\partial v}{\partial y} dy \hat{j} = \begin{bmatrix} \frac{\partial u}{\partial x} dx + \frac{\partial u}{\partial y} dy  \\
\frac{\partial v}{\partial x} dx + \frac{\partial v}{\partial y} dy\end{bmatrix} = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} \quad \frac{\partial v}{\partial y}\end{bmatrix} \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ \begin{bmatrix}  du \\
dv\end{bmatrix} = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} \quad \frac{\partial v}{\partial y}\end{bmatrix} \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ f\prime (z) = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} \quad \frac{\partial v}{\partial y}\end{bmatrix} $$

#### clarification and cauchy-reimann equations

technicaly a term like $\partial u_y$ seems like the change in $u$ when $z$ adds $dy$, but actually it is the change in $u$ when $z$ moves up by $dyi$, but this is just $x + yi + dyi$, so $x + (y + dy)i$ which means that it is a change in $u$ when $y$ increses

in short, $\partial u_y$ is not the change in $u$ when $z$ adds $dy$, but the change of $u$ when you increse $y$

on another note, the equation or jacobian matrix is a matrix, but as you know, evry complex number has a corrasponding matrix but not every matrix has a corrasponding complex number, so to  find out if the jacobian matrix is a complex number or just a matrix, or said another way, if complex function $f(z)$ has a derivitave, we need the cauchy-reimann equations, lets go derive them!

so, if the jacobian matrix is a complex number $a + bi$ which I have been saving for something like this, than the corrasponding matrix is:

$$ \begin{bmatrix} a & -b \\
b & a\end{bmatrix} $$

so that means that

$$ \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} \quad \frac{\partial v}{\partial y}\end{bmatrix} = \begin{bmatrix} a & -b \\
b & a\end{bmatrix} $$

well, what makes a matrix of that form?

for one, the top left equals the bottom right equals the real part

and for another, the top right equals the negatave of the bottom left equals the negatave of the imaginary part

### in conclusion...

$$ f\prime (z) = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} \quad \frac{\partial v}{\partial y}\end{bmatrix} $$

and to test if this is a matrix or a complex number

$$ \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} $$

$$ -\frac{\partial u}{\partial y} = \frac{\partial v}{\partial x} $$

### examples

$$ f(z) = z^2 $$

$$ f(x +yi) = (x^2 - y^2) + (2xy)i $$

$$ u = x^2 - y^2 $$

$$ v = 2xy $$

$$ \frac{\partial u}{\partial x} = \frac{\partial}{\partial x} (x^2 - y^2) = 2x $$

$$ \frac{\partial u}{\partial y} = \frac{\partial}{\partial y} (x^2 - y^2) = -2y $$

$$ \frac{\partial v}{\partial x} = \frac{\partial}{\partial x} (2xy) = 2y $$

$$ \frac{\partial v}{\partial y} = \frac{\partial}{\partial y} (2xy) = 2x $$

$$ 2x = 2x $$

$$ 2y = 2y $$

$$ f\prime (z) = 2x + 2yi = 2z $$

another one!

$$ f(z) = \text{ccong} (z) $$

$$ f(x + yi) = x - yi $$

$$ \frac{\partial u}{\partial x} = \frac{\partial}{\partial x} x = 1 $$

$$ \frac{\partial u}{\partial y} = \frac{\partial}{\partial y} x = 0 $$

$$ \frac{\partial v}{\partial x} = \frac{\partial}{\partial x} (-y) = 0 $$

$$ \frac{\partial v}{\partial y} = \frac{\partial}{\partial y} (-y) = -1 $$

$$ 1 \ne -1 $$

$$ 0 = 0 $$

$$ f\prime (z) = \begin{bmatrix}  1 & 0 \\
0 & -1 \end{bmatrix} $$

in conclution, $z^2$ has a derivitave, and $\text{ccong} (z)$ does not.
