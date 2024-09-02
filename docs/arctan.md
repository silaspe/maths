### First, some history

Before this website was even created, I was on a vacation to europe for family, and I solved at last $2$ puzzles. After that, I said that I solved the strand puzzle and the arctan puzzle. First, I solved the strand puzzle in praha, but I only solved fir $x_n$ and not $y_n$, the time that I truly solved the strand puzzle was while I was writing it down on the page. I solved the strand puzzle first by the way. I know what you might be thinking,

## what even is the arctan puzzle?

$$ z = a + bi = re^{i\theta} = r(cos(\theta) + i \text{ } sin(\theta)) = rcos(\theta) + irsin(\theta) $$

$$ a = rcos(\theta) $$

$$ b = rsin(\theta) $$

Good, you can convert from polar to cartesian coordinates, but what about back from cartesian to polar? ($r$ Is the distance from the origin at $0$, and $\theta$ is the angle counerclockwise from the positave $x$ axis. I'm saying this, because either I didn't say it earlier, or as a reminder) You would probably use the pythagorian therom to prove this, but this website doesn't heve illustrations, so I will prove the pythagorian therom without geometry. First, take the complex conjegate.

$$ a - bi = rcos(\theta) - irsin(\theta) $$

$$ cos(\theta) = cos(-\theta) $$

$$ -sin(\theta) = sin(-\theta) $$

$$ a - bi = rcos(-\theta) + irsin(-\theta) $$

$$ a - bi = re^{-i\theta} $$

$$ \text{Side note!} $$

$$ \text{ccong} (e^{i\theta}) = e^{-i\theta} = \frac{1}{e^{i\theta}} $$

$$ \text{End of side note.} $$

$$ (a + bi)(a - bi) = a^2 - abi + bia + b^2 = a^2 + b^2 = re^{i\theta} re^{-i\theta} = r^2 $$

$$ \text{Side note!.. Again.} $$

$$ r = |z| \text{ The distance from } 0 \text{, get it?} $$

$$ z \text{ ccong} (z) = |z|^2 $$

$$ \text{ccong} (z) = \frac{|z|^2}{z} $$

$$ \frac{1}{z} = \frac{|z|^2}{\text{ccong} (z)} $$

$$ \text{End of side note... Again.} $$

$$ a^2 + b^2 = r^2 $$

Okay, that is the pythagonian therom done, bou I was looking for $r$.

$$ r \text{ (Insert is greater than or equal to symbol here.) } 0 $$

$$ r = \sqrt{a^2 + b^2} $$

That's $r$, but what about $\theta$?

$$ \frac{b}{a} = \frac{rsin(\theta)}{rcos(\theta)} = \frac{sin(\theta)}{cos(\theta)} = tan(\theta) $$

$$ \text{Good, } r \text{ doesn't change } \theta! $$

$$ \theta = arctan(\frac{b}{a}) = ? $$

There's the arctan. By the way, this was when I used $h$ instead of $dx$. If $arctan = tan^{-1}$, than I tried to find the derivitves of the inverse for the taylor seiries. I accedentally proved the chain rule with the proof that is now on the [calculus page](https://silaspe.github.io/maths/derivatives.html) as a bonus. I thought "different method for finding $\theta$. First, normalise $z$."

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

Ok, so that's the end of that train of thought. I googled "derivitave of arctan" for the result. When I found the awnser $\frac{1}{1 + x^2}$, I diden't find an awnser why. So, of course I asked ChatGPT, the proof went something like this:

Actually, I forgot it and this is my best guess, with $\frac{}{f}$ as the inverse of $f$:

### derivitave of arctan

$$ f(\frac{}{f} (x)) = : x $$

$$ \frac{d}{dx} f(\frac{}{{}^f} (x)) = f\prime (\frac{}{f} (x)) \frac{}{f}\prime (x) = 1 $$

$$ \frac{}{f}\prime (x) = \frac{1}{f\prime (\frac{}{f} (x))} $$

$$ f(x) = tan(x) $$

$$ \frac{}{f} = arctan(x) $$

$$ arctan\prime (x) = \frac{1}{tan\prime (arctan(x))} $$

$$ \text{Oh! I forgot to tell you about (well, for one, it's pi day today) the other trigonometric functions other than } \text{sin} \text{ pronounced "sine", and } cos \text{ pronounced "cosine" or "cos", but I prefer cosine, theres } tan = \frac{sin}{cos} \text{ pronounced "tan" or "tangent", which I use interchangibly in real life, and it's inverse } arctan \text{ pronounced execly how it is spelled, but theres also } sec = \frac{1}{cos} \text{ pronounced "secant" or "sec", but I prefer secant, but theres also } csc = \frac{1}{sin} \text{ counterintuitivly, but it's pronounced "cosec" or "cosecant", but I prefer cosec. You can also square any of these for a } 2 \text{ superscript in front of the function instead of the parenthasies} $$

$$ tan\prime (x) = (\frac{sin(x)}{cos(x)}) \prime = \frac{sin\prime (x) cos(x) - sin(x) cos\prime (x)}{cos^2(x)} = \frac{cos(x) cos(x) + sin(x) sin(x)}{cos^2(x)} $$

$$ \text{Okay, we have } cos^2 + sin^2 \text{. Eccept, I still have to derive that.} $$

$$ z = e^{i\theta} = r(cos(\theta) + i \text{ } sin(\theta)) = rcos(\theta) + irsin(\theta) $$

$$ r = 1 $$

$$ z = cos(\theta) + isin(\theta) = a + bi $$

$$ a = cos(\theta) $$

$$ b = sin(\theta) $$

$$ r = \sqrt{a^2 + b^2} $$

$$ cos^2 (\theta) + sin^2 (\theta) = 1 $$

$$ \text{Okay, time to keep going.} $$

$$ tan\prime (x) = \frac{1}{cos^2(x)} $$

$$ tan\prime (x) = sec^2 (x) $$

$$ tan^2 (x) = \frac{sin^2 (x)}{cos^2 (x)} = \frac{sin^2 (x) + cos^2 (x) - cos^2 (x)}{cos^2 (x)} = \frac{sin^2 (x) + cos^2 (x)}{cos^2 (x)} - \frac{cos^2 (x)}{cos^2 (x)} $$

$$ tan^2 (x) = sec^2 (x) - 1 $$

$$ arctan\prime (x) = \frac{1}{sec^2 (arctan(x))} = \frac{1}{1 + sec^2 (arctan(x)) - 1} = \frac{1}{1 + tan^2 (arctan(x))} = \frac{1}{1 + tan(arctan(x))tan(arctan(x))} $$

$$ arctan\prime (x) = \frac{1}{1 + x^2} $$

### Many weeks later...

I asked ChatGPT for awnsers, and it solved it immediety. This is why I called the arctan puzzle the "tricky puzzle that took $1$ ChatGPT search to solve". Warning: This counts as a [taylor seiries](suibl.aisop/em.agtihtsh/) (404 page not found) for $arctan(x)$ in the interval $-1 < x < 1$ (or equal to $1$!)

$$ arctan(0) = 0 $$

$$ arctan(x) = \int_{0}^{x} \frac{1}{1 + t^2} dt $$

#### Quick tangent (no pun intended, plus this is more about arctan than tan)

$$ \sum\limits_{n=0}^{\infty}x^n = ? $$

$$ \text{By the convention in the harmonic page below, if } -1 < x < 1 \text{, than the powers of } x \text{ approach } 0 $$

[.](https://silaspe.github.io/maths/harmonic.html#frac1infty)

$$ ? x = x \sum\limits_{n=0}^{\infty}x^n = \sum\limits_{n=0}^{\infty}x^{n + 1} = \sum\limits_{n=1}^{\infty + 1}x^n = \sum\limits_{n=0}^{\infty}x^n - x^0 + x^{\infty + 1} $$

$$ x^0 = 1 $$

$$ x^{\infty + 1} \to 0 $$

$$ ? x = ? - 1 $$

$$ ? (x - 1) = -1 $$

$$ ? = \frac{-1}{x - 1} $$

$$ \sum\limits_{n=0}^{\infty}x^n = \frac{1}{1 - x} $$

#### back on track

$$ \frac{1}{1 + x^2} = \frac{1}{1 - (-x^2)} = \sum\limits_{n=0}^{\infty} (-x^2)^n = \sum\limits_{n=0}^{\infty} (-1)^n x^{2n} $$

$$ arctan(x) = \int_{0}^{x} \sum\limits_{n=0}^{\infty} (-1)^n t^{2n} dt = \sum\limits_{n=0}^{\infty} \int_{0}^{x} (-1)^n t^{2n} dt $$

$$ \int_{0}^{x} (-1)^n t^{2n} dt = (-1)^n \frac{x^{2n + 1}}{2n + 1} $$

$$ arctan(x) = \sum\limits_{n=0}^{\infty} (-1)^n \frac{x^{2n + 1}}{2n + 1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} \dots $$
