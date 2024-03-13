### First, some history

Before this website was even created, I was on a vacation to europe for family, and I solved at last $2$ puzzles. After that, I said that I solved the strand puzzle and the arctan puzzle. First, I solved the strand puzzle in praha, but I only solved fir $x_n$ and not $y_n$, the time that I truly solved the strand puzzle was while I was writing it down on the page. I solved the strand puzzle first by the way. I know what you might be thinking, what even is the arctan puzzle?

$$ z = a + bi = re^{i\theta} = r(cos(\theta) + i \text{ } sin(\theta)) = rcos(\theta) + irsin(\theta) $$

$$ a = rcos(\theta) $$

$$ b = rsin(\theta) $$

Good, you can convert from polar to cartesian coordinates, but what about back from cartesian to polar? ($r$ Is the distance from the origin at $0$, and $\theta$ is the angle counerclockwise from the positave $x$ axis. I'm saying this, because either I didn't say it earlier, or as a reminder) You would probably use the pythagorian therom to prove this, but this website dosen't heve illustrations, so I will prove the pythagorian therom without geometry. First, take the complex conjegate.

$$ a - bi = rcos(\theta) - irsin(\theta) $$

$$ cos(\theta) = cos(-\theta) $$

$$ -sin(\theta) = sin(-\theta) $$

$$ a - bi = rcos(-\theta) + irsin(-\theta) $$

$$ a - bi = re^{-i\theta} $$

$$ \text{Side note!} $$

$$ ccong{e^{i\theta}} = e^{-i\theta} = \frac{1}{e^{i\theta}} $$

$$ \text{End of side note.} $$

$$ (a + bi)(a - bi) = a^2 - abi + bia + b^2 = a^2 + b^2 = re^{i\theta} re^{-i\theta} = r^2 $$

$$ \text{Side note!.. Again.} $$

$$ r = |z| \text{ The distance from } 0 \text{, get it?} $$

$$ z ccong(z) = |z|^2 $$

$$ ccong(z) = \frac{|z|^2}{z} $$

$$ \frac{1}{z} = \frac{|z|^2}{ccong(z)} $$

$$ \text{End of side note... Again.} $$

$$ a^2 + b^2 = r^2 $$

Okay, that is the pythagonian therom done, bou I was looking for $r$.

$$ r \text{ (Incert is greater than or equal to symbol here.) } 0 $$

$$ r = \sqrt{a^2 + b^2} $$

That's $r$, but what about $\theta$?

$$ \frac{b}{a} = \frac{rsin(\theta)}{rcos(\theta)} = \frac{sin(\theta)}{cos(\theta)} = tan(\theta) $$

$$ \text{Good, } r \text{ dosen't change } \theta $$

$$ \theta = arctan(\frac{b}{a}) = ? $$

There's the arctan. By the way, this was when I used $h$ instead of $dx$. If $arctan = tan^{-1}$, than I tried to find the derivitves of the inverse for the taylor seiries. I accedentally proved the chain rule with the proof that is now on the [calculus](https://silaspe.github.io/maths/derivatives.html) page as a bonus. I thought "different method for finding $\theta$. First, normalise $z$."

$$ ln(z) = ln(e^{i\theta}) = i\theta $$

$$ i^2 = -1 $$

$$ (i) (-i) = 1 $$

$$ \frac{1}{i} = -i $$

$$ \theta = -i \text{ } ln(z) $$

$$ \text{But what about } ln(z) \text{?} $$

$$ \text{You might remember the formula } \frac{a^{dx} - 1}{dx} \text{ for } ln(a) \text{, so let's try that!} $$

$$ \theta = -i \frac{z^{dx} - 1}{dx} $$

$$ \text{But then, what about }z^{dx} \text{?} $$

$$ \theta = -i \text{ } \frac{((1 + i dx)^{\frac{\theta}{dx}})^{dx} - 1}{dx} = \frac{1}{i} \text{ } \frac{(1 + i dx)^\theta - 1}{dx} = \text{ } \frac{(1 + i\theta dx) - 1}{i dx} $$

$$ \theta = \theta $$

So, all that we have proved is that $\theta = \theta$. Yay!

Ok, so that's the end of that train of thought. I googled "derivitave of arctan" for the result. When I found the awnsser $\frac{1}{1 + x^2}$, I diden't find an awnser why. So, of course I asked ChatGPT, the proof went something like this:

Actually, I forgot it and this is my best guess, with $\frac{}{f}$ as the inverse of $f$:

$$ f(\frac{}{f} (x)) = : x $$

$$ \frac{d}{dx} f(\frac{}{{}^f} (x)) = f\prime (\frac{}{f} (x)) \frac{}{f}\prime (x) = 1 $$

$$ \frac{}{f}\prime (x) = \frac{1}{f\prime (\frac{}{f} (x))} $$
