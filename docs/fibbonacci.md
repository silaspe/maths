okay two things, for one, this might be the first time I started a page without any big text (other than the big ghostly text on the top), for another, I'll start by ctrl $+$ c ctrl $+$ v ing the part that I typed out in the eigenstuff page

$$ F_n = F_{n - 1} + F_{n - 2} $$

$$ F_1 = 1 $$

$$ F_2 = 1 $$

$$ F_{n + 1} = ?(F_n) $$

$$ F_n = 1 F_{n - 1} + 1 F_{n - 2} $$

$$ F_{n - 1} = 1 F_{n - 1} + 0 F_{n - 2} $$

$$ \begin{bmatrix} F_n \\
F_{n - 1} \\ \end{bmatrix} = \begin{bmatrix} 1 & 1 \\
1 & 0 \\ \end{bmatrix} \begin{bmatrix} F_{n - 1} \\
F_{n - 2} \\ \end{bmatrix} $$

$$ \lambda = \frac{1 + \sqrt{5}}{2} = \phi, \lambda = \frac{1 - \sqrt{5}}{2} = \psi $$

$$ \phi = : 1 + \frac{1}{\phi} = \frac{1 + \sqrt{5}}{2} $$

$$ \psi = : 1 + \frac{1}{\psi} = \frac{1 - \sqrt{5}}{2} $$

the one with the plus is convergent, the other one is not

$$ r = \frac{1}{\phi}, r =\frac{1}{\psi}  $$

once again, the $\phi$ one is convergent, the $\psi$ one is not.

but, if it is convergent when making the next fibbonacci number, then all possible starting conditions* will eventually approach the $\frac{F_n}{F_{n - 1}} = \phi$, but if that is true than...

*even if it is not stable, if the starting conditions lie directly the alternitave line, the ratio of terms dosen't approach, but always is, $\psi$, but that is irrational so an easy fix is to make both of the enitial conditions integers. Anyways...

$$ \frac{F_{n + 1}}{F_n} \to \phi $$

$$ F_{n + 1} \approx \phi F_n $$

### luca numbers

$$ L_N = : F_{n - 1} + F_{n + 1} = L_{n - 2} + L_{n - 1} $$
