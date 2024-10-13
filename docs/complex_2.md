## the roots of unity

$$ z = r e^{i \theta} $$

$$ \tau = : 2 \pi $$

$$ e^{i \tau} = 1 $$

$$ e^{k i \tau} = 1 $$

$$ z = r e^{i \theta + k i \tau} $$

$$ z^n = 1 $$

$$ (r e^{i \theta} e^{k i \tau})^n = 1 $$

$$ r^n {e^{i \theta}}^n {e^{k i \tau}}^n = 1 $$

$$ r^n e^{i \theta n} e^{k i \tau n} = 1 $$

$$ r^n = 1 $$

$$ r = 1 $$

$$ e^{i \theta n} e^{k i \tau n} = 1 $$

$$ e^{i \theta n} = e^{m i \tau} $$

$$ (z^n)^m = 1^m = 1 $$

$$ i \theta n = m i \tau $$

$$ \theta n = \tau m $$

$$ \theta = \tau \frac{m}{n} $$

$$ rou_{m, n} = e^{i \tau \frac{m}{n}} $$

The "rou" means root of unity, because unity means $1$, and root because $z$ is the $n$'th root of $1$. but all of the roots of unity can be constructed with what is called the principal value $rou_{1, n}$ (actually no, the principal value is $rou_{0, n}$, so just $1$), but that is:

$$ e^{i \frac{\tau}{n}} $$

This is because the more common $e^{i \tau \frac{m}{n}}$ is just $(e^{i \frac{\tau}{n}})^m$, so the following statement is:

$$ rou_{m, n} = (rou_{1, n})^m $$

$$ rou_n = : rou_{1, n} $$

$$ rou_{m, n} = rou_n^m $$

This also looks kind of like notation, but it is just a power.
