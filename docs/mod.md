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

That's better, just use the last digit of a number. But you might be asking: What about the equals sign? In this case, the equals sign tells if two numbers have the same last digit, I'll use the O-plus sign for this (I couldn't find an O-equals in LaTeX). So instead of trying to find what a number is equal to, you find what a number is O-plus to.

$$ n = 10 $$

$$ k \oplus k + n $$

$$ k \oplus k + 2n $$

$$ k \oplus k + 3n $$

$$ \vdots $$

$$ k \oplus k - n $$

$$ k \oplus k - 2n $$

$$ k \oplus k - 3n $$

$$ \vdots $$

$$ \text{Remember, these are only integers so far!} $$

$$ a \oplus b \to M(a) = M(b) $$

$$ a \oplus M(a) $$

A function like $M$ would be useful for converting back and forth, but what should it be? What about $M(k)$ equals the $k$'th term in, I'll call it the modular counting.

$$ -1 < M(k) < n $$

$$ a = a_d n + M(a) $$

$$ M(a + b) = ? $$

$$ k \oplus M(k) \text{, So } M(M(k)) = M(k) \text{.} $$
