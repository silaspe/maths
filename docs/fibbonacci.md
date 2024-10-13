## fibonacci

$$ F_n = F_{n - 1} + F_{n - 2} $$

$$ F_1 = 1 $$

$$ F_2 = 1 $$

$$ x^2 = x + 1 $$

$$ x = \begin{Bmatrix} \frac{1}{2} + \frac{\sqrt{5}}{2} = \phi \\
\frac{1}{2} - \frac{\sqrt{5}}{2} = \psi \\ \end{Bmatrix} $$

$$ (-\frac{1}{x})^2 = \frac{1}{x^2} $$

$$ 1 = \frac{1}{x} + \frac{1}{x^2} $$

$$ 1 - \frac{1}{x} = \frac{1}{x^2} = (-\frac{1}{x})^2 $$

$$ (-\frac{1}{x})^2 = (-\frac{1}{x}) + 1 $$

$$ x = 1 + \frac{1}{x} $$

$$ -\frac{1}{x} ? = ? x = 1 + \frac{1}{x} $$

$$ -1 - \frac{1}{x} = -x ? = ? \frac{1}{x} $$

$$ -x^2 ? = ? 1 $$

$$ x ? = ? i, -i $$

$$ \phi \ne i $$

$$ \phi \ne -i $$

$$ \psi \ne i $$

$$ \psi \ne -i $$

$$ \text{Thus...} $$

$$ \phi^{-1} = -\psi $$

$$ \psi^{-1} = -\phi $$

$$ \psi^{n - 1} = -\phi \psi^n $$

$$ \phi^{n - 1} = -\psi \phi^n $$

$$ \text{And don't forget that!} $$

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

$$ \phi^{n + 1} = C_{n + 1} \phi + C_n = \phi^n \phi = C_n \phi^2 + C_{n - 1} \phi = C_n \phi + C_n + C_{n - 1} \phi $$

$$ C_{n + 1} = C_n + C_{n - 1} $$

$$ C_n = C_{n - 1} + C_{n - 2} $$

$$ \phi^2 = \phi + 1 = \phi C_2 + C_1 $$

$$ C_1 = 1 $$

$$ C_2 = 1 $$

$$ C_n = F_n $$

$$ \phi^n = F_n \phi + F_{n - 1} $$

$$ \text{Yay, now I can solve for $F_n$ if it weren't for the second fibonacci term, so how can I solve that?} $$

$$ \text{Well, this is only because $\phi^2 = \phi + 1$, but same goes for $\psi$, so...} $$

$$ \psi^n = F_n \psi + F_{n - 1} $$

$$ \text{And subtracting, we get...} $$

$$ \phi^n - \psi^n = F_n \phi + F_{n - 1} -  F_n \psi - F_{n - 1} = (\phi - \psi) F_n = (\frac{1}{2} + \frac{\sqrt{5}}{2} - \frac{1}{2} + \frac{\sqrt{5}}{2}) F_n = \sqrt{5} F_n $$

$$ F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} = \frac{\phi^n - \psi^n}{\phi - \psi} $$

$$ F_n \approx \frac{\phi^n}{\sqrt{5}} $$

### luca numbers

$$ L_n = : F_{n + 1} + F_{n - 1} = L_{n - 1} + L_{n - 2} $$

$$ L_1 = 1 $$

$$ L_2 = 3 $$

$$ L_0 = 2 \text{ And } F_0 = 0 \text{ btw.} $$

$$ L_n = \frac{\phi^{n + 1} - \psi^{n + 1}}{\phi - \psi} + \frac{\phi^{n - 1} - \psi^{n - 1}}{\phi - \psi} = \frac{\phi^{n + 1} - \psi^{n + 1} + \phi^{n - 1} - \psi^{n - 1}}{\phi - \psi} $$

$$ \text{I hope that you remembered!} $$

$$ L_n = \frac{\phi^n \phi - \psi^n \psi - \phi^n \psi + \psi^n \phi}{\phi - \psi} = \frac{\phi^n (\phi - \psi) + \psi^n (\phi - \psi)}{\phi - \psi} $$

$$ L_n = \phi^n + \psi^n $$

$$ L_n \approx \phi^n $$

### fibonacci numbers?

$$ L_{n + 1} + L_{n - 1} = \phi^{n + 1} + \psi^{n + 1} + \phi^{n - 1} + \psi^{n - 1} = \phi^n \phi + \psi^n \psi - \phi^n \psi - \psi^n \phi = \phi^n (\phi - \psi) - \psi^n (\phi - \psi) = \phi^n \sqrt{5} - \psi^n \sqrt{5} = \frac{\phi^n - \psi^n}{\sqrt{5}} 5 $$

$$ L_{n + 1} + L_{n - 1} = 5 F_n $$

$$ F_n = \frac{L_{n + 1} + L_{n - 1}}{5} $$

$$ L_n \phi + L_{n - 1} = (\phi^n + \psi^n) \phi + \phi^{n - 1} + \psi^{n - 1} = \phi^{n + 1} + \psi^n \phi + \phi^{n - 1} - \psi^n \phi = \phi^{n + 1} + \phi^{n - 1} = \phi^n (\phi + \phi^{-1}) $$

$$ \phi^n \sqrt{5} = L_n \phi + L_{n - 1} = \phi^{n + 1} + \phi^{n - 1} $$

$$ \phi^n = \frac{L_n \phi + L_{n - 1}}{\sqrt{5}} = \frac{\phi^{n + 1} + \phi^{n - 1}}{\sqrt{5}} $$

$$ \phi^n = \phi^{n - 1} + \phi^{n - 2} \text{ btw} $$

### everything up 'till now

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

.

$$ F_n \approx \frac{\phi^n}{\sqrt{5}} $$

$$ \phi^n \approx \frac{F_{n + 1}}{F_n} $$

$$ L_n \approx \phi^n $$

### one more thing

$$ \text{how would one combine } \phi^n = F_n \phi + F_{n - 1} \text{ and } \phi^n = \frac{L_n \phi + L_{n - 1}}{\sqrt{5}}? $$

$$ \text{for one, rearrange the second one} $$

$$ \phi^n = F_n \phi + F_{n - 1} $$

$$ \phi^n \sqrt{5} = L_n \phi + L_{n - 1} $$

$$ F_{n - 1} = F_n - F_{n - 2} $$

$$ L_{n - 1} = F_n + F_{n - 2} $$

$$ \phi^n = F_n \phi + F_n - F_{n - 2} $$

$$ \phi^n \sqrt{5} = L_n \phi + F_n + F_{n - 2} $$

$$ (1 + \sqrt{5}) \phi^n = 2 \phi \phi^n = (F_n + L_n) \phi + F_n - F_{n - 2} + F_n + F_{n - 2} = (F_n + L_n) \phi + 2F_n $$

$$ \phi \phi^n = \frac{1}{2} (F_n + L_n) \phi + F_n $$

$$ \phi^n = \frac{1}{2} (F_n + L_n) + F_n \phi^{-1} = \frac{1}{2} F_n + \frac{1}{2} L_n - F_n \psi = \frac{1}{2} F_n + \frac{1}{2} L_n - \frac{1}{2} F_n + \frac{\sqrt{5}}{2} F_n $$

$$ \phi^n = \frac{1}{2} L_n + \frac{\sqrt{5}}{2} F_n \approx \frac{1}{2} \phi^n + \frac{\sqrt{5}}{2} \frac{\phi^n}{\sqrt{5}} = \phi^n $$

## fibonacci 2

$$ S_n = ? $$

$$ S_0 = a $$

$$ S_1 = b $$

$$ S_n = S_{n - 1} + S_{n - 2} $$

$$ F_{-1} = 1 \text{ Btw.} $$

$$ S_2 = a + b $$

$$ S_3 = a + b + b = a + 2b $$

$$ S_4 = a + 2b + a + b = 2a + 3b $$

$$ S_5 = 2a + 3b + a + 2b = 3a + 5b $$

Yes, I know that this text is not centered and is in a different font. I'm tired of proving things that the corresponding youtube narrator just says "I'll leave this as an exercise for the viewer", for example I used lines $58$ thru $88$ just to prove that the numbers that you were seeing were the fibonacci numbers, I got too lazy to prove this next one, so I hate to say it, but I will leave proving the following statement as an exercise for the viewer:

$$ S_n = F_n b + F_{n - 1} a = \frac{(\phi^n - \psi^n) b + (\phi^{n - 1} - \psi^{n - 1}) a}{\phi - \psi} = \frac{\phi^n b - \psi^n b - \psi \phi^n a + \phi \psi^n a}{\phi - \psi} $$

$$ S_n = \frac{\phi^n (b - \psi a) - \psi^n (b - \phi a)}{\phi - \psi} $$
