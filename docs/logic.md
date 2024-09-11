This page dosen't require seeing the set theory page, but you can see it anyways.

The idea behind this page is that you can derive all of set theory from logic, so $\text{T}$ is true, and $\text{F}$ is false.

Tools: $\text{T}$, $\text{F}, $=*$, and another thing that will be defined later.

*Returns true if the two things are the same, and false if they are not.

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

$$ \text{E} (x; p(x)) = \text{ The extention of } p(x) \text{ (and the secret } 4 \text{th tool), the set of all } x \text{ such that } p(x) \text{ (is true), and this is how I'm going to define sets. This function } p(x) \text{ inputs, well, anything, and outputs a boolean (true or false) (e.g. is } x \text{ an odd number?).} $$

$$ \text{The extention of that particular function is the set of all odd numbers.} $$

You can also derive the membership or element sign like this:

$$ x \in \text{E} (y; p(y)) \iff p(x) \text{ (} = \text{T)} $$

which goes somewhere in between not and and in the order of operations.

And just for fun, I'll also derive the for any and there exists signs like this:

$$ \text{I'll start with the general form for the for any sign: } ∀(x) \cdot p(x) \text{ (} = \text{T)}: q(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } p(x) → q(x) $$

$$ \text{I think that you can see why I won't be using this one.} $$

$$ \text{And the general form for the there exists sign: } \exists (x) \cdot p(x) \text{ (} = \text{T)} $$

$$ \text{And that example in logic: } ¬(p(x) = \text{F}) $$

$$ \text{Maybe I'll use it.} $$

Next stop: numbers!

$$ 0 = Ø = \text{E} (x; \text{F}) $$

$$ \text{succ} (x) = \text{E} (y; y = x) $$

$$ \text{succ} (0) = 1 $$

$$ \text{succ} (1) = 2 $$

$$ \text{succ} (2) = 3 $$

$$ 0 \in ℕ $$

$$ x \in ℕ → \text{succ} (x) \in ℕ $$

$$ ℕ = \text{E} (x; (x = 0) ∨ \exists (y) \cdot (\text{succ} (y) = x) ∩ y \in ℕ) = \text{E} (x; (x = 0) ∨ ¬(((\text{succ} (y) = x) ∩ y \in ℕ) = \text{F})) $$

Next stop: Russell's paradox!

$$ R = \text{E} (x; ¬(x \in x)) $$

$$ \text{Now, the question is, is } R \in R \text{? Because if } ¬(R \in R) \text{, than } ¬(x \in x) \text{ would be true (for } x \text{ equal to } R \text{), but then, } R \text{ would be an element of } R \text{, but if } R \in R \text{, than } ¬(x \in x) \text{ would be false (for } x \text{ equal to } R \text{), but then, } R \text{ wouldn't be an element of } R \text{, paradox!)} $$


$100$ Lines.

$$ x \in \text{E} (y; p(y)) = \text{N (} \ne ℕ \text{)} \iff (¬(x \in \text{E} (y; p(y))) → p(x) = \text{T}) ∩ ((x \in \text{E} (y; p(y))) → p(x) = \text{F}) $$

$$ R \in R = \text{N} $$

Now, I'll define an infinate set of things $x1, x2, x3, x4, x5,...$ that are all in $\text{E} (x; \text{T}) $$

Next stop: arithmetic!
