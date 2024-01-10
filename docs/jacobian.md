## linear algebra

$$\begin{bmatrix}  a \\
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
\frac{\partial v}{\partial x} dx + \frac{\partial v}{\partial y} dy\end{bmatrix} = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial v}{\partial x} \\
\frac{\partial u}{\partial y} \quad \frac{\partial v}{\partial y}\end{bmatrix} \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ \begin{bmatrix}  du \\
dv\end{bmatrix} = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial v}{\partial x} \\
\frac{\partial u}{\partial y} \quad \frac{\partial v}{\partial y}\end{bmatrix} \begin{bmatrix}  dx \\
dy\end{bmatrix} $$

$$ f\prime (z) = \begin{bmatrix}  \frac{\partial u}{\partial x} \quad \frac{\partial v}{\partial x} \\
\frac{\partial u}{\partial y} \quad \frac{\partial v}{\partial y}\end{bmatrix} $$

#### clarification and cauchy-reimann equations

technicaly a term like $\partial u_y$ seems like the change in $u$ when $z$ adds $dy$, but actually it is the change in $u$ when $z$ moves up by $dyi$, but this is just $x + yi + dyi$, so $x + (y + dy)i$ which means that it is a change in $u$ when $y$ increses

in short, $\partial u_y$ is not the change in $u$ when $z$ adds $dy$, but the change of $u$ when you increse $y$

on another note, the equation or jacobian matrix is a matrix, but as you know, evry complex number has a corrasponding matrix but not every matrix has a corrasponding complex number, so to  find out if the jacobian matrix is a complex number or just a matrix, or said another way, if complex function $f(z)$ has a derivitave, we need the cauchy-reimann equations, lets go derive them!
