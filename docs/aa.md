The equations below are the beginning of pages that may or may not get added to my website. All pages after Modular arithmetic and this one started here in the brainstorm page. I got these from copying things from a piece of paper that hes potential to become a digital page. And finaly, the titles have a question mark if they are my best guss for the titles of the page, no question mark if I made the page and know the title, a question mark if I never published the page, but still want the world to see it, and extra small if is just one puzzle, but didn't fit anywhere and/or was worth making a dedicated page. Also, happy eclipse day! The eclipse was worth the $10$ (total) hours of driving.

### galois theory/field theory?

A field of numbers is a collection of numbers where you can add, subtract, multiply, and even sometimes divide two numbers (as long as you don't divide by zero) in that field to get another number in that field. For example, the rationals, the reals and the complex numbers ane all fields that are infinate and you can divide them. The complex lattice points (which are complex numbers of the form $integer + integer \cdot i$ ), the matrixes (incert joke here), and the integers, are all in the infinate but can not always be divided. I know what you might be thinking: "what the (abbreviation that I am allowed to say for a curse word that I am not allowed to say) is a non-infinate field?". A non-infinite field or finite field is something like the [modulo numbers](https://silaspe.github.io/maths/mod.html). You might not be able to divide in a non-prime base, but you can do it in a prime base. So that completes the venn diagram!

Today, I want to show you an infinate field where you can not divide, I'm talking (well, typing) about numbers of the form

$$ a + b \sqrt{7} $$

for integers $a$ and $b$.

Side note! A number of this form can only be written in one way. Not because $\sqrt{7}$ is an imaginary number, but because $\sqrt{7}$ is irrational. End of side note.

You can probably take my word for it that you can add, subtract, and multiply these numbers, but here's a proof (which was the only thing on that was on the paper that inspired this (digital) page. *Other than division and square roots).

$$ (a + b \sqrt{7}) + (c + d \sqrt{7}) = a + b \sqrt{7} + c + d \sqrt{7} $$

$$ (a + b \sqrt{7}) - (c + d \sqrt{7}) = a + b \sqrt{7} - c - d \sqrt{7} $$

$$ (a + b \sqrt{7}) \cdot (c + d \sqrt{7}) = ac + a d \sqrt{7} + b \sqrt{7} c + b \sqrt{7} d \sqrt{7} $$

.

$$ (a + b \sqrt{7}) + (c + d \sqrt{7}) = (a + c) + (b + d) \sqrt{7} $$

$$ (a + b \sqrt{7}) - (c + d \sqrt{7}) = (a - c) + (b - d) \sqrt{7} $$

$$ (a + b \sqrt{7}) \cdot (c + d \sqrt{7}) = (ac + 7bd) + (ad + bc) \sqrt{7} $$

$$ \text{And all of these are a number of this form. The end! Yeah, that was my whole* idea.} $$

#### that one puzzle

$$ \frac{\partial (x^2 + y^2)}{\partial (x + y)} = ? $$

$$ \text{Okay fine, yes, that one was a joke. But it took me a whole weekend to solve.} $$

$$ \text{Not that every day isn't a weekend for me, but I remember solving it on sunday and posing ist the day before.} $$

#### I might not work today (sad emoji)

... Because there is a science something, what was it again? Physics festival! So I am sad to say that, today, I will break my at least $1$ edit to my website per day rule... Wait! This text that I am writing counts as something, so I'll add this to my website. Anyways, I need to leave, and everyone is waiting for me.

#### or today

... That chapter title and this text will be what I add to my website today.

### why can't you multiply two vectors? (all endings)?

$$ \vec{v} = \begin{bmatrix} v_x \\
v_y \\
v_z \\ \end{bmatrix} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k} $$

$$ \vec{w} = \begin{bmatrix} w_x \\
w_y \\
w_z \\ \end{bmatrix} = w_x \hat{i} + w_y \hat{j} + w_z \hat{k} $$

$$ \vec{v} \vec{w} = (v_x \hat{i} + v_y \hat{j} + v_z \hat{k}) (w_x \hat{i} + w_y \hat{j} + w_z \hat{k}) = v_x \hat{i} w_x \hat{i} + v_x \hat{i} w_y \hat{j} + v_x \hat{i} w_z \hat{k} + v_y \hat{j} w_x \hat{i} + v_y \hat{j} w_y \hat{j} + v_y \hat{j} w_z \hat{k} + v_z \hat{k} w_x \hat{i} + v_z \hat{k} w_y \hat{j} + v_z \hat{k} w_z \hat{k} $$

$$ \text{For lack of a better way to display this, } \vec{v} \vec{w} \text{ equals the thing below:} $$

$$ (\hat{i} \hat{i})(v_x w_x) + (\hat{i} \hat{j})(v_x w_y) + (\hat{i} \hat{k})(v_x w_z) $$

$$ (\hat{j} \hat{i})(v_y w_x) + (\hat{j} \hat{j})(v_y w_y) + (\hat{j} \hat{k})(v_y w_z) $$

$$ (\hat{k} \hat{i})(v_z w_x) + (\hat{k} \hat{j})(v_z w_y) + (\hat{k} \hat{k})(v_z w_z) $$

$$ \text{Ending } 1 \text{, I give up.} $$

Because there is no way that this is a vector

### ending 2, geometric algebra/clifford algebra?

Yeah, I forgot all endings to multiplying vectors, so I came up with the previous one. Well, I guss I had this one, but I would rather make it into it's own page. After waching [A Swift Introduction to Geometric Algebra](https://www.youtube.com/watch?v=60z_hpEAtD8) (litteraly, that was the name), I thought that (if it is a scalar plus a bivector), than it is just a scalar plus a vector times $i$ (or $-i$, I am not sure yet), but I will call it $U$ instead. But first, here's the definition of multiplying two basis vectors (all the alternitave endings probably just had alternitave definitions for this. I think that I remember the definition that multiplication was anticomutative, which would lead me to the cross product)
