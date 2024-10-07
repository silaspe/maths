## Like the title suggests, what would happen if you restart counting after $10$?

You (supposedly) started counting when you were very young, so starting with counting to the intergrs, we will rebuild arithmatic from the ground up.

$$ 1 $$

$$ 2 $$

$$ 3 $$

$$ 4 $$

$$ 5 $$

$$ 6 $$

$$ 7 $$

$$ 8 $$

$$ 9 $$

$$ 10 $$

$$ 1 $$

$$ 2 $$

Okay, this seems about right, but the whole point (kinda) is for there to be one digit, so instead of $10$, what about $0$?

$$ 1 $$

$$ 2 $$

$$ 3 $$

$$ 4 $$

$$ 5 $$

$$ 6 $$

$$ 7 $$

$$ 8 $$

$$ 9 $$

$$ 0 $$

$$ 1 $$

$$ 2 $$

That's better, just use the last digit of a number. But you might be asking: What about the equals sign? In this case, the equals sign tells if two numbers have the same last digit, I'll use the O-equals sign for this.

$$ n = 10 $$

$$ k ⊜ k + n $$

$$ k ⊜ k + 2n $$

$$ k ⊜ k + 3n $$

$$ \vdots $$

$$ k ⊜ k - n $$

$$ k ⊜ k - 2n $$

$$ k ⊜ k - 3n $$

$$ \vdots $$

$$ \text{Remember, these are only integers so far!} $$

$$ a ⊜ b \to M(a) = M(b) $$

$$ a ⊜ M(a) $$

A function like $M$ would be useful for converting back and forth, but what should it be? What about $M(k)$ equals the $k$'th term in, I'll call it the modular counting. Also, instead of the objectave of finding what numbers are equal to, you try to find it's $M$. Also, there are only $10$ numbers in modular arithmetic, because

$$ -1 < M(k) < n. $$

$$ k = k_d n + M(k) $$

$$ k ⊜ M(k) \text{, So } M(M(k)) = M(k) \text{.} $$

$$ M(a + b) = ? $$

$$ a = a_d n + M(a) $$

$$ b = b_d n + M(b) $$

$$ M(a + b) = M(a_d n + M(a) + b_d n + M(b)) = M((a_d + b_d) n + M(a) + M(b)) $$

$$ M(a + b) = M(M(a) + M(b)) $$

$$ M(ab) = ? $$

$$ M(ab) = M((a_d n + M(a))(b_d n + M(b))) = M(a_d n b_d n + a_d n M(b) + M(a) b_d n + M(a) M(b)) = M((a_d b_d n + a_d M(b) + b_d M(a)) n + M(a) M(b)) $$

$$ M(ab) = M(M(a)M(b)) $$

$$ M(a - b) = M(M(a) + M(-b)) $$

$$ M(-b) ⊜ -b ⊜ -M(b) $$

$$ M(a - b) = M(M(a) - M(b))) $$

### Non-integers

$$ M(\frac{a}{b}) = M(M(a)M(\frac{1}{b})) $$

Remember, these are only integers so far, this should be the part where you learn about non-integers, but modular arithmetic actually has only $10$ numbers in it. But first, we need to take a leap of faith, the multiplicitave inverse.

$$ 3 \cdot 7 = 21 ⊜ 1 $$

$$ \text{Thus} $$

$$ 7 ⊜ \frac{1}{3} $$

$$ \text{and} $$

$$ 3 ⊜ \frac{1}{7} $$

$$ \frac{5}{7} = 5 \cdot 3 = 15 ⊜ 5. $$

But there is a problem, and it's not $\frac{1}{10}$, but here is the problem with $\frac{1}{10}$ anyways.

$$ 10 ⊜ 0 $$

$$ \frac{1}{10} ? ⊜ ? \frac{1}{0} $$

$$ \frac{1}{10} ⊜ ? $$

$$ ? \cdot 10 ⊜ 1 $$

$$ \text{any number} \cdot 10 ⊜ 0 $$

$$ ? ⊜ \frac{1}{0} $$

$$ \frac{1}{10} ⊜ \frac{1}{0} $$

$$ \text{The problem is that } 1 \text{ divided by a non-} 0 \text{ number is undefined, say } 2. $$

$$ 2 ⊜ / ⊜ 0 $$

$$ \frac{1}{2} ? ⊜ / ⊜ ? \frac{1}{0} $$

$$ \frac{1}{2} ⊜ ? $$

$$ 1 \cdot 2 ⊜ 2 \ne 1 $$

$$ ? \ne 1 $$

$$ 2 \cdot 2 ⊜ 4 \ne 1 $$

$$ ? \ne 2 $$

$$ 3 \cdot 2 ⊜ 6 \ne 1 $$

$$ ? \ne 3 $$

$$ \vdots $$

$$ 5 \cdot 2 ⊜ 0 \text{ again} $$

$$ \vdots $$

$$ 10 \cdot 2 ⊜ 0 \ne 1 $$

$$ ? \ne 3 $$

$$ \frac{1}{2} ⊜ \frac{1}{0} $$

So the promlem is that you can't divide by some non-0 numbers like I said. This happens when you are dividing by a factor of the base of the modulas (the base of the modulas is the term where you restart couning first) and the numerator does not also have a factor of it. Said simply

$$ \frac{a}{b} ⊜ \frac{1}{0} \text{ precisely when } n \text{ divides } b \text{, and } a \text{ does not divide } b. $$

$$ \text{The solution, of coarse, is to swich the base from } 10 \text{ to } 5 $$

$$ n = 5. $$

$$ \text{Side note! } 2 \text{ and } 3 \text{ are } i \text{ and } -i \text{ respectavely. Actually I don't know which is } i \text{ and which is } -i \text{, but here's proof!} $$

$$ i^2 = -1 $$

$$ (-i)^2 = -1 $$

$$ 2^2 = 4 = 5 - 1 ⊜ -1 $$

$$ 3^2 = 9 = 2 \cdot 5 - 1 ⊜ -1 $$

$$ i \cdot -i = 1 $$

$$ 2 \cdot 3 = 6 ⊜ 1 $$


($200$ lines btw)

$$ i + (-i) = 0 $$

$$ -(i) = -i $$

$$ -(-i) = i $$

$$ 2 + 3 = 5 = 5 \cdot 1 + 0 ⊜ 0 $$

$$ -2 = 5 \cdot (-1) + 3 ⊜ 3 $$

$$ -3 = 5 \cdot (-1) + 2 ⊜ 2 $$

So, because $0$ $1$ $i$ $-i$ and $-1$ would multiplty to get another one of $0$ $1$ $i$ $-i$ and $-1$. This means that if you want to multiply numbers mod $5$, just use the beautiful angle addition of the complex plane. Let's try to fnd the mod $7$ equivilant using last monday's work. That took all day. First, the times tables mod $7$

$$ \begin{bmatrix} \times \quad 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
0 \quad 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 \quad 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
2 \quad 0 & 2 & 4 & 6 & 1 & 3 & 5 \\
3 \quad 0 & 3 & 6 & 2 & 5 & 1 & 4 \\
4 \quad 0 & 4 & 1 & 5 & 2 & 6 & 3 \\
5 \quad 0 & 5 & 3 & 1 & 6 & 4 & 2 \\
6 \quad 0 & 6 & 5 & 4 & 3 & 2 & 1 \\ \end{bmatrix} $$

So, I would want numbers $2$ - $5$ to corraspond with letters $a$ - $d$. And no letter for $6$, because it is already equal to $-1$ mod $7$. So the puzzle is to solve for complex numbers $a$ $b$ $c$ and $d$ with the following times table:

$$ \begin{bmatrix} \times \quad 0 & 1 & a & b & c & d & -1 \\
0 \quad 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 \quad 0 & 1 & a & b & c & d & -1 \\
a \quad 0 & a & c & -1 & 1 & b & d \\
b \quad 0 & b & -1 & a & d & 1 & c \\
c \quad 0 & c & 1 & d & a & -1 & b \\
d \quad 0 & d & b & 1 & -1 & c & a \\
-1 \quad 0 & -1 & d & c & b & a & 1 \\ \end{bmatrix} $$

$$ j = \pm i $$

$$ k = -j = \mp i $$

$$ \text{So, mod } 5 $$

$$ 2 = j $$

$$ 3 = k $$

$$ \text{back to mod } 7 \text{ with a more flattened out times table without multiplication by } 0 \text{ or } 1 \text{, because that is pretty self explanitory.} $$

$$ aa = c $$

$$ ab = -1 $$

$$ ac = 1 $$

$$ ad = b $$

$$ a (-1) = d $$

$$ bb = a $$

$$ bc = d $$

$$ bd = 1 $$

$$ b (-1) = c $$

$$ cc = a $$

$$ cd = -1 $$

$$ c (-1) = d $$

$$ dd = c $$

$$ d (-1) = a $$

$$ (-1) (-1) = 1 $$

I'll let you think about it.

SPOILERS BELOW

.

.

.

.

.

.

.

### answer

You might have gussed that all of these have absolute value $1$, but you might not have known that these are the [roots of unity](https://silaspe.github.io/maths/complex_2.html). But remember to use that $j$ thing. And yes, as opposed to $e^{i\theta} = cos(\theta) + i \text{ } sin(\theta)$,

$$ e^{j\theta} = cos(\theta) + j sin(\theta). $$

Also, $300$ lines by the way.

You might have also noticed that these numbers can circle around in two different ways. (I found the $d$ one before the $b$ one by the way)

$$ 1b = b $$

$$ bb = a $$

$$ ab = -1 $$

$$ (-1) b = c $$

$$ cb = d $$

$$ db = 1. $$

and also

$$ 1d = d $$

$$ dd = c $$

$$ cd = -1 $$

$$ (-1) d = a $$

$$ ad = b $$

$$ bd = 1. $$

Here's a diagram of both in the complex plane:

<iframe src="https://www.desmos.com/calculator/romrb3jmbq?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

And for $d$:

<iframe src="https://www.desmos.com/calculator/fhdf4mg7bb?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

And also, if two numbers on the complex plane have absolute value $1$, and they multiply to $1$, then they are complex congegates or as you might know as $ccong$, so the correct picture translating back from letters $a$ - $d$ and $-1$ to numbers $2$ - $5$ and $6$ would be the $b$ - picture with up being $j$ and down being $k$. And here it is:

<iframe src="https://www.desmos.com/calculator/nbtmgnbayw?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

Isn't it beautiful? I can just add the angles and multiply the magnitudes of any two numbers to get their product mod $7$. $6$ is on $-1$ which makes sense because $6 = 7 - 1$. Also, numers on opposite sides add to $7$, and "opposite side" in complex numbers means "negatave", so that is also just so perfect to me to. Also, if two numbers are complex conjugates on the unit circle, then they are inverses of each other, and I've never seen that in a real desmos graph before! Also, that was a bit of a lie, because I'm actually editing on the repo, so the graph isn’t loading, and I would have to click on the tab with the graph to see it. Alternatively, I could just hit the "Commit changes" button on the top-right and wait for $2$ minutes to see it on the website. Yeah, I'll do that.

I will add only this line of text to my website, because it would be sad to add anything else to my website on easter.

I will add only this line of text to my website, because it would be sad to add anything else to my website on April $1$'st. Well, no it wouldn't be, but no one would belive something added on April $1$'st. So I'll take the day off.

Okay, you know the drill. Time to copy paste and tweak the preveous line, just give me a sec... Wait! April $2$'nd is not a holiday. But that means that I have to work today. I think I liked the quadruple weekend more.

And, would you look at that. I forgot to work at all yesterday, and I have to take the day off for family. Like I said many times: I'll imbed the desmos graphs tomorrow, or maybe today if I am lucky

At this point on April $4$'th, I'll just stop working on this page and write down below the day that I imbed the desmos graphs.

April $6$'th, I deleted the thing I did the day before, and that's why it dosen't look different.

### how to make your own diagram for modular arithmetic in base $p$ in the desmos graphing calculator

You don't actually need to write out the full times table, you just have to find the smallest primitave root $r$ of the base (a primitave root of a base is a number where it's power's would result in all different numbers (exept $0$) in the modular base. e.g. $2$ in mod $5$, $2^0 ⊜ 1$, $2^1 ⊜ 2$, $2^2 ⊜ 4$, $2^3 ⊜ 3$, $2^4 ⊜ 1$. One way to find one is to google it, or use brute force) and then put it a $p - 1$'th around the unit circle from $1$, which is just the point ($1$, $0$). Anyways, first boot up [the desmos graphing calculator](https://www.desmos.com/calculator), then I realized that the colors of the functions you draw go red, blue, green, purple, black, and back to red. First, type $x$ and check if it is a good color for your circle,  if it is, remove the letter $x$ and copy this "x^{2}+y^{2}=1" and paste it into desmos, if not, press the button on the top-right of the box that you are writing in, which I will call the $x$ button, and repeat until you either find a good color, or choose the least worst color available. In my case, black. Oh, and paste in `p=1` to make a slider called $p$ and set it to the base that you chose. then do the same thing for the dots, but click on the emptyness underneith the box before pressing the $x$ button. Once you find a good dot color, paste in `\left(0,0\right)`. Then, this is the tricky part, click on the emptyness underneith the box, then press the $x$ button, repeat $5$ times to get the same color, this will be known as "repeat until same color". then copy and paste in `\left(1,0\right)`, repeat until same color, than paste in `\left(\cos\left(\frac{2\pi}{p - 1}\right),\sin\left(\frac{2\pi}{p - 1}\right)\right)`, repeat until same color, than paste in `\left(\cos\left(2\frac{2\pi}{p - 1}\right),\sin\left(2\frac{2\pi}{p - 1}\right)\right)`, repeat until same color, than paste in `\left(\cos\left(3\frac{2\pi}{p - 1}\right),\sin\left(3\frac{2\pi}{p - 1}\right)\right)`... For this reason, you should probably choose $p$ to be small like $5$ or $7$, and I probably should've told you that earlier. Then the best part, press "label" on each dot and click on the big underscore to start naming, the dot in the center is named " $0$ ". the one directly to the right and not up or down is named " $1$ ". The name of the one that directly counterclockwise to the previous is found by multiplying the previous's value by $r$ and subtracting $p$ until you get $0$ or a number less than $p$. And yeah, that's really all there is to it, I'm sorry for those who decided to read through this wall of text (which is the biggest one yet) and didn't just skip to here, but for those pepole who did read this whole thing, you should now have a beautiful diagram for modular arithmatic.

Say goodbye to the modular arithmetic page and say hello to a new page, It's name is the name of the first chapter on the [brainstorm page](https://silaspe.github.io/maths/brainstorm.html) without a question mark... Or just scroll down the dropdown menu or home page.

And with that, the page has ended.
