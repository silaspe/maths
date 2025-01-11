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

#### Proof number one: there's only one identity element.

This proof uses a proof by contradiction strategy. Let's say that there are more than one identity element. So I'm going to choose the first two being $e_1$ and $e_2$.

Now, I ask of you, what is $e_1$ ∘ $e_2$? Because on the one hand, it should equal $e_2$ because $e_1$ times anything is that thing. But on the other hand, it should equal $e_1$ because anything times $e_2$ is that thing.

Thus, because they are both equal to $e_1$ ∘ $e_2$, they must themselves be equal. Thus there is only one identity element.

And you can keep going with this logic, doing the same thing with the next one, and the next one, until there is only one left.

QED!

#### Proof number two: The inverse of the inverse is the original.

Every element has an inverse. So, by definition, the inverse has an inverse.

Let's operate all of these together and see what happens.

$$ a ∘ a^{-1} ∘ (a^{-1})^{-1} $$

This should of course equal $a$ because $a^{-1}$ times its inverse should cancel out. But also this should equal $(a^{-1})^{-1}$ because $a$ and its inverse should cancel out. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

#### Proof number three: The inverse can cancel out from either side.

The term $a^{-1}$ ∘ $a$ can also be simplified. Because $a$ is equal to $(a^{-1})^{-1}$, I can cancel $a^{-1}$ with its inverse, resulting in the identity.


$100$ Lines.

$$ a^{-1} ∘ a = a^{-1} ∘ (a^{-1})^{-1} = e $$

QED!

#### Proof number four: There's only one inverse for a given term.

This one uses the same general strategy as proof number one. Let's assume that there were multiple inverses, denoted $a^{-1}_1$ and $a^{-1}_2$. Then of course, $a$ ∘ $a^{-1}_1 = e$.

Let's see what happens when you ∘ both sides on the left by $a^{-1}_2$.

$$ a^{-1}_2 ∘ a ∘ a^{-1}_1 = a^{-1}_2 ∘ e $$

Then $a^{-1}_2$ and $a$ would cancel out resulting in $a^{-1}_1$ on the left. But on the other side, the identity element cancels out resulting in $a^{-1}_2$. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

#### Proof number five: $(a^2)^{-1} = (a^{-1})^2$ and they can both be denoted as $a^{-2}$.

$$ a^2 ∘ (a^2)^{-1} = e $$

$$ a^2 ∘ (a^{-1})^2 = a ∘ a ∘ a^{-1} ∘ a^{-1} = a ∘ a^{-1} = e $$

Because these are both the inverse of $a^2$ and because of proof number four, they must both be the same.

QED!

Using the example of the integers, we have just proved that: there's only one zero, $-(-3) = 3$, $3 + (-3) = (-3) + 3 = 0$, and there's only one $-3$

At the same time, we have just proved that: there's only one one, $\frac{1}{\frac{1}{3}} = 3$, $3 \frac{1}{3} = \frac{1}{3} 3 = 1$, and there's only one $\frac{1}{3}$

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

$200$ Lines.

You can take this as either a subgroup or a proof that everything in the group is covered by at least one coset

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

Then what if we just label $e$ as zero, $a$ as one, $a^2$ as 2, and so on, also ∘ as $+$.

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

Here's an example: if I want to map from $ℤ_6$ to $ℤ_3$, I only need one output, which is $\varphi (1)$. Let me explain.

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

More importantly, we just derived what all of the outputs should be for a given input using only one example.

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

But there was one that I didn't expect (but in hindsight it makes sense): $\text{A}_4$, A group described by three blue one brown as permutations of four things that preserve a certain parity.

This does kind of make sense as you could define a homomorphism $\varphi$ from the group $\text{S}_4$ to the group $ℤ_2$. And if you plug in the numbers...

$$ \varphi (p ∘ q) = \varphi (p) ∘ \varphi (q) $$

Suppose that both $p$ and $q$ have even parity. Then even parity ∘ even parity would of course be even parity. Thus, $p$ ∘ $q$ has even parity. So, this system is completely closed, and hence, this group has a name: $\text{A}_4$.

By the way, the parity is if it takes an even or odd amount of $2$-swaps to get to it from the identity.

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

You know the thing I said about how homomorphisms sometimes mapping to smaller groups? Well, I got the terminology wrong again, and ChatGPT got the terminology wrong. If the homomorphism maps from from one group to another group where they're the same size, then it's called an isomorphism.
