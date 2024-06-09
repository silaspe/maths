This page is not on the website (yet), because it is entirely psudo-code and python code.

### asterisk operator (psudo)
```
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
```
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

### alternitave asterisk operator (python)

```py
def va, b, n):
  if n == 1:
    return a + b
  if n == 2:
    return a*b
  k = a
  for i in range(b - 1):
    k = Asterisk(a, k, n - 1)
```

### the exact digits of square roots (psudo)

404 page not found

### the exact digits of square roots (python) (I have been working on this since this page was made)

```py
def Root(x, y, n):
  f = 0
  while f**x <= y:
    f += 1
  f -= 1
  a = f
  l = 0
  for i in range(n):
    a *= 10
    l += 1
    while a**x <= y*(10**(l*x)):
      a += 1
    a -= 1
  a -= f*(10**l)
  if n > 1:
    return str(f) + '.' + str(a)
  else:
    return str(f)
```

### the exact digits of logarithms (psudo)

404 page not found

### the exact digits of logarithms (python)

```py
def Log(x, y, n):
  f = 0
  while x**f <= y:
    f += 1
  f -= 1
  a = f
  l = 0
  for i in range(n):
    a *= 10
    l += 1
    while x**a <= y**(10**(l)):
      a += 1
    a -= 1
  a -= f*(10**l)
  if n > 1:
    return str(f) + '.' + str(a)
  else:
    return str(f)
```

#### as a cherry on top, the exact digits of the roots of polynomials (psudo)

```
def Roots(p(x), StartValue, n):
  f = StartValue
  while x**f <= y:
    f += 1
  f -= 1
  a = f
  l = 0
  for i in range(n):
    a *= 10
    l += 1
    while p(a*(10**(-l) <= p(y):
(coment) you will have to expand and simplify the equation so that it is a differance of integers
      a += 1
    a -= 1
  a -= f*(10**l)
  if n > 1:
    return str(f) + '.' + str(a)
  else:
    return str(f)
```

### set theory numbers

```py
def SetTheoryNumbers(n):
  string = "{"
  k = n - 1
  while k >= 0:
    string += SetTheoryNumbers(k)
    k -= 1
  string += "}"
  return string
```

### alternitave set theory numbers

```py
def AlmostSetTheoryNumbers(n):
  if n == 0:
    return ""
  return SetTheoryNumbers(n - 1) + AlmostSetTheoryNumbers(n - 1)
```

```py
def SetTheoryNumbers(n):
  return "{" + AlmostSetTheoryNumbers(n) + "}"
```

### base names

```py
def SmallestPrimeDivisor(n):
  k = 2
  while n % k != 0:
    k += 1
  return k
```

```py
def AlmostBase(n):
  if n == 2:
    return "bi"
  if SmallestPrimeDivisor(n) == n:
    return "un" + AlmostBase(n - 1) + "sna"
  string = ""
  k = n
  while k != 1:
    spdk = SmallestPrimeDivisor(k)
    string += AlmostBase(spdk)
    k /= spdk
  return string
```

```py
def base(n):
  if n < 2:
    return "n must be a positave integer!"
  return AlmostBase(n) + "nary"
```

### the exact digits of reciprocals (in any base) (using my home made method)

```py
def frac(n, b):
  if n == 1:
    return "this code can not compute one over one!"
  if b == 1:
    return "the base must not equal one!"
  if n < b:
    nb = n
  else:
    nb = b
  for K in range(nb - 1):
    k = K + 2
    if n % k == 0:
      if b % k == 0:
        return "this code will not work if you give it two numbers that are coprime"
  rem = b % n
  string = "0. repeating " + str(b // n)
  for i in range(n - 2):
    rem *= b
    string += " " + str(rem // n)
    rem %= n
    if rem == 1:
      return string
```

also, this is the $400$'th commit to this branch.
