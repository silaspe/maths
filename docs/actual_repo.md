This page is not on the website (yet), because it is entirely psudo-code and python code.

### asterisk operator (psudo)

define Asterisk(x,y,n)
  (coment) if n is 1, it is adding x and y
  (coment) if n is 2, it is multiplying x and y
  (coment) if n is 3, it is it is taking x to the power of y
  (coment) and so on.
  
  if n = 1
    return x + y

  (coment) because I said that earlier.

  else if y = 1
    return x

  (coment) x times 1 = x, x to the power of 1 = x, ect

  else 
    return Asterisk(x,Asterisk(x,y - 1,n),n - 1)

  (coment) this makes sense if you think about it.

### asterisk operator (python)

```py
def Asterisk(a, b, n):
  if n == 1:
    return a + b
  elif n == 2:
    return a*b
  elif b == 1:
    return a
  else:
    return Asterisk(a,Asterisk(a,b - 1,n),n - 1)
```

### the exact digits of square roots (psudo)

### the exact digits of square roots (python)

```py
def Root(x, y, n):
  f = 0
  while f^x <= y:
    f += 1
  f -= 1
  a = f
  l = 0
  t = n - 1
  for t:
    a *= 10
    l += 1
    while a^x <= y*(10^(lx)):
      a += 1
    a -= 1
  a -= f*(10^l)
  if n >> 1:
    return (str(f) + str(.)) + str(a)
  else:
    return str(f)
```

### the exact digits of logarithms (psudo)

### the exact digits of logarithms (python)
