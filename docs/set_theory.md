## What even is a set?

A set is a well defined collection of objects, a set could contain the two shoes on you feet, or the $5$ pieces of cheese on this cutting board (that I'm going to pretend exists), sets can even contain other sets, but sets can not contain themselves, because it would lead to a paradox: would the set that contains every set that doesn't contain itself contain itself?" This also means that there isn't a set that contains everything.

But the thing is, using some symbols, you can describe almost all of math. These symbols can just be pronounced as words, and it would make a sentence, such as " $¬ \exists (x): |x| < 0$ " as " there does not exist $x$ such that the absolute value of $x$ is strictly less than $0$ ". Time to rapidfire through each one's pronunciation and meaning.

### meanings of things

$$ ∀ \text{ Is pronounced "for any" or "for all" (but I prefer "for any") and means what it says. It than has an open parentheses, a thing (or sometimes multiple things separated by a comma) (} x, y, z, \text{ or a set) that I will call } x \text{ for now, a closed parentheses (parenthese is not a word), a } \cdot \text{, a statement that implies something about } x \text{, a colon, and finish it off with a statement including } x. $$

$$ \text{left and right parentheses are not pronounced.} $$

$$ \cdot \text{ Is pronounced "such that" and it's only used in two contexts: "for any } x \text{ such that..." and "there exists } x \text{ such that...".} $$

$$ : \text{ Is pronounced however a colon is pronounced.} $$

$$ , \text{ Is pronounced however a comma is pronounced.} $$

$$ \exists \text{ Is pronounced "there exists" and I don't think I need to explain that.} $$

$$ ¬ \text{ Is pronounced "is not" or "does not" as in "there does not exist } x \text{".} $$

$$ \in \text{ Is pronounced "is an element of" where an element of a set is a singular object that is contained in that set.} $$

$$ x, y, \text{ And } z \text{ are pronounced "} x, y, \text{ And } z \text{" and they all mean "a thing that could be an element of a set".} $$

$$ \text{capital letters are sets.} $$

$$ \iff \text{ Is pronounced "if and only if" as in "if statement } a \text{ is true, statement } b \text{ is true, and if statement } a \text{ is false, statement } b \text{ is false".} $$

$$ ∩ \text{ Is pronounced "and" and means "} a ∩ b \text{ is true if and only if statement } a \text{ is true and } b \text{ is true", it can also mean the intersection of two sets, in that case, it is pronounced "intersectioned with", but I'll get to its formal meaning in the next chapter.} $$

$$ = : \text{ Is pronounced "equals by definition" and means "define the thing on the left as the thing on the right", or was it the other way around?} $$

$$ ∨ \text{ Is pronounced "or" and means "} a ∨ b \text{ is true if statement } a \text{ is true or } b \text{ is true... Or both!", it can also mean the union of two sets, in that case, it is pronounced "unioned with", but I'll get to its formal meaning in the next chapter.} $$

$$ \text{succ Is pronounced "the immediate successor of" and means "that number } + 1 \text{".} $$

$$ → \text{ Is technically called the if then sign, but it is pronounced "implies" and means "statement } a → b \text{ is true if statement } a \text{ being true implies statement } b \text{ is true", so } a → b \text{ is true if statement } a \text{ is true and statement } b \text{ is true, or if statement } a \text{ is false and statement } b \text{ is false, or if statement } a \text{ is true and statement } b \text{ is false, but not if statement } a \text{ is false and statement } b \text{ is true. Also, if there was an element sign two spaces behind, pronounce it "being an element of" as opposed to  "is an element of".} $$

$$ \text{I don't think that I need to explain the } < \text{sign.} $$

$$ ℝ \text{ Is pronounced "the set of all real numbers" and means, well, the set of all real numbers.} $$

$$ ℕ \text{ Is pronounced "the set of all natural numbers" and means "the set of all positive integers", it's debatable weather or not it includes } 0 \text{.} $$

### definitions

$$ Ø \text{ Is pronounced "the empty set" and means "the set of which is empty inside", but here that is in set theory:} $$

$$ ¬ \exists (x) \cdot x \in Ø $$

$$ ⊆ \text{ Is pronounced "is a subset of", and the meaning of that is:} $$

$$ A ⊆ B \iff ∀(x) \cdot x \in A: x \in B $$

$$ pow \text{ Is pronounced "the power set of" as in "} pow(S) \text{", and the meaning of that is:} $$

$$ ∀(P) \cdot ∀(U) \cdot U ⊆ S: U \in P ∩ ∀(T) \cdot T ¬ ⊆ S: T ¬ \in P: P = : pow(S) $$

$$ = \text{ Is pronounced "is the same as" or "is equal to", and the meaning of that is:} $$

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

$$ \in^S \text{ Is pronounced "is a super element of" (} S \text{ for super), and the definition is:} $$

$$ x \in^S S \iff x \in S ∨ \exists (U) \cdot U \in S ∩ x \in^S U $$

###### .

Was [recursion](https://silaspe.github.io/maths/set_theory.html#_1) in the rule book? I guess so.

[Recursion?](https://silaspe.github.io/maths/set_theory.html#_1) Get it?

### numbers

$$ 0 = Ø $$

$$ \text{succ} (n) \text{ (Which mathematically equals } n + 1 \text{) Is how you would usually define numbers, so I'll define numbers that way, I'll say that succ} (n) \text{ is the set that contains all numbers } 0 \text{-} n \text{. But first: the union of two sets, denoted as an } ∨ \text{ sign.} $$

$$ x \in A ∨ B \iff x \in A ∨ x \in B $$

$$ set \text{ Is pronounced "the set containing" as in "} set(S) \text{", and} $$

$$ ∀(S) \cdot E \in S ∩ ∀(T) \cdot T ¬= E: T ¬ \in S: S = : set(E) $$

$$ \text{Around } 100 \text{ lines?? (I might add or remove another definition, but at the time of typing this, this is on } 95 \text{ lines.)} $$

$$ \text{succ} (n) = : set(n) ∨ n $$

### back to definitions

$$ ∩ \text{ Is pronounced "and" and means "} a ∩ b \text{ is true if and only if statement } a \text{ is true and } b \text{ is true", it can also mean the intersection of two sets, in that case, it is pronounced "intersectioned with", but} $$

$$ x \in A ∩ B \iff x \in A ∩ x \in B $$

$$ \text{Here's another definition of the subset: } ∀(A, B) \cdot ¬ \exists (x) \cdot x \in A ¬ → x \in B: A ⊆ B. $$

$$ \text{And another one! } A ⊆ B \iff ¬ \exists (x) \cdot x \in A ∩ x ¬ \in B $$

$$ n_1 < n_2 \iff n_1 \in n_2 $$

$$ \text{WARNING! The next statement is the axiom of choice, kinda controversial.} $$

$$ ∀(S) \cdot S ¬= Ø: \exists (x) \cdot x \in S $$

### group theory

A group (call it $G$) is a certain type of set, including an addition like thing represented with a $+$ sign (this addition like thing could also be multiplication), let's start with the set of numbers $0$ - $4$ under [modular](https://silaspe.github.io/maths/mod.html) addition. To be a group, it has to follow $4$ different rules.

$$ 1 \text{, Closure} $$

$$ ∀(a, b) \cdot a \in G ∩ b \in G: a + b \in G $$

Because it is modular, this holds true for modular addition.

$$ 2 \text{, Associativity} $$

$$ ∀(a, b, c) \cdot a \in G ∩ b \in G ∩ c \in G: (a + b) + c = a + (b + c) $$

Because addition is associative, this holds true for modular addition.

$$ 3 \text{, Identity} $$

$$ \exists (e) \cdot e \in G ∩ ∀(a) \cdot a \in G: a + e = a ∩ ∀(b) \cdot b \in G: e + b = b $$

Because of $0$, this holds true for modular addition.

$$ 4 \text{, Inverses} $$

$$ ∀(a) \cdot a \in G: \exists (b) \cdot b \in G ∩ a + b = e ∩ b + a = e $$

Because of negatives and them looping back around, this holds true for modular addition. (Also, modular multiplication almost works, but it fails at this step because there is no $\frac{1}{0}$.)

Thus, the set of numbers $0$ - $4$ under modular addition is a group.

#### limits

$$ \lim_{n \to \infty} f(n) = x \iff ∀(y) \cdot y \in ℝ ∩ y \ne x: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: |f(k) - x| < |f(k) - y| $$

$$ \lim_{n \to \infty} f(n) \to \infty \iff ∀(y) \cdot y \in ℝ: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: f(k) > y $$

$$ \lim_{n \to \infty} f(n) \to -\infty \iff ∀(y) \cdot y \in ℝ: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: f(k) < y $$

$$ \lim_{n \to \infty} f(n) = 0 \iff ∀(y) \cdot y \in ℝ ∩ y \ne 0: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: |f(k)| < |y| $$

$$ \lim_{n \to \infty} f(n) = x^{+} \iff ∀(y) \cdot y \in ℝ ∩ y \ne x: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: |f(k) - x| < |f(k) - y| ∩ f(k) > x $$

$$ \lim_{n \to \infty} f(n) = x^{-} \iff ∀(y) \cdot y \in ℝ ∩ y \ne x: \exists (n) \cdot n \in ℕ ∩ ∀(k) \cdot k \in ℕ ∩ k ≥ n: |f(k) - x| < |f(k) - y| ∩ f(k) < x $$

### set theory proofs?

No.
