## What even is a set?

A set is a well defined collection of objects, a set could contain the two shoes on you feet, or the $5$ peices of chese on this cutting board (that I'm going to pretend exists), sets can even contain other sets, but sets can not contain themselfes, because tis would lead to a paradox: would the set that contains every set that dosen't contain itsef contain itself?" this also means that there isn't a set that contains everything.

But the thing is, using some symbols, you can describe almost all of math. These symbols can just be pronounced as words, and it would make a sentence, such as " $¬ \exists (x): |x| < 0$ " as " there does not exist $x$ such that the absolute value of $x$ is strictly less than $0$ ". Time to rapidfire through each one's pronunciation and meaning.} $$

### definitions

$$ ∀ \text{ Is pronounced "for any" or "for all" (but I prefer "for any") and means what it says. It than has an open parentheses, a thing (} x, y, z, \text{ or a set) that I will call } x \text{ for now, a closed parentheses (parenthese is not a word), a } \cdot \text{, a statement that implies something about } x \text{, a colon, and finish it off with a statement including } x. $$

$$ ( \text{ and } ) \text{ are not pronounced.} $$

$$ \cdot \text{ Is pronounced "such that" and it's only used in two contexts: "for any } x \text{ such that..." and "there exists } x \text{ such that...".} $$

$$ : \text{ Is pronounced however a colon is pronounced.} $$

$$ \exists \text{ Is pronounced "there exists" and I don't think I need to explain that.} $$

$$ ¬ \text{ Is pronounced "is not" or "does not" as in "there does not exist } x \text{".} $$

$$ \in \text{ Is pronounced "is an element of" where an element of a set is a singular object that is contained in that set.} $$

$$ Ø \text{ Is pronounced "the empty set" and means "the set of which is empty inside".} $$

$$ x, y, \text{ And } z \text{ are pronounced "} x, y, \text{ And } z \text{" and they all mean "a thing that could  be an element of a set".} $$

$$ ⊆ \text{ Is pronounced "is a subset of" and I'll get to the meaning of that in the next chapter.} $$

$$ \text{capital letters are sets.} $$

$$ \iff \text{ Is pronounced "if and only if" as in "if statement } a \text{ is true, statement } b \text{ is true, and if statement } a \text{ is false, statement } b \text{ is false".} $$

$$ pow \text{ Is pronounced "the power set of" as in "} pow(S) \text{" and I'll get to the meaning in the next chapter.} $$

$$ ∩ \text{ Is pronounced "and" and means "} a ∩ b \text{ is true if and only if statement } a \text{ is true and } b \text{ is true", it can also mean the intersection of two sets, in that case, it is pronounced "intersectioned with", but I'll get to it's formal meaning in the next next next chapter..} $$

$$ = : \text{ Is pronounced "equals by definition" and means "define the thing on the left as the thing on the right", or was it the other wat around?} $$

$$ = \text{ Is pronounced "is the same as" and I'll get to it's formal meaning in the next chapter.} $$

$$ \in^S \text{ Is pronounced "is a super element of" (} S \text{ for super) and I'll get to it's meaning in the next chapter.} $$

$$ ∨ \text{ Is pronounced "or" and means "} a ∨ b \text{ is true if statement } a \text{ is true or } b \text{ is true... Or both!", it can also mean the union of two sets, in that case, it is pronounced "unioned with", but I'll get to it's formal meaning in the next chapter.} $$

$$ \text{succ Is pronounced "the immediate successor of" and means "that number } + 1 \text{".} $$

$$ set \text{ Is pronounced "the set containing" as in "} set(S) \text{" and I'll get to it's formal meaning in the next chapter.} $$

### definitions from those definitions

$$ ¬ \exists (x) \cdot x \in Ø $$

$$ A ⊆ B \iff ∀(x) \cdot x \in A: x \in B $$

$$ ∀(P) \cdot ∀(U) \cdot U ⊆ S: U \in P ∩ ∀(T) \cdot T ¬ ⊆ S: T ¬ \in P: P = : pow(S) $$

$$ A = B \iff A ⊆ B ∩ B ⊆ A $$

$$ ¬ \exists (S) \cdot S \in S $$

$$ x \in \in S \iff \exists (U) \cdot U \in S ∩ x \in U $$

$$ x \in \in S \text{ can also be written as } \in^2 $$

$$ x \in \in \in S \iff \exists (U) \cdot U \in S ∩ x \in^2 U $$

$$ x \in \in \in S \text{ can also be written as } \in^3 $$

$$ x \in \in \in \in S \iff \exists (U) \cdot U \in S ∩ x \in^3 U $$

$$ x \in \in \in \in S \text{ can also be written as } \in^4 $$

$$ \vdots $$

$$ x \in^{a + b} S \iff \exists (U) \cdot U \in^a S ∩ x \in^b U $$

$$ x \in^{a + b} S \text{ can also be written as } x \in^a \in^b S $$

$$ x \in^S S \iff x \in S ∨ \exists (U) \cdot U \in S ∩ x \in^S U $$

###### .

Was [recursion](https://silaspe.github.io/maths/set_theory.html#_1) in the rule book? I guess so.

### numbers

$$ 0 = Ø $$

$$ \text{succ} (n) \text{ (Which mathematicly equals } n + 1 \text{) Is how you would usually define numbers, so I'll define numbers that way, I'll say that succ} (n) \text{ is the set that contains all numbers } 0 \text{-} n \text{. But first: the union of two sets, denoted as an } ∨ \text{ sign.} $$

$$ x \in A ∨ B \iff x \in A ∨ x \in B $$

$$ ∀(S) \cdot E \in S ∩ ∀(T) \cdot T ¬ = E: T ¬ \in S: S = : set(E) $$

$$ \text{Around } 100 \text{ lines?? (I might add another definition, but at the time of typing this, this is on } 95 \text{ lines.)} $$

$$ \text{succ} (n) = : set(n) ∨ n $$

### back to definitions from those definitions

$$ x \in A ∩ B \iff x \in A ∩ x \in B $$

### set theory proofs?

no.
