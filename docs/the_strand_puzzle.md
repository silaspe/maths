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

just to clarify, there are no houses on the other side of the street, and the house numbers don't skip any. To solve the puzzle, you find the number of his house, and the total number of houses on the street / number of the last house on the street, and that one is in between $50$ and $500$. For future refrence, I will call those unknowns $x$ and $y$ respectively. When someone gave ramanujan (I'm a big fan of him by the way), he (supposedly) solved it in under $10$ seconds.

### calculation

also, because it is against MY rules to use something that I haven't derived (which is why the [polynomial](https://silaspe.github.io/maths/polynomial.html) page has more that $10$ lines), and why most of the contents of this website are derivations), first I will derive the formula for the sums of integers using [discrete calculas](https://silaspe.github.io/maths/binomial.html)

#### the formula for the sums of integers (I couldn't find a better name)

$$ \sum\limits_{k = 0}^{n} k = f(n) $$

$$ \Delta f(n) = \sum\limits_{k = 0}^{n + 1} (k) - \sum\limits_{k = 0}^{n} (k) = n + 1 + \sum\limits_{k = 0}^{n} (k) - \sum\limits_{k = 0}^{n} (k) $$

$$ \Delta f(n) = n + 1 $$

$$ f(n - 1) + n = f(n) $$

$$ f(n - 1) = f(n) - n $$

$$ f(1) = 1 $$

$$ f(1 - 1) = f(0) = f(1) - 1 $$

$$ f(0) = 0 $$

$$ \Delta^2 g(n) = : \Delta (\Delta g(n)) = \Delta (n + 1) = n + 1 + 1 - n - 1 = 1 $$

$$ \Delta^2 f(n) = \Delta (n + 1) = n + 1 + 1 - n - 1 = 1 $$

$$ \Delta f(0) = 0 + 1 = 1 $$

$$ \Delta^2 f(0) = 1 $$

$$ \text{for the rest of this page, until I say "ao!", the things about } f(n) \text{ and } g(n) \text{ work for any } f \text{ and } g $$

$$ \Delta (f(n) + g(n)) = f(n + 1) + g(n + 1) - f(n) - g(n) = f(n + 1) - f(n) + g(n + 1) - g(n) = \Delta f(n) + \Delta g(n) $$

$$ f(n + 1) = f(n) + \Delta f(n) $$

$$ \Delta (c f(n)) \text{(in respect to n)} = c f(n + 1) - c f(n) = c (f(n) + \Delta f(n)) - c f(n) = c f(n) + c \Delta f(n) - c f(n) = c \Delta f(n) $$

#### putting it all together

$$ \Delta \begin{pmatrix} n \\
k \\ \end{pmatrix} \text{(in respect to n)} = \begin{pmatrix} n \\
k - 1 \\ \end{pmatrix} $$

$$ \begin{pmatrix} n \\
k \\ \end{pmatrix} = \frac{n^{\frac{k}{}}}{k!} $$

$$ \Delta f(n) = 5 \begin{pmatrix} n \\
0 \\ \end{pmatrix} + 1 \begin{pmatrix} n \\
1 \\ \end{pmatrix} + 4 \begin{pmatrix} n \\
2 \\ \end{pmatrix} + 2 \begin{pmatrix} n \\
3 \\ \end{pmatrix} $$

$$ f(n) = f(0) + 5 \begin{pmatrix} n \\
1 \\ \end{pmatrix} + 1 \begin{pmatrix} n \\
2 \\ \end{pmatrix} + 4 \begin{pmatrix} n \\
3 \\ \end{pmatrix} + 2 \begin{pmatrix} n \\
4 \\ \end{pmatrix} = f(0) \begin{pmatrix} n \\
0 \\ \end{pmatrix} + 5 \begin{pmatrix} n \\
1 \\ \end{pmatrix} + 1 \begin{pmatrix} n \\
2 \\ \end{pmatrix} + 4 \begin{pmatrix} n \\
3 \\ \end{pmatrix} + 2 \begin{pmatrix} n \\
4 \\ \end{pmatrix} $$

$$ \text{ao!} $$

$$ \Delta^2 f(n) = \begin{pmatrix} n \\
0 \\ \end{pmatrix} $$

$$ \Delta f(0) = 1 $$

$$ \Delta f(n) = \begin{pmatrix} n \\
0 \\ \end{pmatrix} + \begin{pmatrix} n \\
1 \\ \end{pmatrix} $$

$$ f(0) = 0 $$

$$ f(n) = \begin{pmatrix} n \\
1 \\ \end{pmatrix} + \begin{pmatrix} n \\
2 \\ \end{pmatrix} $$

$$ \begin{pmatrix} n \\
0 \\ \end{pmatrix} = 1 $$

$$ \begin{pmatrix} n \\
1 \\ \end{pmatrix} = n $$

$$ \begin{pmatrix} n \\
2 \\ \end{pmatrix} = \frac{n (n - 1)}{2} $$

$$ f(n) = \frac{n (n - 1)}{2} + n = \frac{n (n - 1)}{2} + \frac{2n}{2} = \frac{(n - 1) n + (2) n}{2} = \frac{n (n - 1 + 2)}{2} $$

$$ \sum\limits_{k = 0}^{n} k = \frac{n (n + 1)}{2} $$

### back to the strand puzzle or whatever I was doing because I don't remember

now I can find formulas for the sums of house numbers and say that they are equal. The first starts at $1$ and stops at $x - 1$, so the formula is:

$$ \frac{(x - 1) x}{2} $$

Now, for the second formula, there are two methods. If I say "ao!", then forget the last $2$ lines, if i say "oa!", than remember them. With that being said...

one method is to pull out an $x$ at each of the $y - x$ steps, which amounts to an addded $x(y - x)$, so it is:

$$ \frac{(y - x) (y - x + 1)}{2} + x(y - x) = \frac{1}{2}((y - x) (y - x + 1) + 2x(y - x)) = \frac{1}{2}(y^2 - xy + y - xy + x^2 - x + 2xy - 2x^2) = \frac{1}{2}(y^2 + y - x^2 - x) = \frac{y (y + 1)}{2} - \frac{x (x + 1)}{2} $$

ao!

one method is to realize that this is the difference between the first $y$ houses and the first $x$ houses, so it is:

$$ \frac{y (y + 1)}{2} - \frac{x (x + 1)}{2} $$

oa!

you can probably tell that the first was made by me, but time for some algebra!

$$ \frac{(x - 1) x}{2} = \frac{y (y + 1)}{2} - \frac{x (x + 1)}{2} $$

$$ (x - 1) x = y (y + 1) - x (x + 1) $$

$$ x^2 - x = y^2 + y - x^2 - x $$

$$ 2x^2 = y^2 + y $$

Bit more!

$$ 2 (4x^2) = 4y^2 + 4y $$

$$ 2 (2x)^2 = 4y^2 + 4y + 1 - 1 = (4y^2 + 4y + 1) - 1 = (2y + 1)^2 - 1 $$

$$ (2y + 1)^2 - 2 (2x)^2 - 1 = 0 $$

$$ (2y + 1)^2 - 2 (2x)^2 = 1 $$

$$ X = : 2x $$

$$ Y = : 2y + 1 $$

$$ Y^2 - 2X^2 = 1 $$

Which you might (but probably don't) know as the...

### pell equation
