$$ \text{Where we last left off, we were at Maxwell's equations.} $$

$$ \vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0} $$

$$ \vec{\nabla} \times \vec{B} = \mu_0 (\vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t}) $$

$$ \vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

$$ \vec{\nabla} \cdot \vec{B} = 0 $$

$$ \text{That's it!} $$

#### Credits

$$ \text{A.P. (For privacy reasons, I won't say his full name.) He helped sometimes.} $$

$$ \text{Sugey (that's just his username) who made a great introduction to geometric algebra.} $$

$$ \text{Silaspe (me) did evereything else.} $$

#### JK

It would be easier to go from Maxwell's equation (singular) to Maxwell's equations (plural) than to go the other way around. Here it is... After I combine some stuff. (By the way, $i = \hat{x} \hat{y} \hat{z}$ because it is $3d$.)

$$ \text{First, the differentials. There are two, to combine into into the spacetime gradient, the partial derivitave with respect to time (} \frac{\partial}{\partial t} \text{), and the gradient with respect to space (} \vec{\nabla} \text{) (which equals } \frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{y} + \frac{\partial}{\partial z} \hat{z} \text{) this spacetime gradient will be called } \nabla \text{. (As opposed to } \vec{\nabla} \text{.)} $$

$$ \nabla = \frac{\partial}{\partial t} + \vec{\nabla} $$

$$ \text{Actually, no. } $$

$$ \nabla = \frac{1}{c} \frac{\partial}{\partial t} + \vec{\nabla} $$

$$ \text{Doing this may seem familiar if you've worked with relativity enough.} $$

$$ \text{This combonation also makes sense because we now just have the sum of four derivatives (} \nabla = \frac{1}{c} \frac{\partial}{\partial t} + \frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{y} + \frac{\partial}{\partial z} \hat{z} \text{), so in the end, it's pretty similar to the traditional gradient.} $$

$$ \text{Next: combine the sources that create the electric and magnetic fields (to create the source that creates the electromagnetic field), there are two (again), the charge density (} \rho \text{), and the current (} \vec{J} \text{). (by the way, this source will be caled } J \text{, as opposed to } \vec{J} \text{)To combine these, just add them!} $$

$$ J = \rho + \vec{J} $$

$$ \text{Actually, subtract them.} $$

$$ J = \rho - \vec{J} $$

$$ \text{Don't worry about the minus sign.} $$

$$ \text{Actually, wrong again, but this can be fixd by adding a factor of } c \text{ to the charge density.} $$

$$ J = c \rho - \vec{J} $$

$$ \text{Again, this is seen a lot in realitivity, so it's nothing new in physics.} $$

$$ \text{It also gives an interesting new interpretation of charge density as a current that is moving through time and not space.} $$

$$ \text{Finaly, we need to combine the electric and magnetic fields(} \vec{E} \text{ and } \vec{B} \text{) into one electromagnetic field (} F \text{). But unlike before, we can NOT just add them, the issue this time is that they are both vectors, so they're components will mix. But now's the time to kill two birds with one stone, you see, the magnetic feild is traditionally defined with a cross product, and NOT a wedge product, but instead of re-defining the magnetic feild, remember how the wedge product is just } i \text{ times the cross product? Using that instead, we get this:} $$

$$ F = \vec{E} + i \vec{B} $$

$$ \text{Actually, wrong again, again, but this can be fixd by adding a factor of } c \text{ to the magnetic feild.} $$

$$ F = \vec{E} + ic \vec{B} $$

$$ \text{Some pepole actually call } c \vec{B} \text{ the magnetic feild, so this factor of } c \text{ is not too strangely placed.} $$

$$ \text{Are you ready to see Maxwell's equation? (Not to equations (plural), but equation (singular)).} $$

$$ \nabla F = J $$

$$ \text{That's it, this one simple equation describes all electromagnetic phenomina.} $$

$$ \text{Actually, I will admit, I cheated a bit} $$

$$ \nabla F = \frac{J}{c \epsilon_0} $$

$$ \text{I said it that way so that it would look better.} $$

$$ \text{To prove this foumula, we need} $$

#### Maxwell's translation (I just came up with that name.)

