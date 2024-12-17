This page doesn't require seeing the set theory page, but you can see it anyways.

The idea behind this page is that you can derive all of set theory from logic, so $\text{T}$ is true, and $\text{F}$ is false.

Tools: $\text{T}$, $\text{F}$, $=$*, and another thing that will be defined later.

*Returns true if the two things are the same, and false if they are not.

### boolean operations

I can derive the and operation like this:

$$ \text{F} ∩ \text{F} = \text{F} $$

$$ \text{F} ∩ \text{T} = \text{F} $$

$$ \text{T} ∩ \text{F} = \text{F} $$

$$ \text{T} ∩ \text{T} = \text{T} $$

and the or operation like this:

$$ \text{F} ∨ \text{F} = \text{F} $$

$$ \text{F} ∨ \text{T} = \text{T} $$

$$ \text{T} ∨ \text{F} = \text{T} $$

$$ \text{T} ∨ \text{T} = \text{T} $$

and the not operation like this:

$$ ¬ \text{F} = \text{T} $$

$$ ¬ \text{T} = \text{F} $$

and the less famous implies operation like this:

$$ \text{F} → \text{F} = \text{T} $$

$$ \text{F} → \text{T} = \text{T} $$

$$ \text{T} → \text{F} = \text{F} $$

$$ \text{T} → \text{T} = \text{T} $$

$$ (p \iff q) = (p = q) $$

$$ (p = q) \iff (p → q) ∩ (q → p) $$

$$ \text{Order of operations: } ¬ > ∩ > ∨ > = > → > \iff \text{.} $$

#### extensions

$$ \{ x| p(x) \} = \text{ The extension of } p(x) \text{ (and the secret } 4 \text{th tool) (curly braces didn't work for rendering reasons), the set of all } x \text{ such that } p(x) \text{ (is true), and this is how I'm going to define sets. This function } p(x) \text{ inputs, well, anything, and outputs a boolean (true or false) (e.g. is } x \text{ an odd number?).} $$

$$ \text{The extension of that particular function is the set of all odd numbers.} $$

### other things from set theory

You can also derive the membership or element sign like this:

$$ x \in \{ y| p(y) \} \iff p(x) \text{ (} = \text{T)} $$

which goes somewhere in between and and not in the order of operations.

And just for fun, I'll also derive the for any and there exists signs like this:

$$ \text{But first, } p(x) ≡ \text{T} \text{ Means } p(x) = \text{T} \text{ for all values of } x \text{, same thing for } p(x) ≡ \text{F} \text{ and } p(x) ≡ q(x) \text{.} $$

$$ \text{And it goes in between or and equals in the order of operations.} $$

$$ \text{I'll start with the general form for the for any sign: } ∀(x) \cdot p(x) \text{ (} = \text{T)}: q(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } p(x) → q(x) \text{, at least, I think.} $$

$$ \text{Yeah, it doesn't work, different values for } x \text{ would give different outputs.} $$

$$ \text{But, there's a simple trick, take the and over all values for } x \text{, so } (p(x) → q(x)) ≡ \text{T} \text{.} $$

$$ \text{And the general form for the there exists sign: } \exists (x) \cdot p(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } ¬(p(x) ≡ \text{F}) $$

$$ \text{Maybe I'll use it.} $$

$$ \text{There's also the highlander function, it's general form is} $$

$$ \exists ! (x) \cdot p(x) \text{ (} = \text{T)}  $$

$$ \text{And that example in logic: } ¬(p(x) ≡ \text{F}) ∩ (p(x) → (¬(y = x) → p(y) = \text{F})) $$

$$ \text{Alternative: } ¬(p(x) ≡ \text{F}) ∩ (p(x) ∩ ¬(y = x) → p(y) = \text{F}) $$

#### numbers

$$ 0 = Ø = \{ x| \text{F} \} $$

$$ \text{succ} (x) = \{ y| y = x \} $$


$100$ Lines.

$$ \text{succ} (0) = 1 $$

$$ \text{succ} (1) = 2 $$

$$ \text{succ} (2) = 3 $$

$$ 0 \in ℕ $$

$$ x \in ℕ → \text{succ} (x) \in ℕ $$

$$ ℕ = \{ x| (x = 0) ∨ \exists (y) \cdot (\text{succ} (y) = x) ∩ y \in ℕ \} = \{ x| (x = 0) ∨ ¬(((\text{succ} (y) = x) ∩ y \in ℕ) ≡ \text{F}) \} $$

#### Russell's paradox

$$ R = \{ x| ¬(x \in x) \} $$

$$ \text{Now, the question is, is } R \in R \text{? Because if } ¬(R \in R) \text{, than } ¬(x \in x) \text{ would be true (for } x \text{ equal to } R \text{), but then, } R \text{ would be an element of } R \text{, but if } R \in R \text{, than } ¬(x \in x) \text{ would be false (for } x \text{ equal to } R \text{), but then, } R \text{ wouldn't be an element of } R \text{, paradox!)} $$

$$ x \in \{ y| p(y) \} = \text{N (} \ne ℕ \text{)} \iff (¬(x \in \{ y| p(y) \}) → p(x) = \text{T}) ∩ ((x \in \{ y| p(y) \}) → p(x) = \text{F}) $$

$$ \text{N} ∩ \text{Anything} = \text{N} $$

$$ \text{N} ∨ \text{Anything} = \text{N} $$

$$ ¬ \text{N} = \text{N} $$

$$ R \in R = \text{N} $$

Now, I'll define an infinite set of things $x1, x2, x3,...$ that are all in $\{ x| \text{T} \}$.

And define $x1, x2, x3 \in S$ as $x1 \in S ∩ x2 \in S ∩ x3 \in S$.

And that, if a statement involves $x1$ or $x2$ or $x3$ and so on, then it's true for any value $x1, x2, x3,...$.

#### addition

$$ \text{I already defined the successor, what about addition?} $$

$$ x1, x2 \in ℕ → x1 + succ(x2) = succ(x1 + x2) $$

$$ x1 \in ℕ → x1 + 0 = x1 $$

### mappings

A mapping $f$ is, well, first pick a domain $X$ and codomain $Y$. Then, um, I gotta get out the set theory textbook.

Ok, I got out The real number system, in an algebraic setting, by J. B. Roberts. A gift from my grandpa.

A mapping $f$ is kinda like a function or a dictionary in python, (a mapping $f$ from domain $X$ and codomain $Y$ is denoted as $f: X → Y$) if you pick an $x$ in $X$, is it $tied$ $to$ some $y$ in $Y$. The particular value of $y$ for given $x$ is denoted as $f(x)$, but for a given $y$ in $Y$, there could be $0$, $1$, or more values of $x$ (e.g. The absolute value function). How you represent a mapping would be something like $f(x) = x^2$, $x ↦ x^2$, or $\lambda x. x^2$ [.](https://silaspe.github.io/maths/lambda.html). $f(x)$ for $¬(x \in X)$ is $\text{N}$ ($\text{N}$ stands for neither, but it can also br interpreted an NoneType from python). And finally, the image of $f$ is ($I(f)$):

$$ I(f) = \{ y| y \in Y ∩ \exists (x) \cdot x \in X ∩ f(x) = y \} $$

So

$$ I(f) = \{ y| y \in Y ∩ ¬((x \in X ∩ f(x) = y) ≡ \text{F}) \} $$

But if you don't like domains and codomains, here's the versions without them:

$$ I(f) = \{ y| ¬(y = \text{N}) ∩ \exists (x) \cdot f(x) = y \} $$

$$ I(f) = \{ y| ¬(y = \text{N}) ∩ ¬((f(x) = y) ≡ \text{F}) \} $$

#### cardinality

$$ \text{The cardinality of } S \text{ is denoted as hashtag } S \text{, but hashtags aren't allowed in git, so it's } C(S) \text{ instead.} $$

$$ (\exists (n) \cdot n \in ℕ ∩ (S = \{ k| k < n \})) → C(S) = n $$

$$ C(S) = C(T) \iff \exists (f: S → T) \cdot ∀(t) \cdot t \in T: \exists ! (s) \cdot f(s) = t $$

### mappings (again)

A definition that I thought of for mappings (that dosent imply a domain or codomain) uses a new thing to define axiomatioly (i.e. A thing that I have to define that it exists, and hasn't been seen before (e.g. How sets and extensions are not booleans)) (e.g. The $\text{N}$ in the Russell's paradox section): $→$ (Yes, another arrow (that makes $4$ (boolean arrow $→$, mapping arrow $→$, fancy functional arrow $↦$, and new arrow $→$))). I'll explain with an example: the function $x ↦ x^2$ would be denoted as the set containing $0 → 0$, $1 → 1$, $2 → 4$, $3 → 9$, $4 → 16$, $5 → 25$, and so on. ($(x → y)[1] = x$, And $(x → y)[2] = y$.)

You can also define ordered sets as mappings from natural numbers greater than $0$ (or from all natural numbers if you want it to be confusing like in every single programming language exept fortran) (this is why I didn't use ordered lists last time, because, they are defined with mappings) (I gotta go ice skating now, bye!) (I'm back and it's been $2$ hours).

$$ f(x) = \begin{Bmatrix} ¬ \exists(t) \cdot t \in f ∩ (t[1] = x): \text{N} \\
\exists(t) \cdot t \in f ∩ (t[1] = x): t[2] \\ \end{Bmatrix} $$

### other random stuff

$$ \{ x| p(x)] ∨ \{ x| q(x)] = \{ x| p(x) ∨ q(x)] $$

$$ \{ x| p(x)] ∩ \{ x| q(x)] = \{ x| p(x) ∩ q(x)] $$

$$ S \times T \text{ is pronounced "the cartesian product of } S \text{ and } T \text{".} $$

$$ \{ x| p(x)] \times \{ x| q(x)] = \{ l| l \text{ is a list of size } 2 ∩ (p(l(1)) ∩ q(l(2)))] $$

$$ S \times T = \{ l| l \text{ is a list of size } 2 ∩ (l(1) \in S ∩ l(2) \in T)] $$

The reason why it's called "the cartesian product" is (at least, I think) because $ℝ \times ℝ$ ($ℝ$ is the set of all real numbers) is the set of all ordered pairs of real numbers. That is, the set of all points on the cartesian plane.

The actual axiom of choice:


$200$ Lines.

$$ ∀(S) \cdot S \text{ Is a set of sets}: \exists (f: S → \{ x| \exists(T) \cdot x \in T ∩ T \in S]) \cdot ∀(T) \cdot T \in S: f(T) \in T $$

$$ \text{There's also compositions denoted as } f ∘ g \text{, but that does } g \text{ first, then } f \text{ (} (f ∘ g)(x) = f(g(x)) \text{). So I'll say that } f^* g \text{ does } f \text{ first, then } g \text{ (} (f^* g)(x) = g(f(x)) \text{).} $$

Here's a diagram of sets $A$, $B$, $C$, mappings $f: A → B$ and $g: B → C$, $f^* g: A → C$, and $I: \{ x| \text{T}] → \{ x| \text{T}] = x ↦ x$ [:](https://www.youtube.com/watch?v=DrldYpmwN5s&t=857s) (Just replace $\text{id}$ with $I$, and $g ∘ f$ with $f^* g$)

### the $8$ axioms of Zermelo–Fraenkel set theory (ZFC)

$1$: The Axiom of Extensionality:

$$ ∀(S, T): (∀(x): x \in S \iff x \in T → S = T) $$

$2$: The Axiom of Pairing:

$$ ∀(S, T): \exists (U) \cdot U = \{ x| x = S ∨ x = T] $$

$3$: The Axiom of Union:

$$ ∀(S, T): \exists (U) \cdot U = \{ x| x \in S ∨ x \in T] $$

$4$: The Axiom of the Power Set:

$$ ∀(S): \exists (T) \cdot T = \{ x| x ⊆ S] $$

$5$: The Axiom of Infinity:

$$ \exists (S) \cdot S = \{ x| x = \{ y| \text{F}] ∨ \exists (y) \cdot y \in S ∩ x = \{ z| z \in y ∨ z = y]] $$

$6$: The Axiom of Schema of Replacement:

$$ ∀(f): \exists (S) \cdot S = \{ y| \exists (P) \cdot P \in f ∩ p[2] = y] $$

$7$: The Axiom of Regularity:

$$ ∀(A): (A \ne \{ x| \text{F}] → \exists (B) \cdot (B \in (A ∩ B) ∩ A = \{ x| \text{F}])) $$

$8$: The Axiom of Schema of Separation:

$$ ∀(S): \exists (T) \cdot ∀(x) \cdot x \in T: x \in S $$

#### the secret $9$'th axiom of Zermelo–Fraenkel set theory (ZFC)

The Axiom of Choice:

$$ ∀(S): \exists (f) \cdot ∀(T) \cdot T \in S ∩ T \ne \{ x| \text{F}]: f(T) \in T $$

### comparosins

| My old notation          | Standard notation  | My new notation              |
| -------------------------| ------------------ | ---------------------------- |
| $∀(x) \cdot p(x): q(x)$  | $∀x. p(x) → q(x)$ | $(p(x) → q(x)) =_x \text{T}$ |
| $∀(x): p(x)$             | $∀x. p(x)$        | $p(x) =_x \text{T}$          |
| $\exists (x) \cdot p(x)$ | $\exists x. p(x)$  | $¬p(x) =_x \text{F}$          |
| $∀(A): \exists (f) \cdot ∀(B) \cdot B \in A ∩ ¬B = \{ x \| \text{F}]: f(B) \in B$ | $∀A. \exists f. ∀B. B \in A ∩ B \ne Ø → f(B) \in B$ | $((B^S \in A^S ∩ ¬B = \{ x \| \text{F}] → f(B) \in B) =_f \text{F}) =_{A, B} \text{F}$ |

### my new notation

The $=_x$ sign is pronounced "is equal to, for all values of $x$". Also, I (kinda) wrote $\exists (x) \cdot p(x)$ as $¬(∀(x): p(x) = \text{F}$), because the statement "there exists an $x$ where $p(x)$ is true" is just the inversion of the statemment "$p(x)$ is, for all values of $x$, equal to false". Then I realized that the for any sign takes the and over all values of $x$ and that the there exists sign takes the or over all values of $x$. So that $¬(∀(x): p(x) = \text{F})$ thing is just DeMorgan's laws: $¬(¬p ∩ ¬q) = p ∨ q$ and $¬(¬p ∨ ¬q) = p ∩ q$. So the equuivalent statement for the for any sign is $¬(\exists (x) \cdot p(x) = \text{F})$

### pure logic

All the symbols we need are: $∧$ (and), $∨$ (or), $¬$ (not), $→$ (implies), $\iff$ (if and only if/precisely when), $($ (open parentheses), $)$(close parentheses), $∀$ (for any/all), $∃$ (there exists), $\in$ (is an element) of, a separator (such as a dot), and none of the above (so literally anything else, I'll choose $x$). These are all of the symbols you need to describe all of set theory, and hence, all of modern mathematics.

Order of operations: $() > \in > ¬ > ∩ > ∨ > → > \iff$, and if you have a for any or there exists sign, it keeps going as far to the right as possible, kind of like a lambda.

Also, the statement $x \in S$ is the only possible way to make a statement that might be true and might be false, you can even think of sets as boolean functions that might be true and might be false depending on the input.

Also also, the reason why I'm using a dot as in for any $x$ and then a dots is because all of the variables are just strings of $x$'s, so for any $xx$, $xxx$ and then something, if I didn't have that separator, it would just be written as one block of five $x$'s, and it would not be certain what it actually meant.

Also also also, instead of writing out the full thing with lots of $x$'s, I'm usually just going to write $x$ subscript and then the amount of $x$'s there should be.

An example of a line of logic is: "$∀x.x \ne Ø → ∃xx.xx \in x$, $∀x.x \ne Ø → ∃xx.$ Double $x$ is wihin $x$", "$∀x.x \ne Ø$ implies that there exists double $x$ where double $x$ is wihin $x$", "For all $x$, x not being epty implies that there exists double $x$ where double $x$ is wihin $x$"

#### $1 + 1$

Before I start, none of this was scripted.

What I want to do here is prove that $1 + 1 = 2$. But most of the time, you find yourself in a loop of defining things. For example: what is $1$? $1$ is the successor of $0$. What is the successor operation? The successor operation is the function that-

"Stop right there!" Said person #$2$, "What is a function?".

"Okay, fine!" Said person #$1$, "I'll instead say that $1$ is the set that contains $0$." (written $\{ 0 \}$.)

"That's better, but can you express $\{ 0 \}$ more formally?" Said person #$2$.

"Well, what I mean by that is: $∀x.x \in \{ 0 \} \iff x = 0$." Said person #$1$. (For any/all $x$, $x$ is within $\{ 0 \}$ precisely when $x = 0$.)

"But what is $=$?" Said person #$2$.

"Axiom #$1$ of ZFC: the axiom of extensionality" said person #$1$, "it states that $S = T$ precisely when for any $s \in S$, $s \in T$, and for any $t \in T$, $t \in S$"

"Okay, so what you're saying is that $∀x.x \in 1 \iff (∀y.y \in x → y \in 0) ∧ (∀y.y \in 0 → y \in x)$." Said person #$2$.

"Yes. Is there anything else left undefined?" Said person #$1$.

"Yes, always!" Said person #$2$. "What is $0$?"


$300$ Lines.

"Are you really gonna make me answer that?" Said person #$1$.

"Yes!" Said person #$2$.

"Okay, fine!" Person #$1$ said with frustration. "$0$ is Ø" (the empty set) "is the set with nothing in it, so $¬∃x.x \in Ø$."

"So, what you really meant by $∀x.x \in 1 \iff (∀y.y \in x → y \in 0) ∧ (∀y.y \in 0 → y \in x)$ was $∀x.x \in 1 \iff ¬∃y.y \in x$." Said person #$2$

"Yes!" Said person #$1$.

"So $1$ is the set of all empty sets, of which there are only one" Said person #$2$ "am I understanding this correctly?" Said person #$2$

"Yes!" Said person #$1$.

I'm tired of this conversation between a mathematician and probably a mathematical snob who only accepts the truest logical statements crafted from pure mathematical set theory.

$$ ∀x_1.(∀x_2.x_2 \in x_1 \iff ¬∃x_3.x_3 \in x_2) → x_1 + x_1 = 2 $$

$$ \text{"For any variable (call it } x_1 \text{), that variable being } 1 \text{ implies that adding it to itself results in } 2 \text{, that is, there is not an } x_3 \in x_2 \text{"} $$

$$ ∀x_1.x_1 \in 2 \iff (∀x_2.x_2 \in x_1 \iff ¬∃x_3.x_3 \in x_2) $$

$$ \text{"For any variable (call it } x_1 \text{), } x_1 \in 2 \text{ implies that } x_1 = 1 \text{, that is, for any variable (call it } x_2 \text{), } x_2 \in 1 \text{ precisely when } x_2 = 0 \text{, that is, there is not an } x_3 \in x_2 \text{"} $$

$$ ∀x_1.∀x_2.(∀x_3.x_3 \in x_1 \iff ¬∃x_4.x_4 \in x_3) ∧ (∀x_3.x_3 \in x_2 \iff (∀x_4.x_4 \in x_3 \iff ¬∃x_5.x_5 \in x_4)) → ∀x_3.x_3 \in x_1 + x_1 \iff x_3 \in x_2 $$

$$ A(m, n) = m + n $$

$$ A(n, 0) = n $$

$$ S(n) = n + 1 $$

$$ A(m, S(n)) = S(A(m, n)) $$

$$ ∀m.∀n.n = S(m) \iff (∀x.x \in n \iff x = m) $$

$$ ∀m.∀n.n = S(m) \iff (∀x_1.x_1 \in n \iff (∀x_2.x_2 \in x_1 \iff x_2 \in m)) $$

I feel like doing something else, how about Russel's paradox? It states that there is no set that conain only sets that don't contain themselves.

$$ ¬∃x_1.∀x_2.x_2 \in x_1 \iff ¬x_2 \in x_2 $$

Next: the first axiom of set theory (The Axiom of Extensionality). It states that two sets are equal if they have the same elements, but I think it actually means that if two sets are equal (i.e. they have the same elements), a set cannot contain just one of them, it has to contain either both or neither of the sets.

$$ ∀x_1.∀x_2.x_1 = x_2 → ∀x_3.x_1 \in x_3 \iff x_2 \in x_3 $$

$$ ∀x_1.∀x_2.(∀x_3.x_3 \in x_1 \iff x_3 \in x_2) → ∀x_3.x_1 \in x_3 \iff x_2 \in x_3 $$

Next: the second axiom of set theory (The Axiom of Foundation). It states that every set must have an element disjoint from itself (i.e. an element where the union of that element and the original set is empty (i.e. they don't have any common elements)).

$$ ∀x_1.x_1 \ne Ø → ∃x_2.x_2 \in x_1 ∧ x_2 ∩ x_1 = Ø $$

$$ ∀x_1.¬x_1 = Ø → ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

$$ ∀x_1.x_1 = Ø ∨ ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

$$ ∀x_1.¬(∃x_2.x_2 \in x_1) ∨ ∃x_2.x_2 \in x_1 ∧ ¬∃x_3.x_3 \in x_1 ∧ x_3 \in x_2 $$

Next: the third axiom of set theory (The Axiom of Pairing). Actually, I'm not going to use the axiom of pairing, I'm going to use the closely related singleton axiom, It states that if you have a set then there exists the set containing that set, as opposed to the axiom of pairing which says that if you have two sets then there is a set containing both of them. These two statements are equivalent, but I prefer the first one.

Also I realized that this axiom makes the axiom a regularity redundant. Let's say that $S = \{ S \}$. then you would say that $S$ is a set because it is equal to the set containing $S$. So we would also need to assume that $S$ is a set for that to work, so that would mean that we need to prove that $S$ is a set, so that would mean that we need to prove that $S$ is a set, you just never get to the bottom of it and you can never declare that $S$ is a set.

Also this is a weird kind of axiom because it doesn't always make the set containing a set into a set, you still have to prove it with the other rules. So we just knocked out two axioms of set theory with one stone.
