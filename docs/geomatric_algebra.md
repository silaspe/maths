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

WARNING! This page requires knowing [linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), mostly just vectors, and the first part of [A Swift Introduction to Geometric Algebra](https://www.youtube.com/watch?v=60z_hpEAtD8&t=179s) (literally, that was the name) to know what a $k$-vector is. (Also, it's where these ideas come from (at least in this chapter and the [complex numbers chapter](https://silaspe.github.io/maths/geomatric_algebra.html#complex-numbers) coming soon... And the Maxwell's equation chapter at the end).) Here is the definition for the product of basis vectors: The prodct of a basis vector $e_i$ and it self is $1$, and the product of two basis vectors $e_i$ and $e_j$ equals $-e_j e_i (i \ne j)$. This means that you can do this at any point in the product of basis vectors (this should make sense). By the way, $U = \hat{i} \hat{j} \hat{k}$

$$ \hat{i} = \hat{x} $$

$$ \hat{j} = \hat{y} $$

$$ \hat{k} = \hat{z} $$

$$ \text{Now is about as good of a time as any to simplify the product.} $$

$$ \vec{u} \vec{v} = \begin{pmatrix} (\hat{x} \hat{x})(u_x v_x) + (\hat{x} \hat{y})(u_x v_y) + (\hat{x} \hat{z})(u_x v_z) +  \\
(\hat{y} \hat{x})(u_y v_x) + (\hat{y} \hat{y})(u_y v_y) + (\hat{y} \hat{z})(u_y v_z) + \\
(\hat{z} \hat{x})(u_z v_x) + (\hat{z} \hat{y})(u_z v_y) + (\hat{z} \hat{z})(u_z v_z) \\ \end{pmatrix} = \begin{pmatrix} (\hat{x} \hat{x})(u_x v_x) + (\hat{x} \hat{y})(u_x v_y) - (\hat{z} \hat{x})(u_x v_z) -  \\
(\hat{x} \hat{y})(u_y v_x) + (\hat{y} \hat{y})(u_y v_y) + (\hat{y} \hat{z})(u_y v_z) + \\
(\hat{z} \hat{x})(u_z v_x) - (\hat{y} \hat{z})(u_z v_y) + (\hat{z} \hat{z})(u_z v_z) \\ \end{pmatrix} = \begin{pmatrix} u_x v_x + (\hat{x} \hat{y})(u_x v_y) - (\hat{z} \hat{x})(u_x v_z) -  \\
(\hat{x} \hat{y})(u_y v_x) + u_y v_y + (\hat{y} \hat{z})(u_y v_z) + \\
(\hat{z} \hat{x})(u_z v_x) - (\hat{y} \hat{z})(u_z v_y) + u_z v_z \\ \end{pmatrix} = u_x v_x +  u_y v_y + u_z v_z + \begin{pmatrix} (\hat{x} \hat{y})(u_x v_y - u_y v_x) +  \\
(\hat{y} \hat{z})(u_y v_z - u_z v_y) + \\
(\hat{z} \hat{x})(u_z v_x - u_x v_z) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + \begin{pmatrix} (\hat{x} \hat{y})(u_x v_y - u_y v_x) +  \\
(\hat{y} \hat{z})(u_y v_z - u_z v_y) + \\
(\hat{z} \hat{x})(u_z v_x - u_x v_z) \\ \end{pmatrix} $$

$$ \text{But now, I need to turn a bivector into a vector. What about that } U \text{ thing?} $$

Puzzle time! Prove that $U \vec{v} = \vec{v} U$.

$$ U^2 = \hat{x} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = -\hat{x} \hat{y} \hat{z} \hat{x} \hat{z} \hat{y} = \hat{x} \hat{y} \hat{z} \hat{z} \hat{x} \hat{y} = \hat{x} \hat{y} \hat{x} \hat{y} = -\hat{x} \hat{x} \hat{y} \hat{y} $$

$$ U^2 = -1 $$

$U$ is usually called $i$ for this reason.

$$ U^3 = \hat{x} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = -\hat{x} \hat{y} \hat{x} \hat{z} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = \hat{x} \hat{x} \hat{y} \hat{z} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = \hat{y} \hat{z} \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = -\hat{y} \hat{y} \hat{z} \hat{z} \hat{x} \hat{y} \hat{z} = -\hat{x} \hat{y} \hat{z} = -U = \hat{x} \hat{z} \hat{y} = -\hat{z} \hat{x} \hat{y} = \hat{z} \hat{y} \hat{x} $$

$$ U^4 = U^2 U^2 = (-1) (-1) = 1 $$

$$ U^4 = U^3 U = (-U) U = -U^2 = -(-1) = 1 $$

.

$$ U^1 = U = \hat{x} \hat{y} \hat{z} $$

$$ U^2 = 1 $$

$$ U^3 = -U = \hat{z} \hat{y} \hat{x} = -\hat{x} \hat{y} \hat{z} $$

$$ U^4 = (-U) U  = 1 $$

.

$$ \hat{x} \hat{y} = \hat{x} \hat{y} \hat{z} \hat{z} = U \hat{z} $$

$$ \hat{y} \hat{z} = \hat{y} \hat{z} \hat{x} \hat{x} = -\hat{y} \hat{x} \hat{z} \hat{x} = \hat{x} \hat{y} \hat{z} \hat{x} = U \hat{x} $$

$$ \hat{z} \hat{x} = \hat{z} \hat{x} \hat{y} \hat{y} = -\hat{z} \hat{y} \hat{x} \hat{y} = -(-U) \hat{y} = U \hat{y} $$

$$ \text{Yes! Now I can finaly solve the puzzle.} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \begin{pmatrix} (U \hat{z})(u_x v_y - u_y v_x) +  \\
(U \hat{x})(u_y v_z - u_z v_y) + \\
(U \hat{y})(u_z v_x - u_x v_z) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + U \begin{pmatrix} \hat{x} (u_y v_z - u_z v_y) +  \\
\hat{y} (u_z v_x - u_x v_z) + \\
\hat{z} (u_x v_y - u_y v_x) \\ \end{pmatrix} = \vec{u} \cdot \vec{v} + U \begin{bmatrix} u_y v_z - u_z v_y \\
u_z v_x - u_x v_z \\
u_x v_y - u_y v_x \\ \end{bmatrix} $$

.

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + U \text{ } \vec{u} \times \vec{v} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \hat{x} \hat{y} \hat{z} \text{ } \vec{u} \times \vec{v} $$

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \vec{u} \times \vec{v} \text{ } i $$

Also, the cross product only works in $3d$ while this $U \text{ } \vec{u} \times \vec{v}$ thing works in any dimention. This operator actually has a name (well, two names), the outer product (as oppose to the dot product sometimes refered to as the inner product) or wedge product for it's apperance as a wedge unicode character. This more genaral cross product is written $\vec{u} ∧ \vec{v}$. Also, I have to interrupt this for...


$100$ lines! But

$$ \vec{u} \vec{v} = \vec{u} \cdot \vec{v} + \vec{u} ∧ \vec{v}. $$

### $\frac{1}{\vec{v}}$ (and $\vec{v}^2$)

$$ \text{Lets say that we are in dimension } d \text{. First, basis vectors} $$

$$ e_1 = \hat{i} = \hat{x} $$

$$ e_2 = \hat{j} = \hat{y} $$

$$ e_3 = \hat{k} = \hat{z} $$

$$ e_4 = \hat{l} = \hat{w} $$

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

$$ \vec{u} \vec{v} = \begin{bmatrix} (\hat{x} \hat{x}) u_1 v_1 & (\hat{x} \hat{y}) u_1 v_2 & (\hat{x} \hat{z}) u_1 v_3 & (\hat{x} \hat{w}) u_1 v_4 & \dots & (\hat{x} e_d) u_1 v_d  \\
(\hat{y} \hat{x}) u_2 v_1 & (\hat{y} \hat{y}) u_2 v_2 & (\hat{y} \hat{z}) u_2 v_3 & (\hat{y} \hat{w}) u_2 v_4 & \dots & (\hat{y} e_d) u_2 v_d \\
(\hat{z} \hat{x}) u_3 v_1 & (\hat{z} \hat{y}) u_3 v_2 & (\hat{z} \hat{z}) u_3 v_3 & (\hat{z} \hat{w}) u_3 v_4 & \dots & (\hat{z} e_d) u_3 v_d \\
(\hat{w} \hat{x}) u_4 v_1 & (\hat{w} \hat{y}) u_4 v_2 & (\hat{w} \hat{z}) u_4 v_3 & (\hat{w} \hat{w}) u_4 v_4 & \dots & (\hat{w} e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(e_d \hat{x}) u_d v_1 & (e_d \hat{y}) u_d v_2 & (e_d \hat{z}) u_d v_3 & (e_d \hat{w}) u_d v_4 & \dots & (e_d e_d) u_d v_d \\ \end{bmatrix} = \begin{bmatrix} u_1 v_1 & (\hat{x} \hat{y}) u_1 v_2 & (\hat{x} \hat{z}) u_1 v_3 & (\hat{x} \hat{w}) u_1 v_4 & \dots & (\hat{x} e_d) u_1 v_d  \\
(\hat{y} \hat{x}) u_2 v_1 & u_2 v_2 & (\hat{y} \hat{z}) u_2 v_3 & (\hat{y} \hat{w}) u_2 v_4 & \dots & (\hat{y} e_d) u_2 v_d \\
(\hat{z} \hat{x}) u_3 v_1 & (\hat{z} \hat{y}) u_3 v_2 & u_3 v_3 & (\hat{z} \hat{w}) u_3 v_4 & \dots & (\hat{z} e_d) u_3 v_d \\
(\hat{w} \hat{x}) u_4 v_1 & (\hat{w} \hat{y}) u_4 v_2 & (\hat{w} \hat{z}) u_4 v_3 & u_4 v_4 & \dots & (\hat{w} e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(e_d \hat{x}) u_d v_1 & (e_d \hat{y}) u_d v_2 & (e_d \hat{z}) u_d v_3 & (e_d \hat{w}) u_d v_4 & \dots & u_d v_d \\ \end{bmatrix} $$

$$ \vec{u} \vec{v} = (u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d) + \begin{bmatrix}  & (\hat{x} \hat{y}) u_1 v_2 & (\hat{x} \hat{z}) u_1 v_3 & (\hat{x} \hat{w}) u_1 v_4 & \dots & (\hat{x} e_d) u_1 v_d  \\
-(\hat{x} \hat{y}) u_2 v_1 &  & (\hat{y} \hat{z}) u_2 v_3 & (\hat{y} \hat{w}) u_2 v_4 & \dots & (\hat{y} e_d) u_2 v_d \\
-(\hat{x} \hat{z}) u_3 v_1 & -(\hat{y} \hat{z}) u_3 v_2 &  & (\hat{z} \hat{w}) u_3 v_4 & \dots & (\hat{z} e_d) u_3 v_d \\
-(\hat{x} \hat{w}) u_4 v_1 & -(\hat{y} \hat{w}) u_4 v_2 & -(\hat{z} \hat{w}) u_4 v_3 &  & \dots & (\hat{w} e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) u_d v_1 & -(\hat{y} e_d) u_d v_2 & -(\hat{z} e_d) u_d v_3 & -(\hat{w} e_d) u_d v_4 & \dots & \\ \end{bmatrix} $$

$$ \text{It was really frustrating to write a plus in between, so I just gave up. Just assume that the results above and below are summed together (I kept swiching between "Just assume that the result above is summed together" and "Just assume that the results above and below are summed together") (you can assume that every matrix on this page is a sum). Here's an idea! Square the vector.} $$

$$ \vec{v} \vec{v} = (v_1 v_1 + v_2 v_2 + v_3 v_3 + v_4 v_4 + \dots + v_d v_d) + \begin{bmatrix}  & (\hat{x} \hat{y}) v_1 v_2 & (\hat{x} \hat{z}) v_1 v_3 & (\hat{x} \hat{w}) v_1 v_4 & \dots & (\hat{x} e_d) v_1 v_d  \\
-(\hat{x} \hat{y}) v_2 v_1 &  & (\hat{y} \hat{z}) v_2 v_3 & (\hat{y} \hat{w}) v_2 v_4 & \dots & (\hat{y} e_d) v_2 v_d \\
-(\hat{x} \hat{z}) v_3 v_1 & -(\hat{y} \hat{z}) v_3 v_2 &  & (\hat{z} \hat{w}) v_3 v_4 & \dots & (\hat{z} e_d) v_3 v_d \\
-(\hat{x} \hat{w}) v_4 v_1 & -(\hat{y} \hat{w}) v_4 v_2 & -(\hat{z} \hat{w}) v_4 v_3 &  & \dots & (\hat{w} e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) v_d v_1 & -(\hat{y} e_d) v_d v_2 & -(\hat{z} e_d) v_d v_3 & -(\hat{w} e_d) v_d v_4 & \dots &  \\ \end{bmatrix} $$


(incert filler text here)

$$ \text{By the way, } \hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{\hat{w}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}. $$

$$ \text{Also by the way, here's the formulas for the dot product and absolute value of two and one vector respectively.} $$

$$ \vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 + u_4 v_4 + \dots + u_d v_d = \sum\limits_{n = 1}^{d} u_n v_n $$

$$ || \vec{v} || = \sqrt{v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2} $$

$$ || \vec{v} ||^2 = || v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 || $$

$$ \text{But the square of a number is always positave (this is VGA (vannila geomatric algebra), not CGA (
complex geomatric algebra (the term CGA actually means conformal geomatric algebra)) also, the square of the square root of itself, and } i^2 \text{ is still } -1 \text{, I think that I was confusing the square of the square root with the square root of the square), and the sum of positave numbers is positave, and the absolute value of a positave number is positave, so...} $$

$$ || \vec{v} ||^2 = v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 $$

$$ \vec{v} \cdot \vec{v} = v_1^2 + v_2^2 + v_3^2 + v_4^2 + \dots + v_d^2 $$

$$ || \vec{v} ||^2 = \vec{v} \cdot \vec{v} $$

$$ \text{But then I realized, this if halfway to the square of a vector.} $$

$$ \vec{v}^2 = \vec{v} \cdot \vec{v} + \vec{v} ∧ \vec{v} = || \vec{v} ||^2 + \vec{v} ∧ \vec{v} $$

$$ \text{If the cross product of a vector with itself is the zero vector, and the } 3d \text{ wedge product is proportional to the cross product, than it would make sense that the wedge product of a vector with itself is zero as well (this argument works in } 3d \text{ by the way). You might have noticed earlier that we almost proved this.} $$

$$ \vec{v}^2 = || \vec{v} ||^2 + \begin{bmatrix}  & (\hat{x} \hat{y}) v_1 v_2 & (\hat{x} \hat{z}) v_1 v_3 & (\hat{x} \hat{w}) v_1 v_4 & \dots & (\hat{x} e_d) v_1 v_d  \\
-(\hat{x} \hat{y}) v_2 v_1 &  & (\hat{y} \hat{z}) v_2 v_3 & (\hat{y} \hat{w}) v_2 v_4 & \dots & (\hat{y} e_d) v_2 v_d \\
-(\hat{x} \hat{z}) v_3 v_1 & -(\hat{y} \hat{z}) v_3 v_2 &  & (\hat{z} \hat{w}) v_3 v_4 & \dots & (\hat{z} e_d) v_3 v_d \\
-(\hat{x} \hat{w}) v_4 v_1 & -(\hat{y} \hat{w}) v_4 v_2 & -(\hat{z} \hat{w}) v_4 v_3 &  & \dots & (\hat{w} e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) v_d v_1 & -(\hat{y} e_d) v_d v_2 & -(\hat{z} e_d) v_d v_3 & -(\hat{w} e_d) v_d v_4 & \dots &  \\ \end{bmatrix} = || \vec{v} ||^2 + \begin{bmatrix}  & (\hat{x} \hat{y}) v_1 v_2 & (\hat{x} \hat{z}) v_1 v_3 & (\hat{x} \hat{w}) v_1 v_4 & \dots & (\hat{x} e_d) v_1 v_d  \\
-(\hat{x} \hat{y}) v_1 v_2 &  & (\hat{y} \hat{z}) v_2 v_3 & (\hat{y} \hat{w}) v_2 v_4 & \dots & (\hat{y} e_d) v_2 v_d \\
-(\hat{x} \hat{z}) v_1 v_3 & -(\hat{y} \hat{z}) v_2 v_3 &  & (\hat{z} \hat{w}) v_3 v_4 & \dots & (\hat{z} e_d) v_3 v_d \\
-(\hat{x} \hat{w}) v_1 v_4 & -(\hat{y} \hat{w}) v_2 v_4 & -(\hat{z} \hat{w}) v_3 v_4 &  & \dots & (\hat{w} e_d) v_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) v_1 v_d & -(\hat{y} e_d) v_2 v_d & -(\hat{z} e_d) v_3 v_d & -(\hat{w} e_d) v_4 v_d & \dots &  \\ \end{bmatrix} $$

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

$$ \vec{u} ∧ \vec{v} = \begin{bmatrix}  & (\hat{x} \hat{y}) u_1 v_2 & (\hat{x} \hat{z}) u_1 v_3 & (\hat{x} \hat{w}) u_1 v_4 & \dots & (\hat{x} e_d) u_1 v_d  \\
-(\hat{x} \hat{y}) u_2 v_1 &  & (\hat{y} \hat{z}) u_2 v_3 & (\hat{y} \hat{w}) u_2 v_4 & \dots & (\hat{y} e_d) u_2 v_d \\
-(\hat{x} \hat{z}) u_3 v_1 & -(\hat{y} \hat{z}) u_3 v_2 &  & (\hat{z} \hat{w}) u_3 v_4 & \dots & (\hat{z} e_d) u_3 v_d \\
-(\hat{x} \hat{w}) u_4 v_1 & -(\hat{y} \hat{w}) u_4 v_2 & -(\hat{z} \hat{w}) u_4 v_3 &  & \dots & (\hat{w} e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) u_d v_1 & -(\hat{y} e_d) u_d v_2 & -(\hat{z} e_d) u_d v_3 & -(\hat{w} e_d) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \vec{v} ∧ \vec{u} = \begin{bmatrix}  & (\hat{x} \hat{y}) v_1 u_2 & (\hat{x} \hat{z}) v_1 u_3 & (\hat{x} \hat{w}) v_1 u_4 & \dots & (\hat{x} e_d) v_1 u_d  \\
-(\hat{x} \hat{y}) v_2 u_1 &  & (\hat{y} \hat{z}) v_2 u_3 & (\hat{y} \hat{w}) v_2 u_4 & \dots & (\hat{y} e_d) v_2 u_d \\
-(\hat{x} \hat{z}) v_3 u_1 & -(\hat{y} \hat{z}) v_3 u_2 &  & (\hat{z} \hat{w}) v_3 u_4 & \dots & (\hat{z} e_d) v_3 u_d \\
-(\hat{x} \hat{w}) v_4 u_1 & -(\hat{y} \hat{w}) v_4 u_2 & -(\hat{z} \hat{w}) v_4 u_3 &  & \dots & (\hat{w} e_d) v_4 u_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) v_d u_1 & -(\hat{y} e_d) v_d u_2 & -(\hat{z} e_d) v_d u_3 & -(\hat{w} e_d) v_d u_4 & \dots &  \\ \end{bmatrix} = -\begin{bmatrix}  & -(\hat{x} \hat{y}) v_1 u_2 & -(\hat{x} \hat{z}) v_1 u_3 & -(\hat{x} \hat{w}) v_1 u_4 & \dots & -(\hat{x} e_d) v_1 u_d  \\
(\hat{x} \hat{y}) v_2 u_1 &  & -(\hat{y} \hat{z}) v_2 u_3 & -(\hat{y} \hat{w}) v_2 u_4 & \dots & -(\hat{y} e_d) v_2 u_d \\
(\hat{x} \hat{z}) v_3 u_1 & (\hat{y} \hat{z}) v_3 u_2 &  & -(\hat{z} \hat{w}) v_3 u_4 & \dots & -(\hat{z} e_d) v_3 u_d \\
(\hat{x} \hat{w}) v_4 u_1 & (\hat{y} \hat{w}) v_4 u_2 & (\hat{z} \hat{w}) v_4 u_3 &  & \dots & -(\hat{w} e_d) v_4 u_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
(\hat{x} e_d) v_d u_1 & (\hat{y} e_d) v_d u_2 & (\hat{z} e_d) v_d u_3 & (\hat{w} e_d) v_d u_4 & \dots &  \\ \end{bmatrix} = -\begin{bmatrix}  & (\hat{x} \hat{y}) u_1 v_2 & (\hat{x} \hat{z}) u_1 v_3 & (\hat{x} \hat{w}) u_1 v_4 & \dots & (\hat{x} e_d) u_1 v_d  \\
-(\hat{x} \hat{y}) u_2 v_1 &  & (\hat{y} \hat{z}) u_2 v_3 & (\hat{y} \hat{w}) u_2 v_4 & \dots & (\hat{y} e_d) u_2 v_d \\
-(\hat{x} \hat{z}) u_3 v_1 & -(\hat{y} \hat{z}) u_3 v_2 &  & (\hat{z} \hat{z}) u_3 v_4 & \dots & (\hat{z} e_d) u_3 v_d \\
-(\hat{x} w) u_4 v_1 & -(\hat{y} w) u_4 v_2 & -(\hat{z} w) u_4 v_3 &  & \dots & (w e_d) u_4 v_d \\
\vdots & \vdots & \vdots & \vdots &  & \vdots \\
-(\hat{x} e_d) u_d v_1 & -(\hat{y} e_d) u_d v_2 & -(\hat{z} e_d) u_d v_3 & -(w e_d) u_d v_4 & \dots &  \\ \end{bmatrix} $$

$$ \vec{v} ∧ \vec{u} = - \vec{u} ∧ \vec{v} $$

Also, halfway through (well, more like mostly through), if I added one more $\hat{w}$, it would be "unabe to render expression". By the way, $2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ lines.

$$ \vec{v} \vec{u} = \vec{u} \cdot \vec{v} - \vec{u} ∧ \vec{v} $$

### complex numbers

$$ \text{complex numbers (surprisingly in geomatric algebra) come from } 2d \text{ geomatric algebra. So time to re-derive that! (And use } i \text{ this time instead of } U \text{.) (I thought that } i \text{ should have a hat, but that wouldn't work.) Here's the definitions and link to the complex numbers page:} $$

[.](https://silaspe.github.io/maths/complex.html)

$$ \hat{i} = \hat{x} \text{ (This is so that } \hat{i} \text{ isn't confused with } i \text{).} $$

$$ \hat{j} = \hat{y} $$

$$ \hat{x} \hat{y} = i $$

$$ \hat{x}^2 = 1 $$

$$ \hat{y}^2 = 1 $$

$$ \hat{x} \hat{y} = -\hat{y} \hat{x} \text{(} = i \text{)} $$

$$ \text{And with those, you can derive} $$

$$ i^2 = -1 $$

$$ \text{this is why it was called } i. $$

.

$$ \text{Also, a bivector in } 2 \text{ dimensions has one degree of freedom (just like how a vector behaves in } 1d \text{) (by the way, a } k \text{-vector in } n \text{ dimensions has } \begin{pmatrix} n \\
k \\ \end{pmatrix} \text{ DoF's (degrees of freedom)), so I'll call it, I dunno, a pseudoscalar. (} i \text{ Is always the unit pseudoscalar no matter the dimension.)} $$

$$ \vec{u} = \begin{bmatrix} u_x \\
u_y \\ \end{bmatrix} = u_x \hat{x} + u_y \hat{y} $$

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\ \end{bmatrix} = v_x \hat{x} + v_y \hat{y} $$

$$ \vec{u} \vec{v} = \begin{pmatrix} (\hat{x} \hat{x}) u_x v_x & (\hat{x} \hat{y}) u_x v_y \\
(\hat{y} \hat{x}) u_y v_x & (\hat{y} \hat{y}) u_y v_y \\ \end{pmatrix} = (u_x v_x + u_y v_y) + (u_x v_y - u_y v_x)i $$



$300$ Lines!

$$ \vec{u} ∧ \vec{v} = i \cdot Det \begin{bmatrix} u_x & u_y \\
v_x & v_y \\ \end{bmatrix} $$

Here's a [determinat video](https://www.youtube.com/watch?v=Ip3X9LOh2dk) and [linear algebra playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) for context (make sure to skip the cross product video) (also, that determinant is probably the only matrix on this page. I'll come back here when I finish the page and put the awnser here: ). ( $\text{ }$ : ) $\text{ }$ Btw.)

$$  \text{Text over time! (As oppose to voice over, it's a font swich.) What's something that veiwers of this website would want from geomatric algebra? I think I have an idea: rotate a vector by the angle between two other vectors. I'l do it in } 20 \text{ minutes.} $$

$$ \text{It's the next day.} $$

$$ \vec{v} i = (v_x \hat{x} + v_y \hat{y})i = v_x \hat{x} i + v_y \hat{y} i = v_x \hat{x} \hat{x} \hat{y} + v_y \hat{y} \hat{x} \hat{y} = v_x \hat{y} - v_y \hat{x} \hat{y} \hat{y} = v_x \hat{y} - v_y \hat{x} $$

```py
def complexify(v_x, v_y):
  return v_x + v_y * j
```

$$ \text{I just realized that this isn't a code repo(sitory). It was my instinct to write it in code form.} $$

$$ \text{complexify} (v_x \hat{x} + v_y \hat{y}) = v_x + v_y i $$

(incert filler text here)

$$ \text{complexify} (\vec{v} i) = i \text{ complexify} (\vec{v}) $$

$$ i \vec{v} = i(v_x \hat{x} + v_y \hat{y}) = i v_x x + i v_y \hat{y} $$

$$ \text{But } v_x \text{ and } v_y \text{ are scalars, so} $$

$$ i \vec{v} = v_x i \hat{x} + v_y i \hat{y} = v_x \hat{x} \hat{y} \hat{x} + v_y \hat{x} \hat{y} \hat{y} = -v_x \hat{y} \hat{x} \hat{x} + v_y \hat{x} = -v_x \hat{y} + v_y \hat{x} $$

$$ \text{complexify} (i \vec{v}) = -i \text{ complexify} (\vec{v}). $$

$$ \text{Next: vector times a complex number.} $$

$$ \text{vectorize} (a + bi) = a \hat{x} + b \hat{y} $$

$$ \text{complexify} (\text{vectorize} (z)) = z $$

$$ \text{vectorize} (\text{complexify} (\vec{v})) = \vec{v} $$

$$ (a \hat{x} + b \hat{y})(c + di) = a \hat{x} c + a \hat{x} di + b \hat{y} c + b \hat{y} di = \begin{pmatrix} ac (\hat{x}) & ad (\hat{x} i) \\
bc (\hat{y}) & bd (\hat{y} i) \\ \end{pmatrix} = \begin{pmatrix} ac (\hat{x}) & ad (\hat{x} \hat{x} \hat{y}) \\
bc (\hat{y}) & bd (\hat{y} \hat{x} \hat{y}) \\ \end{pmatrix} = \begin{pmatrix} ac (\hat{x}) & ad (\hat{y}) \\
bc (\hat{y}) & -bd (\hat{x} \hat{y} \hat{y}) \\ \end{pmatrix} = \begin{pmatrix} ac (\hat{x}) & ad (\hat{y}) \\
bc (\hat{y}) & -bd (\hat{x}) \\ \end{pmatrix} = (ac - bd) \hat{x} + (ad + bc) \hat{y} $$

$$ z = a + bi $$

$$ w = c + di $$

$$ \text{vectorize} (z) w = \text{vectorize} (zw) $$

$$ \vec{u} \text{ complexify} (\vec{v}) = \text{vectorize} (\text{complexify} (\vec{u}) \text{ complexify} (v)) $$

$$ \vec{v} z = \text{vectorize} (\text{complexify} (\vec{v}) z) $$

Wait a minute! (Which was the catch phrase of sugey (pronounced soo-gey) in the quick introduction that I mentioned earlier.) If multiplying a vector by a complex number acts like comlex number multiplication (rotating and scaling) (exempt it returns a vector, not a complex number), and a vector times a vector is a complex number, that what rotation is that? (Well, the rotation and scaling of a complex number scales by the magnitude and rotates by the angle counterclockwise from the positave $x$ axis.)

$$ \text{By the way, } \vec{v} \vec{u} = \text{ccong} (\vec{u} \vec{v}) $$

$$ |a + bi| = \sqrt{a^2 + b^2} $$

$$ a + bi = \vec{u} \vec{v} $$

$$ a = \vec{u} \cdot \vec{v} = u_x v_x + u_y v_y $$

$$ bi = \vec{u} ∧ \vec{v} = (u_x v_y - u_y v_x)i \text{ (This also means that } b = u_x v_y - u_y v_x = \vec{u} \times \vec{v} \text{).} $$

$$ || \vec{u} \vec{v} || = \sqrt{(\vec{u} \cdot \vec{v})^2 + (\vec{u} \times \vec{v})^2} = \sqrt{(u_x v_x + u_y v_y)^2 + (u_x v_y - u_y v_x)^2} = \sqrt{u_x v_x u_x v_x + u_x v_x u_y v_y + u_y v_y u_x v_x + u_y v_y u_y v_y + u_x v_y u_x v_y - u_x v_y u_y v_x - u_y v_x u_x v_y + u_y v_x u_y v_x} = \sqrt{u_x^2 v_x^2 + u_x^2 v_y^2 + u_y^2 v_x^2 + u_y^2 v_y^2} = \sqrt{(u_x^2 + u_y^2)(v_x^2 + v_y^2)} = \sqrt{u_x^2 + u_y^2} \sqrt{v_x^2 + v_y^2} $$

$$ || \vec{u} || = \sqrt{u_x^2 + u_y^2} $$

$$ || \vec{v} || = \sqrt{v_x^2 + v_y^2} $$

$$ || \vec{u} \vec{v} || = || \vec{u} || \text{ } || \vec{v} || $$

$$ \text{Next: the part that I have no idea how to prove!} $$

$$ \vec{u} \vec{v} = || \vec{u} || \text{ } || \vec{v} || e^{i \theta} $$

$$ \theta = \text{ The angle counterclockwise from } \vec{u} \text{ towards } \vec{v}. $$

$$ \text{By the way, with this can derive two new equations! (But you probably know the first.)} $$

$$ \vec{u} \cdot \vec{v} = || \vec{u} || \text{ } || \vec{v} ||  cos(\theta) $$

$$ \vec{u} ∧ \vec{v} = || \vec{u} || \text{ } || \vec{v} ||sin(\theta) i $$

But what I wanted was that $\theta!$ But it is ([almost](https://silaspe.github.io/maths/arctan.html)) impossible to find $\theta$ when all you know is $e^{i \theta}$. Wait a minute! If a complex number of the form $e^{i \theta}$ is just a rotation, and if multiplying a vector by a complex number acts like they were both complex numbers (exempt it returns a vector), than you can rotate a vecor $\vec{w}$ by the angle between two unit vectors (or just ones with inverse magnitude, but normalizing them is easier) without having to even know about complex numbers!

$$ \hat{u} = \frac{\vec{u}}{|| \vec{u} ||} $$

$$ \hat{v} = \frac{\vec{v}}{|| \vec{v} ||} $$

$$ \hat{u} \hat{v} = e^{i \theta} $$

$$ \text{So, the rotation is} $$

$$ \vec{w} \hat{u} \hat{v}. $$

(Mic drop.) Also, that was on $400$ lines exactly.

$$ \text{One more thing before maxwell's equation and rotors.} $$

$$ (c + di)(a \hat{x} + b \hat{y}) = ca \hat{x} + cb \hat{y} + dia \hat{x} + dib \hat{y} = \begin{pmatrix} ca (\hat{x}) & cb (\hat{y}) \\
da (i \hat{x}) & db (i \hat{y}) \\ \end{pmatrix} = \begin{pmatrix} ca (\hat{x}) & cb (\hat{y}) \\
da (\hat{x} \hat{y} \hat{x}) & db (\hat{x} \hat{y} \hat{y}) \\ \end{pmatrix} = \begin{pmatrix} ca (\hat{x}) & cb (\hat{y}) \\
-da (\hat{y} \hat{x} \hat{x}) & db (\hat{x}) \\ \end{pmatrix} = \begin{pmatrix} ca (\hat{x}) & cb (\hat{y}) \\
-da (\hat{y}) & db (\hat{x}) \\ \end{pmatrix} = (ca + db) \hat{x} + (cb - da) \hat{y} = (a \hat{x} + b \hat{y})(c - di) $$

$$ z \vec{v} = \vec{v} \text{ ccong} (z) $$

$$ \text{But if you remember, } \vec{v} \vec{u} = \text{ccong} (\vec{u} \vec{v}) \text{ and } \vec{u} \vec{v} \text{ is a complex number, so...} $$

$$ \vec{u} \vec{v} \vec{w} = \vec{w} \text{ ccong} (\vec{u} \vec{v}) = \vec{w} \vec{v} \vec{u} $$

$$ \text{One more thing.} $$

$$ \theta (\vec{u}, \vec{v}) = \text{ The angle counterclockwise from } \vec{u} \text{ towards } \vec{v}. $$

$$ \vec{w} \vec{u} \vec{v} = \vec{w} \text{ Scaled by the length of } \vec{u} \text{ and } \vec{v} \text{, and rotated by } \theta (\vec{u}, \vec{v}).  $$

### Rotors

A rotor is a way to rotate a vector by any angle $\theta$ in any plane (Yes, plane. I think it makes the same if not more sense to rotate in a plane. I also think that this is simalar to the ∧ v.s. $\times$ Product.) in any dimention. Let's start with the simplest possible rotor I can think of, in $3d$, $90$°, $\hat{x}$ - $\hat{y}$ plane. (I'll call $\vec{v}$ rotated by the name of $\vec{v} \prime$)

$$ \vec{v} = v_x \hat{x} + v_y \hat{y} + v_z \hat{z} $$

$$ \vec{v} \prime = v_x \hat{y} - v_y \hat{x} + v_z \hat{z} $$

$$ \vec{v} \prime = \vec{v} \hat{x} \hat{y} ? $$

$$ \vec{v} \hat{x} \hat{y} = (v_x \hat{x} + v_y \hat{y} + v_z \hat{z}) \hat{x} \hat{y} = v_x \hat{x} \hat{x} \hat{y} + v_y \hat{y} \hat{x} \hat{y} + v_z \hat{z} \hat{x} \hat{y} = v_x \hat{y} - v_y \hat{x} \hat{y} \hat{y} - v_z \hat{x} \hat{z} \hat{y} = (v_x) \hat{y} - (v_y) \hat{x} + (v_z) \hat{x} \hat{y} \hat{z} $$

$$ \text{What was that thing he said at this point? Oh right, it was: Well, it almost worked, the } x \text{ and the } y \text{ coordinates got rotated correctly, but the } z \text{ coordinate got turned into this trivector, let's try something else.} $$

$$ \text{Do you remember that time when I proved that } z \vec{v} = \vec{v} \text{ ccong} (z) \text{, that means that I can now prove this: } \vec{v} z = \text{ccong} (z) \vec{v} \text{. I'll assume that that means } \hat{y} \hat{x} \text{, I'll try that!} $$

$$ \hat{y} \hat{x} \vec{v} = \hat{y} \hat{x} (v_x \hat{x} + v_y \hat{y} + v_z \hat{z}) = \hat{y} \hat{x} v_x \hat{x} + \hat{y} \hat{x} v_y \hat{y} + \hat{y} \hat{x} v_z \hat{z} = v_x \hat{y} \hat{x} \hat{x} + v_y \hat{y} \hat{x} \hat{y} + v_z \hat{y} \hat{x} \hat{z} = v_x \hat{y} - v_y \hat{x} \hat{y} \hat{y} - v_z xyz = (v_x) y - (v_y) x - (v_z) \hat{x} \hat{y} \hat{z} $$

$$ \text{Once again, the } x \text{ and the } y \text{ coordinates got rotated correctly, but the } z \text{ coordinate got turned into the inverse trivector this time, maybe doing both at once would cancel out?} $$

$$ \hat{y} \hat{x} \vec{v} \hat{x} \hat{y} = \hat{y} \hat{x} (v_x \hat{x} + v_y \hat{y} + v_z \hat{z}) \hat{x} \hat{y} = \hat{y} \hat{x} v_x \hat{x} \hat{x}  \hat{y} + \hat{y} \hat{x} v_y \hat{y} \hat{x} \hat{y} + \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} = v_x \hat{y} \hat{x} \hat{y} + v_y \hat{y} \hat{x} \hat{y} \hat{x} \hat{y} + \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} = - v_x \hat{x} \hat{y} \hat{y} - v_y \hat{y} \hat{y} \hat{x} \hat{x} \hat{y} + \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} = - v_x \hat{x} - v_y \hat{y} + \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} $$

$$ \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} = v_z \hat{y} \hat{x} \hat{z} \hat{x} \hat{y} = -v_z \hat{y} \hat{x} \hat{x} \hat{z} \hat{y} = -v_z \hat{y} \hat{z} \hat{y} = v_z \hat{y} \hat{y} \hat{z} $$

$$ \hat{y} \hat{x} v_z \hat{z} \hat{x} \hat{y} = v_z \hat{z} $$

$$ \hat{y} \hat{x} \vec{v} \hat{x} \hat{y} = - v_x \hat{x} - v_y \hat{y} + v_z \hat{z} $$

$$ \text{ The } z \text{ coordinate is correct! Success! But the } x \text{ and } y \text{ got messed up, of coarse they did, we rotated twice. (Once for } \hat{y} \hat{x} \text{ on the left, and once for } \hat{x} \hat{y} \text{ on the right.) let's add back in that angle } \theta \text{ to prove that we did rotate twice.} $$

Do you remember [euler's identity](https://silaspe.github.io/maths/complex.html), $e^{i \theta} = cos(\theta) + isin(\theta)$ right? Well, this actually for any $i$ whose square is $-1$, the thing is that $(\hat{x} \hat{y})^2 = \hat{x} \hat{y} \hat{x} \hat{y} = -\hat{x} \hat{x} \hat{y} \hat{y} = -1$, so

$$ e^{\hat{x} \hat{y} \theta} = cos(\theta) + \hat{x} \hat{y} \text{ } sin(\theta). $$

$$ \text{And just to make sure, let's test for } \theta = 90° $$

$$ cos(90°) + \hat{x} \hat{y} \text{ } sin(90°) = 0 + \hat{x} \hat{y} \text{ } 1 = \hat{x} \hat{y}. $$

$$ \text{Also, } cos(\theta) = c \text{ and } sin(\theta) = s $$

$$ \text{So, replace } \hat{x} \hat{y} \text{ and } \hat{y} \hat{x} \text{ with } c + \hat{x} \hat{y} \text{ } s \text{ and } cos(-\theta) + \hat{x} \hat{y} \text{ } sin(-\theta) \text{ respectively.} $$

$$ \text{(The second one can simplify to } c - \hat{x} \hat{y} \text{ } s \text{).} $$

$$ \vec{v} \prime = (v_x c - v_y s) \hat{x} + (v_y c + v_x s) \hat{y} + v_z \hat{z} $$

$$ (c - \hat{x} \hat{y} \text{ } s) \text{ } \vec{v} \text{ } (c + \hat{x} \hat{y} \text{ } s) = (c - \hat{x} \hat{y} \text{ } s) (v_x \hat{x} + v_y \hat{y} + v_z \hat{z}) (c + \hat{x} \hat{y} \text{ } s) $$

$$ (c - \hat{x} \hat{y} \text{ } s) \text{ } \vec{v} \text{ } (c + \hat{x} \hat{y} \text{ } s) = c v_x \hat{x} \text{ } c + c v_x \hat{x} \hat{x} \hat{y} \text{ } s - \hat{x} \hat{y} \text{ } s v_x \hat{x} \text{ } c - \hat{x} \hat{y} \text{ } s v_x \hat{x} \hat{x} \hat{y} \text{ } s + c v_y \hat{y} \text{ } c + c v_y \hat{y} \hat{x} \hat{y} \text{ } s - \hat{x} \hat{y} \text{ } s v_y \hat{y} \text{ } c - \hat{x} \hat{y} \text{ } s v_y \hat{y} \hat{x} \hat{y} \text{ } s + c v_z \hat{z} \text{ } c + c v_z \hat{z} \hat{x} \hat{y} \text{ } s - \hat{x} \hat{y} \text{ } s v_z \hat{z} \text{ } c - \hat{x} \hat{y} \text{ } s v_z \hat{z} \hat{x} \hat{y} \text{ } s = (v_x cc) \hat{x} + (v_x cs) \hat{x} \hat{x} \hat{y} - (v_x sc) \hat{x} \hat{y} \hat{x} - (v_x ss) \hat{x} \hat{y} \hat{x} \hat{x} \hat{y} + (v_y cc) \hat{y} + (v_y cs) \hat{y} \hat{x} \hat{y} - (v_y sc) \hat{x} \hat{y} \hat{y} - (v_y ss) \hat{x} \hat{y} \hat{y} \hat{x} \hat{y} + (v_z cc) \hat{z} + (v_z cs) \hat{z} \hat{x} \hat{y} - (v_z sc) \hat{x} \hat{y} \hat{z} - (v_z sin(\theta) sin(\theta)) \hat{x} \hat{y} \hat{z} \hat{x} \hat{y} $$

$$ \text{I had to split it in } 2 \text{, it reached the limit of LaTeX symbols per line.} $$

$$ \hat{x} \hat{x} \hat{y} = \hat{y} $$

$$ \hat{x} \hat{y} \hat{x} = -\hat{y} \hat{x} \hat{x} = -\hat{y} $$

$$ \hat{x} \hat{y} \hat{x} \hat{x} \hat{y} = \hat{x} \hat{y} \hat{y} = \hat{x} $$

$$ \hat{y} \hat{x} \hat{y} = -\hat{y} \hat{y} \hat{x} = -\hat{x} $$

$$ \hat{x} \hat{y} \hat{y} = \hat{x} $$

$$ \hat{x} \hat{y} \hat{y} \hat{x} \hat{y} = \hat{x} \hat{x} \hat{y} = \hat{y} $$

$$ \hat{z} \hat{x} \hat{y} = -\hat{x} \hat{z} \hat{y} = \hat{x} \hat{y} \hat{z} $$

$$ \hat{x} \hat{y} \hat{z} \hat{x} \hat{y} = -\hat{x} \hat{y} \hat{x} \hat{z} \hat{y} = \hat{x} \hat{x} \hat{y} \hat{z} \hat{y} = \hat{y} \hat{z} \hat{y} = -\hat{z} \hat{y} \hat{y} = -\hat{z} $$

$$ (c - \hat{x} \hat{y} \text{ } s) \text{ } \vec{v} \text{ } (c + \hat{x} \hat{y} \text{ } s) = (v_x cc) \hat{x} + (v_x cs) \hat{y} + (v_x sc) \hat{y} - (v_x ss) \hat{x} + (v_y cc) \hat{y} - (v_y cs) \hat{x} - (v_y sc) \hat{x} - (v_y ss) \hat{y} + (v_z cc) \hat{z} + (v_z cs) \hat{x} \hat{y} \hat{z} - (v_z sc) \hat{x} \hat{y} \hat{z} + (v_z ss) \hat{z} $$

$$ (v_x cc) \hat{x} + (v_x cs) \hat{y} + (v_x sc) \hat{y} - (v_x ss) \hat{x} = (v_x cc - v_x ss) \hat{x} + (v_x cs + v_x sc) \hat{y} = (v_x(cos(\theta) cos(\theta) - sin(\theta) sin(\theta))) \hat{x} + (v_x(cos(\theta) sin(\theta) + sin(\theta) cos(\theta))) \hat{y} $$

And then, with some [trigonometry identities](https://silaspe.github.io/maths/trigonometry.html)...

$$ cos(\theta + \theta) = cos(\theta) cos(\theta) - sin(\theta) sin(\theta) $$

$500$ Lines!

$$ sin(\theta + \theta) = cos(\theta) sin(\theta) + sin(\theta) cos(\theta) $$

$$ (v_x cc) \hat{x} + (v_x cs) \hat{y} + (v_x sc) \hat{y} - (v_x ss) \hat{x} = (v_x cos(2 \theta)) \hat{x} + (v_x sin(2 \theta)) \hat{y} $$

$$ (v_y cc) \hat{y} - (v_y cs) \hat{x} - (v_y sc) \hat{x} - (v_y ss) \hat{y} = (v_y cc - v_y ss) \hat{y} - (v_y cs + v_y sc) \hat{x} = (v_y(cos(\theta) cos(\theta) - sin(\theta) sin(\theta))) \hat{y} - (v_y(cos(\theta) sin(\theta) + sin(\theta) cos(\theta))) \hat{x} $$

$$ (v_y cc) \hat{y} - (v_y cs) \hat{x} - (v_y sc) \hat{x} - (v_y ss) \hat{y} = (v_y cos(2 \theta)) \hat{y} - (v_y sin(2 \theta)) \hat{x} $$

$$ (v_x cc) \hat{x} + (v_x cs) \hat{y} + (v_x sc) \hat{y} - (v_x ss) \hat{x} + (v_y cc) \hat{y} - (v_y cs) \hat{x} - (v_y sc) \hat{x} - (v_y ss) \hat{y} = (v_x cos(2 \theta)) \hat{x} + (v_x sin(2 \theta)) \hat{y} + (v_y cos(2 \theta)) \hat{y} - (v_y sin(2 \theta)) \hat{x} = (v_x cos(2 \theta) - v_y sin(2 \theta)) \hat{x} + (v_y cos(2 \theta) + v_x sin(2 \theta)) \hat{y} $$

$$ (v_z cc) \hat{z} + (v_z cs) \hat{x} \hat{y} \hat{z} - (v_z sc) \hat{x} \hat{y} \hat{z} + (v_z ss) \hat{z} = (v_z cc) \hat{z} + (v_z ss) \hat{z} = (v_z(cc + ss)) \hat{z} $$

And then, with some more [trigonometry identities](https://silaspe.github.io/maths/arctan.html#what-even-is-the-arctan-puzzle)...

$$ (v_z cc) \hat{z} + (v_z cs) \hat{x} \hat{y} \hat{z} - (v_z sc) \hat{x} \hat{y} \hat{z} + (v_z ss) \hat{z} = (v_z) \hat{z} $$

$$ \text{Also, } cos(2 \theta) = C \text{ and } sin(2 \theta) = S $$

$$ \vec{v} \prime \prime = (v_x C - v_y S) \hat{x} + (v_y C + v_x S) \hat{y} + v_z \hat{z} $$

$$ e^{-\hat{x} \hat{y} \theta} \vec{v} e^{\hat{x} \hat{y} \theta} = \vec{v} \prime \prime $$

$$ \text{Yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss! (Yes, that was } 100 \text{ s's.) Now I have proved that it did rotate twice, there is a simple fix, divide the angle by } 2. $$

$$ \vec{v} \prime = e^{-\hat{x} \hat{y} \frac{\theta}{2}} \vec{v} e^{\hat{x} \hat{y} \frac{\theta}{2}} $$

$$ \text{And there it is, } \vec{v} \text{ in it's prime.} $$

### Maxwell's equation (singular) (#spoilers)

$$  = \text{ the } $$

$$ \text{First, the un-simplified Maxwell's equations:} $$

$$ \text{'s law:} $$
.
