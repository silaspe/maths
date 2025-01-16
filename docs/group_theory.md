I am finally making this page to celebrate the upcoming $2000$th line on the brainstorm page.

Here's some great videos about the subject that should get at least some credit: [Group theory, abstraction, and the 196,883-dimensional monster](https://www.youtube.com/watch?v=mH0oCDa74tE) for the intuition, [This playlist by Nemean](https://www.youtube.com/playlist?list=PLFw-I5kGJQ3TKSMHJdAqjmZAJVD6y0CFs) for the proofs, the examples of things, and I would assume isomorphism examples (I decided not to watch the second video yet), and [This playlist by Another Roof](https://www.youtube.com/playlist?list=PLsdeQ7TnWVm_KATm7HjPoZ-q0UaQNjYrC) Which I don't think I'll take any of the same things from it.

I'll start off with the textbook definition of a group:

PS I don't have a group theory textbook.

### textbook definitions

It is a set or collection of things together with a binary operation (e.g. addition or multiplication because they input two things and output one thing) (this binary operation is usually denoted with a composition circle (this thing: ∘) so that is the notation that I will use) such that...

$1$. Closure: (this one is sometimes a given) If you have $a$ and $b$ in the group, then $a$ ∘ $b$ is also within the group.

$2$. Associativity: If you have $a$, $b$ and $c$ in the group, then $(a$ ∘ $b)$ ∘ $c$ is equal to $a$ ∘ $(b$ ∘ $c)$. For this reason, I will be denoting both as $a$ ∘ $b$ ∘ $c$

$3$. Identity (or neutral depending on where you're from): There must always be a term in the group (call it $e$) where if you have $a$ in the group, then $a$ ∘ $e$ is equal to $e$ ∘ $a$ is equal to $a$.

$4$. Inverses: If you have $a$ in the group, then there is also $a^{-1}$ in the group where $a$ ∘ $a^{-1}$ is equal to $e$.

Notice there is no point where I say that the operation is commutative (i.e. $a$ ∘ $b = b$ ∘ $a$). If it is commutative, it is also known as an Abelian group.

Also by the way, it is common to notate $a$ ∘ $a$ ∘ $a$ ∘ $\dots$ ∘ and so on $n$ times as $a^n$

A good way to think about what some groups actually are is as sets of symmetries. This is because these four rules are exactly what you would expect rotations and reflections to do with the operation of doing one after the other.

For example, now the inverses rule makes sense because if you rotate clockwise then of course you should also be able to rotate counterclockwise.

### example groups

An example of a group is the integers with the operation of addition.

Adding two integers would result in another integer. Addition is associative and there is only one $a + b + c$. There is of course an identity element of which is zero. And the inverse would of course be the negative.

Thus, it is a group! And the symbol is $ℤ$.

Let's see what happens to the integers with an operation of multiplication!

Multiplying two integers would result in another integer. There is only one $a \times b \times c$. There is an identity element (i.e. $1$). But sadly, only one and $-1$ have inverses.

Thus this is not a group :(

This is also why it's written $ℤ$ and not $ℤ^+$

But this does hint that the rationals with the operation of multiplication form a group (as long as you exclude zero because it doesn't have an inverse), and that is correct!

And the symbol is $ℚ^\times$.

And if you follow through all of the steps yourself or you got a hint from that times superscript then you know that the rationals with an operation of addition also form a group: $ℚ^+$.

Let me introduce you to another type of group, some finite groups: The dihedral groups! I'll use the example of $\text{D}_3$. It is the group of all rotations and reflections of an  equilateral triangle that leave it looking the same, with the operation of doing one after the other.

The operations are: do nothing, rotate clockwise $120$°, rotate counterclockwise $120$° reflect along the vertical axis, reflect on a $60$° tilted axis, and reflect along a $60$° tilted in the other direction axis.

This group works similarly for other numbers, with the subscript being the amount of faces on the regular polygon.

But there's a big debate over if it should be $n$ or $2n$.

Because on the one hand, it should be $n$ because that's the amount of sides it has, the group is kind of based off of that thing.

Personally, I think that the subscript should be the amount of faces.

But on the other hand, subscripts also usually denote the size and the size is always $2n$ (unless $n = 2$ or less)

There was this one time when I was talking to ChatGPT, and it said that $\text{D}_4$ was the dihedral group of order $8$.

There's also the integers with the operation of addition, and it loops back around once you reach a certain number (These groups are also known as the [modular](https://silaspe.github.io/maths/mod.html) groups). If that number is $n$ (i.e. the elements of the group are $0$ all the way up to $n - 1$), then it is denoted $ℤ_n$

### proofs

#### Proof number $1$: there's only $1$ identity element.

This proof uses a proof by contradiction strategy. Let's say that there are more than $1$ identity element. So I'm going to choose the first two being $e_1$ and $e_2$.

Now, I ask of you, what is $e_1$ ∘ $e_2$? Because on the one hand, it should equal $e_2$ because $e_1$ times anything is that thing. But on the other hand, it should equal $e_1$ because anything times $e_2$ is that thing.

Thus, because they are both equal to $e_1$ ∘ $e_2$, they must themselves be equal. Thus there is only $1$ identity element.

And you can keep going with this logic, doing the same thing with the next one, and the next one, until there is only $1$ left.

QED!

#### Proof number $2$: The inverse of the inverse is the original.

Every element has an inverse. So, by definition, the inverse has an inverse.

Let's operate all of these together and see what happens.

$$ a ∘ a^{-1} ∘ (a^{-1})^{-1} $$

This should of course equal $a$ because $a^{-1}$ times its inverse should cancel out. But also this should equal $(a^{-1})^{-1}$ because $a$ and its inverse should cancel out. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

#### Proof number $3$: The inverse can cancel out from either side.

The term $a^{-1}$ ∘ $a$ can also be simplified. Because $a$ is equal to $(a^{-1})^{-1}$, I can cancel $a^{-1}$ with its inverse, resulting in the identity.


$100$ Lines.

$$ a^{-1} ∘ a = a^{-1} ∘ (a^{-1})^{-1} = e $$

QED!

#### Proof number $4$: There's only $1$ inverse for a given term.

This one uses the same general strategy as proof number $1$. Let's assume that there were multiple inverses, denoted $a^{-1}_1$ and $a^{-1}_2$. Then of course, $a$ ∘ $a^{-1}_1 = e$.

Let's see what happens when you ∘ both sides on the left by $a^{-1}_2$.

$$ a^{-1}_2 ∘ a ∘ a^{-1}_1 = a^{-1}_2 ∘ e $$

Then $a^{-1}_2$ and $a$ would cancel out resulting in $a^{-1}_1$ on the left. But on the other side, the identity element cancels out resulting in $a^{-1}_2$. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

#### Proof number $5$: $(a^2)^{-1} = (a^{-1})^2$ and they can both be denoted as $a^{-2}$.

$$ a^2 ∘ (a^2)^{-1} = e $$

$$ a^2 ∘ (a^{-1})^2 = a ∘ a ∘ a^{-1} ∘ a^{-1} = a ∘ a^{-1} = e $$

Because these are both the inverse of $a^2$ and because of proof number four, they must both be the same.

QED!

Using the example of the integers, we have just proved that: there's only $1$ zero, $-(-3) = 3$, $3 + (-3) = (-3) + 3 = 0$, and there's only $1$ $-3$

At the same time, we have just proved that: there's only one $1$, $\frac{1}{\frac{1}{3}} = 3$, $3 \frac{1}{3} = \frac{1}{3} 3 = 1$, and there's only one $\frac{1}{3}$

They're all connected! They're all secretly the same! Group theory (or, more generally abstract algebra) really is the grand unified theory of algebraic systems! 

### subgroups & cosets

#### subgroups

Once again, I'll start with the textbook definition of a subgroup.

##### textbook definitions

If you have a group and, taking just a portion of it, operating any of those elements together would result in another thing within that portion, then that portion is also known as a subgroup, as it is a group within a group.

And yeah, I think that that's pretty intuitive of a definition, you can take just some of the elements of the group and they still form a group.

##### examples

Some examples of a subgroup are: the even integers for $ℤ$, the integers for $ℚ^+$, just the rotations from the dihedral groups (Which by the way are just the modular groups), or if the base is composite then the dihedral group from any of its factors, or the same thing for the modular group.

But notice, the odd integers don't form a group because of the closure axiom, Adding two odd integers forms an even integer.

But there are better ways to form and notate subgroups than to just guess and check. For example, the rotations can be formed by repeatedly applying the $120$° rotation. And an example of a subgroup of a modular group is the $0$, $3$, $6$ group within $ℤ_9$ (which is isomorphic to $ℤ_3$, but will get to isomorphism later).

Something these all have in common is that they are formed by starting at the identity and then checking everything that is formed by repeatedly ∘ing with a thing.

There is a notation for this: $⟨a⟩$ represents the sets of all powers of $a$.

The system is closed because a power of $a$ ∘ a power of $a$ is a power of $a$.

And this is indeed a group even for finite groups. Because if it's a finite group then repeatedly operating $a$ on it should eventually go through all of the elements and loop back around to itself. So the one before $a$ has to be the identity.

Also, if $e = a^8$, then the inverse of $a^n$ is just $a^{8 - n}$.

I know you might be thinking: why does it have to loop back around to the identity? What if $a^n$ were equal to $a$? Well, then ∘ing both sides by the inverse of $a$, you would get $a^8$ ∘ $a^{-1}$, which is of course equal to $a^7$. However, on the right of the equation, you get $a$ ∘ $a^{-1}$ which is of course the identity. So then $a^7$ would be the identity.

However, this argument doesn't necessarily work for integers as the group is infinitely large, and $⟨2⟩$ would only result in $2$, $4$, $6$, $8$, and so on, and not all of the even integers.

Just going to say: this is still valid notation even if it isn't a group.

But, this can be fixed! The true definition includes the identity element and the negative powers when needed, so $⟨2⟩$ is now a group!

#### cosets

Cosets can be explained as shifted copies of subgroups.

How you can more formally define cosets are as subgroups but each term is ∘ed on the left (or on the right depending on the context) by a certain thing.

Notice: it uses the word "set" because it isn't necessarily a group. For example, the odd numbers are a coset, but not a group.

The notation for cosets is kind of what you'd expect. For example, the odd numbers are just notated $1 + ⟨2⟩$ (This notation makes them seem more like arrays in coding than lists)

Also, $3 + ⟨2⟩$ or $5 + ⟨2⟩$ or $6 + ⟨2⟩$ would also work.

Also, because of notation like $⟨a⟩$ ∘ $e$, subgroups are a type of coset.

Also, within the dihedral group, the reflections are cosets. The reason why is because if you do a reflection then a rotation, then it just rotates the reflection line.

You can do the same thing the other way around with the identity and a flip with the shift being a rotation, and you get another case of perfect symmetry of a subgroup and its corresponding cosets perfectly filling up the group. I feel like this is building up to something big!

#### Lagrange's theorem

Lagrange's theorem (or at least something equivalent to it) states that if you pick a subgroup, then every element of the group will be covered once and only once by that subgroup and its cosets.

Let's say that the group has $16$ elements and that the elements of the subgroup are $e$, $a$, $b$, and $c$.

If I have any element $x$, then it is not too hard to cover it with a subgroup. Just shift it over by $x$, and the corresponding term to the identity element will cover it as $x$ ∘ $e = x$.

You can take this as either a subgroup or a proof that everything in the group is covered by at least one coset.

$200$ Lines.

Now, we have elements: $e$, $a$, $b$, $c$, $x$, $x$ ∘ $a$, $x$ ∘ $b$, and $x$ ∘ $c$

Also, now I would like to convince you that the cosets are of course the same size.

Because if the code set is bigger than there must have been an extra term you ∘ by to get to it.

But it can't be any less because if $x$ ∘ $a = x$ ∘ $b$, then ∘ing both sides by $x^{-1}$ (and using a little bit of proof number three), you get that $a = b$, which would just mean that the original subgroup is smaller, not that the coset is smaller than the subgroup.

But, you might still be thinking: what if the cosets overlap? Well, this is very complicated to prove. First: can a coset overlap with the original group? Well, then $x$ ∘ $a = b$, so $x = b$ ∘ $a^{-1}$

Because of the inverse property for the subgroup, $a^{-1}$ is also within the subgroup. And because of the closure property for the subgroup, $b$ ∘ $a^{-1}$ is in the subgroup.

Thus, $x$ must be within the subgroup. And shifting by something within the subgroup doesn't really change anything, so subgroups and cosets can't overlap.

However, you can technically define $x$ ∘ $a$ as $(x$ ∘ $y^{-1})$ ∘ $(y$ ∘ $a)$, so you can convince yourself that they can't overlap.

Now, we have elements: $e$, $a$, $b$, $c$, $x$, $x$ ∘ $a$, $x$ ∘ $b$, $x$ ∘ $c$, $y$, $y$ ∘ $a$, $y$ ∘ $b$, $y$ ∘ $c$, $z$, $z$ ∘ $a$, $z$ ∘ $b$, and $z$ ∘ $c$.

We have just proven that you can neatly partition a group with a subgroup and its cosets, and from this, you can drive The following theorem:

For any group $G$ and subgroup $H$, the size of $G$ is divisible by the size of $H$.

This theorem is also known as Lagrange's theorem (Which Lagrange knew nothing about).

We've been building up to this for the entire chapter! We have seen that the reflections and the rotations are both of size $n$! We have seen that the $0$, $3$, $6$ group is of size $3$ and $ℤ_9$ is of size $9$! We... actually have seen no other examples for this because this only works for finite groups.

Here's one way to think about it: if the size of a group is a prime number (like $7$), then the only possible size is of subgroups are of size $1$ (which is clearly just the set containing the identity (yes, it is a group)) and the whole thing itself. So if you take any term $a$ in the group and you keep ∘ing by it, then you will eventually form a subgroup.

Except, the size of the subgroup is either $1$ or $7$, and if it's $1$, then clearly, $a$ was just the identity.

But if it's anything else, then the size has to be $7$ as $a$, not being the identity, wouldn't have an identity element. And if it's of size $7$, that must be the whole group, so you can just label each term as $e$, $a$, $a^2$, $a^3$, $a^4$, $a^5$, and $a^6$.

Then what if we just label $e$ as zero, $a$ as $1$, $a^2$ as 2, and so on, also ∘ as $+$.

Then we realize that every single group of which its size is prime number $p$, the group is actually just $ℤ_p$ and disguise!

### isomorphic groups and homomorphisms

#### isomorphic groups

First, let's just parse this term "isomorphic" (by the way, I think isomorphic and homomorphic mean the same thing. But isomorphic is used in group theory and category theory, while homeomorphic is used in topology) two things are isomorphic if they are related via homeomorphism (that's a direct quote from ChatGPT). homo means the same, and morphic means what you think it means. So homeomorphic means you can morph one into the other and they still look the same (as you do in topology, and it's kind of the same thing in group theory) and a homeomorphism is a method of doing just that.

Long story short, two groups are isomorphic when they have the same general structure.

I'll take the example of $\text{V}_4$ (what I called the $2x2$ sudoku group (long story), then the rock paper scissors group, then it's formal name), then there's an identity element, if you take two non-identity ones that are themselves distinct and you ∘ them, you get the third one, and if you take two of the same one and you ∘ them, you get the identity.

If a group $G$ has the same structure, then we write:

$$ G \cong \text{V}_4 $$

($G$ is isomorphic to $\text{V}_4$)

Now, how do we formally define this "isomorphism"? Well, I have a definition, except it's kind of long. It is:

If you have groups $G$ and $H$ and $G$ has operation $\cdot$ while $H$ has operation $*$, then they are isomorphic if you can find an isomorphism (which is a type of one to one correspondence) between them. But, it has to do the following: if you pick $a$ and $b$ that are within $G$, then if $a \cdot b$ is equal to $c$, then with the corresponding $E$ ($e$ was taken) and $f$ in $H$, you get that $E * f$ is the corresponding term to $c$.

Okay, that definition was terrible. Here's a definition that was given to me by ChatGPT:

$$ \varphi : G → H $$

(A mapping $\varphi$ from $G$ to $H$)

$$ \varphi (a \cdot b) = \varphi (a) * \varphi (b) $$

(If you pick $a$ and $b$ in $G$, then $\varphi (a \cdot b) = \varphi (a) * \varphi (b)$)

It shouldn't be too hard to convince yourself that these two are the same. $\varphi (a)$ is $E$, $\varphi (b)$ is $f$, $a \cdot b$ is $c$, $\varphi (x)$ is the corresponding term in $H$ to the term $x$ in $G$, and then, if you substitute those in, you get $\varphi (c) = E * f$.

And that's actually a Silas original definition, intuition, and example! (Well, apart from the ChatGPT part.)

Now, let's look at another example of isomorphism: the real numbers with the operation of addition ($ℝ^+$), and the real numbers with the operation of multiplication (excluding zero) ($ℝ^\times$) (This example was found in a three blue and brown video about group theory, except I don't remember which one. Just search "three blue brown group theory").

If we're trying to find an isomorphism between $ℝ^+$ and $ℝ^\times$, then what function would work?

$$ f(x + y) = f(x)f(y) $$

Does this equation look familiar to anyone? This function $f$ not only exists, but it's an exponential function!

$$ e^{x + y} = e^x e^y $$

Thus, $ℝ^+ \cong ℝ^\times$.

Okay, now I'm going to watch the [video by Nemean](https://youtu.be/VZiLpYC0t5E).

#### homomorphisms

I got $9$ minutes and $46$ seconds into the video and I already have so many ideas.

First, I got the terminology wrong. ChatGPT didn't misspeak when it said "two things are isomorphic if they're related via homomorphism".

But let's explore this idea of a homomorphism more. First, it might only take a few elements to define the homomorphism. Kind of like how a linear transformation only needs the two basis vectors to determine what it is for all outputs.

In group theory, this ($\varphi (a$ ∘ $b) = \varphi (a)$ ∘ $\varphi (b)$) relation of the homomorphism acts in kind of the same way, only needing a few outputs to define the whole thing. (In fact, I think that linear algebra is part of abstract algebra, of which group theory is a part of.)

Also, homomorphisms can go between groups of different sizes, but I don't think that that means that they're isomorphic because they don't feel the same, they aren't bijections, they're surjections.

Here's an example: if I want to map from $ℤ_6$ to $ℤ_3$, I only need $1$ output, which is $\varphi (1)$. Let me explain.

$300$ Lines.

$$ \varphi (1) = 1 $$

$$ \varphi (2) = \varphi (1 \cdot 1) = \varphi (1) * \varphi (1) = 1 * 1 = 2 $$

$$ \varphi (2) = 2 $$

$$ \varphi (3) = \varphi (2 \cdot 1) = \varphi (2) * \varphi (1) = 2 * 1 = 0 $$

$$ \varphi (3) = 0 $$

$$ \varphi (4) = \varphi (3 \cdot 1) = \varphi (3) * \varphi (1) = 0 * 1 = 1 $$

$$ \varphi (4) = 1 $$

$$ \varphi (5) = \varphi (4 \cdot 1) = \varphi (4) * \varphi (1) = 1 * 1 = 2 $$

$$ \varphi (5) = 2 $$

$$ \varphi (0) = \varphi (5 \cdot 1) = \varphi (5) * \varphi (1) = 2 * 1 = 0 $$

$$ \varphi (0) = 0 $$

If you know that $\cdot$ loops around every six and $*$ loops around every three, this should make sense.

More importantly, we just derived what all of the outputs should be for a given input using only $1$ example.

##### parity

By the way, I came up with pretty much this entire sub-subchapter at the ice skating rink today.

We can find more examples of homomorphism. For example, a homomorphism between $ℤ$ and $ℤ_2$.

$ℤ_2$ is a small group (in fact, the second smallest possible group), one containing only two elements, one where if you operate the non-identity element (that will henceforth be called $a$) with itself, you get the identity element.

$a$ to the power of any number $n$ is $a$ if $n$ is odd and the identity elements if $n$ is even. This can capture the idea of even or odd-ness, a.k.a. parity. So we can define the map $\varphi$ as just $a$ raised to the power of the input number.

No we get an important fact that I would rather show than tell:

$$ \varphi (n + k) = \varphi (n) ∘ \varphi (k) $$

What it was saying is that the parity of $n + k$ is determined by the parity of $n$ and the parity of $k$ in exactly the way you'd expect. Even plus even is even, even plus odd is odd, odd plus even is odd, and odd plus odd is even. The same way how ∘ works in $ℤ_2$: $e$ ∘ $e = e$, $e$ ∘ $a = a$, $a$ ∘ $e = a$, and $a$ ∘ $a = e$.

But there are more examples of a homomorphism from a group to $ℤ_2$ (a.k.a. a parity homomorphism).

Case in point: this one time I was talking to ChatGPT about all of the subgroups of $\text{S}_4$ (which is the group of all of the ways to arrange four things) (the reason why was because my code was so inefficient that after waiting for a solid $30$ seconds, it only had the trivial group because it had to loop through every single combination of the $24$ inputs which is very slow).

The results given to me by ChatGPT were the things I expected: the trivial group, variations of $ℤ_2$, variations of $ℤ_3$, variations of $ℤ_4$, even the group $\text{V}_4$ which was a pleasant surprise, and the group $\text{D}_4$ (which by the way ChatGPT called the dihedral group of order $8$).

But there was one that I didn't expect (but in hindsight it makes sense): $\text{A}_4$, A group described by $3$ blue $1$ brown as permutations of four things that preserve a certain parity.

This does kind of make sense as you could define a homomorphism $\varphi$ from the group $\text{S}_4$ to the group $ℤ_2$. And if you plug in the numbers...

$$ \varphi (p ∘ q) = \varphi (p) ∘ \varphi (q) $$

Suppose that both $p$ and $q$ have even parity. Then even parity ∘ even parity would of course be even parity. Thus, $p$ ∘ $q$ has even parity (this is explained better in the next sub-subchapter). So, this system is completely closed, and hence, this group has a name: $\text{A}_4$.

By the way, the parity is if it takes an even or odd amount of $2$-swaps to get to it from the identity.

Also by the way, Along with the whole group $\text{S}_4$, this completes ChatGPT's list.

Also by the way, there's a great [mathologer video about the parity of permutations](https://www.youtube.com/watch?v=w0mxdo5ur_A).

Now that I think about it, this should mean that there's a general theorem. The theorem is as follows:

##### theorem

If you have a mapping $\varphi$ from a group $G$ to a group $H$, then all of the elements where the output of $\varphi$ is the identity element in $H$, those elements themselves form a subgroup of $G$.

I actually just came up with this theorem while I was writing this, and I'm going to ask ChatGPT if this is a well-known theorem.

The answer is of course yes, and the theorem is known as the Kernel theorem. The reason why is because the set of all elements where the output is the identity is known as the kernel of $\varphi$.

ChatGPT also provided a sketch of a proof:

$1$. Closure. I've already done this proof, but I'll say it again.

$$ a, b \in \text{ker} (\varphi) $$

$$ \varphi (a) = \varphi (b) = e $$

$$ \varphi (a \cdot b) = \varphi (a) * \varphi (b) = e * e = e $$

$$ \varphi (a \cdot b) = e $$

$$ a \cdot b \in \text{ker} (\varphi) $$

$2$. Associativity. This one is a given as a subgroup has the same operation as the original, and thus, you don't need to prove that it is associative.

$3$. Identity. This one uses a proof by contradiction strategy. First, let's assume that $\varphi (e) \ne e$

$$ \varphi (a \cdot e) = \varphi (a) * \varphi (e) = e * \text{not } e = \text{not } e $$

$$ a \cdot e = e $$

$$ \varphi (a) \ne e $$

Contradiction!

$4$. Inverses. As there is only one inverse for a given term, I'll have to prove that the one inverse is within $\text{ker} (\varphi)$

$400$ lines.

$$ \varphi (a) = \varphi (a) $$

$$ \varphi (a \cdot a) = \varphi (a) * \varphi (a) $$

$$ \varphi (a \cdot a \cdot a) = \varphi (a) * \varphi (a) * \varphi (a) $$

$$ \vdots $$

$$ \varphi (a \cdot a \cdot a \cdot \dots \cdot a) = \varphi (a) * \varphi (a) * \varphi (a) * \dots * \varphi (a) $$

$$ \varphi (a^n) = \varphi (a)^n $$

Assuming that $G$ is finite, I can plug $-1$ into this equation.

$$ \varphi (a^{-1}) = (\varphi (a))^{-1} = e^{-1} = e $$

$$ \varphi (a^{-1}) = e $$

$420$ Lines. (I'm a kid, can you blame me?)

$$ a^{-1} \in \text{ker} (\varphi) $$

This completes the proof.

I also found in the video a simple reproof that $\varphi (e) = e$:

$$ \varphi (a \cdot e) = \varphi (a) * \varphi (e) $$

$$ \varphi (a \cdot e) = \varphi (a) $$

$$ \varphi (a) = \varphi (a) * \varphi (e) $$

And as there's only one identity element, this completes the proof.

I also found a proof in the video about the inverse rule:

$$ a \in \text{ker} (\varphi) $$

$$ \varphi (a \cdot a^{-1}) = \varphi (a) * \varphi (a^{-1}) $$

$$ \varphi (a \cdot a^{-1}) = \varphi (e) = e $$

$$ \varphi (a) * \varphi (a^{-1}) = e $$

And as there's only one inverse element, this completes the proof.

#### isomorphisms

You know the thing I said about how homomorphisms sometimes mapping to smaller groups? Well, I got the terminology wrong again, and ChatGPT got the terminology wrong. If the homomorphism maps from one group to another group where they're the same size, then it's called an isomorphism.

By the way, if there's an isomorphism $\varphi$ from a group $G$ to a group $H$, then there's an isomorphism $\varphi^{-1}$ from $H$ to $G$

He also said [here](https://youtu.be/VZiLpYC0t5E?t=1329s) that it was crazy that if you use multiplication for the modular groups instead of addition, then $ℤ^{\times}_p = ℤ_{p - 1}$, and I already knew this fact because one: computer, two: modular arithmetic $10$ months ago.

He also said [here](https://youtu.be/VZiLpYC0t5E?t=1349s) that there is no pattern, but it's literally just an exponential function.

#### automorphisms

An automorphism is an isomorphism from a group to itself, and I remember calling this one a self-homomorphism.

Here's an example: if you swap any of the non-identity elements in $\text{V}_4$, it's still the same.

Also, right now we stumble upon a sort of meta group theory (which to me is more similar to category theory): if you have a given group, then all of its automorphisms form a group with the operation of composition.

Now that I'm done with pretty much the entire page, I can finally copy over work that I did on the brainstorm page that never made it into the story.

### finite groups

Because the story of the pages is already complete and you should already understand the concepts, this is where I'll put my group theory work from now on.

When I talk about all of these group categories, it really makes you think: what are all of the groups? (Or at least finite groups.) I will answer this question with at least the first few groups (ranked by size), and once I reach one of my favorites, I'll talk about it.

At every step of the way. there is of course the cyclic group of that size, which is when you can repeatedly ∘ by one term to go all the way around.

These are kind of boring (at least to me).

By the definition of a set (of which a group is a type of set), the amount of elements within it have to be a positive integer (including zero).

So, let's start with...

#### groups of size $0$

As the set not having any elements doesn't have an identity element, this breaks the identity rule.

By the way, the empty group is closed as not having elements means it's impossible to ∘ two of them to get outside the group.

It is associative, and I'll prove that to you by going through all of the possibilities:

with all the elements, we need every element to have an inverse. But as there are no elements, we don't need to add extra inverses.

But anyways, every group of size zero fumbles at the identity rule. Time for...

#### groups of size $1$

Of course, because of the identity rule, the one element has to be the identity element, and this is a group as:

$500$ Lines.

$1$. It is closed, as $e$ ∘ $e = e$

$2$. It is associative, and I'll prove that to you by going through all of the possibilities: $(e$ ∘ $e)$ ∘ $e = e$ ∘ $e = e$. But also: $e$ ∘ $(e$ ∘ $e) = e$ ∘ $e = e$. Because they're both equal to the identity, they themselves must be equal, and because we have comprehensively gone through all possibilities, this group must have an associative operation.

$3$. it obviously has an identity element

$4$ inverses. I'll go through each term along with its inverse in the following table:

| element | inverse |
| ------- | ------- |
| e       | e       |

And yeah, that's kind of it, the group containing the identity is the only $1$ element group, and all other $1$ element groups are just isomorphic to it, with their own identity element and own operation.

Time for...

#### groups of size $2$

As we have proved in the Lagrange's theorem subchapter, every group whose size is a prime number must be isomorphic to each other and to the corresponding cyclic group. Thus, the only group of size $2$ is $ℤ_2$, and as this is a cyclic group, I'll say that it's already proved that it is a group.

I didn't really feel like doing this argument for the last subchapter.

Everything I liked about this group was discussed in the parity sub-subchapter.

And yeah, that's kind of it, $ℤ_2$ is the only $2$ element group, and all other $2$ element groups are just isomorphic to it, with their own operation.

Time for...

#### groups of size $3$

By the same logic, there can only be one $3$ element group.

I never really thought about this group too hard.

And yeah, I'm kind of tired of repeatedly copying and pasting the same thing. But $ℤ_3$ is the only $3$ element group.

Time for...

#### groups of size $4$

What I would like to prove to you is that the only $4$ element groups are $ℤ_4$ and $\text{V}_4$.

By the way, I thought of (almost) this whole proof last night.

Let's say you pick an element $a$ and you keep ∘ing by it until you form a subgroup. By Lagrange's theorem, the size of the subgroup is either $1$, $2$ or $4$.

If it's $1$, you clearly just picked the identity element. If it's $4$, it's just the cyclic group, and the only other possibility is that it's $2$. If it is $2$, then $a^2$ must be $e$.

Let's do the same with another term $b$. Once again, if the size is $1$, you clearly just picked the identity, and if the size is $4$, it's clearly just the cyclic group. (And this is the only part that I didn't figure out last night.) But this is still consistent as $b^2$ must equal $a$, then that term squared must have been the identity.

Anyways, the point is that $a^2$ must be $e$ if the group isn't just the cyclic group.

Let's pick the final element $c$. You know the drill by now, so I won't go over it again.

But what's worth noting is that  this subgroup can't be of size $4$, because if it was, then it would just be the cyclic group, but it can't be the cyclic group as the cyclic group only has one non-identity term that squares to the identity.

Anyways, we now know that any cyclic group with non-identity elements $a$, $b$, and $c$ has to have the following equality:

$$ a^2 = b^2 = c^2 = e $$

The proof is almost complete, I just have to ask the question: what is $a$ ∘ $b$? It can't be the identity because of the following, it can't be $a$ because of the following after that, it can't be $b$ because of the one after that, so the only possibility is that it is $c$. The same argument works even when you swap out $a$ and $b$ for something else.

$$ a ∘ b = e $$

$$ b ∘ b = e $$

$$ a ∘ b = b ∘ b $$

$$ a ∘ b ∘ b^{-1} = b ∘ b ∘ b^{-1} $$

$$ a ∘ e = b ∘ e $$

$$ a = b $$

.

$$ a ∘ b = a $$

$$ a ∘ e = a $$

$$ a ∘ b = a ∘ e $$

$$ a^{-1} ∘ a ∘ b = a^{-1} ∘ a ∘ e $$

$$ e ∘ b = e ∘ e $$

$$ b = e $$

.

$$ a ∘ b = b $$

$$ e ∘ b = b $$

$$ a ∘ b = e ∘ b $$

$$ a ∘ b ∘ b^{-1} = e ∘ b ∘ b^{-1} $$

$600$ Lines.

$$ a ∘ e = e ∘ e $$

$$ a = e $$

.

Note: you can swap $a$ and $b$ in this argument, meaning that the operation is also commutative.

Now, let's look at the evidence we have for what this non-cyclic group is: it's a $4$ element group where every term squared is the identity, it has a commutative operation, and ∘ing two non-identity terms results in the third.

The only group that fits this description is $\text{V}_4$.

QED!

Because $\text{V}_4$ is my favorite group (and because this is the best time to talk about it), I would like to tell you why I gave it the nickname "the $2x2$ sudoku group":

One day many years ago I played a game of $2x2$ sudoku with a completely blank board. I went through each term within a square, then throughout all four of the squares, always picking the smallest number that would still follow the rules. You quickly run into a contradiction with a board of size $3$, but when I did it with a board of size $2$, I always got the same pattern. Within any square, there was a repeating pattern, and it was the same for each row and each column. The pattern was $1$ $2$ $3$ $4$, $3$ $4$ $1$ $2$, $2$ $1$ $4$ $3$, and $4$ $3$ $2$ $1$. Time went by, and then I eventually asked "do all of these swaps for my group?" The answer is yes, and that is the story of why I always called it "the $2x2$ sudoku group"

By the way, $\text{V}_4$ is the only group that uses the letter $\text{V}$ because it's just that special.

Also, $\text{V}_4$ is the first composite group. This is an actual definition that I just guessed one day well in a bath: $G \times H$ is a group where the elements of it are ordered pairs of things from $G$ and $H$. The operation is to just do it with each individual term.

I just thought it would be cool for there to be a product of two groups, and then ChatGPT gave me a definition.

If you're curious, $\text{V}_4$ is equal to $ℤ_2 \times ℤ_2$, kind of like how $4$ is the first composite number because it's equal to $2 \times 2$

Time for...

#### groups of size $5$

By the same logic I used before, there can only be one $5$ element group.

And I'll stop here. Here's my table:

| group size | groups with that size |
| ---------- | --------------------- |
| $0$        |                       |
| $1$        | $\{ e \}$             |
| $2$        | $ℤ_2$                 |
| $3$        | $ℤ_3$                 |
| $4$        | $ℤ_4$, $\text{V}_4$   |
| $5$        | $ℤ_5$                 |

#### misc

Also, because now is the best time to talk about it, I made a ∘ table, but instead of symbols, I used colors. I first had this idea while I was trying to visualize the group $\text{S}_4$, but I made some in MS paint. One for the trivial group, one for $\text{D}_3$, one for $ℤ_2$, and one for $\text{V}_4$.

What I realized was that I saw the same pattern again in all of the rows: in the right order, then swap the first two along with the second two, then you swap the first two with the second two, then you put everything in reverse. The idea of the swaps being isomorphic to the original group does kind of make sense as these swaps encapsulate the idea of ∘ing on the left by your thing.

So of course ∘ing on the left by $b$, then by $a$ is just ∘ing on the left by their product. Thus, these swaps are isomorphic to the original.

I also plan to make a T-shirt about group theory as I did for [Modular Arithmeic](https://silaspe.github.io/maths/mod.html) and [The Lambda Calculus](https://silaspe.github.io/maths/lambda.html), and this is just the thing for that!

If you were wondering, here's the diagrams:

<img width="100" alt="{e}" src="https://github.com/user-attachments/assets/224327ac-1ec0-4ed3-aedf-7f156b8be228" />

<img width="100" alt="z2 2" src="https://github.com/user-attachments/assets/aef0c8d7-4648-490a-b13f-de299e625f99" />

<img width="100" alt="V4" src="https://github.com/user-attachments/assets/4418657f-32c7-490b-980f-22ea30dcd5da" />

On the left column is the first term with each color corresponding to a term. On the top is the second term, and if you look at The corresponding pixel color to that row and that column, that can tell you what the product is.

By the way, the background color is black.

It's the first idea that came to mind when I thought about how to display the underlying structure of a group that would be the same for all isomorphic groups.

Also, this is the first time I've imported an image into my website.

But being able to multiply modular groups does beg the question: what is $ℤ_2 \times ℤ_n$? Well, it's the group of ordered lists of either $0$ or $1$ in the first position, and any number $0$ to $n - 1$ in the second. The group has operations you can probably guess.

Note: the part where I was talking about $\text{V}_4$ earlier and the text here were originally in the same area, so that's why I would ask this question.

So, what is, for example, the group $ℤ_2 \times ℤ_3$? Last night I made a full ∘ table, but then I just asked ChatGPT, and the answer was surprisingly $ℤ_6$*. I was first thinking why this is the case, but as you can see below, they are perfectly isomorphic.

Also, because the operation in the modular groups is similar to addition, I'm going to replace the multiplicationy notation with more additiony notation.

$$ 0(1, 1) = (0, 0) $$

$$ 1(1, 1) = (1, 1) $$

$$ 2(1, 1) = (1, 1) ∘ (1, 1) = (1 ∘ 1, 1 ∘ 1) = (0, 2) $$

$$ 3(1, 1) = 2(1, 1) ∘ (1, 1) = (0, 2) ∘ (1, 1) = (0 ∘ 1, 2 ∘ 1) = (1, 0) $$

$$ 4(1, 1) = 3(1, 1) ∘ (1, 1) = (1, 0) ∘ (1, 1) = (1 ∘ 1, 0 ∘ 1) = (0, 1) $$

$$ 5(1, 1) = 4(1, 1) ∘ (1, 1) = (0, 1) ∘ (1, 1) = (0 ∘ 1, 1 ∘ 1) = (1, 2) $$

$$ 6(1, 1) = 5(1, 1) ∘ (1, 1) = (1, 2) ∘ (1, 1) = (1 ∘ 1, 2 ∘ 1) = (0, 0) $$

$$ (0, 0) = 0(1, 1) $$

$$ (0, 1) = 4(1, 1) $$

$$ (0, 2) = 2(1, 1) $$


$700$ Lines. I remember when the code repo page and brainstorm page were competing over which one would get to $700$ first, in order to be declared the largest page on the website. The reason why is because those two pages specifically (also maybe they set theory pages) don't really ever get finished, because there's always more to do. Except this page, this page (which definitely has a clear well defined story) got there. It just shows you-, it just shows $\text{me}$ how much math $\text{I}$ can do when $\text{I}$ put my mind to something.

$$ (1, 0) = 3(1, 1) $$

$$ (1, 1) = 1(1, 1) $$

$$ (1, 2) = 5(1, 1) $$

$$ \varphi (n(1, 1)) = n $$

This same method of proof works as long as $n$ is an odd number as you can see below. But if $n$ is an even number, then I guess there's really no way to categorize them, other than that they are a composite group. Personally, I would denote them with the letter $\text{V}$.

$$ 0(1, 1) = (0, 0) $$

$$ 1(1, 1) = (1, 1) $$

$$ 2(1, 1) = (1, 1) ∘ (1, 1) = (1 ∘ 1, 1 ∘ 1) = (0, 2) $$

$$ 3(1, 1) = 2(1, 1) ∘ (1, 1) = (0, 2) ∘ (1, 1) = (0 ∘ 1, 2 ∘ 1) = (1, 2) $$

$$ \vdots $$

$$ n(1, 1) = (n - 1)(1, 1) ∘ (1, 1) = (0, n - 1) ∘ (1, 1) = (0 ∘ 1, (n - 1) ∘ 1) = (1, 0) $$

$$ (n + 1)(1, 1) = n(1, 1) ∘ (1, 1) = (1, 0) ∘ (1, 1) = (1 ∘ 1, 0 ∘ 1) = (0, 1) $$

$$ (n + 2)(1, 1) = (n + 1)(1, 1) ∘ (1, 1) = (0, 1) ∘ (1, 1) = (1 ∘ 1, 1 ∘ 1) = (1, 2) $$

$$ (n + 3)(1, 1) = (n + 2)(1, 1) ∘ (1, 1) = (1, 2) ∘ (1, 1) = (1 ∘ 1, 2 ∘ 1) = (0, 3) $$

$$ \vdots $$

$$ 2n(1, 1) = (2n - 1)(1, 1) ∘ (1, 1) = (1, 2n - 1) ∘ (1, 1) = (1 ∘ 1, (n - 1) ∘ 1) = (0, 0) $$

$$ (x, y) = \Begin{bmatrix} x + y = 2k: y(1, 1) \\
x + y = 2k + 1: (y + n)(1, 1) \\ \end{Bmatrix} $$

$$ \varphi (n(1, 1)) = n $$
