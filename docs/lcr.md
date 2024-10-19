## coder's perspective

### Introduction

Let's start out with a function $I$ equal to $\lambda x. x$. If I plug in $1$ to this function, what do I get back? What is $I(1)$? Yeah, $I(1) = 1$, $I(2) = 2$, what about $I(I)$? Yeah, it's $I$.

So, the identity combinator takes in an input $x$, and returns an output, also $x$. So the identity of any $x$ is $x$, and as seen before, we can use functions as arguments, verbs are nouns and nouns are verbs, so the identity of identity is itself.

### What is this $\lambda$?

So, you might've seen this lambda stuff ($\lambda x. x$) earlier and wondered what it ment, so I'll break it down into small parts. Lambda ($\lambda$) is a signifier, a notation that I'm gonna use, to indicate that we're starting the definition of a function.

So we can read this as: we're starting to define a function ($\lambda$), that takes a single input ($x$), or parameter, and returns some expression, some body ($x$). This whole thing is called a lambda abstraction in the lambda calculus, but it just means that it's a unary (takes a single input) anonymous function

### What is The Lambda Calculus?

A purely functional programming language. It's called "calculus" because the term "calculus" just means a method of moving around symbols on a page, but instead of the calculus of the very small and the very large, it's the calculus of evaluating and defining functions.

### syntax

So in the lambda calculus, we have variables (which are kinda boring), we have expressions (applying a function to an argument), and we have lambda abstractions. In total, lambda terms are of the Backus-Naur Form:

$$ M, N ::= x \text{ } | \text{ } M(N) \text{ } | \text{ } \lambda x. M $$

I gotta go do kid stuff now.

It's been $20$ minutes.

Oh, right, there's also parens.

And that's the entire lambda calculus.

### examples/comparisons

Let's start with the Backus-Naur Form...

#### $x$

there's pretty much one thing to say about variables in the lambda calculus: they are immutable, they can not be changed after the fact, there's no concept of "assignment" per say, in the lambda calculus (there is binding, i.e. You can assign a variable to a value, but only once, it becomes a "bound variable"), if a variable is bound to a value, that's its value for now and forever more.

On the other hand, the Backus-Naur Form $M(N)$ is slightly more interesting

#### $M(N)$

In the lambda calculus, application is just a space, there's no parens for invocation. So, correction:

$$ M, N ::= x \text{ } | \text{ } M \text{ } N \text{ } | \text{ } \lambda x. M $$

This seems weird at first, but in reality, it ends up removing a lot of noise from our expressions.

| The Lambda Calculus | Code |
| ------------------- | ---- |
| $f$ $x$| `f(x)` |
| $f$ $x$ $y$ | `f(x)(y)`!! |

Now, I have to interrupt this to explain...

#### currying

In the lambda calculus, all functions are unary, this ($f$ $x$ $y$) is really a curried function, $f$ takes in $x$, and outputs a new function that takes in $y$. A classic example of a curried function is the curried addition function, `add(1)` is the add $1$ function, and if I apply it to $2$, I get $3$ (`add(1)(2) == 3`).

So $f$ $x$ $y$ can be read as $f$ first taking in an $x$, then a $y$, and if there were more inputs, they would also be fed in one by one from the left to the right.

### back to examples/comparisons

#### $M$ $N$

You could make $f$ $x$ $y$ more clear by saying $(f$ $x)$ $y$, but that dosen't do anything because application is left associative.

But you can use parens to force it to be evaluated in a different order. So $f$ $(x$ $y)$ is actually a different expression from $(f$ $x)$ $y$, it means first apply $x$ to $y$, then the result of that to $f$.

| The Lambda Calculus | Code        |
| ------------------- | ----------- |
| $f$ $x$             | `f(x)`      |
| $f$ $x$ $y$         | `f(x)(y)`   |
| $(f$ $x)$ $y$       | `(f(x))(y)` |
| $f$ $(x$ $y)$       | `f(x(y))`   |

On the third hand, let's look at the Backus-Naur Form...

#### $\lambda x. M$

Let's go from simple to complicated.

$$ \lambda a. b $$

(Or `a => b`.)

Takes in an input $a$, throws it away, and outputs whatever $b$ is.

$$ \lambda a. b \text{ } x $$

(Or `a => b(x)`.)

Takes in an input $a$, throws it away, and outputs whatever $b$ is, but applied to whatever $x$ is.

Footnote: the lambda abstraction swallows up as many things to the right as it can (use parens to stop the lambda term).


$100$ Lines!

$$ \lambda a. (b \text{ } x) $$

(Or `a => (b(x))`.)

But that's the same thing.

$$ (\lambda a. b) \text{ } x $$

(Or `(a => b)(x)`.)

Which is actually a different thing, it's the function that takes an input, throws it away, and outputs whatever $b$ is. That is, applied to $x$

$$ \lambda x. \lambda y. x $$

(Or `x => y => x`.)

This is an example of a curried function. In particular, it does the first of two things.

$$ \lambda x. (\lambda y. x) $$

(Or `x => (y => x)`.)

But that's the same thing.

| The Lambda Calculus         | JS              | py                        |
| --------------------------- | --------------- | ------------------------- |
| $\lambda a. b$              | `a => b`        | `lambda a: b`             |
| $\lambda a. b \text{ } x$   | `a => b(x)`     | `lambda a: b(x)`          |
| $\lambda a. (b \text{ } x)$ | `a => (b(x))`   | `lambda a: (b(x))`        |
| $(\lambda a. b) \text{ } x$ | `(a => b)(x)`   | `(lambda a: b)(x)`        |
| $\lambda x. \lambda y. x$   | `x => y => x`   | `lambda x: lambda y: x`   |
| $\lambda x. (\lambda y. x)$ | `x => (y => x)` | `lambda x: (lambda y: x)` |

### $\beta$-reduction and others

Beta reduction is literally just plugging arguments into functions.

$$ (\lambda a. a)(\lambda b. \lambda c. b)(x)(\lambda e. f) $$

Plugging the argument into the parameter, and replacing the parameter in the body

$$ (\lambda b. \lambda c. b)(x)(\lambda e. f) $$

Plugging the argument into the parameter, and replacing the parameter in the body

$$ (\lambda c. x)(\lambda e. f) $$

Plugging the argument into the parameter, and replacing the parameter in the body

$$ x $$

And now, it is in $\beta$-normal form (that is, it has no redexes (that is, a thing that can be reduced (that is, an application where the function part starts with a $\lambda$)))

All in an honest days work (I've added the entire page up to this point in one Oct. $15$'th)

There's also bound and free variables: bound ones are the ones that start out in between a $\lambda$ and a $.$ and free variables are the other ones.

There's also $\alpha$-equivalence: two things are alpha equivalent if they differ only in the name of a bound variable.

There's extensionally vs intentionally equal: extensionally equal means giving the same inputs gives the same outputs, and intentionally equal means the same formula.

You can abbreviate $\lambda x. \lambda y. \lambda z.$ as $\lambda xyz.$, which you can interpret as a ternary (takes three inputs) function, but don't be fooled, as every function in the lambda calculus is unary.

And finally, I know what you might be thinking: you keep using that word 'combinator', I don't think it means what you think it means. To that, I say: yes, I do know what it means, other than function in the lambda calculus, it means function that has no free variables. I'm gonna give some examples, and you try to figure out which ones are combinators.

$$ \lambda b. b $$

$$ \lambda b. a $$

$$ \lambda ab. a $$

$$ \lambda a. a \text{ } b $$

$$ \lambda abc. c(\lambda e. b) $$

First one: a combinator, nothing left undefined.

Second one: not a combinator, what is $a$?

Third one: a combinator, doesn't matter if $b$ isn't used.

Fourth one: not a combinator, what is $b$?

Fifth one: a combinator.

| Function                        | Combinator |
| ------------------------------- | ---------- |
| $\lambda b. b$                  | Yes        |
| $\lambda b. a$                  | No         |
| $\lambda ab. a$                 | Yes        |
| $\lambda a. a$ $b$              | No         |
| $\lambda abc. c$ $\lambda e. b$ | Yes        |

## formalism

Ok, to any mathematicians reading this (which is my general audience), you can stop holding your breath, I'm gonna rigorously define all of this.


$200$ Lines!

###  extensional vs. intensional view of functions

What is a function? Probably that "functions as graphs" thing: every function (call it $f$) has a fixed domain (call it $X$) and codomain (call it $Y$). We often say $f: X → Y$ to denote this (pronounced $f$ maps $X$ to $Y$). The function is a subset of $X \times Y$ (the set of all ordered pairs of size $2$ where the first term is in $X$ and the second in $Y$) such that if $x \in X$ there exists one and only one $y \in Y$ such that the ordered pair $(x, y) \in f$ (Side note! If both $X$ and $Y$ were the set of all real numbers, the ordered pair $(x, y)$ would not just look like a point, but would be the (well, at least, my) definition of a point. End of side note). Two functions $f, g: X → Y$ are considered equal if they are the same set, that is, giving the same inputs gives the same outputs, a.k.a. An extensional perspective.

Alternitavely, there's the "functions as rules" paradigm, commonlly used in the $19$th century: each function has a rule (e.g. the square function is a rule, and you can write this rule like $x^2 = x \cdot x$, or $^2 = x ↦ x \cdot x$). Yeah, that's it. But it is as intensional view.

Pop quiz/famous unsolved problem: are $x ↦ x$ and $y ↦ y$ intensionally equal?

In this notion, you don't need to know the exact domain and codomain of a function. e.g. $f(x) = x$ has domain and codomain $X$ for any set $X$.

In most of mathematics, the "functions as graphs" paradigm is the most elegant and appropriate way of dealing with functions. Graphs define a more general class of functions, because it includes functions that are not necessarily given by a rule.

On the other hand, in computer science, the “functions as rules” paradigm is often more appropriate. Think of a computer program as defining a function that maps input to output. Most computer programmers (and users) do not only care about the extensional behavior of a program (which inputs are mapped to which outputs), but also about how the output is calculated: How much time does it take? How much memory and disk space is used in the process? How much communication bandwidth is used? These are intensional questions having to do with the particular way in which a function was defined.

### The lambda calculus

... Is a method for defining functions as rules.

Time for arihmetic! Arithmetic expressions are made up from variables ($x$, $y$, $z$...), numbers ($1$, $2$, $3$,...), and operators ($+$, $-$, $\times$ etc.). An expression such as $x + y$ stands for the result of an addition (as opposed to an instruction to add, or the statement that something is being added). The great advantage of this language is that expressions can be nested without any need to mention the intermediate results explicitly (e.g. "$A = (x + y) \times z^2$" and not "let $w = x + y$, then let $u = z^2$, then let $A = w \times u$").

The lambda calculus extends the idea of an expression language to include functions. Where we normally write "Let $f$ be the function x ↦ x^2. Then consider A = f(5)", in the lambda calculus we just write $A = (x ↦ x^2)(5)$. But, because I want it to look more fancy, it is written $A = (\lambda x. x^2)(5)$. The expression $\lambda x. x^2$ stands for the function that maps $x$ to $x^2$ (as opposed to the statement that $x$ is being mapped to $x^2$). As in arithmetic, we use parentheses to group terms.

It is understood that the variable $x$ is a local variable in the term $\lambda x. x^2$. Thus, it does not make any difference if we write $\lambda y. y^2$ instead. A local variable is also called a bound variable.

One advantage of the lambda notation is that it allows us to easily talk about higher-order functions, i.e., functions whose inputs and/or outputs are themselves functions. An example is the operation $f ↦ f ∘ f$ in mathematics, which takes a function $f$ and maps it to $f ∘ f$, the composition of f with itself. In the lambda calculus, $f ∘ f$ is written as $\lambda x. f(f(x))$, and the operation that maps $f$ to $f ∘ f$ is written as $\lambda f. \lambda x. f(f(x))$.
