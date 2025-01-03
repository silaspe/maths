$$ \text{Where we last left off, we were at Maxwell's equations.} $$

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$

$$ \vec{\nabla} \times \vec{B} = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

$$ \vec{\nabla} \cdot \vec{B} = 0 $$

$$ \text{That is, in the order of: Gauss's law, Ampere's law, Faraday's law, } \vec{\nabla} \cdot \vec{B} = 0 \text{'s law.} $$

$$ \text{That's it!} $$

#### Credits

$$ \text{A.P. (For privacy reasons, I won't say his full name.) He helped sometimes.} $$

$$ \text{Sudgy (that's just his username) who made a great introduction to geometric algebra.} $$

$$ \text{Silaspe (me) did everything else.} $$

#### JK

It would be easier to go from Maxwell's equation (singular) to Maxwell's equations (plural) than to go the other way around. Here it is... After I combine some stuff. (By the way, $i = \hat{x} \hat{y} \hat{z}$ because it is $3d$.)

#### the spacetime gradient

$$ \text{First, the differentials. There are two, to combine into into the spacetime gradient, the partial derivative with respect to time (} \frac{\partial}{\partial t} \text{), and the gradient with respect to space (} \vec{\nabla} \text{) (which equals } \frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{y} + \frac{\partial}{\partial z} \hat{z} \text{) this spacetime gradient will be called } \nabla \text{. (As opposed to } \vec{\nabla} \text{.)} $$

$$ \nabla = \frac{\partial}{\partial t} + \vec{\nabla} $$

$$ \text{Actually, no. } $$

$$ \nabla = \frac{1}{c} \frac{\partial}{\partial t} + \vec{\nabla} $$

Doing this may seem familiar if you've worked with [realitivity](https://silaspe.github.io/maths/derivaives.html?query=This_is_my_broken_website!) enough.

$$ \text{This combination also makes sense because we now just have the sum of four derivatives (} \nabla = \frac{1}{c} \frac{\partial}{\partial t} + \frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{y} + \frac{\partial}{\partial z} \hat{z} \text{), so in the end, it's pretty similar to the traditional gradient.} $$

#### the electromagnetic source

$$ \text{Next: combine the sources that create the electric and magnetic fields (to create the source that creates the electromagnetic field), there are two (again), the charge density (} \rho \text{), and the current (} \vec{J} \text{). (by the way, this source will be called } J \text{, as opposed to } \vec{J} \text{)To combine these, just add them!} $$

$$ J = \rho + \vec{J} $$

$$ \text{Actually, subtract them.} $$

$$ J = \rho - \vec{J} $$

$$ \text{Don't worry about the minus sign.} $$

$$ \text{Actually, wrong again, but this can be fixed by adding a factor of } c \text{ to the charge density.} $$

$$ J = c \rho - \vec{J} $$

Again, this is seen a lot in [realitivity](https://www.youtube.com/@LolGet404NotFound-Ed), so it's nothing new in physics.

$$ \text{It also gives an interesting new interpretation of charge density as a current that is moving through time and not space.} $$

#### the electromagnetic field

$$ \text{Finally, we need to combine the electric and magnetic fields(} \vec{E} \text{ and } \vec{B} \text{) into one electromagnetic field (} F \text{). But unlike before, we can NOT just add them, the issue this time is that they are both vectors, so they're components will mix. But now's the time to kill two birds with one stone, you see, the magnetic field is traditionally defined with a cross product, and NOT a wedge product, but instead of re-defining the magnetic field, remember how the wedge product is just } i \text{ times the cross product? Using that instead, we get this:} $$

$$ F = \vec{E} + i \vec{B} $$

$$ \text{Actually, wrong again, again, but this can be fixed by adding a factor of } c \text{ to the magnetic field.} $$

$$ F = \vec{E} + ic \vec{B} $$

$$ \text{Some people actually call } c \vec{B} \text{ the magnetic field, so this factor of } c \text{ is not too strangely placed.} $$

$$ \text{Are you ready to see Maxwell's equation? (Not to equations (plural), but equation (singular)).} $$

$$ \nabla F = J $$

$$ \text{That's it, this one simple equation describes all electromagnetic phenomena.} $$

$$ \text{Actually, I will admit, I cheated a bit} $$

$$ \nabla F = \frac{J}{c \epsilon_0} $$

$$ \text{I said it that way so that it would look better.} $$

$$ \text{To prove this formula, we need} $$

### Maxwell's translation (I just came up with that name.)

$$ \text{First, expand out all of the definitions that we made earlier.} $$

$$ (\frac{1}{c} \frac{\partial}{\partial t} + \vec{\nabla}) \text{ } (\vec{E} + ic \vec{B}) = \frac{c \rho - \vec{J}}{c \epsilon_0} $$

$$ \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + \vec{\nabla} \vec{E} + ic \frac{1}{c} \frac{\partial \vec{B}}{\partial t} + ic \vec{\nabla} \vec{B} = \frac{c \rho - \vec{J}}{c \epsilon_0} $$

$$ \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + \vec{\nabla} \cdot \vec{E} + \vec{\nabla} ∧ \vec{E} + i \frac{\partial \vec{B}}{\partial t} + ic \vec{\nabla} \cdot \vec{B} + ic \vec{\nabla} ∧ \vec{B} = \frac{c \rho}{c \epsilon_0} - \frac{\vec{J}}{c \epsilon_0} $$

$$ \vec{\nabla} \cdot \vec{E} + \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + ic \vec{\nabla} ∧ \vec{B} + \vec{\nabla} ∧ \vec{E} + i \frac{\partial \vec{B}}{\partial t} + ic \vec{\nabla} \cdot \vec{B} = \frac{\rho}{\epsilon_0} - \frac{\vec{J}}{c \epsilon_0} $$


$100$ Lines.

$$ \vec{\nabla} \cdot \vec{E} = \text{A scalar} $$

$$ \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + ic \vec{\nabla} ∧ \vec{B} = \text{a vector} $$

$$ \vec{\nabla} ∧ \vec{E} + i \frac{\partial \vec{B}}{\partial t} = \text{a bivector} $$

$$ ic \vec{\nabla} \cdot \vec{B} = \text{a trivector} $$

$$ \text{And on the right hand side:} $$

$$ \frac{\rho}{\epsilon_0} = \text{A scalar} $$

$$ \frac{\vec{J}}{c \epsilon_0} = \text{a vector.} $$

$$ \text{But then, you realize (or, at least, I realize) } 2 \text{ things, } 1 \text{: there are also bivector and trivector components on the right, but they are both } 0 \text{, } 2 \text{: for both to be equal, they must have the same scalar component, vector component, bivector component, and trivector component. So, we can derive four new equations:} $$

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$

$$ \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + ic \vec{\nabla} ∧ \vec{B} = -\frac{\vec{J}}{c \epsilon_0} $$

$$ \vec{\nabla} ∧ \vec{E} + i \frac{\partial \vec{B}}{\partial t} = 0 $$

$$ ic \vec{\nabla} \cdot \vec{B} = 0 $$

$$ \text{The first equation is Gauss's law!} $$

$$ \text{Second equation:} $$

$$ \frac{1}{c^2} \frac{\partial \vec{E}}{\partial t} + i \vec{\nabla} ∧ \vec{B} = -\frac{\vec{J}}{c^2 \epsilon_0} $$

$$ c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} $$

$$ c^2 = \frac{1}{\mu_0 \epsilon_0} $$

$$ \frac{1}{c^2} = \mu_0 \epsilon_0 $$

$$ \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} + i \vec{\nabla} ∧ \vec{B} = -\frac{1}{c^2} \frac{\vec{J}}{\epsilon_0} $$

$$ \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} + i \vec{\nabla} ∧ \vec{B} = -\mu_0 \epsilon_0 \frac{\vec{J}}{\epsilon_0} $$

$$ \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} + i \vec{\nabla} ∧ \vec{B} = -\mu_0 \vec{J} $$

$$ \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} + i^2 \vec{\nabla} \times \vec{B} = -\mu_0 \vec{J} $$

$$ \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} - \vec{\nabla} \times \vec{B} = -\mu_0 \vec{J} $$

$$ -\vec{\nabla} \times \vec{B} = -\mu_0 \vec{J} - \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} $$

$$ \vec{\nabla} \times \vec{B} = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \text{We now have Ampere's law.} $$

$$ \text{Third equation:} $$

$$ i \vec{\nabla} \times \vec{E} + i \frac{\partial \vec{B}}{\partial t} = 0 $$

$$ \vec{\nabla} \times \vec{E} + \frac{\partial \vec{B}}{\partial t} = 0 $$

$$ \vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

$$ \text{We now have Faraday's law.} $$

$$ \text{Finally, we have the fourth (and easiest equation after Gauss's law):} $$

$$ \vec{\nabla} \cdot \vec{B} = 0 $$

and, that proves it! (and in the original order as a bonus.) (Insert text here about how I had a lot of fun in this $3$ month long journey (started on Apr $16$), and that I could go on for an entire page about using geometric algebra for group theory, number theory, modular arithmetic, and so on. And how, if only, this was the $500$'th commit to this website.) And, with that, the page has ended, thanks for watching! (Sorry, reading. I watch way too much youtube.)

### Credits

$$ \text{I think that I already did this part.} $$

.

.

.

.

.

.

.

.

.

.

.

.

.

$200$ Lines.

.

.

.

.

.

### post credit scene

even if Hestenes' law (I looked it up (on ChatGPT), that is the name of $\nabla F = \frac{J}{c \epsilon_0}$) is more compressed, it is an equality of multivectors, and there should be a version that has four different equations, except they are about $k$-vectors (slightly less confusing). Also, if you don't know how to use $\nabla$, $J$, $F$, and the geometric product, then you shouldn't have to (the wedge product just makes sense). But still, a few things should be simplified (e.g. every cross product) (I will use the $\rightarrow$ sign to denote a re-definition), and I will be adding these definitions as I go.

$$ \text{First, } B = i \vec{B} \text{ is a must have.} $$

Do you remember when we turned the equality of multivectors into four equalities of $k$-vectors that were turned into Maxwell's equations? That means that Maxwell's equations seem like a good starting point. Let's go from easiest to hardest, so, first, Gauss's law.

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$

$$ \text{Ok, it has an electric field (I approve), a dot product (I approve), and a bunch of other things that I approve of. In total, I approve.} $$

$$ \text{Next, Faraday's law.} $$

$$ \vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

$$ \frac{\vec{\nabla} ∧ \vec{E}}{i} = \frac{-\frac{\partial B}{\partial t}}{i} $$

$$ \vec{\nabla} ∧ \vec{E} = -\frac{\partial B}{\partial t} $$

$$ \text{Next, } \vec{\nabla} \cdot \vec{B} = 0 \text{'s law.} $$

$$ \vec{\nabla} \cdot \vec{B} = 0 $$

$$ \text{You can't really just go } \vec{\nabla} \cdot \frac{B}{i} = 0 \text{, } \frac{\vec{\nabla} \cdot B}{i} = 0 \text{, } \vec{\nabla} \cdot B = 0 \text{, because that is not necessarily true, you see, } U ∧ (VW) \text{ does not necessarily equal } (U ∧ V) W \text{, Instead, you have to think about what } \vec{\nabla} \cdot \vec{B} = 0 \text{ is trying to say.} $$

$$ \text{Actually, I checked, you can just go } \vec{\nabla} \cdot \frac{B}{i} = 0 \text{, } \frac{\vec{\nabla} \cdot B}{i} = 0 \text{, } \vec{\nabla} \cdot B = 0 \text{!} $$

$$ \vec{\nabla} \cdot B = 0 $$

#### Maxwell's alternative equations

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$

$$ \vec{\nabla} \cdot B = 0 $$

$$ \vec{\nabla} ∧ \vec{E} = -\frac{\partial B}{\partial t} $$

$$ \text{And, I can't figure out Ampere's law. The most recent attempt where I expanded out Hesthenes' law with bivector } B \text{ ended up with } 4 \text{ really weird equations. If I eventually figure it out, or someone else solves an equivalent problem, I'll put it below this text.} $$

### Ampere's law

$$ \text{Actually, I checked, you can't just go } \vec{\nabla} \cdot \frac{B}{i} = 0 \text{, } \frac{\vec{\nabla} \cdot B}{i} = 0 \text{, } \vec{\nabla} \cdot B = 0 \text{. The true equation for } \vec{\nabla} \cdot B \text{ was called "Ampere's law" by, I forgot his name. Here's } \vec{\nabla} \cdot \vec{B} = 0 \text{/Ampere's law anyways.} $$

$$ \vec{\nabla} \cdot B = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \text{But then I realized, there should be } 5 \text{ equations, one for } \vec{\nabla} \cdot \vec{E} \text{, one for } \vec{\nabla} ∧ \vec{E} \text{, one for } \vec{\nabla} \cdot B \text{, one for } \vec{\nabla} ∧ B \text{, and one for } \vec{\nabla} ∘ B \text{. (That I will name after the person who discovers it first.)} $$

$$ \text{Let me explain what this "∘" thing is. First, it is the "surface product" as opposed to dot product or wedge product (in between the inner and outer products). If } \vec{\nabla} \cdot \text{ is the divergence and } \vec{\nabla} ∧ \text{ is the curl, } \vec{\nabla} ∘ \text{ is the "semicurl".} $$

$$ \text{But what actually is ∘? } \Lambda \text{wnser: (well, it's a thing that I came up with, but) } \vec{U} \vec{V} \text{ for bivectors } \vec{U} \text{ and } \vec{V} \text{ is } \vec{U} \cdot \vec{V} + \vec{U} ∧ \vec{V} + \vec{U} ∘ \vec{V} \text{ (actually, } \vec{U} ∧ \vec{V} \text{ is a } 4 \text{-vector, so the following statement only works in } 4 \text{d or higher). You see, if you multiply } \vec{U} \text{ and } \vec{V} \text{ numerically, you get a scalar (the dot product), a } 4 \text{-vector (the wedge product), and a bivector (the surface product). Actually, there is a handy formula for the geometric product of an } n \text{-vector and a } k \text{-vector, it's an } |n - k| \text{-vector, plus an } |n - k| + 2 \text{-vector, plus an } |n - k| + 4 \text{-vector, all the way to an } n + k \text{-vector. The } |n - k| \text{-vector is the dot product, the } n + k \text{-vector is the wedge product, and everything else is a surface product. But for bivectors, there is only one, and if there is more than one, the bivector one would be ∘}_2 \text{, the trivector one would be ∘}_3 \text{, the } 4 \text{-vector one would be ∘}_4 \text{, and the } k \text{-vector one would be ∘}_k \text{.} $$

#### plan of attack!

$$ \text{OG Ampere's law:} $$

$$ \vec{\nabla} \times \vec{B} = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \text{I'll just focus on the left side of this equation for now.} $$

$$ \frac{\vec{\nabla} ∧ \vec{B}}{i} $$

$$ \frac{1}{i} (\vec{\nabla} ∧ \vec{B}) $$

$$ \frac{1}{i} (\vec{\nabla} ∧ \frac{B}{i}) $$

$$ \frac{1}{i} (\vec{\nabla} ∧ ((\frac{1}{i} B)) $$

$$ i^2 = -1 $$

$$ i i = -1 $$

$$ -i i = 1 $$

$$ (i)(-i) = 1 $$

$$ \frac{1}{i} = -i $$

$$ \frac{1}{i} (\vec{\nabla} ∧ (-iB)) $$

$$ (c \vec{u}) ∧ \vec{v} = c (\vec{u} ∧ \vec{v}) \text{ (For scalar } c \text{.)} $$

$$ -\frac{1}{i} (\vec{\nabla} ∧ (iB)) $$

$$ \frac{1}{-i} (\vec{\nabla} ∧ (iB)) $$

$$ \frac{1}{-i} (\vec{\nabla} ∧ (iB)) = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$300$ Lines.

$$ \vec{\nabla} ∧ (iB) = -i \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \text{So, the problem essentially boils down to finding } \vec{u} ∧ (iV) \text{.} $$

$$ \vec{u} = u_1 \hat{x} + u_2 \hat{y} + u_3 \hat{z} $$

$$ V = V_1 \hat{x} \hat{y} + V_2 \hat{x} \hat{z} + V_3 \hat{y} \hat{z} $$

$$ iV = (V_1 \hat{x} \hat{y} + V_2 \hat{x} \hat{z} + V_z \hat{y} \hat{z}) \hat{x} \hat{y} \hat{z} = V_1 \hat{x} \hat{y} \hat{x} \hat{y} \hat{z} + V_2 \hat{x} \hat{z} \hat{x} \hat{y} \hat{z} + V_3 \hat{y} \hat{z} \hat{x} \hat{y} \hat{z} = - V_1 \hat{x} \hat{x} \hat{y} \hat{y} \hat{z} - V_2 \hat{x} \hat{x} \hat{z} \hat{y} \hat{z} - V_3 \hat{y} \hat{z} \hat{y} \hat{x} \hat{z} = - V_1 \hat{z} - V_2 \hat{z} \hat{y} \hat{z} + V_3 \hat{y} \hat{y} \hat{z} \hat{x} \hat{z} = - V_1 \hat{z} + V_2 \hat{z} \hat{z} \hat{y} + V_3 \hat{z} \hat{x} \hat{z} = - V_1 \hat{z} + V_2 \hat{y} - V_3 \hat{z} \hat{z} \hat{x} = - V_1 \hat{z} + V_2 \hat{y} - V_3 \hat{x} $$

$$ iV = - V_3 \hat{x} + V_2 \hat{y} - V_1 \hat{z} $$
