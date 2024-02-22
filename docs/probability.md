## to cheat, or not to cheat?

let's start with a game! The game is that you flip a coin 10 times and then you add the total number of heads and you want the most heads total, this game is preatty popular in some hypothetical town where there is a rumor going around that some pepole are using (somehow) using a weighted coin that has a $75$% chance of landing heads, the notation is $\frac{3}{4}$ chance, because what else (other than $100$) are you going to take a percent of? Anyways, this town has anominated you to be the detectave and test everyone with a test has all three of the properties:

1, false accusation: accuse less than $5$% of fair players

2, true accusation: accuse more than $80$% of cheaters

3, make it short: do as little coin flips as possible because we don't have all day

this is usualy where I solve the puzzle, but now's the chance to solve it yourself using the tools in the next chapter

### solution

#### binomial

do you remember that time when I proved the [binomial therom](https://silaspe.github.io/maths/binomial.html)
? Well, I can count the number of heads and the number of tails and the total number of flips is always the same. For example, no matter if you get $1$ heads and $4$ tails, $3$ heads and $2$ tails, whatever it is, it shuld  add up to $5$ flips total. The same happens with the probability, because if there always has to be $5$ flips, then there could be $0$ to $5$ heads and $5$ minus that tails, so if you add up the probability of each thing happening, then you should have to get $1$ or $100$%

even if I proved that:

$$ (1 + x)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k = \sum\limits_{k = 0}^{\infty} \frac{n! x^k}{k!(n - k)!} $$

you can use a simalar argument that:

$$ (x + y)^n = \sum\limits_{k = 0}^{\infty} \begin{pmatrix} n \\
k \\ \end{pmatrix} x^k y^{n - k} = \sum\limits_{k = 0}^{\infty} \frac{n! x^k y^{n - k}}{k!(n - k)!} $$

so if I made $x$ into the probability $p$ of landing heads, made $y$ into $(1 - p)$, and made $n$ into the number of flips, than on the left, I would get $1^n$, which is just $1$, but on the right, knowing that multaplying probabilities is the probability that they happen in parellel (if independent!), I would get the sum of the probability of any number number of heads times the probability of getting tails $5$ minus the total number of heads times (which is the total number of tails) times each orientation e.g.heads, tails, heads tails, heads is the same as heads, heads, heads, tails, tails. So this is taking the probability of getting some number of heads and tails, adding them up, and saying that it is $100$%, going one step back, each term is the probability of getting some number of heads which I will call $k$, I will also swap $5$ with $n$.

This seems preatty useful and what I did was took apart the binomial therom and the probability is the probability of getting $k$ heads and $n - k$ tails and each oreintation. I will write this probability below saying that there are $n$ flips, $k$ heads, and probability $p$ of landing heads

$$ P(n, k, p) = \begin{pmatrix} n \\
k \\ \end{pmatrix} p^k (1 - p)^{n - k} $$
