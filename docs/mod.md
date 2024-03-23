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
