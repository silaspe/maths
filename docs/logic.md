This page dosen't require seeing the set theory page, but you can see it anyways.

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

#### extntions

$$ [x| p(x)] = \text{ The extention of } p(x) \text{ (and the secret } 4 \text{th tool) (curly braces didn't work for rendering reasons), the set of all } x \text{ such that } p(x) \text{ (is true), and this is how I'm going to define sets. This function } p(x) \text{ inputs, well, anything, and outputs a boolean (true or false) (e.g. is } x \text{ an odd number?).} $$

$$ \text{The extention of that particular function is the set of all odd numbers.} $$

### other things from set theory

You can also derive the membership or element sign like this:

$$ x \in [y| p(y)] \iff p(x) \text{ (} = \text{T)} $$

which goes somewhere in between and and not in the order of operations.

And just for fun, I'll also derive the for any and there exists signs like this:

$$ \text{But first, } p(x) ≡ \text{T} \text{ Means } p(x) = \text{T} \text{ for all values of } x \text{, same thing for } p(x) ≡ \text{F} \text{ and } p(x) ≡ q(x) \text{.} $$

$$ \text{And it goes in between or and equals in the order of operations.} $$

$$ \text{I'll start with the general form for the for any sign: } ∀(x) \cdot p(x) \text{ (} = \text{T)}: q(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } p(x) → q(x) \text{, at least, I think.} $$

$$ \text{Yeah, it dosen't work, different values for } x \text{ would give different outputs.} $$

$$ \text{But, there's a simple trick, take the and over all values for } x \text{, so } (p(x) → q(x)) ≡ \text{T} \text{.} $$

$$ \text{And the general form for the there exists sign: } \exists (x) \cdot p(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } ¬(p(x) ≡ \text{F}) $$

$$ \text{Maybe I'll use it.} $$

$$ \text{There's also the highlander function, it's general form is} $$

$$ \exists ! (x) \cdot p(x) \text{ (} = \text{T)}  $$

$$ \text{And that example in logic: } ¬(p(x) ≡ \text{F}) ∩ (p(x) → (¬(y = x) → p(y) = \text{F})) $$

$$ \text{Alternative: } ¬(p(x) ≡ \text{F}) ∩ (p(x) ∩ ¬(y = x) → p(y) = \text{F}) $$

#### numbers

$$ 0 = Ø = [x| \text{F})] $$

$$ \text{succ} (x) = [y| y = x] $$


$100$ Lines.

$$ \text{succ} (0) = 1 $$

$$ \text{succ} (1) = 2 $$

$$ \text{succ} (2) = 3 $$

$$ 0 \in ℕ $$

$$ x \in ℕ → \text{succ} (x) \in ℕ $$

$$ ℕ = [x| (x = 0) ∨ \exists (y) \cdot (\text{succ} (y) = x) ∩ y \in ℕ] = [x| (x = 0) ∨ ¬(((\text{succ} (y) = x) ∩ y \in ℕ) ≡ \text{F})] $$

#### Russell's paradox

$$ R = [x| ¬(x \in x)] $$

$$ \text{Now, the question is, is } R \in R \text{? Because if } ¬(R \in R) \text{, than } ¬(x \in x) \text{ would be true (for } x \text{ equal to } R \text{), but then, } R \text{ would be an element of } R \text{, but if } R \in R \text{, than } ¬(x \in x) \text{ would be false (for } x \text{ equal to } R \text{), but then, } R \text{ wouldn't be an element of } R \text{, paradox!)} $$

$$ x \in [y| p(y)] = \text{N (} \ne ℕ \text{)} \iff (¬(x \in [y| p(y)]) → p(x) = \text{T}) ∩ ((x \in [y| p(y)]) → p(x) = \text{F}) $$

$$ \text{N} ∩ \text{Anything} = \text{N} $$

$$ \text{N} ∨ \text{Anything} = \text{N} $$

$$ ¬ \text{N} = \text{N} $$

$$ R \in R = \text{N} $$

Now, I'll define an infinate set of things $x1, x2, x3,...$ that are all in $[x| \text{T}]$.

And define $x1, x2, x3 \in S$ as $x1 \in S ∩ x2 \in S ∩ x3 \in S$.

And that, if a statement involves $x1$ or $x2$ or $x3$ and so on, then it's true for any value $x1, x2, x3,...$.

#### addition

$$ \text{I already defined the successor, what about addition?} $$

$$ x1, x2 \in ℕ → x1 + succ(x2) = succ(x1 + x2) $$

$$ x1 \in ℕ → x1 + 0 = x1 $$

### mappings

A mapping $f$ is, well, first pick a domain $X$ and codomain $Y$. Then, um, I gotta the set theory text book.

Ok, I got out The real number system, in an algebraic setting, by J. B. Roberts. A gift from my grandpa.

A mapping $f$ is kinda like a function or a dictionary in python, (a mapping $f$ from domain $X$ and codomain $Y$ is denoted as $f: X → Y$) if you pick an $x$ in $X$, is it $tied$ $to$ some $y$ in $Y$. The particular value of $y$ for given $x$ is denoted as $f(x)$, but for a given $y$ in $Y$, there could be $0$, $1$, or more values of $x$ (e.g. The absolute value function). How you represent a mapping would be something like $f(x) = x^2$, $x ↦ x^2$, or $\lambda x. x^2$ [.](https://silaspe.github.io/maths/lambda.html). $f(x)$ for $¬(x \in X)$ is $\text{N}$ ($\text{N}$ stands for neither, but it can also br interpreted an NoneType from python). And finally, the image of $f$ is ($I(f)$):

$$ I(f) = [y| y \in Y ∩ \exists (x) \cdot x \in X ∩ f(x) = y] $$

So

$$ I(f) = [y| y \in Y ∩ ¬((x \in X ∩ f(x) = y) ≡ \text{F})] $$

But if you don't like domains and codomains, here's the versions without them:

$$ I(f) = [y| ¬(y = \text{N}) ∩ \exists (x) \cdot f(x) = y] $$

$$ I(f) = [y| ¬(y = \text{N}) ∩ ¬((f(x) = y) ≡ \text{F})] $$

#### cardinality

$$ \text{The cardinality of } S \text{ is denoted as hashtag } S \text{, but hashtags aren't allowed in git, so it's } C(S) \text{ instead.} $$

$$ (\exists (n) \cdot n \in ℕ ∩ (S = [k| k < n])) → C(S) = n $$

$$ C(S) = C(T) \iff \exists (f) \cdot f \text{ Is a mapping } ∩ f: S → T ∩ ∀(t) \cdot t \in T: \exists ! (s) \cdot f(s) = t $$

### mappings (again)

A definition that I thought of for mappings (that dosent imply a domain or codomain) uses a new thing to define axiomatioly (i.e. A thing that I have to define that it exists, and hasn't been seen before (e.g. How sets and extensions are not booleans)) (e.g. The $\text{N}$ in the Russell's paradox section): $→$ (Yes, another arrow (that makes $4$ (boolean arrow $→$, mapping arrow $→$, fancy functional arrow $↦$, and new arrow $→$))). I'll explain with an example: the function $x ↦ x^2$ would be denoted as the set containing $0 → 0$, $1 → 1$, $2 → 4$, $3 → 9$, $4 → 16$, $5 → 25$, and so on.

You can also define ordered sets as mappings from natural numbers greater than $0$ (or from all natural numbers if you want it to be confusing like in every single programming language exept fortran) (this is why I didn't use ordered lists last time, because, they are defined with mappings) (I gotta go ice skating now, bye!)
