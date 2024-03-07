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

$$ \Delta^2 g(n) = : \Delta (\Delta g(n)) $$

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

$$ Y^2 - 2X^2 \approx 0 $$

$$ Y^2 \approx 2X^2 $$

$$ \frac{Y^2}{X^2} \approx 2 $$

$$ (\frac{Y}{X})^2 \approx 2 $$

$$ \frac{Y}{X} \approx \sqrt{2} $$

But that is besides the point. The pell equation can be rearanged into $Y = \sqrt{2X^2 + 1}$, then plug in values for $X$ until $Y$ is an integer. Doing this, (and remembering to divide by $2$ and take the floor), I'll list the solutions that we get.

$$ 6 \quad 8 $$

$$ 35 \quad 49 $$

Just barely misses!

$$ 204 \quad 288 $$

There it is!

### in genaral

the real soluion would be a formula for the $n$'th solution to the strand puzzle droppng the second rule, it is a bit tedious to check using this method and someone probably would have used the formula and this wouldn't work. I usually don't tell you [the video](https://www.youtube.com/watch?v=V2BybLCmUzs) that this page is built on, but this time, you would notice that it takes a completely different method. So yes, I built the rest of this page from the ground up.

Something that is easy to notice but hard to prove is that the bigger the $X$ and $Y$, the better the approxamation of $\sqrt{2}$, so I will conjecture the following: Any ratio $\frac{Y}{X}$ for $X$ and $Y$ solving the pell equation*, is closer to $\sqrt{2}$ than any other fraction with denominator less than or equal to $X$.

*The numbers $X$ and $Y$ could solve the alternitave $Y^2 - 2X^2 = - 1$ that alternates with the pell equation as $X$ and $Y$ get bigger, so instead of the pell equation, from now on, it is more like $|Y^2 - 2X^2| = 1$.

By the way, the conjecture was an "I'll leave this as an exersize for the veiwer", and I made up the proof as I went.

Proof (by contradiction): Let's say that there is a fraction $\frac{b}{a}$ that is a better approxamation of $\sqrt{2}$ than $\frac{Y}{X}$ with $a$ strictly* less than $X$. $X$ and $Y$ solve $|Y^2 - 2X^2| = 1$, and $X$ is the next biggest solution than $a$. Well, what is $|b^2 - 2a^2|$? By the thing that is easy to notice but hard to prove, even if $|b^2 - 2a^2| = 1$, it still dosen't work, so $|b^2 - 2a^2| \neq 1$, and by the fact that $\sqrt{2}$ is irrational** (I'll prove that later), $|b^2 - 2a^2| \neq 0$, and by the fact that $a$ and $b$ are integers, $|b^2 - 2a^2| = an$ $integer$. So $|b^2 - 2a^2|$ is an integer, does not equal $0$, and does not equal $1$. But the closer to $1$, the better the approxamation (unless the numbers are is bigger). Thus, the proof is complete!

*If $a = X$, than $|b^2 - 2a^2| = |b^2 - 2X^2|$. If $b = Y$, than I can ignore that case because $\frac{Y}{X}$ cannot be a better approxamation of $\sqrt{2}$ than $\frac{Y}{X}$. So if $b < Y$, $b^2 < Y^2$ * *, so $|b^2 - 2X^2|$ aslo is not $1$.


(* *) If $a$, $b$, $X$, and $Y$ are all negatave, than $b^2 > Y^2$. But for one, if they are both ngatave, then they are not in reduced fractions. And for another, if one is negatave, than the whole thing is negatave, and $\sqrt{2}$ is not. Also if $b > Y$ (yes, it was only a constraint on $a$ and not $b$), than it still wouldn't work.

** Warning! I will swap $a$ and $b$ in this proof: Note that an even number is two times an integer, if the square of a number is even, than the number that is being squared is even, and a ratio of two even numbers is not in reduced form. You can derive these because I am too busy writing this proof down. Lets say that a fraction $\frac{a}{b}$ in lowest terms (that will be important in the contradiction part of proof by contradiction) that equals $\sqrt{2}$. Going back, this means that $a^2 = 2b^2$. But $b^2$ is an integer, so $a^2$ is even, so $a$ is even. if $a$ is even, than lets say that $a = 2m$ for some integer $m$, $a^2 = 4m^2$, so $4m^2 = 2b^2$, so $2m^2 = b^2$. But $m^2$ is an integer, so $b^2$ is even, so $b$ is even, so $a$ and $b$ are both even, but if they are both even, (and if you remembered), this is a contradiction!

Side note! With this proof, you can prove the thing that is easy to notice but hard to prove, but this would be a circular argument, because we need it to be true for it to be true. To this day, I haven't found a proof of this fact. But if I do, then you know the drill by now, I'll write the proof here and put this in quotation marks.

Now, the proof is finally complete! Where was I again?

### Time to keep going

$$ Y^2 - 2X^2 = 1 $$

$$ \hat{Y} = 2X + Y $$

$$ \hat{X} = X + Y $$

$$ \hat{Y}^2 - 2 \hat{X}^2 = (2X + Y)^2 - 2(X + Y)^2 = 4X^2 + 4XY + Y^2 - 2X^2 - 4XY - 2Y^2 = 2X^2 - Y^2 = -(Y^2 - 2X^2) $$

$$ \hat{Y}^2 - 2 \hat{X}^2 = - 1 $$

$$ Y_N = 2 \hat{X} + \hat{Y} $$

$$ \text{(N for next)} $$

$$ X_N = \hat{X} + \hat{Y} $$

But the calculations that I did earlier still work, so

$$ Y_N^2 - 2X_N^2 = 1 $$

So like I said, solutions for the pell equation and inverse pell equation alternate.

Okay, this actially happend: I was soving the strand puzzle and got up to this point. I met someone new, and naturally, I opened with how I got here and where I was with the strand puzzle. She said "can you prove that this is the next solution to the pell equation", and I said "I'm too tired fot that". My point is that you shold just run with it.

From now on, $X$ will be replaced with $X_n$, $Y$ will be replaced with $Y_n$, $\hat{X}$ will be replaced with $X_{n + 1}$, $\hat{Y}$ will be replaced with $Y_{n + 1}$, $X_N$ will be replaced with $X_{n + 2}$, and $Y_N$ will be replaced with $Y_{n + 2}$. this is because it will look more like a formula on $n$ when you solve for $Y_n$ as appose to $Y$. Also these can be solutions to the inverse pell equation. For the pell equation, I want to have a $2n$, so it has to be the inverse pell equation first, an easy answer is

$$ X_1 = 1 $$

$$ Y_1 = 1 $$

and the first solution to the strand puzzle is $1 \quad 1$, so $2 \quad 3$ falls out of that, you can verify this solution yourself (you might recognize $\frac{17}{12}$ from the mathologer video, it translates to $6 \quad 8$ considered as the first real solution, but we’ll get there), so

$$ X_2 = 2 $$

$$ Y_2 = 3 $$

and because of the recurance...

$$ X_{n + 1} = X_n + Y_n $$

$$ Y_{n + 1} = 2X_n + Y_n $$

$$ X_{n + 2} = X_{n + 1} + Y_{n + 1} = X_n + Y_n + 2X_n + Y_n = 3X_n + 2Y_2 = 2(X_n + Y_n) + X_n = 2X_{n + 1} + X_n $$

$$ Y_{n + 2} = 2X_{n + 1} + Y_{n + 1} = X_n + X_n + Y_n + Y_n + 2X_n + Y_n = 4X_n + 3Y_n = 2(2X_n + Y_n) + Y_n = 2Y_{n + 1} + Y_n $$

$$ X_n = 2X_{n - 1} + X_{n - 2} $$

$$ Y_n = 2Y_{n - 1} + Y_{n - 2} $$

### The final dash in the silaspe marithon (yes, that is a referance to mathologer)

For now, I will just copy some text from the [fibbonacci](https://silaspe.github.io/maths/fibbonacci.html) page, and minipulate it.

$$ z^2 = z + 1 $$

$$ z = \begin{Bmatrix} 1 + \sqrt{2} = c \\
1 - \sqrt{2} = d \\ \end{Bmatrix} $$

$$ c^2 = 2c + 1 $$

$$ c^3 = 2c^2 + c = 5c + 2 $$

$$ c^4 = 5c^2 + 2c = 12c + 5 $$

$$ \vdots $$

$$ c^n = c_{n, n} c + c_{n, n - 1} $$

$$ c^{n + 1} = c_{n + 1, n + 1}c + c_{n + 1, n} = c^n c = c_{n, n} c^2 + c_{n, n - 1} c = 2c_{n, n}c + c_{n, n} + c_{n, n - 1} c $$

$$ c_{n + 1, n} = c_{n, n} $$

$$ c_{n + 2, n} = c_{n + 1, n} = c_{n, n} $$

$$ \vdots $$

$$ c_{n + k, n} = c_{n, n} $$

$$ C_n = : c_{n, n} $$

$$ c^n = C_n c + C_{n - 1} $$

$$ c^{n + 1} = C_{n + 1}c + C_n = c^n c = C_n c^2 + C_{n - 1} c = 2C_n c + C_n + C_{n - 1} c $$

$$ C_{n + 1} = C_n + C_{n - 1} $$

$$ C_n = 2C_{n - 1} + C_{n - 2} $$

$$ c^2 = 2c + 1 = c C_2 + C_1 $$

$$ C_1 = 1 $$

$$ C_2 = 2 $$

$$ C_n = X_n $$

$$ c^n = X_n c + X_{n - 1} $$

$$ \text{Yay, now I could solve for $X_n$ if it weren't for the second term, so how can I solve that?} $$

$$ \text{Well, this is only because $c^2 = 2c + 1$, but same goes for $d$, so...} $$

$$ d^n = X_n d + X_{n - 1} $$

$$ \text{and subtracting, we get...} $$

$$ c^n - d^n = X_n c + X_{n - 1} - X_n d - X_{n - 1} = (c - d) X_n = (1 + \sqrt{2} - 1 + \sqrt{2}) X_n =2\sqrt{2} X_n $$

$$ X_n = \frac{c^n - d^n}{2\sqrt{2}} = \frac{c^n - d^n}{c - d} $$

$$ \text{And rearanging the reccurance, we get} $$

$$ X_{n - 2} = X_n - 2X_{n - 1} $$

$$ Y_{n - 2} = Y_n - 2Y_{n - 1} $$

$$ X_2 = 2 = 2X_1 + X_0 = 2 + X_0 $$

$$ Y_2 = 3 = 2Y_1 + Y_0 = 2 + Y_0 $$

$$ X_0 = 0 $$

$$ Y_0 = 1 $$

$$ \text{but that is besides the point, what I want is a formula for } Y \text{. Skipping through a lot of trial and error, you might try this:} $$

$$ X_n = 2X_{n - 1} + X_{n - 2} $$

$$ X_{n - 1} = 2X_{n - 2} + X_{n - 3} $$

$$ X_n + X_{n - 1} = 2X_{n - 1} + X_{n - 2} + 2X_{n - 2} + X_{n - 3} $$

$$ (X_{(n)} + X_{(n) - 1}) = 2(X_{(n - 1)} + X_{(n - 1) - 1}) + (X_{(n - 2)} + X_{(n - 2) - 1}) $$

$$ X_1 + X_{1 - 1} = X_1 + X_0 = 1 + 0 $$

$$ X_1 + X_{1 - 1} = 1 $$

$$ X_2 + X_{2 - 1} = X_2 + X_1 = 2 + 1 $$

$$ X_2 + X_{2 - 1} = 3 $$

$$ \text{Sound familiar? If not, I'll write down the formlas that we have just derived along with the formulas for } Y. $$

$$ (X_{(n)} + X_{(n) - 1}) = 2(X_{(n - 1)} + X_{(n - 1) - 1}) + (X_{(n - 2)} + X_{(n - 2) - 1}) $$

$$ X_1 + X_{1 - 1} = 1 $$

$$ X_2 + X_{2 - 1} = 3 $$

$$ \text{Now for } Y. $$

$$ Y_n = 2Y_{n - 1} + Y_{n - 2} $$

$$ Y_1 = 1 $$

$$ Y_2 = 3 $$

$$ \text{Now it should click.} $$

$$ X_n + X_{n - 1} = Y_n $$
