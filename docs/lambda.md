Ok, so, lambda calculus, I'll be following along with [the first part](https://www.youtube.com/watch?v=3VQ382QG-y4), at least for now, and I haven't seen this in a year, so we'll be reacting to it together.

### Chapter $1$: Introduction

Ok, so, it looks like he's starting off with a function (written as $I$) that he calls "the identity". Now, what do you think $I(1)$ is? * Man in the backround says " same value! "*, and that is correct, $I(1) = 1$, $I(2) = 2$, what about $I(I)$? * No one awnsers*, yeah, it's $I$. (By the way, functions in lambda calculus are also called "combinators", each one has a function name (e.g. $I$), a more descriptive function name (e.g. identity), and an alias (which is always a bird for some reason) (e.g. Idiot bird.)) (Also by the way, I'll be copying what he's saying for the rest of this page, and putting my thoughts in between parenthases.) And then he uses some fancy notation " $\lambda a. a$ ". It takes in ($\lambda$) a value ($a$), and outputs ($.$) that same value ($a$). So, $I(x) = x$ for any $x$. As you saw, you can use functions as arguments (which is why they are called "combinators". Also, to me, this is the heart of lambda calculus), erbs are nouns and nouns are erbs. 

#### chapter $2$: What is this $\lambda$?

Ok, so, what was this $\lambda$ stuff from earlier? (Finally he explains it.) So, lambda is a signafier, it's a way to indicate that we are starting the definition of a function. So, we can read this (this $\lambda a. a$) as: we're starting the definition of a function ($\lambda$), which takes a single input ($a$), or parameter (The $.$ signafies that we are no longer writing down the parameters, and now), and returns some expression ($a$). This whole thing is called a lambda abstraction in lambda calculus.

### chapter $3$: What is Lambda Calculus?

Lambda calculus is a really tiny symbol manipulation framework, a calculus is just a way of moving around symbols on a page (I actually didn't know that), the subject that you may have learnd in school called "calculus" is a specific calculus for things like differentials and integrals and stuff like that, derivatives. But this calculus is about something else, this calculus is about evaluating and defining functions.

### chapter $4$: I'm tired of this, here's a crash course on lambda calculus.

Functions (aka combinators) act on other functions, each one has a single letter abbreviation, and an alias. For the $2$ example functions, they are written " $M$ " and " $K$ ", and called "The Mockingbird" and "The Kestrel". Now, how it's defined in lambda calculus is " $M = : \lambda a. aa$ " and " $K = : \lambda x. \lambda y. x$ ". Now, this is where it starts to get complicated (that's a family meme). First, there's a $\lambda$ (aka lambda), which means: defining inputs (functions). Then, it defines an input ($a$), then, there's a $.$, which means: stop defining inputs. (Right here in the other one, there's another $\lambda$, so, define inputs again.) Then, there's an $aa$ (which is actually $a(a)$, it's just auto-parenthesized). The $a$ being a function is explaind by when I said "inputs (functions)", but then, there's another question: why is $a$ also an input? One or the other, right? Well, no, it is explaind by when I said "Functions act on other functions". Putting it all together, The Mockingbird function takes in one input, and evaluates it on itself, and The Kestrel takes in two inputs, and just does the first one.

### chapter $5$: Big numbers and Transfinite ordinals

This chapter dosen't have much lambda calculus, it's just what I have been doing for the past week. [This](https://www.youtube.com/watch?v=b-Bb_TyhC1A&t=1449s), [this](https://www.youtube.com/watch?v=Mzgw6zMtipQ&t=465s), and [this](https://www.youtube.com/watch?v=0X9DYRLmTNY&t=486s) were my only evinence (in that order) (you should watch them anyways, they're really cool videos), I knew enough about the fast-growing hierachies, but very little about the infinite ordinals.

Also, that second video had a preatty cool premise of "biggest textible number" (the video went into more detail on that), so I'm gonna steal it.

$$ f_0 (x) = : x + 1 $$

$$ f_{n + 1} (x) = : f_n(f_n(f_n(...(f_n(x)))))... = f_n^x(x) $$

$$ f_1 (x) = 2x $$

$$ f_2 (x) = x \cdot 2^x $$

$$ f_3 (3) > 10^{100} \times \text{The american national debt.} $$

$$ f_\omega (x) = : f_x (x) $$

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


$100$ lines.

$$ \zeta_{n + 1} = : \epsilon_{\epsilon_{\epsilon_{\epsilon_\ddots}}} \text{ Where the final epsilon is an } \epsilon_{\zeta_n + 1} \text{.} $$

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

$2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ Lines!

$$ \varphi_{\varphi_{\varphi_{\varphi_\ddots (0)} (0)} (0)} (0) = : \Gamma_0 = \varphi_{\Gamma_0} (0) $$

$$ \text{Ok, here's the connection: Let's say that we want to turn an infinate ordinal (} \epsilon_0 \text{) into a function. First, the function will be } f_{\epsilon_0} (x) \text{, but for even more notational shorthand, it is written } \epsilon_0 (x) \text{. But here's how it's defined: step } 1 \text{: write the ordinal in terms of omega (so }^\omega \omega \text{), maybe easier said that done, step } 2 \text{: replace every omega with an } x \text{ (so, }^x x \text{), step } 3 \text{: make it a subscript for } f \text{ and evaluate it on } x \text{ (so } f_{^x x} (x) \text{).} $$

Now, you can go over to [my repo](https://silaspe.github.io/maths/actual_repo.html#big-numbers-and-transfinite-ordinals) to see how to do it in python.

#### logic

Feel free to skip this part if you just want to see the big number in lambda calculus.

$$ K = \text{Kestrel} = \lambda x. \lambda y. x = : \text{True} = \text{T} $$

$$ Ki = \text{Kite} = \lambda x. \lambda y. y = : \text{False} = \text{F} $$

$$ \text{And} = : \lambda pq. p(q(\text{T}, \text{F}), q(\text{F}, \text{F})) = \lambda pq. p(q, \text{F}) = \lambda pq. p(q, p) $$

$$ \text{And} = \lambda pq. pqp $$

$$ \text{Or} = : \lambda pq. p(q(\text{T}, \text{T}), q(\text{T}, F)) = \lambda pq. p(\text{T}, q) = \lambda pq. p(p, q) $$

$$ \text{Or} = \lambda pq. ppq $$

$$ \text{Not} = : \lambda p. p(\text{F}, \text{T}) $$

$$ \text{Not} = \lambda p. p \text{F} \text{T} $$

### chapter $7$: currying operations, numbers, arithmetic operations, groupings, subtraction, is $0$, inequalities, equalities, and the biggest (codable) number

$$ \text{By the way, everything else that I had learned (other than this page's main plot of the biggest (codable) number) while writing this (currying operations, arithmetic operations, groupings, and subtraction) (that I learned via actually watching through the videos) was going to be in a post credit scene, but they were actually required for the code (e.g. I nedded an exponent function for the `for i in range(x - 1): result = x ** result` on lines $4$ - $5$ of the epsilon subscript function).} $$

$$ \text{First: currying. How I think of it is like this (this entire next line):} $$

$$ \text{A function can have as many (or as few) inputs as possible. If the function is, say, The Kestrel (} 2 \text{ inputs), you can easily define the } 2 \text{ input version, and the no input version would just always return itself. Three is harder, but doable, and everything bigger has the same idea (one of two ideas both refered to as currying), it requires the first half of currying: } f(a, b) \text{ for single input function } f \text{ is equal to } (f(a))(b) \text{. But for } 1 \text{ input, it is much harder. New function: addition (yes, number addition) (specificly the } 2 \text{ input one). If you only give it } 1 \text{ input (} 1 \text{ for example), you get the add } 1 \text{ function. So that's the second rule of currying!} $$

$$ \text{So basicly, currying is when you give a function the incorrect amount of inputs, and it either waits for more, or evaluates the function on the next input.} $$

$$ \text{you can also combine these to get } f(a, b) = f(a)(b) \text{ for } 2 \text{ input function } f \text{, making the comma redundant.} $$

$$ \text{Next: numbers (church numerals).} $$

$$ n0 = \lambda f. \lambda x. x \text{ } ( = \text{False}) $$

$$ n1 = \lambda f. \lambda x. f x $$

$$ n2 = \lambda f. \lambda x. f(f x) $$

$$ n3 = \lambda f. \lambda x. f(f(f x)) $$

$$ \text{So, } 1 \text{ equals once, } 2 \text{ equals twice, } 3 \text{ equals thrice, } 4 \text{ equals fourfold, and so on.} $$

$$ \text{Next: successor!} $$

$$ \text{Successor} (n2) = n3 $$

$$ \text{Successor} (f(f x)) = f(f(f x)) $$

$$ \text{Successor} (n) = f(n) $$

$$ Succ = \lambda nfx. f(n(f, x)) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Succ = \lambda nfx. f(nfx) $$

$$ \text{Next: addition!} $$

$$ \text{Addition} (n2, n3) = n5 $$

$$ \text{Addition} (2, 3) = 2 + 1 + 1 + 1 = 3( + 1, 2) $$

$200$ Lines.

$$ Add = \lambda nk. n(Succ, k) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Add = \lambda nk. n \text{ } Succ \text{ } k $$

$$ \text{Next: NOT subtraction, multiplication instead!} $$

$$ \text{because subtraction is so hard, it's going into it's own subchapter.} $$

$$ Mult \text{ } n2 \text{ } n3 = n6 $$

$$ \text{Before I expand that, I would like to say that } f f f f f f x \text{ is interpreted as } f(f, f, f, f, f, x) \text{, because of currying, so I'll say that } (f ∘ f ∘ f ∘ f ∘ f ∘ f) x \text{ is equal to } f(f(f(f(f(f x))))) \text{.} $$

$$ Mult \text{ } n2 \text{ } n3 \text{ } f \text{ } x = (f ∘ f ∘ f ∘ f ∘ f ∘ f) (x) $$

$$ \text{By the way, that's a curried function on the left.} $$

$$ \text{But, compasition is associative (Which is a word that he used } 6 \text{ times) (a function like } + \text{ is associative if and only if } a + (b + c) = (a + b) + c \text{), so you can write it like this:} $$

$$ Mult \text{ } n2 \text{ } n3 \text{ } f \text{ } x = ((f ∘ f ∘ f) ∘ (f ∘ f ∘ f)) (x) $$

$$ \text{you can kinda replace the } f ∘ f ∘ f \text{ with an } n3(f) \text{, but be careful, it's a curried function, so it will wait for an input, and then do } (f ∘ f ∘ f) (x) \text{. But the function is kinda already waiting for an input, so} $$

$$ Mult \text{ } n2 \text{ } n3 \text{ } f \text{ } x = ((n3(f)) ∘ (n3(f)) (x) $$

$$ \text{And we can use the same trick now to get} $$

$$ Mult \text{ } n2 \text{ } n3 \text{ } f \text{ } x = n2(n3(f)) (x) $$

$$ \text{But, because it's a curried function on the left, the } x \text{ on the right, and the fact that if } f(x) = g(x) \text{, than } f = g \text{, I can say that} $$

$$ Mult \text{ } n2 \text{ } n3 \text{ } f = n2(n3(f)) $$

$$ Mult = \lambda nkf. n(k(f)) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Mult = \lambda nkf. n(kf) $$

$$ \text{Now, I'm just gonna say, multiplication is just function composition, represented with The Bluebird combinator.} $$

$$ B = \lambda fgx. f(gx) $$

$$ Mult = B $$

$$ \text{Next: exponents!} $$

$$ Pow \text{ } n2 \text{ } n4 = n16 $$

$$ Pow \text{ } n2 \text{ } n4 \text{ } f \text{ } x = (f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f) (x) $$

$$ Pow \text{ } n2 \text{ } n3 \text{ } f = f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f ∘ f = (((f ∘ f) ∘ (f ∘ f)) ∘ ((f ∘ f) ∘ (f ∘ f))) ∘ (((f ∘ f) ∘ (f ∘ f)) ∘ ((f ∘ f) ∘ (f ∘ f))) = ((n2(f) ∘ n2(f)) ∘ (n2(f) ∘ n2(f))) ∘ ((n2(f) ∘ n2(f)) ∘ (n2(f) ∘ n2(f))) = (n2(n2(f)) ∘ n2(n2(f))) ∘ (n2(n2(f)) ∘ n2(n2(f))) = n2(n2(n2(f))) ∘ n2(n2(n2(f))) = n2(n2(n2(n2(f))))) = n4(n2, f) = n4(n2)(f) $$

$2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ Lines!

$$ Pow \text{ } n2 \text{ } n4 = n4(n2) $$

$$ Pow = \lambda nk. k(n) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Pow = \lambda nk. kn $$

$$ \text{Next: groupings!} $$

$$ \text{This subchapter is about the smallest data structure in lambda calculus, The Vireo (V), here's it's definition:} $$

$$ \text{V} = \lambda abf. f(a, b) $$

$$ \text{And the auto-parenthesized one:} $$

$$ \text{V} = \lambda abf. fab $$

$$ \text{This function mainly works with the second rule of currying, you see, The Vireo can do this:} $$

$$ \text{V} (a, b) (f) = f(a, b) $$

$$ \text{but what happens to the V} (a, b) \text{ before the } f \text{? Solution: } a \text{ and } b \text{ are paired together.} $$

$$ \text{By the way, because it is used so much (and this just makes sense), V} (a, b) = (a, b) \text{.} $$

$$ \text{Now, when you want to evaluate a regular function } f \text{ on a pair } p \text{, than that would be } p(f) \text{, but if you wanted a function that evaluates more like } f(p) \text{ than } p(f) \text{, then you need a pairwise function (not to be confused with piecewise function, as it is the only result when you google "pairwise function", and piecewise functions don't actually exist in lambda calculus) (e.g. a function that inputs a pair, and outpts the first thing in that pair) actually, that second thing would be really usefull, I'm gonna try to derive it (as well as a function that inputs a pair, and outpts the second thing in that pair).} $$

$$ Fst((a, b)) = a $$

$$ \text{And because this is the first pairwise function that I'm gonna derive, it has to use regular functions in it's definition, so} $$

$$ Fst((a, b)) = (a, b)(f) = f(a, b) = a $$

$$ \text{Hmm... } f(a, b) = a \text{, sounds like The Kestril!} $$

$$ Fst = \lambda p. p (\text{T}) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Fst = \lambda p. p \text{ } \text{T} $$

$300$ Lines.

$$ \text{And, because } \text{F} \text{ is like the opposite of } \text{T} \text{ (in that it does the second and not the first), } Snd \text{ should just be } \lambda p. p \text{ } \text{F} \text{!} $$

$$ \text{Ok, fine, I'll prove it (the } Snd = \lambda p. p \text{ } \text{F} \text{ thing).} $$

$$ (a, b)(\text{F}) = \text{F}(a, b) = b $$

$$ \text{And that's exactly what you'd expect (from a function that inputs a pair, and outpts the second thing in that pair), proof complete!} $$

$$ \text{Next: (it might not seem obvius why, but) I want to tell you about The Phi Combinator!} $$

$$ \Phi = \lambda p. \text{V} (Snd(p))(Succ(Snd(p))) $$

$$ \text{And the auto-parenthesized one:} $$

$$ \Phi = \lambda p. \text{V} (Snd \text{ } p)(Succ(Snd \text{ } p)) $$

$$ \text{And the pair notation one:} $$

$$ \Phi = \lambda p. (Snd(p), Succ(Snd(p))) $$

$$ \text{And the auto-parenthesized and pair notation one:} $$

$$ \Phi = \lambda p. (Snd \text{ } p, Succ(Snd \text{ } p)) $$

$$ \Phi((\text{doesn't matter what the first thing is}, n0)) = (n0, n1) $$

$$ \Phi((n0, n1)) = \Phi(\Phi((\text{doesn't matter what the first thing is}, n0))) = (n1, n2) $$

$$ \Phi((n1, n2)) = \Phi(\Phi(\Phi((\text{doesn't matter what the first thing is}, n0)))) = (n2, n3) $$

$$ \vdots $$

$$ \Phi((n6, n7)) = \Phi(\Phi(\Phi(\Phi(\Phi(\Phi(\Phi(\Phi((\text{doesn't matter what the first thing is}, n0))))))))) = n8(\Phi, (\text{doesn't matter what the first thing is}, n0)) = (n7, n8) $$

$$ Fst(n8(\Phi, (\text{doesn't matter what the first thing is}, n0))) = Fst((n7, n8)) $$

$$ Fst(n8(\Phi, (\text{doesn't matter what the first thing is}, n0))) = n7 $$

$$ Pred = \lambda n. Fst(n(\Phi, \text{V} (\text{doesn't matter what the first thing is}, n0))) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Pred = \lambda n. Fst(n \text{ } \Phi \text{ } (\text{V} \text{ doesn't matter what the first thing is } n0)) $$

$$ \text{And the pair notation one:} $$

$$ Pred = \lambda n. Fst(n(\Phi, (\text{doesn't matter what the first thing is}, n0))) $$

$$ \text{And the auto-parenthesized and pair notation one:} $$

$$ Pred = \lambda n. Fst(n \text{ } \Phi \text{ } (\text{doesn't matter what the first thing is}, n0)) $$

$$ \text{Before we do subtraction, what is } Pred(n0) \text{?} $$

$$ Pred(n0) = Fst(n0(\Phi, (\text{doesn't matter what the first thing is}, n0))) $$

$$ n0(\Phi, (\text{doesn't matter what the first thing is}, n0)) = (\text{doesn't matter what the first thing is}, n0) $$

$$ Fst((\text{doesn't matter what the first thing is}, n0)) = \text{doesn't matter what the first thing is} $$

$$ \text{I'll just choose } n0 \text{.} $$

$$ \text{This also means that I have to redo the predecessor function.} $$

$$ Pred = \lambda n. Fst(n(\Phi, \text{V} (n0, n0))) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Pred = \lambda n. Fst(n \text{ } \Phi \text{ } ( \text{V } n0 \text{ } n0)) $$

$$ \text{And the pair notation one:} $$

$$ Pred = \lambda n. Fst(n(\Phi, (n0, n0))) $$

$$ \text{And the auto-parenthesized and pair notation one:} $$

$$ Pred = \lambda n. Fst(n \text{ } \Phi \text{ } (n0, n0)) $$

$$ \text{Next: subtraction!} $$

$$ Sub = \lambda nk. n(Pred, k) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Sub = \lambda nk. n \text{ } Pred \text{ } k $$

$$ \text{Next: is } 0 \text{!} $$

$$ f(n0) = \text{T} $$

$$ f(n) = \text{F } (n > 0) $$

$$ f(n) = n(g, x) $$

$$ f(n0) = n0(g, x) = x = \text{T} $$

$$ x = \text{T} $$

$400$ Lines.

$$ f(n) = n(g, \text{T}) $$

$$ f(n1) = n1(g, \text{T}) = g(\text{T}) = \text{F} $$

$$ g(\text{T}) = \text{F} $$

$$ g = \text{Not???} $$

$$ f(n2) = n2(g, \text{T}) = g(g(\text{T})) = g(\text{F}) = \text{F} $$

$$ g(\text{F}) = \text{F} $$

$$ g(p) = \text{F} $$

$$ g = h(y) $$

$$ h(y)(p) = \text{F} $$

$$ h(y, p) = \text{F} $$

$$ y = \text{F} $$

$$ h = K $$

$$ g = K(\text{F}) $$

$$ f(n) = n(K(\text{F}), \text{T}) $$

$$ is0 = \lambda n. n(K(\text{F}))(\text{T}) $$

$$ \text{And the auto-parenthesized one:} $$

$$ is0 = \lambda n. n \text{ } (K \text{F}) \text{ } \text{T} $$

$$ \text{Next: I'll keep it a mystery, 'cause the question is:} $$

$$ \text{When is } n - k \text{ equal to } 0 \text{? (Well, } n0 \text{ actually.)} $$

$$ \text{Well, there's obvius awnser of when } n \text{is equal to } k \text{, but remember when I said that the predecessor of } n0 \text{ is } n0 \text{? So, any time } n \text{ is less than } k \text{, } n - k = n0 \text{. So} $$

$$ Leq = \lambda nk. is0(Sub(n, k)) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Leq = \lambda nk. is0(Sub \text{ } n \text{ } k)) $$

$$ \text{Next: } ≥ \text{!} $$

$$ Geq = \lambda nk. is0(Sub(k, n)) $$

$$ \text{And the auto-parenthesized one:} $$

$$ Geq = \lambda nk. is0(Sub \text{ } k \text{ } n)) $$

$$ \text{Next: } > \text{!} $$

$$ Gt = \text{Not} (Leq) $$

$$ \text{Next: } < \text{!} $$

$$ Lt = \text{Not} (Geq) $$

$$ \text{Next: } = \text{!} $$

$$ Eq = \text{And} (Leq, Geq) $$

$$ \text{Next: } \ne \text{!} $$

$$ Neq = \text{Not} (Eq) $$

$$ \text{before we do the biggest (codable) number, let's write down every function that we know in one line.} $$

$$ I \text{ } M \text{ } K / \text{T} \text{ } Ki / \text{F} \text{ } \text{And} \text{ } \text{Or} \text{ } \text{Not} \text{ } n0 \text{ } n1 \text{ } n2 \text{ } n3 \text{ } Succ \text{ } Add \text{ } Mult \text{ } B \text{ } Pow \text{ } \text{V} \text{ } Fst \text{ } Snd \text{ } \Phi \text{ } Pred \text{ } Sub \text{ } is0 \text{ } Leq \text{ } Geq \text{ } Gt \text{ } Lt \text{ } Eq \text{ } Neq $$

$$ \text{Finally, the thing you've all been waiting for (final boss music starts playing), the biggest (codable) number} $$

$$ Fgh = \lambda nx. is0(n)(Succ(x), Eq(n, n1)(Mult(n2, x), Eq(n, n2)(Mult(x, Pow(2, x)), x(Fgh(Pred(n)), x)))) $$

$$ \text{Next: I'm skipping omega, because there's already an omega combinator (even though it's a capital omega), and it's equivilant to } M(M) \text{. So, epsilon next} $$

$$ Epss = \lambda xn. is0(n)(Pred(x)(Pow(x), x), Pred(x)(Pow(Epss(x, Pred(n))), Epss(x, Pred(n)))) $$

$$ Eps = \lambda xn. Fgh(Epss(x, n), x) $$

$$ \varphi_s = \lambda nxy. is0(n)(Pow(x, y), Eq(n, n1)(Epss(x, y), is0(y)(x(\varphi_s (Pred(n), x), 0), Pred(x)(Pow(\varphi_s (n, x, Pred(y))), x)))) $$
