### group theory?

I am finally making this page to celebrate the up upcoming $2000$th line on the brainstorm page.

Here's some great videos about the subject that should get at least some credit: [Group theory, abstraction, and the 196,883-dimensional monster](https://www.youtube.com/watch?v=mH0oCDa74tE), [What is Group Theory? — Group Theory Ep. 1](https://www.youtube.com/watch?v=KufsL2VgELo) (Yes, I know, there's a part two. But I decided not to watch it because I was worried that if I watched it then I would just copy some of it), [This playlist by Another Roof](https://www.youtube.com/playlist?list=PLsdeQ7TnWVm_KATm7HjPoZ-q0UaQNjYrC) (I've only seen the third part).

I'll start off with the textbook definition of a group:

PS I don't have a group theory textbook.

It is a set or collection of things together with a binary operation (e.g. addition or multiplication because they input two things and output one thing) (this binary operation is usually denoted with a composition circle (this thing: ∘) so that is the notation that I will use) such that...

$1$. Closure: (this one is sometimes a given) If you have $a$ and $b$ in the group, then $a ∘ b$ is also within the group.

$2$. Associativity: If you have $a$, $b$ and $c$ in the group, then $(a ∘ b) ∘ c$ is equal to $a ∘ (b ∘ c)$. For this reason, I will be denoting both as $a ∘ b ∘ c$

$3$. Identity (or neutral depending on where you're from): There must always be a term in the group (call it $e$) where if you have $a$ in the group, then $a ∘ e$ is equal to $e ∘ a$ is equal to $a$.

$4$. Inverses: If you have $a$ in the group, then there is also $a^{-1}$ in the group where $a ∘ a^{-1}$ is equal to $e$.

Notice there is no point where I say that the operation is commutative (i.e. $a ∘ b = b ∘ a$). If it is commutative, it is also known as an Abelian group.

Also by the way, it is common to notate $a ∘ a ∘ a ∘ ... ∘ a$ $n$ times as $a^n$

A good way to think about what groups actually are is as symmetries. This is because these four rules are exactly what you would expect rotations and reflections to do with the operation of doing one after the other.

For example, now the inverses rule makes sense because if you rotate clockwise then of course you should also be able to rotate counterclockwise.

An example of a group is the integers with the operation of addition, but not the integers with an operation of multiplication because only $1$ and $-1$ have an inverse. The rational numbers under multiplication (excluding $0$) also form a group and so can the rationals under addition. Also of course, the real numbers with addition and multiplication (excluding $0$).

#### proofs

Proof number one: there's only one identity element.

This proof uses a proof by contradiction strategy. Let's say that there are more than one identity element. So I'm going to choose the first two being $e_1$ and $e_2$.

Now, I ask of you, what is $e_1 ∘ e_2$? Because on the one hand, it should equal $e_2$ because $e_1$ times anything is that thing. But on the other hand, it should equal $e_1$ because anything times $e_2$ is that thing.

Thus, because they are both equal to $e_1 ∘ e_2$, they must themselves be equal. Thus there is only one identity element.

And you can keep going with this logic, doing the same thing with the next one, and the next one, until there is only one left.

QED!

Proof number two: The inverse of the inverse is the original.

Every element has an inverse. So, by definition, the inverse has an inverse.

Let's operate all of these together and see what happens.

$$ a ∘ a^{-1} ∘ (a^{-1})^{-1} $$

This should of course equal $a$ because $a^{-1}$ times its inverse should cancel out. But also this should equal $(a^{-1})^{-1}$ because $a$ and its inverse should cancel out. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

Proof number three: The inverse can cancel out from either side.

The term $a^{-1} ∘ a$ can also be simplified. Because $a$ is equal to $(a^{-1})^{-1}$, I can cancel $a^{-1}$ with its inverse, resulting in the identity.

$$ a^{-1} ∘ a = a^{-1} ∘ (a^{-1})^{-1} = e $$

QED!

Proof number four: There's only one inverse for a given term.

This one uses the same general strategy as proof number one. Let's assume that there were multiple inverses, denoted $a^{-1}_1$ and $a^{-1}_2$. Then of course, $a ∘ a^{-1}_1 = e$.

Let's see what happens when you multiply both sides on the left by $a^{-1}_2$.

$$ a^{-1}_2 ∘ a ∘ a^{-1}_1 = a^{-1}_2 ∘ e $$

Then $a^{-1}_2$ and $a$ would cancel out resulting in $a^{-1}_1$ on the left. But on the other side, the identity element cancels out resulting in $a^{-1}_2$. Thus, because they are both equal to the same thing, they themselves must be equal.

QED!

Proof number five: $(a^2)^{-1} = (a^{-1})^2$ and they can both be denoted as $a^{-2}$.

$$ a^2 ∘ (a^2)^{-1} = e $$

$$ a^2 ∘ (a^{-1})^2 = a ∘ a ∘ a^{-1} ∘ a^{-1} = a ∘ a^{-1} = e $$

Because these are both the inverse of $a^2$ and because of proof number four, they must both be the same.

QED!

#### subgroups & cosets
