Links: [Why Negative Times Negative is Positive - Definition of Ring | Ring Theory E1](https://www.youtube.com/watch?v=4nG49xTTjIA), [Zero Product Property is False - Divisibility, Units, Zero Divisors | Ring Theory E2](https://www.youtube.com/watch?v=u1uW_BOUGoM), and [Number Systems Invented to Solve the Hardest Problem - History of Rings | Ring Theory E0](https://www.youtube.com/watch?v=M-9_rZfVQVE) all by [EpsilonDelta](https://www.youtube.com/@EpsilonDeltaMain), and [Every Hypercomplex Number Explained #SoME4](https://www.youtube.com/watch?v=DuNXn6qA2NE) by [Johttacus J. J. Begallo](https://www.youtube.com/@johttacusj.j.begallo1432)

It's another day.

#### what is a ring?

A ring is a number system where you can add numbers, multiply numbers, and subtract numbers. More formally, a ring is a set that has operations of addition and multiplication that have the following requirements:

$1$: Closure ($+$): if $a$ is in the ring and $b$ is in the ring, then $a + b$ is also in the ring.

$2$: Closure ($\cdot$): if $a$ is in the ring and $b$ is in the ring, then $a b$ is also in the ring.

$3$: Associativity ($+$): if $a$, $b$, and $c$ are all in the ring, then $(a + b) + c = a + (b + c) = a + b + c$.

$4$: Associativity ($\cdot$): if $a$, $b$, and $c$ are all in the ring, then $(a b) c = a (b c) = a b c$.

$5$: Commutativity ($+$): if $a$ is in the ring and $b$ is in the ring, then $a + b = b + a$.

$6$: Identity ($+$): there must always be a $0$ where, if you pick any $a$ in the ring, then $a + 0 = a$.

$7$: Identity ($\cdot$): there must always be a $1$ where, if you pick any $a$ in the ring, then $1 a = a 1 = a$.

$8$: Inverses ($+$): if $a$ is in the ring, then there must always be a $-a$ in the ring where $a + -a = 0$.

$9$: Distributivity ($+$ & $\cdot$): if $a$, $b$, and $c$ are all in the ring, then $a (b + c) = (b + c) a = a b + a c$.

So, if you know the definition of a group, then ignoring distributivity gives you the following: if you remove multiplication, you're left with an abelian group, and if you remove addition, you're left with something that's like a group, but it has no inverse requirement.

It's another day.

Notice: I said addition, multiplication, and subtraction at the start. This is to emphasize that you can take the negatives of things, but not necessarily the multiplicative inverses.

After re-watching the first half of [Why Negative Times Negative is Positive - Definition of Ring | Ring Theory E1](https://www.youtube.com/watch?v=4nG49xTTjIA) yesterday, or two days ago, or three days ago, or however long ago I last worked on this, I have forgotten what's inside of the video, and I'll just do something else for the next part.

#### why is a ring?

This isn't a chapter as much as it is the reason why these rules are in place, especially distributivity. It turns out, some of these rules are designed so that the first definition of multiplication you learned actually works.

$$ R \text{ is a ring} $$

$$ a \text{ is in } R $$

$$ 3 a = (1 + 1 + 1) a = 1 a + 1 a + 1 a = a + a + a $$

I came up with that in the middle of the night.

$$ \frac{1}{3} \text{ is in } R $$

$$ \frac{1}{3} a = x $$

$$ 3 (\frac{1}{3} a) = 3 x $$

$$ \frac{1}{3} a + \frac{1}{3} a + \frac{1}{3} a = (\frac{1}{3} + \frac{1}{3} + \frac{1}{3}) a = x + x + x $$

$$ \frac{1}{3} + \frac{1}{3} + \frac{1}{3} : = 1 $$

$$ (\frac{1}{3} + \frac{1}{3} + \frac{1}{3}) a = 1 a = a $$

$$ x + x + x = a $$

I came up with that after seeing a scene in the movie Arrival where someone said something like $\frac{1}{6}$ means $1$ of $6$ parts.

$$ b \text{ is in } R $$

$$ a b = a (b + 0) = a b + a 0 $$

$$ a b = a b + a 0 $$

$$ a b + -(a b) = a b + a 0 + -(a b) $$

$$ a 0 = 0 $$

I came up with that after trying to prove that it's true.

$$ (-1) a = x $$

$$ a 0 = 0 $$

$$ a 0 = a (1 + (-1)) = a 1 + a (-1) = a + a (-1) $$

$$ a + a (-1) = 0 $$

$$ a + a (-1) + (-a) = 0 + (-a) $$

$$ a (-1) = -a $$

I came up with this one while writing it, and I think it was also in [Why Negative Times Negative is Positive - Definition of Ring | Ring Theory E1](https://www.youtube.com/watch?v=4nG49xTTjIA).

There's probably more to put in this chapter, but you can just watch [Why Negative Times Negative is Positive - Definition of Ring | Ring Theory E1](https://www.youtube.com/watch?v=4nG49xTTjIA)

#### basic ring information

You might have noticed that it's been a while (actually, I think it's been a month), and that's because I always decided to work on the problem set I had instead of working on this page, but now problem set $3$ has been turned in, I can finally work on this page!

But anyways, I thought it would be helpful if I showed examples of what's a ring and what isn't a ring. The definition of a ring is very general, so most things you can think of as number systems count as rings. (And even some things you wouldn't ever really think of as number systems are rings!)

The most famous rings I can think of are, well, there's the integers, the rational numbers, the real numbers, matrices*, and complex numbers.


$100$ Lines.

*$\begin{bmatrix} 0 & 0 \\
0 & 0 \\ \end{bmatrix}$ is $0$, $\begin{bmatrix} 1 & 0 \\
0 & 1 \\ \end{bmatrix}$, $\begin{bmatrix} 1 & 0 \\
0 & 1 \\ \end{bmatrix}$ is $1$.

Something strange just happened: when I pressed the edit button, for the first time in this website's history, there wasn't an empty line.

Anyways, it's Wednesday. Wednesday is a week after midterms, which is a week and a day after problem set five, and it said earlier that it was problem set three, so it's been a month.

What about the different types of rings? Well, a commutative ring is one where the multiplication operation is commutative.  (Remember how I only wrote down commutativity for addition?) A division ring is one where every number has a multiplicative inverse. If something is both a commutative and a division ring, it's called a field, the highest honor a ring can have.

But the requirements for a division ring still seem too strict (and don't allow for primes, because any $p$ is equal to $x (x^{-1} p)$, for $x \ne 0$). If only there was another requirement that all division rings have where it would be nice if you had it for your ring. Well, it turns out there is! They're called cancelable rings, and they're called that because in a cancelable ring, the following holds:

$$ a b = a c, a \ne 0 → b = c $$

It turns out that this is the same as the property that if $ab = 0$, then $a = 0$ or $b = 0$. If this is not the case, then $a$ is called a left zero divisor and $b$ is called a right zero divisor. Here's a proof that cancelable ring and no zero divisors are the same statement:

Proof of backward case:

$$ a b = a c $$

$$ a \ne 0 $$

$$ a b - a c = 0 $$

$$ a (b - c) = 0 $$

$$ \text{Because } a \ne 0 \text{, } b - c = 0 $$

$$ b = c $$

Proof of forward case:

$$ a b = 0 $$

$$ a (b + 0) = 0 $$

$$ a b + a 0 = 0 $$

This is obviously true if $a = 0$, but if $a \ne 0$ then we can use our assumption that the ring is cancelable. This would mean that $b = 0$ which, together with $a = 0$ being a solution, means that means that if $ab = 0$ then $a = 0$ or $b = 0$.

Now it's time to finish categorizing rings. As you know, if a ring has no zero divisors, then it's cancelable. But if a ring is cancelable and is also commutative, then it's called an integral ring (because it behaves like the integers). Also, if something is a division ring, then it should be obvious that there are no zero divisors, because if $ab = 0$ and $a$ and $b$ are both nonzero, then you can just divide by $b$ and then get that $a = 0$.

So, you know that list I said earlier? Well, the integers are an integral ring (like I said earlier), the rational numbers form a field, the real numbers form a field, and the complex numbers form a field.

#### what's in a ring?

As I said earlier, zero divisors could be in a ring, but there's actually another thing that's kind of the opposite of a zero divisor: a unit.

A unit $u$ has a number $u^{-1}$ that is also in the ring where $u u^{-1} = u^{-1} u = 1$.

Units have the same annoying property as $1$ where they divide everything because $a = u (u^{-1} a)$. you have probably seen units before, you know how in the definition for a prime, it says that a prime if it is is a number that's divisible by $1$ and itself only? Well, because the positive integers don't form a ring, inside of the integers you have to also consider that, for example, $5$ is equal to $(-1) (-5)$, or $(-1) (-1) 5$.

I will continue to talk about primes for the rest of this page (if I end up finishing it), but for now, just know that units are another thing that could be inside of a ring where everything inside a division ring (other than $0$) is one of them.

Everything above this line was made in the concept for this page. Everything below and including this line was made after the creation of this page.
