This page is not on the website (yet), because it is entirely pseudo-code and python code.

### asterisk operator (pseudo)
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
def (a, b, n):
  if n == 1:
    return a + b
  if n == 2:
    return a*b
  k = a
  for i in range(b - 1):
    k = Asterisk(a, k, n - 1)
```

### the exact digits of square roots (pseudo)

404 Page not found.

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

### the exact digits of logarithms (pseudo)

```py
404 Page not found.
```

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

#### as a cherry on top, the exact digits of the roots of polynomials (pseudo)

```
def Roots(p(x), StartValue, n):
  f = StartValue
  while p(f) <= y:
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

### base names (first $n$ values)

```py
def SmallestPrimeDivisor(n):
  k = 2
  while n % k != 0:
    k += 1
  return k
```

```py
for n in range(101):
  L = [None, None]
  if n == 2:
    L += ["bi"]
    print("binary")
  if SmallestPrimeDivisor(n) == n:
    L.append("un" + L[n - 1] + "sna")
    print("un" + AlmostBase(n - 1) + "snanary")
  string = ""
  k = n
  while k != 1:
    spdk = SmallestPrimeDivisor(k)
    string += L[spdk]
    k /= spdk
  L.append(string)
  print(string + "nary")
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

### virus (DO NOT RUN THIS CODE)

```py
def crash(exponent):
  result = "1"
  for i in range(exponent):
    result += result
  return result
```

```py
print(crash(crash(crash(crash(crash(crash(crash(crash(crash(crash(10000)))))))))))
```

### virus #2 (it goes without saying at this point)

```py
result = "1"
while true:
  result += result
  print result
```

### group theory (I've kinda been doing a lot of group theory today and yesterday)

```py
def GroupTheory(TheNumberOfFaces, TransformationNumberOne, TransformationNumberOnesIndex, TransformationNumberTwo, TransformationNumberTwosIndex):
  if (TheNumberOfFaces < 2) or (TransformationNumberOne != "f" and TransformationNumberOne != "r") or (TransformationNumberOnesIndex < 0 or TransformationNumberOnesIndex >= TheNumberOfFaces) or (TransformationNumberTwo != "f" and TransformationNumberTwo != "r") or (TransformationNumberTwosIndex < 0 or TransformationNumberTwosIndex >= TheNumberOfFaces):
    return "that isn't group theory!"
  if TransformationNumberOne == "f":
    if TransformationNumberTwo == "f":
      return "r" + str((TransformationNumberTwosIndex - TransformationNumberOnesIndex) % TheNumberOfFaces)
    return "f" + str((TransformationNumberOnesIndex - TransformationNumberTwosIndex) % TheNumberOfFaces)
  if TransformationNumberTwo == "f":
    return "f" + str((TransformationNumberTwosIndex - TransformationNumberOnesIndex) % TheNumberOfFaces)
  return "r" + str((TransformationNumberOnesIndex + TransformationNumberTwosIndex) % TheNumberOfFaces)
```

### binary

```py
def replace(string, n):
  result = ""
  for i in range(n):
    result += string[i]
  if string[n] == "0":
    result += "1"
  else:
    result += "0"
  for i in range(n + 1, len(string)):
    result += string[i]
  return result
```

```py
def BinarySuccessor(string):
  for i in range(len(string)):
    if string[i] != "0" and string[i] != "1":
      return "this code will not work if you don't give it a binary string!"
  k = 0
  result = string
  while result[k] == "1":
    result = replace(result, k)
    k += 1
  result = replace(result, k)
  return result
```

```py
def binaryfy(n):
  result = "0"
  for i in range(n):
    result = BinarySuccessor(result)
  return result
```

### binary names (I have been procrastinating on this for a month!)

```py
def IsZero(string):
  for i in range(len(string)):
    if string[i] != "0":
      return "false"
  return "true"
```

```py
def IsOne(string):
  for i in range(len(string) - 1):
    if string[i] != "0":
      return "false"
  if string[len(string)] != "1":
    return "false"
  return "true"
```

```py
def BinaryNames(n):
  if n >= 65536
    return "false"
  string = binaryfy(n)
  if IsZero(string) == "true":
    return ""
  if IsOne(string) == "true":
    return "one "
  split = 1
  length = len(string)
  while split < length:
    split *= 2
  split /= 2
  split = length - split
  string_one = ""
  for i in range(split):
    string_one += string[i]
  string_two = ""
  for i in range(split + 1, length):
    string_two += string[i]
  if IsZero(string_one) == "true":
    return string_two
  if length - split == 1
    strpow = "two "
  if length - split == 2
    strpow = "four "
  if length - split == 4
    strpow = "hex "
  if length - split == 8
    strpow = "byte "
  if IsOne(string_one) == "true":
    return strpow + string_two
  return string_one + strpow + string_two
```

### alternitave numbers

```py
def SmallestPrimeDivisor(n):
  k = 2
  while n % k != 0:
    k += 1
  return k
```

```py
def AlmostNumber(n, threshold):
  if n <= threshold and n > 0:
    isPrime = "false"
    return str(n)
  if SmallestPrimeDivisor(n) == n:
    isPrime = "true"
    return "((" + AlmostNumber(n - 1) + ")+1)"
  else:
    isPrime = "false"
  string = ""
  k = n
  while k != 1:
    spdk = SmallestPrimeDivisor(k)
    string += AlmostBase(spdk)
    k /= spdk
  return string
```

```py
def number(n, threshold):
  if isPrime == "false":
    return AlmostNumber(n, threshold)
  result = ""
  for i in range(1, len(AlmostNumber(n, threshold)) - 1):
    result += AlmostNumber(n, threshold)[i]
  return result
```

### magic sequences

[magic sequences](https://www.youtube.com/watch?v=rDDaEVcwIJM&t=2420s)

```py
def MagiSeq(n):
  MagicSequence = [1]
  MagicNext = 1
  for i in range(n - 1):
    MagicNext *= 2
    MagicNext %= n
    MagicSequence += [MagicNext]
    if MagicNext in MagicSequence[:-1]:
      return MagicSequence
```

### The Apocalyptic Numbers

[The Apocalyptic Numbers](https://www.youtube.com/watch?v=0LkBwCSMsX4)

```py
for i in range(1000):
  power = str(2 ** i)
  for j in range(len(power)):
    if power[j] == "6":
      if len(power) >= j + 2:
        if power[j + 1] == "6":
          if power[j + 2] == "6":
            if power[j + 3] != "6":
              result = ""
              for k in range(j):
                result += power[k]
              result += "  666  "
              for k in range(j + 3, len(power)):
                result += power[k]
              if i != 157:
                print()
              print(f"{i}, 2^{i} = {result}")
```

### nsuemtb etrh etohreyo#r#y#

```py
def SmallestPrimeDivisor(n):
  k = 2
  while n % k != 0:
    k += 1
  return k
```

```py
N = 100
```

```py
for n in range(N):
  L = ["", "{}"]
  if SmallestPrimeDivisor(n) == n:
    L.append("{" + L[n - 1] + "}")
    print("{" + L[n - 1] + "}")
  string = "{"
  k = n
  while k != 1:
    spdk = SmallestPrimeDivisor(k)
    string += L[spdk]
    k /= spdk
  L.append(string + "}")
  print(string + "}")
```
