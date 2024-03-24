## Like the title suggests, what would happen if you restart counting after $10$?

You (supposedly) started counting when you were very young, so starting with counting to the interers, we will rebuild arithmatic from the ground up.

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

$$ \frac{1}{2} ⊜ \frac{1}{0} $$

So the promlem is that you can't divide by some non-0 numbers like I said. This happens when you are dividing by a factor of the base of the modulas (the base of the modulas is the term where you restart couning first) and the numerator does not also have a factor of it. Said simply

$$ \frac{a}{b} ⊜ \frac{1}{0} \text{ precisely when } n \text{ divides } b \text{, and } a \text{ does not divide } b. $$

$$ \text{The solution, of coarse, is to swich the base from } 10 \text{ to } 5 $$

$$ n = 5 $$
