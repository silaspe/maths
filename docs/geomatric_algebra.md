### why can't you/you can't multiply two vectors

$$ \vec{u} = \begin{bmatrix} u_x \\
u_y \\
u_z \\ \end{bmatrix} = u_x \hat{i} + u_y \hat{j} + u_z \hat{k} $$

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\
v_z \\ \end{bmatrix} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k} $$

$$ \vec{u} \vec{v} = (u_x \hat{i} + u_y \hat{j} + u_z \hat{k}) (v_x \hat{i} + v_y \hat{j} + v_z \hat{k}) = u_x \hat{i} v_x \hat{i} + u_x \hat{i} v_y \hat{j} + u_x \hat{i} v_z \hat{k} + u_y \hat{j} v_x \hat{i} + u_y \hat{j} v_y \hat{j} + u_y \hat{j} v_z \hat{k} + u_z \hat{k} v_x \hat{i} + u_z \hat{k} v_y \hat{j} + u_z \hat{k} v_z \hat{k} $$

$$ \text{For lack of a better way to display this, } \vec{u} \vec{v} \text{ equals the sum of the things below:} $$

$$ (\hat{i} \hat{i})(u_x v_x) + (\hat{i} \hat{j})(u_x v_y) + (\hat{i} \hat{k})(u_x v_z) $$

$$ (\hat{j} \hat{i})(u_y v_x) + (\hat{j} \hat{j})(u_y v_y) + (\hat{j} \hat{k})(u_y v_z) $$

$$ (\hat{k} \hat{i})(u_z v_x) + (\hat{k} \hat{j})(u_z v_y) + (\hat{k} \hat{k})(u_z v_z) $$

### geometric algebra

[A Swift Introduction to Geometric Algebra](https://www.youtube.com/watch?v=60z_hpEAtD8) exists (literally, that was the name), and it is where these ideas come from (at least in this chapter and the complex numbers chapter coming soon). The prodct of a basis vector $e_1$ and it self is $1$, and the product of two basis vectors $e_1$ and $e_2$ equals $-e_2 e_1$. This means that you can do this at any point in the product of basis vectors (this should make sense). By the way, $U = \hat{i} \hat{j} \hat{k}$

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

$$ \text{But now, I need to turn a bivector into a vector. What about that } U \text{ thing?} $$

Puzzle time! Prove that $U \vec{v} = \vec{v} U$.

$$ U^2 = xyzxyz = -xyzxzy = xyzzxy = xyxy = -xxyy $$

$$ U^2 = -1 $$

$U$ is usually called $i$ for this reason.

$$ U^3 = xyzxyzxyz = -xyxzyzxyz = xxyzyzxyz = yzyzxyz = -yyzzxyz = -xyz = -U = xzy = -zxy = zyx $$

$$ U^4 = U^2 U^2 = (-1) (-1) = 1 $$

$$ U^4 = U^3 U = (-U) U = -U^2 = -(-1) = 1 $$

.

$$ U^1 = U = xyz $$

$$ U^2 = 1 $$

$$ U^3 = -U = zyx = -xyz $$

$$ U^4 = (-U) U  = 1 $$

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

Also, the cross product only works in $3d$ while this $U \text{ } \vec{u} \times \vec{v}$ thing works in any dimention. This operator actually has a name (well, two names), the outer product (as oppose to the dot product sometimes refered to as the inner product) or wedge product for it's apperance as a wedge unicode character. This more genaral cross product is written $\vec{u} ∧ \vec{v}$. Also, I have to interrupt this for...


$100$ lines! But

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \vec{u} ∧ \vec{v} $$

### $\frac{1}{\vec{v}}$ (and $\vec{v}^2$)

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
(e_d x) u_d v_1 & (e_d y) u_d v_2 & (e_d z) u_d v_3 & (e_d w) u_d v_4 & \dots &  \\ \end{bmatrix} = (u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d) + \begin{bmatrix}  & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
-(xy) u_2 v_1 &  & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
-(xz) u_3 v_1 & -(yz) u_3 v_2 &  & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
-(xw) u_4 v_1 & -(yw) u_4 v_2 & -(zw) u_4 v_3 &  & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) u_d v_1 & -(y e_d) u_d v_2 & -(z e_d) u_d v_3 & -(w e_d) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \text{It was really frustrating to write a plus in between, so I just gave up. Just assume that the results above and below are summed together (I kept swiching between "Just assume that the result above is summed together" and "Just assume that the results above and below are summed together") (you can assume that every matrix on this page is a sum).} $$

$$ \text{Here's an idea! Square the vector.} $$

$$ \vec{v} \vec{v} = (v_1 v_1 + v_2 v_2 + v_3 v_3 + v_4 v_4 + \dots + v_d v_d) + \begin{bmatrix}  & (xy) v_1 v_2 & (xz) v_1 v_3 & (xw) v_1 v_4 & \dots & (x e_d) v_1 v_d  \\
-(xy) v_2 v_1 &  & (yz) v_2 v_3 & (yw) v_2 v_4 & \dots & (y e_d) v_2 v_d \\
-(xz) v_3 v_1 & -(yz) v_3 v_2 &  & (zw) v_3 v_4 & \dots & (z e_d) v_3 v_d \\
-(xw) v_4 v_1 & -(yw) v_4 v_2 & -(zw) v_4 v_3 &  & \dots & (w e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) v_d v_1 & -(y e_d) v_d v_2 & -(z e_d) v_d v_3 & -(w e_d) v_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \text{By the way, here's the dot product and absolute value of two and one vector respectively.} $$

$$ \vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d = \sum\limits_{n = 1}^{d} u_n v_n $$

$$ || \vec{v} || = \sqrt{v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2} $$

$$ || \vec{v} ||^2 = || v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 || $$

$$ \text{But the square of a number is always positave (this is VGA (vannila geomatric algebra), not CGA (
complex geomatric algebra)), and the sum of positave numbers is positave, and the absolute value of a positave number is positave, so...} $$

$$ || \vec{v} ||^2 = v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 $$

$$ \vec{v} \cdot \vec{v} = v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 $$

$$ || \vec{v} ||^2 = \vec{v} \cdot \vec{v} $$

$$ \text{But then I realized, this if halfway to the square of a vector.} $$

$$ \vec{v}^2 = \vec{v} \cdot \vec{v} + \vec{v} ∧ \vec{v} = || \vec{v} ||^2 + \vec{v} ∧ \vec{v} $$

$$ \text{If the cross product of a vector with itself is the zero vector, and the } 3d \text{ wedge product is proportional to the cross product, than it would make sense that the wedge product of a vector with itself is zero as well (this argument works in } 3d \text{ by the way). You might have noticed earlier that we almost proved this.} $$

$$ \vec{v}^2 = || \vec{v} ||^2 + \begin{bmatrix}  & (xy) v_1 v_2 & (xz) v_1 v_3 & (xw) v_1 v_4 & \dots & (x e_d) v_1 v_d  \\
-(xy) v_2 v_1 &  & (yz) v_2 v_3 & (yw) v_2 v_4 & \dots & (y e_d) v_2 v_d \\
-(xz) v_3 v_1 & -(yz) v_3 v_2 &  & (zw) v_3 v_4 & \dots & (z e_d) v_3 v_d \\
-(xw) v_4 v_1 & -(yw) v_4 v_2 & -(zw) v_4 v_3 &  & \dots & (w e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) v_d v_1 & -(y e_d) v_d v_2 & -(z e_d) v_d v_3 & -(w e_d) v_d v_4 & \dots &  \\ \end{bmatrix} = || \vec{v} ||^2 + \begin{bmatrix}  & (xy) v_1 v_2 & (xz) v_1 v_3 & (xw) v_1 v_4 & \dots & (x e_d) v_1 v_d  \\
-(xy)v_1 v_2  &  & (yz) v_2 v_3 & (yw) v_2 v_4 & \dots & (y e_d) v_2 v_d \\
-(xz) v_1 v_3 & -(yz) v_2 v_3 &  & (zw) v_3 v_4 & \dots & (z e_d) v_3 v_d \\
-(xw) v_1 v_4 & -(yw) v_2 v_4 & -(zw) v_3 v_4 &  & \dots & (w e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) v_1 v_d & -(y e_d) v_2 v_d & -(z e_d) v_3 v_d & -(w e_d) v_4 v_d & \dots &  \\ \end{bmatrix} $$

$$ \text{As you can see, each term is perfectly canceled out by the term across the diagonal. And perfect timing, it will be on } 200 \text{ lines.} $$

$$ \vec{v}^2 = || \vec{v} ||^2 $$

$$ \text{Also, now I can solve for } \frac{1}{\vec{v}} $$

$$ \vec{v} \vec{v} = || \vec{v} ||^2 $$

$$ \vec{v} = \frac{|| \vec{v} ||^2}{\vec{v}} $$

$$ \frac{1}{\vec{v}} = \frac{\vec{v}}{|| \vec{v} ||^2} $$

$$ \text{I had this proof that } \frac{1}{\frac{1}{\vec{v}}} = \vec{v} \text{ that I would put right here, but I accedentally deleted that one (and it is now an exersize for the veiwer). In conclution:} $$

$$ \vec{v}^2 = || \vec{v} ||^2 $$

$$ \text{And} $$

$$ \frac{1}{\vec{v}} = \frac{\vec{v}}{|| \vec{v} ||^2}. $$

$$ \text{By the way, this means that the inverse of a vector is a vector, } \frac{\vec{u}}{\vec{v}} = \frac{\vec{u} \vec{v}}{|| \vec{v} ||^2} \text{. The inverse of a } 2d \text{ is it's circle inverse, the inverse of a } 3d \text{ vector is it's sphere inverse, the inverse of a } 4d \text{ vector is it's hypersphere inverse, and so on.} $$

#### fun fact!

As you know, $\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d$. But what about $\vec{v} \cdot \vec{u}$? And what about the wedge product? (By the way, this is about the vector product or sometimes called the geometric product)

$$ \vec{v} \cdot \vec{u} = v_1 u_1 + v_2 u_2 + v_3 u_3 + v_4 u_4 + \dots + v_d u_d = u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d $$

$$ \vec{v} \cdot \vec{u} = \vec{u} \cdot \vec{v} $$

$$ \vec{v} \vec{u} = \vec{u} \cdot \vec{v} + \vec{v} ∧ \vec{u} $$

$$ \vec{u} ∧ \vec{v} = \begin{bmatrix}  & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
-(xy) u_2 v_1 &  & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
-(xz) u_3 v_1 & -(yz) u_3 v_2 &  & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
-(xw) u_4 v_1 & -(yw) u_4 v_2 & -(zw) u_4 v_3 &  & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) u_d v_1 & -(y e_d) u_d v_2 & -(z e_d) u_d v_3 & -(w e_d) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \vec{v} ∧ \vec{u} = \begin{bmatrix}  & (xy) v_1 u_2 & (xz) v_1 u_3 & (xw) v_1 u_4 & \dots & (x e_d) v_1 u_d  \\
-(xy) v_2 u_1 &  & (yz) v_2 u_3 & (yw) v_2 u_4 & \dots & (y e_d) v_2 u_d \\
-(xz) v_3 u_1 & -(yz) v_3 u_2 &  & (zw) v_3 u_4 & \dots & (z e_d) v_3 u_d \\
-(xw) v_4 u_1 & -(yw) v_4 u_2 & -(zw) v_4 u_3 &  & \dots & (w e_d) v_4 u_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) v_d u_1 & -(y e_d) v_d u_2 & -(z e_d) v_d u_3 & -(w e_d) v_d u_4 & \dots &  \\ \end{bmatrix} = -\begin{bmatrix}  & -(xy) v_1 u_2 & -(xz) v_1 u_3 & -(xw) v_1 u_4 & \dots & -(x e_d) v_1 u_d  \\
(xy) v_2 u_1 &  & -(yz) v_2 u_3 & -(yw) v_2 u_4 & \dots & -(y e_d) v_2 u_d \\
(xz) v_3 u_1 & (yz) v_3 u_2 &  & -(zw) v_3 u_4 & \dots & -(z e_d) v_3 u_d \\
(xw) v_4 u_1 & (yw) v_4 u_2 & (zw) v_4 u_3 &  & \dots & -(w e_d) v_4 u_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
(x e_d) v_d u_1 & (y e_d) v_d u_2 & (z e_d) v_d u_3 & (w e_d) v_d u_4 & \dots &  \\ \end{bmatrix} = -\begin{bmatrix}  & (xy) u_1 v_2 & (xz) u_1 v_3 & (xw) u_1 v_4 & \dots & (x e_d) u_1 v_d  \\
-(xy) u_2 v_1 &  & (yz) u_2 v_3 & (yw) u_2 v_4 & \dots & (y e_d) u_2 v_d \\
-(xz) u_3 v_1 & -(yz) u_3 v_2 &  & (zw) u_3 v_4 & \dots & (z e_d) u_3 v_d \\
-(xw) u_4 v_1 & -(yw) u_4 v_2 & -(zw) u_4 v_3 &  & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(x e_d) u_d v_1 & -(y e_d) u_d v_2 & -(z e_d) u_d v_3 & -(w e_d) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \vec{v} ∧ \vec{u} = - \vec{u} ∧ \vec{v} $$

By the way, $2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ lines.

$$ \vec{v} \vec{u} = \vec{u} \cdot \vec{v} - \vec{u} ∧ \vec{v} $$

### complex numbers

$$ \text{complex numbers (surprisingly in geomatric algebra) come from } 2d \text{ geomatric algebra. So time to re-derive that! (And use } i \text{ this time instead of } U \text{.) Here's the definitions and link to the complex numbers page:} $$

[.](https://silaspe.github.io/maths/complex.html)

$$ x = \hat{i} \text{ (This is so that } \hat{i} \text{ isn't confused with } i \text{).} $$

$$ y = \hat{j} $$

$$ i = \hat{i} \hat{j} $$

$$ x^2 = 1 $$

$$ y^2 = 1 $$

$$ xy = -yx \text{(} = i \text{)} $$

$$ \text{And with those, you can derive} $$

$$ i^2 = -1 $$

$$ \text{this is why it was called } i. $$

.

$$ \text{Also, a bivector in } 2 \text{ dimensions has one degree of freedom (just like how a vector behaves in } 1d \text{) (by the way, a } k \text{-vector in } n \text{ dimensions has } \begin{pmatrix} n \\
k \\ \end{pmatrix} \text{ DoF's (degrees of freedom)), so I'll call it, I dunno, a pseudoscalar. (} i \text{ Is always the unit pseudoscalar no matter the dimension.)} $$

$$ \vec{u} = \begin{bmatrix} u_x \\
u_y \\ \end{bmatrix} = u_x \hat{i} + u_y \hat{j} = u_x x + u_y y $$

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = v_x \hat{i} + v_y \hat{j} = v_x x + v_y y $$

$$ \vec{u} \vec{v} = (xx) u_x v_x + (xy) u_x v_y + (yx) u_y v_x + (yy) u_y v_y = (u_x v_x + u_y v_y) + (u_x v_y - u_y v_x)i $$

$$ \vec{u} ∧ \vec{v} = i \cdot Det \begin{bmatrix} u_x & u_y \\
v_x & v_y \\ \end{bmatrix} $$

$300$ Lines!

Here's a [determinat video](https://www.youtube.com/watch?v=Ip3X9LOh2dk) and [linear algebra playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) for context (make sure to skip the cross product video) (also, that determinant is probably the only matrix on this page. I'll come back here when I finish the page and put the awnser here: ) ( $\text{ }$ : ) $\text{ }$ Btw.)

$$  \text{Text over time! (As oppose to voice over, it's a font swich.) What's something that veiwers of this website would want from geomatric algebra? I think I have an idea: rotate a vector by the angle between two other vectors. I'l do it in } 20 \text{ minutes.} $$

$$ \text{It's the next day.} $$

$$ \vec{v} i = v_x xi + v_y yi = v_x xxy + v_y yxy = v_x y - v_y xyy = v_x y - v_y x $$

```py
def complexify(v_x x + v_y y):
  return v_x + v_y i
```

$$ \text{I just realized that this isn't a code repo(sitory). It was my instinct to write it in code form.} $$

$$ \text{complexify} (v_x x + v_y y) = v_x + v_y i $$

$$ \vec{v} i = (v_x x + v_y y)i = v_x xi + v_y yi = v_x xxy + v_y yxy = v_x y - v_y xyy = v_x y - v_y x $$

$$ \text{complexify} (\vec{v} i) = i \text{ complexify} (\vec{v}) $$

$$ i \vec{v} = i(v_x x + v_y y) = i v_x x + i v_y y $$

$$ \text{But } v_x \text{ and } v_y \text{ are scalars, so} $$

$$ i \vec{v} = v_x ix + v_y iy = v_x xyx + v_y xyy = -v_x yxx + v_y x = -v_x y + v_y x $$

$$ \text{complexify} (i \vec{v}) = -i \text{ complexify} (\vec{v}). $$

$$ \text{Next: Vector times a complex number.} $$

$$ \text{vectorize} (a + bi) = ax + by $$

$$ \text{complexify} (\text{vectorize} (z)) = z $$

$$ \text{vectorize} (\text{complexify} (\vec{v})) = \vec{v} $$

$$ (ax + by)(c + di) = axc + axdi + byc + bydi = \begin{pmatrix} ac (x) & ad (xi) \\
bc (y) & bd (yi) \\ \end{pmatrix} = \begin{pmatrix} ac (x) & ad (xxy) \\
bc (y) & bd (yxy) \\ \end{pmatrix} = \begin{pmatrix} ac (x) & ad (y) \\
bc (y) & -bd (xyy) \\ \end{pmatrix} = \begin{pmatrix} ac (x) & ad (y) \\
bc (y) & -bd (x) \\ \end{pmatrix} = (ac - bd)x + (ad + bc) y $$

$$ z = a + bi $$

$$ w = c + di $$

$$ \text{vectorize} (z) w = \text{vectorize} (zw) $$

$$ \vec{u} \text{ complexify} (\vec{v}) = \text{vectorize} (\text{complexify} (\vec{u}) \text{ complexify} (v) $$
