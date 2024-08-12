Ok, so, lambda calculus, I'll be following along with [the first part](https://www.youtube.com/watch?v=3VQ382QG-y4), at least for now, and I haven't seen this in a year, so we'll be reacting to it together.

### Chapter $1$: Introduction

Ok, so, it looks like he's starting off with a function (written as $I$) that he calls "the identity". Now, what do you think $I(1)$ is? * Man in the backround says " same value! "*, and that is correct, $I(1) = 1$, $I(2) = 2$, what about $I(I)$? * No one awnsers*, yeah, it's $I$. (By the way, functions in lambda calculus are also called "combinators", each one has a function name (e.g. $I$), a more descriptive function name (e.g. identity), and an alias (which is always a bird for some reason) (e.g. Idiot bird.)) (Also by the way, I'll be copying what he's saying for the rest of this page, and putting my thoughts in between parenthases.) And then he uses some fancy notation " $\lambda a. a$ ". It takes in ($\lambda$) a value ($a$), and outputs ($.$) that same value ($a$). So, $I(x) = x$ for any $x$. As you saw, you can use functions as arguments (which is why they are called "combinators". Also, to me, this is the heart of lambda calculus), verbs are nouns and nouns are verbs. 

#### chapter $2$: What is this $\lambda$?

Ok, so, what was this $\lambda$ stuff from earlier? (Finally he explains it.) So, lambda is a signafier, it's a way to indicate that we are starting the definition of a function. So, we can read this (this $\lambda a. a$) as: we're starting the definition of a function ($\lambda$), which takes a single input ($a$), or parameter (The $.$ signafies that we are no longer writing down the parameters, and now), and returns some expression ($a$). This whole thing is called a lambda abstraction in lambda calculus.

### chapter $3$: What is Lambda Calculus?

Lambda calculus is a really tiny symbol manipulation framework, a calculus is just a way of moving around symbols on a page (I actually didn't know that), the subject that you may have learnd in school called "calculus" is a specific calculus for things like differentials and integrals and stuff like that, derivatives. But this calculus is about something else, this calculus is about evaluating and defining functions.

### chapter $4$: I'm tired of this, here's a crash course on lambda calculus.

Functions (aka combinators) act on other functions, each one has a single letter abbreviation, and an alias. For the $2$ example functions, they are written " $M$ " and " $K$ ", and called "The Mockingbird" and "The Kestrel". Now, how it's defined in lambda calculus is " $M = : \lambda a. a a$ " and " $K = : \lambda x. \lambda y. x$ ". Now, this is where it starts to get complicated (that's a family meme). First, there's a $\lambda$ (aka lambda), which means: defining inputs (functions). Then, it defines an input ($a$), then, there's a $.$, which means: stop defining inputs. (Right here in the other one, there's another $\lambda$, so, define inputs again.) Then, there's an $a a$ (which is actually $a(a)$, it's just auto-parenthesized). The $a$ being a function is explaind by when I said "inputs (functions)", but then, there's another question: why is $a$ also an input? One or the other, right? Well, no, it is explaind by when I said "Functions act on other functions". Putting it all together, The Mockingbird function takes in one input, and evaluates it on itself, and The Kestrel takes in two inputs, and just does the first one.

### chapter $5$: Big numbers and Transfinite ordinals

This chapter dosen't have much lambda calculus, it's just what I have been doing for the past week. [This](https://www.youtube.com/watch?v=b-Bb_TyhC1A&t=1449s), [this](https://www.youtube.com/watch?v=Mzgw6zMtipQ&t=465s), and [this](https://www.youtube.com/watch?v=0X9DYRLmTNY&t=486s) were my only evinence (in that order) (you should watch them anyways, they're really cool videos), I knew enough about the fast-growing hierachies, but very little about the infinite ordinals.

$$ f_0 (x) = : x + 1 $$

$$ f_{n + 1} (x) = : f_n(f_n(f_n(...(f_n(x)))))... = f_n^x(x) $$

$$ f_1 (x) = 2x $$

$$ f_2 (x) = x \cdot 2^x $$

$$ f_3 (3) > 10^{100} \times \text{The american national debt.} $$

$$ f_\omega (x) = : f_x (x) \text{} $$

$$ \text{Yes, that omega is a transfinite ordinal, but there's nothing infinate about it, it just grows faster than any finite number would (e.g. } f_{1000} (x) < f_\omega (x) \text{ because for all } x > 1000 \text{, the subscript would be bigger, thus it would grow faster), it's just notational shorthand, because if the input is really long to write, you would have to write it twice. But there is a connection between transfinite ordinals and these functions (which have a connection to big numbers, hence the name: Big numbers and Transfinite ordinals) that I will explain after I get to the largest ordinal that I know.} $$

$$ \text{For ordinals, there are three rules, } 1 \text{: you start with omega (} \omega \text{), } 2 \text{: you can add } 1 \text{, } 3 \text{: you can repeat 'til infinity*} $$

$$ \text{*only an infinity that you have already reached} $$

$$ \omega $$

$$ \omega + 1 $$

$$ \omega + 2 $$

$$ \omega + 3 $$

$$ \vdots $$

$$ \omega + \omega $$

$$ 2 \omega $$

$$ 2 \omega + 1 $$

$$ 2 \omega + 2 $$

$$ 2 \omega + 3 $$

$$ \vdots $$

$$ 2 \omega + \omega $$

$$ 3 \omega $$

$$ \vdots $$

$$ \omega \omega $$

$$ \omega^2 $$

$$ \omega^\omega $$

$$ \omega^{\omega^\omega} $$

$$ \omega^{\omega^{\omega^{\omega^{.^{.^.}}}}} = : \epsilon_0 = \text{}^\omega \omega $$

$$ \text{Where }^y x \text{ is pronounced "} x \text{ tetrated to } y \text{" and equals } x^{x^{x^{x^{.^{.^.}}}}} y \text{ times. (Also, it's parenthesized from the right to the left.)} $$

$$ \text{Also, } \epsilon_0 = \omega^{\epsilon_0} \text{, so } \epsilon_0 \text{ is a "fixed point" of } \omega \text{.} $$

$$ \epsilon_{n + 1} = : \epsilon_n^{\epsilon_n^{\epsilon_n^{\epsilon_n^{.^{.^.}}}}} $$

$$ \epsilon_\omega $$

$$ \epsilon_{\epsilon_0} $$

$$ \epsilon_{\epsilon_{\epsilon_{\epsilon_\ddots}}} = : \zeta_0 $$

$$ \text{IMPORTANT! This is only } \zeta_0 \text{ because at the end of that tower* of epsilons, there is a } 0 \text{.} $$

$$ \text{*The term "tower" is exclusive to exponents, the term for subscripts is "dungeon".} $$

$$ \zeta_n^{\zeta_n^{\zeta_n^{\zeta_n^{.^{.^.}}}}} = : \epsilon_{\zeta_n + 1} $$

$$ \zeta_{n + 1} = : \epsilon_{\epsilon_{\epsilon_{\epsilon_\ddots}}} \text{ Where the final epsilon is an } \epsilon_{\zeta_n + 1} \text{.} $$


$100$ lines.

$$ \zeta_\omega $$

$$ \zeta_{\epsilon_0} $$

$$ \zeta_{\zeta_0} $$

$$ \zeta_{\zeta_{\zeta_{\zeta_\ddots}}} = : \eta_0 = : \varphi_3 (0) $$

#### chapter $6$: THE VEBLEN HIERARCHY

First, if there's any confusion, the veblen hierarchey is this $\varphi$ thing.

$$ \varphi_0 (\alpha) = : \omega^\alpha $$

$$ \varphi_1 (\alpha) = : \epsilon_\alpha $$

$$ \varphi_2 (\alpha) = : \zeta_\alpha $$

$$ \varphi_3 (\alpha) = : \eta_\alpha $$

$$ \varphi_\omega (0) = \varphi_{\varphi_0 (1)} (0) $$

$$ \varphi_{\varphi_{\varphi_0 (1)} (0)} (0) $$

$$ \varphi_{\varphi_{\varphi_{\varphi_\ddots (0)} (0)} (0)} (0) = : \Gamma_0 = \varphi_{\Gamma_0} (0) $$

$$ \text{Ok, here's the connection: Let's say that we want to turn an infinate ordinal (} \epsilon_0 \text{) into a function. First, the function will be } f_{\epsilon_0} (x) \text{, but for even more notational shorthand, it is written } \epsilon_0 (x) \text{. But here's how it's defined: step } 1 \text{: write the ordinal in terms of omega (so }^\omega \omega \text{), maybe easier said that done, step } 2 \text{: replace every omega with an } x \text{ (so, }^x x \text{), step } 3 \text{: make it a subscript for } f \text{ and evaluate it on } x \text{ (so } f_{^x x} (x) \text{).} $$

Now, you can go over to [my repo](https://silaspe.github.io/maths/actual_repo.html#big-numbers-and-transfinite-ordinals) to see how to do it in python.

#### logic

Feel free to skip this part if you just want to see the big number in lambda calculus.

$$ K = \text{Kestrel} = \lambda x. \lambda y. x = : \text{True} = \text{T} $$

$$ Ki = \text{Kite} = \lambda x. \lambda y. y = : \text{False} = \text{F} $$

$$ \text{And} = : \lambda pq. p(q(\text{T}, \text{F}), q(\text{F}, \text{F})) = \lambda pq. p(q, \text{F}) = \lambda pq. p(q, p) $$

$$ \text{And} = \lambda pq. p q p $$

$$ \text{Or} = : \lambda pq. p(q(\text{T}, \text{T}), q(\text{T}, F)) = \lambda pq. p(\text{T}, q) = \lambda pq. p(p, q) $$

$$ \text{Or} = \lambda pq. p p q $$

$$ \text{Not} = : \lambda p. p(\text{F}, \text{T}) $$

$$ \text{Not} = \lambda p. p \text{F} \text{T} $$

### chapter $7$: currying operations, numbers, operations, groupings, subtraction, and the biggest (codable) number

$$ \text{First: currying. How I think of it is like this (this entire next line):} $$

$$ \text{A function can have as many (or as few) inputs as possible. If the function is, say, The Kestrel (} 2 \text{ inputs), you can easily define the } 2 \text{ input version, and the no input version would just always return itself. Three is harder, but doable, and everything bigger has the same idea (one of two ideas both refered to as currying), it requires the first half of currying: } f(a, b) \text{ for single input function } f \text{ is equal to } f(a)(b) \text{. But for } 1 \text{ input, it is much harder. New function: addition (yes, number addition) (specificly the } 2 \text{ input one). If you only give it } 1 \text{ input (} 1 \text{ for example), you get the add } 1 \text{ function. So that's the second rule of currying!} $$

$$ \text{So basicly, currying is when you give a function the incorrect amount of inputs, and it either waits for more, or evaluates the function on the next input.} $$

$$ \text{you can also combine these to get } f(a, b) = f(a)(b) \text{ for } 2 \text{ inpt function } f \text{, making the comma redundant.} $$

$$ \text{Next: numbers (church numerals).} $$

$$ n0 = \lambda f. \lambda x. x \text{ } ( = \text{False}) $$

$$ n1 = \lambda f. \lambda x. f x $$

$$ n2 = \lambda f. \lambda x. f(f x) $$

$$ n3 = \lambda f. \lambda x. f(f(f x)) $$

$$ \text{So, } 1 \text{ equals once, } 2 \text{ equals twice, } 3 \text{ equals thrice, and so on.} $$

$$ \text{Next: successor!} $$

$$ \text{Successor} (n2) = n3 $$

$$ \text{Successor} (f(f x)) = f(f(f x)) $$

$$ \text{Successor} (n) = f(n) $$

$$ Succ = \lambda n. \lambda f. \lambda x. f(n(f, x)) $$

$$ Succ = \lambda n. \lambda f. \lambda x. f(n f x) $$
