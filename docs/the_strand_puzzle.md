## house numbers

First things first, I have to copy the strand puzzle word for word, having the same punctuation, same capitalisation, and same time pressing enter, and here it is

"There is a man who lives on a long street, numbered on

his side one, two, three, and so on, and that all the

numbers or one side of him added up exacly the same

as all the numbers on the other side of him.

.

He said he knew there was more than

fifty houses on that side of the street, but not so many

as five hundred."

just to clarify, there are no houses on the other side of the street, and the house numbers don't skip any. To solve the puzzle, you find the number of his house, and the total number of houses on the street / number of the last house on the street, and that one is in between $50$ and $500$, for future refrence, I will call those unknowns $x$ and $y$ respectively. When someone gave ramanujan (I'm a big fan of him by the way), he (supposedly) solved it in under $10$ seconds.

### calculation

also, because it is against MY rules to use something that I haven't derived (which is why the [polynomial](https://silaspe.github.io/maths/polynomial.html) page has more that $10$ lines, and why most of the contents of this website are derivations), first I will derive the formula for the sums of integers using [dscrete calculas](https://silaspe.github.io/maths/binomial.html)

#### the formula for the sums of integers (I couldn't find a better name)

$$ f(n) = \sum\limits_{k = 0}^{n} k $$

$$ \Delta f(n) = \sum\limits_{k = 0}^{n + 1} (k) - \sum\limits_{k = 0}^{n} (k) = n + 1 + \sum\limits_{k = 0}^{n} (k) - \sum\limits_{k = 0}^{n} (k) $$

$$ f(n - 1) + n = f(n) $$

$$ f(n - 1) = f(n) - n $$

$$ f(1) = 1 $$

$$ f(1 - 1) = f(0) = f(1) - 1 $$

$$ \Delta^2 f(n) = : \Delta (\Delta f(n)) = \Delta (n + 1) = n + 1 + 1 - n - 1 = 1 $$

.

$$ f(0) = 0 $$

$$ \Delta f(n) = n + 1 $$

$$ \Delta^2 f(n) = 1 $$
