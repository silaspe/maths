## to cheat, or not to cheat?

Let's start with a game! The game is that you flip a coin 10 times and then you add the total number of heads and you want the most heads total, this game is pretty popular in some hypothetical town where there is a rumor going around that some people are using (somehow) using a weighted coin that has a $75$% chance of landing heads, the notation is $\frac{3}{4}$ chance, because what else (other than $100$) are you going to take a percent of? Anyways, this town has nominated you to be the detective and test everyone with a test has all three of the properties:

1, false accusation: accuse less than $5$% of fair players

2, true accusation: accuse more than $80$% of cheaters

3, make it short: do as little coin flips as possible because we don't have all day

this is usually where I solve the puzzle, but now's the chance to solve it yourself using the tools in the next chapter

### solution

#### binomial coefficient

do you remember that time when I proved the [binomial theorem](https://silaspe.github.io/maths/binomial.html)
? Well, I can count the number of heads and the number of tails and the total number of flips is always the same. For example, no matter if you get $1$ heads and $4$ tails, $3$ heads and $2$ tails, whatever it is, it should  add up to $5$ flips total. The same happens with the probability, because if there always has to be $5$ flips, then there could be $0$ to $5$ heads and $5$ minus that tails, so if you add up the probability of each thing happening, then you should have to get $1$ or $100$%

even if I proved that:

$$ (1 + x)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k = \sum\limits_{k = 0}^{\infty} \frac{n! x^k}{k!(n - k)!} $$

you can use a similar argument that:

$$ (x + y)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k y^{n - k} = \sum\limits_{k = 0}^{\infty} \frac{n! x^k y^{n - k}}{k!(n - k)!} $$

so if I made $x$ into the probability $p$ of landing heads, made $y$ into $(1 - p)$, and made $n$ into the number of flips, than on the left, I would get $1^n$, which is just $1$, but on the right, knowing that multiplying probabilities is the probability that they happen in parallel (if independent!), I would get the sum of the probability of any number number of heads times the probability of getting tails $5$ minus the total number of heads times (which is the total number of tails) times each orientation e.g.heads, tails, heads tails, heads is the same as heads, heads, heads, tails, tails. So this is taking the probability of getting some number of heads and tails, adding them up, and saying that it is $100$%, going one step back, each term is the probability of getting some number of heads which I will call $k$, I will also swap $5$ with $n$.

This seems pretty useful and what I did was took apart the binomial theorem and the probability is the probability of getting $k$ heads and $n - k$ tails and each orientation. I will write this probability below saying that there are $n$ flips, $k$ heads, and probability $p$ of landing heads.

$$ P(n, k, p) = \begin{pmatrix} n \\
k \\ \end{pmatrix} p^k (1 - p)^{n - k} $$

#### binomial approximation (ish)

Realistically, the test wouldn't test a specific number of heads or tails, so it would be something more like $7$ or more heads out of $10$ flips, you could say that it is the probability of $7$ heads OR $8$ heads OR $9$ heads OR $10$ heads, but for one, it is hard to define an "OR", for example if there are two coins $a$ and $b$, one has probability $a$ of landing heads, one has probability $b$ of landing heads, the probability of $a$ AND $b$ landing heads is simply $ab$, but the probability of $a$ OR $b$ landing heads (or both!) is $1 - (1 - a) (1  - b)$ and that is pretty easy to prove, anyways my point still stands! And I should not use that definition, because it is computationally intensive, hard to read, and most of all, it uses an "I'll leave this as an exercise for the viewer". Anyways, I am tired of writing text and just want to prove this new formula.

So, now that you know how to manipulate probabilities, I won't use something like the binomial theorem and I will instead just build it from the ground up, so the factor of $p^k$ sounds about right, but if I don't use the $(1 - p)^{n - k}$ term, than it wouldn't necessarily mean that the rest are tails, but what about the $n$ choose $k$ term? You might be asking (actually probably not, because I forgot to tell you what that orientation term is called a loooooooooong time ago) well, same as before, just replace the tails with question marks! Actually, as I am writing this, I realized that those question marks need an orientation too, except sometimes they don't if they are all the same then they don't and it is really confusing. Actually, as I was writing that, I realized, no actually I couldn't find a counter counter point, but what I did realize was that the $\frac{n!}{k!(n - k)!}$ was the thing that was going to change.

There are sooooo many counter counter counter counter counter points, and I know that the solution is something something $1 - (1 - p)^n$, so I will just go off of that. $1 - (1 - p)^n$ Is a term that means the probability of $p$ OR $p$ OR $p$ OR $p$ OR $p \dots$ $n$ times, so the probability of $1$ or more heads out of $n$ total flips, I just made this up, but to add $k$ into the equation, replace $p$ with $p^k$, so now it is the probability of $p^k$ or more heads (if this is wrong, than I will replace it later), anyways it's time to do the thing where I say "Anyways, I am tired of writing text and just want to prove this new formula."

$$ 1 - (1 - p^k)^n $$

###

It's been $2$ months since I worked on this page. i'll accept that (hold on, I need to find it somewhere in this page)

$$ 1 - \prod\limits_{i = k}^{n} (1 - \begin{pmatrix} n \\
k \\ \end{pmatrix} p^k (1 - p)^{n - k}) $$
