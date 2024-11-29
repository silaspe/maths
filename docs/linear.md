## linear algebra

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

### part $4$: matrices and linear transformations

Let's start off this part with a quote:


$100$ Lines.

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
-2x + 0y \\ \end{bmatrix}$. You give me any vector and I tell you the output vector.

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

You could even use this formula as a definition. And then you could teach it to high schoolers worldwide and not teach them the key intuition that makes it intuitive ($x \begin{bmatrix} a \\
c \\ \end{bmatrix} + y \begin{bmatrix} b \\
d \\ \end{bmatrix}$)

Isn't it better to think of the columns of the matrix as where $\hat{x}$ and $\hat{y}$ each go and the result of multiplying a matrix by a vector as the appropriate linear combination?

How would you describe a linear transformation like a 90° counterclockwise rotation? (Yes, that is a linear transformation.) Well, $\hat{x}$ gets shifted up towards $\begin{bmatrix} 0 \\
1 \\ \end{bmatrix}$ ($\hat{y}$) and $\hat{y}$ gets rotated down towards $\begin{bmatrix} -1 \\
0 \\ \end{bmatrix}$ ($-\hat{x}$). So the result should be the matrix $\begin{bmatrix} 0 & -1 \\
1 & 0 \\ \end{bmatrix}$, and if you want to rotate any vector clockwise by 90 degrees, just multiply it by the matrix $\begin{bmatrix} 0 & -1 \\
1 & 0 \\ \end{bmatrix}$.

On the other hand, if the two columns are linearly dependent, the transformation squishes all of space onto one line, the span of the two linearly dependent columns.

Summary:

linear transformations are those that preserve the operations of vector addition and scalar multiplication, of which you can think of as transformations of space that keep the grid lines parallel and evenly spaced with the origin remaining fixed. But to describe your linear transformation, you only need a handful of numbers: the coordinates of where the basis vectors land. matrices give us a language for linear transformations: just read off the columns and you'll know where the basis vectors land. And matrix vector multiplication just tells you what the linear transformation does to a given vector.
