## fibbonacci

#### WARNING

I don't know why, but it might be hard to scroll on this page, just use the scroll bar instead, anyways enjoy the math!

$$ F_n = F_{n - 1} + F_{n - 2} $$

$$ F_1 = 1 $$

$$ F_2 = 1 $$

$$ x^2 = x + 1 $$

$$ x = \begin{Bmatrix} \frac{1 + \sqrt{5}}{2} = \phi \\
\frac{1 - \sqrt{5}}{2} = \psi \\ \end{Bmatrix} $$

$$ \phi^{-1} = -\psi $$

$$ \psi^{-1} = -\phi $$

$$ \text{and don't forget that!} $$

$$ \phi^2 = \phi + 1 $$

$$ \phi^3 = \phi^2 + \phi = 2 \phi + 1 $$

$$ \phi^4 = 2 \phi^2 + \phi = 3 \phi + 2 $$

$$ \vdots $$

$$ \phi^n = c_{n, n} \phi + c_{n, n - 1} $$

$$ \phi^{n + 1} = c_{n + 1, n + 1} \phi + c_{n + 1, n} = \phi^n \phi = c_{n, n} \phi^2 + c_{n, n - 1} \phi = c_{n, n} \phi + c_{n, n} + c_{n, n - 1} \phi $$

$$ c_{n + 1, n} = c_{n, n} $$

$$ c_{n + 2, n} = c_{n + 1, n} = c_{n, n} $$

$$ \vdots $$

$$ c_{n + k, n} = c_{n, n} $$

$$ C_n = : c_{n, n} $$

$$ \phi^n = C_n \phi + C_{n - 1} $$

$$ \phi^{n + 1} = C_{n + 1} \phi + C_{n, n} = \phi^n \phi = C_n \phi^2 + C_{n - 1} \phi = C_n \phi + C_n + C_{n - 1} \phi $$

$$ C_{n + 1} = C_n + C_{n - 1} $$

$$ C_n = C_{n - 1} + C_{n - 2} $$

$$ \phi^2 = \phi + 1 = \phi C_2 + C_1 $$

$$ C_1 = 1 $$

$$ C_2 = 1 $$

$$ C_n = F_n $$

$$ \phi^n = F_n \phi + F_{n - 1} $$

$$ \text{yay, now I could solve for $F_n$ if it weren't for the second fibbonacci term, so how can I solve that?} $$

$$ \text{well this is only because $\phi^2 = \phi + 1$, but same goes for $\psi$, so...} $$

$$ \psi^n = F_n \psi + F_{n - 1} $$

$$ \text{and subtracting we get...} $$

$$ \phi^n - \psi^n = F_n \phi + F_{n - 1} -  F_n \psi - F_{n - 1} = (\phi - \psi) F_n = (\frac{1 + \sqrt{5}}{2} - \frac{1 - \sqrt{5}}{2}) F_n = \sqrt{5} f_n $$

$$ F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} = \frac{\phi^n - \psi^n}{\phi - \psi} $$

$$ F_n \approx \frac{\phi^n}{\sqrt{5}} $$

### luca numbers

$$ L_n = : F_{n + 1} + F_{n - 1} = L_{n - 1} + L_{n - 2} $$

$$ L_1 = 1 $$

$$ L_2 = 3 $$

$$ \text{$L_0 = 2$ and $F_0 = 0$ btw} $$

$$ L_n = \frac{\phi^{n + 1} - \psi^{n + 1}}{\phi - \psi} + \frac{\phi^{n - 1} - \psi^{n - 1}}{\phi - \psi} = \frac{\phi^{n + 1} - \psi^{n + 1} + \phi^{n - 1} - \psi^{n - 1}}{\phi - \psi} = \frac{\phi^n \phi - \psi^n \psi + \phi^n \phi^{-1} - \psi^n \psi^{-1}}{\phi - \psi} $$

$$ \text{I hope that you remembered!} $$

$$ L_n = \frac{\phi^n \phi - \psi^n \psi - \phi^n \psi + \psi^n \phi}{\phi - \psi} = \frac{\phi^n (\phi - \psi) + \psi^n (\phi - \psi)}{\phi - \psi} $$

$$ L_n = \phi^n + \psi^n $$

$$ L_n \approx \phi^n $$

### fibbonacci numbers?

$$ L_{n + 1} + L_{n - 1} = \phi^{n + 1} + \psi^{n + 1} + \phi^{n - 1} + \psi^{n - 1} = \phi^n \phi + \psi^n \psi + \phi^n \phi^{-1} + \psi^n \psi^{-1} = \phi^n \phi + \psi^n \psi - \phi^n \psi - \psi^n \phi = \phi^n (\phi - \psi) - \psi^n (\phi - \psi) = \phi^n \sqrt{5} - \psi^n \sqrt{5} = \frac{\phi^n - \psi^n}{\sqrt{5}} 5 $$

$$ L_{n + 1} + L_{n - 1} = 5 F_n $$

$$ F_n = \frac{L_{n + 1} + L_{n - 1}}{5} $$

$$ L_n \phi + L_{n - 1} = (\phi^n + \psi^n) \phi + \phi^{n - 1} + \psi^{n - 1} = \phi^{n + 1} + \psi^n \phi + \phi^{n - 1} - \psi^n \phi = \phi^{n + 1} + \phi^{n - 1} = \phi^n (\phi + \phi^{-1}) $$

$$ \phi^n \sqrt{5} = L_n \phi + L_{n - 1} = \phi^{n + 1} + \phi^{n - 1} $$

$$ \phi^n = \frac{L_n \phi + L_{n - 1}}{\sqrt{5}} = \frac{\phi^{n + 1} + \phi^{n - 1}}{\sqrt{5}} $$

$$ \text{$\phi^n = \phi^{n - 1} + \phi^{n - 2}$ btw} $$

### everything up 'til now

$$ F_1 = 1 $$

$$ F_2 = 1 $$

$$ F_0 = 0 $$

$$ \phi^1 = \phi $$

$$ \phi^2 = \phi + 1 $$

$$ \phi^0 = 1 $$

$$ L_1 = 1 $$

$$ L_2 = 3 $$

$$ L_0 = 2 $$

.

$$ F_n = F_{n - 1} + F_{n - 2} $$

$$ \phi^n = \phi^{n - 1} + \phi^{n - 2} $$

$$ L_n = L_{n - 1} + L_{n - 2} $$

.

$$ F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} $$

$$ \phi^n = F_n \phi + F_{n - 1} = \frac{L_n \phi + L_{n - 1}}{\sqrt{5}} $$

$$ L_n = \phi^n + \psi^n $$

.

$$ F_n = \frac{L_{n + 1} + L_{n - 1}}{5} $$

$$ \phi^n = \frac{\phi^{n + 1} + \phi^{n - 1}}{\sqrt{5}} $$

$$ L_n = F_{n + 1} + F_{n - 1} $$
