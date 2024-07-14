Ok, so, lambda calculus, I'll be following along with [the first part](https://www.youtube.com/watch?v=3VQ382QG-y4), at least for now, and I haven't seen this in a year, so we'll be reacting to it together.

### Chapter $1$: Introduction

Ok, so, it looks like he's starting off with a function (written as $I$) that he calls "the identity". Now, what do you think $I(1)$ is? * Man in the backround says " same value! "*, and that is correct, $I(1) = 1$, $I(2) = 2$, what about $I(I)$? * No one awnsers*, yeah, it's $I$. (By the way, functions in lambda calculus are also called "combinators", each one has a function name (e.g. $I$), a more descriptive function name (e.g. identity), and an alias (which is always a bird for some reason) (e.g. Idiot bird.)) (Also by the way, I'll be copying what he's saying for the rest of this page, and putting my thoughts in between parenthases.) And then he uses some fancy notation " $\lambda a. a$ ". It takes in ($\lambda$) a value ($a$), and outputs ($.$) that same value ($a$). So, $I(x) = x$ for any $x$. As you saw, you can use functions as arguments (which is why they are called "combinators". Also, to me, this is the heart of lambda calculus), verbs are nouns and nouns are verbs. 

#### chapter $2$: What is this $\lambda$?

Ok, so, what was this $\lambda$ stuff from earlier? (Finally he explains it.) So, lambda is a signafier, it's a way to indicate that we are starting the definition of a function. So, we can read this (this $\lambda a. a$) as: we're starting the definition of a function ($\lambda$), which takes a single input ($a$), or parameter (The $.$ signafies that we are no longer writing down the parameters, and now), and returns some expression ($a$). This whole thing is called a lambda abstraction in lambda calculus.

### chapter $3$: What is Lambda Calculus?

Lambda calculus is a really tiny symbol manipulation framework, a calculus is just a way of moving around symbols on a page (I actually didn't know that), the subject that you may have learnd in school called "calculus" is a specific calculus for things like differentials and integrals and stuff like that, derivatives. But this calculus is about something else, this calculus is about evaluating and defining functions.

### chapter $4$: I'm tired of this, here's a crash course on lambda calculus.

Functions (aka combinators) act on other functions, each one has a single letter abbreviation, and an alias. For the example function, it is written " $M$ ", and is called "The Mockingbird". Now, how it's defined in lambda calculus is " $M = : \lambda a. a(a)$ ". Now, this is where it starts to get complicated (that's a family meme). First, there's a $\lambda$ (aka lambda), which means: defining inputs (functions). Then, it defines an input ($a$), then, there's a $.$, which means: stop defining inputs. Then, there's an $a(a)$. The $a$ being a function is explaind by when I said "inputs (functions)", but then, there's another question: why is $a$ also an input? One or the other, right? Well, no, it is explaind by when I said "Functions act on other functions". Putting it all together, The Mockingbird function takes in one input, and evaluates it on itself.

### chapter $5$: Code repo

