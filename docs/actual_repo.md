WARING: when new code is added, it has not been debugged.

This page is not on the website (yet), because it is entirely pseudo-code and python code.

### asterisk operator (pseudo)
```
define Asterisk(x,y,n)
  (comment) if n is 1, it is adding x and y
  (comment) if n is 2, it is multiplying x and y
  (comment) if n is 3, it is it is taking x to the power of y
  (comment) and so on.
  
  if n = 1
    return x + y

  (comment) because I said that earlier.

  else if y = 1
    return x

  (coment) x times 1 = x, x to the power of 1 = x, ect

  else 
    return Asterisk(x,Asterisk(x,y - 1,n),n - 1)

  (comment) this makes sense if you think about it.
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
    print("un" + L[n - 1] + "snanary")
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

### crash (DO NOT RUN THIS CODE)

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

### crash #2 (it goes without saying at this point)

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

### Big numbers and Transfinite ordinals

#### fast-growing hierachies

```py
def f(x, n):
  if n == 0:
    return x + 1
  if n == 1:
    return 2 * x
  if n == 2:
    return x * 2 ** x
  k = x
  for i in range(x):
    k = f(n - 1, k)
  return k
```

#### omega

```py
def omega(x):
  return f(x, x)
```

#### epsilon

```py
def epsilon_subscript(x, n):
  if n == 0:
    result = x
    for i in range(x - 1):
      result = x ** result
    return result
  result = epsilon_subscript(x, n - 1)
  for i in range(x - 1):
    result = epsilon_subscript(x, n - 1) ** result
  return result
```

```py
def epsilon(x, n):
  return f(x, epsilon_subscript(x, n))
```

#### phi

```py
def veblen_subscript(n, x, y):
  if n == 0:
    return x ** y
  if n == 1:
    return epsilon_subscript(x, y)
  if y == 0:
    k = 0
    for i in range(x):
      k = veblen_subscript(n - 1, x, k)
    return k
  k = veblen_subscript(n, x, y - 1)
  m = k
  for i in range(x - 1):
    k = m ** k
  for j in range(1, n):
    for l in range(x - 1):
      k = veblen_subscript(j, x, k)
  return k
```

```py
def veblen(n, x, y):
  return f(x, veblen_subscript(n, x, y))
```

#### gamma

```py
def gamma(x):
  k = 0
  for i in range(x):
    k = veblen_subscript(k, x, 0)
  return k
```

### essentially crash #3 (it goes without saying, so I'm not going to)

```py
x = f(x, gamma(x) + 1729)
```

### computer within a computer

```py
def AND(b1, b2):
  if b1 == 0:
    return 0
  return b2
```

```py
def OR(b1, b2):
  if b1 == 1:
    return 1
  return b2
```

```py
def NOT(b1):
  if b1 == 0:
    return 1
  return 0
```

```py
def bnot(b1, b2):
  return AND(b1, NOT(b2))
```

```py
def XOR(b1, b2):
  return OR(bnot(b1, b2), bnot(b2, b1))
```

```py
def half(b1, b2):
  return AND(b1, b2),XOR(b1, b2)
```

```py
def full(b1, b2, c):
  i1 = half(b1, b2)
  i2 = half(i1[1], c)
  return OR(i1[0], i2[0]),i2[1]
```

```py
def cadd(B1, B2, c):
  i7 = full(B1[7], B2[7], c)
  i6 = full(B1[6], B2[6], i7[0])
  i5 = full(B1[5], B2[5], i6[0])
  i4 = full(B1[4], B2[4], i5[0])
  i3 = full(B1[3], B2[3], i4[0])
  i2 = full(B1[2], B2[2], i3[0])
  i1 = full(B1[1], B2[1], i2[0])
  i0 = full(B1[0], B2[0], i1[0])
  return i0[1],i1[1],i2[1],i3[1],i4[1],i5[1],i6[1],i7[1]
```

```py
def add(B1, B2):
  return cadd((B1, B2, 0))
```

```py
def sub(B1, B2):
  return cadd(B1, (NOT(B2[0]),NOT(B2[1]),NOT(B2[2]),NOT(B2[3]),NOT(B2[4]),NOT(B2[5]),NOT(B2[6]),NOT(B2[7])), 1)
```

```py
def mini_MUX(b1, b2, b3):
  return OR(bnot(b1, b3), AND(b2, b3))
```

```py
def MUX(B1, B2, b1):
  return mini_MUX(B1[0], B2[0], b3),mini_MUX(B1[1], B2[1], b3),mini_MUX(B1[2], B2[2], b3),mini_MUX(B1[3], B2[3], b3),mini_MUX(B1[4], B2[4], b3),mini_MUX(B1[5], B2[5], b3),mini_MUX(B1[6], B2[6], b3),mini_MUX(B1[7], B2[7], b3)
```

```py
def AU(B1, B2, b1):
  return MUX(add(B1, B2), sub(B1, B2), b1)
```

```py
def LU(B1, B2, b1):
  i1 = AU(B1, B2, b1)
  i2 = NOT(OR(OR(OR(i1[0], i1[1]), OR(i1[2], i1[3])), OR(OR(i1[4], i1[5]), OR(i1[6], i1[7]))))
  return i1[0],OR(i1[0], i2),i2
```

```py
import numpy as np
```

$$ \text{Here's some code that my dad (and ChatGPT) wrote:} $$

```py
class BitArray(np.ndarray):
  def __new__(cls, shape):
    # Create an array of the given shape, initialized to False (0)
    obj = np.zeros(shape, dtype=np.bool_).view(cls)
    return obj

  def __array_finalize__(self, obj):
    if obj is None: return

  def __repr__(self):
    # Convert the boolean array to an integer array for display
    int_array = self.astype(int)
    # Use numpy's array2string function to format the output
    try:
      return '\n'.join(f"{i:3d}  "  + ' '.join([str(v) for v in val]) for i, val in enumerate(int_array))
    except:
      return ' '.join([str(v) for v in int_array])
    #return np.array2string(int_array, separator=' ')

  def __str__(self):
    return self.__repr__()
```

$700+$ (So, 702) lines, this is the new longest page on the website.

$$ \text{Back to my code.} $$

```py
code_lines = BitArray((256, 20))
```

```py
RAM = BitArray((256, 8))
```

```py
def numfy(B1):
  return B1[0] * 128 + B1[1] * 64 + B1[2] * 32 + B1[3] * 16 + B1[4] * 8 + B1[5] * 4 + B1[6] * 2 + B1[7] * 1
```

So, how you use the code is this (entire next line):

if you want to input some data (which has to be a number (which has to be encoded as the binary equivilant with a comma between every bit)) (call it $D$) at some address (call it $a$), run the code `RAM[numfy(a)] = D`. However, if you want to run code, then store the corrasponding opcode (that you can get from the table below) $O$ with corrasponding numbers that go with the opcode (e.g. ssu requires an address to store the subtraction) $n1$ and $n2$ into line $n$ with `code_lines[n] = O + n1 + n2` (that's an o, not a zero).

| Instruction | Stands for | Description | Opcode  |
|-------------|------------|-------------|---------|
| halt | halt | stops the program | 0000 |
| ldi | load immediate | stores directly into RAM | 0001 |
| rtr (optional) | RAM to RAM | stores from RAM into RAM | 0010 |
| lia | load immediate a | stores directly into register a | 0011 |
| lib | load immediate b | stores directly into register b | 0100 |
| ria | RAM into a | stores from RAM into register a | 0101 |
| rib | RAM into b | stores from RAM into register b | 0110 |
| sad | store addition | stores addition of a and b into RAM | 0111 |
| ssu | store subtraction | stores subtraction of a and b into RAM | 1000 |
| jump | jump | jump to a different line of code | 1001 |
| jin | jump if negative | jump if the negative flag (of the LU) is on | 1010 |
| jil | jump if low | jump if the NOZ (negaitve or zero) flag (of the LU) is on | 1011 |
| biz | branch (aka jump) if zero | branch if the zero flag (of the LU) is on | 1100 |

```py
halt = 0,0,0,0
ldi = 0,0,0,1
rtr = 0,0,1,0
lia = 0,0,1,1
lib = 0,1,0,0
ria = 0,1,0,1
rib = 0,1,1,0
sad = 0,1,1,1
ssu = 1,0,0,0
jump = 1,0,0,1
jin = 1,0,1,0
jil = 1,0,1,1
biz = 1,1,0,0
```

```py
t0 = 0,0,0,0,0,0,0,0
```

```py
def yfmun(n):
  i7 = n % 2
  i6 = (n % 4) // 2
  i5 = (n % 8) // 4
  i4 = (n % 16) // 8
  i3 = (n % 32) // 16
  i2 = (n % 64) // 32
  i1 = (n % 128) // 64
  i0 = n // 128
  return i0,i1,i2,i3,i4,i5,i6,i7
```

$$ \text{Now, this is where the code is run, so, if you want to store a program, or some data, put it here.} $$

```py
instr_addr_reg = t0
reg_a = t0
reg_b = t0
while True:
  program = code_lines[numfy(instr_addr_reg)]
  opcode = program[0],program[1],program[2],program[3]
  n1 = program[4],program[5],program[6],program[7],program[8],program[9],program[10],program[11]
  n2 = program[12],program[13],program[14],program[15],program[16],program[17],program[18],program[19]
  if opcode == halt:
    break
  elif opcode == ldi:
    RAM[numfy(n2)] = n1
  elif opcode == rtr:
    RAM[numfy(n2)] = RAM[numfy(n1)]
  elif opcode == lia:
    reg_a = n1
  elif opcode == lib:
    reg_b = n1
  elif opcode == ria:
    reg_a = RAM[numfy(n1)]
  elif opcode == rib:
    reg_b = RAM[numfy(n1)]
  elif opcode == sad:
    RAM[numfy(n1)] = add(reg_a, reg_b)
  elif opcode == ssu:
    RAM[numfy(n1)] = sub(reg_a, reg_b)
  elif opcode == jump:
    instr_addr_reg = n1
  elif opcode == jin:
    if LU(reg_a, reg_b, 1)[0] == 1:
      instr_addr_reg = n1
  elif opcode == jil:
    if LU(reg_a, reg_b, 1)[1] == 1:
      instr_addr_reg = n1
  elif opcode == biz:
    if LU(reg_a, reg_b, 1)[2] == 1:
      instr_addr_reg = n1
  else:
    break
  instr_addr_reg = add(instr_addr_reg, yfmun(1))
```

$$ \text{here's an example instruction:} $$

```py
code_lines[0] = ldi + yfmun(0) + yfmun(2)
code_lines[1] = rtr + yfmun(0) + yfmun(3)
code_lines[2] = ria + yfmun(3) + t0
code_lines[3] = rib + yfmun(1) + t0
code_lines[4] = ssu + yfmun(3) + t0
code_lines[5] = ria + yfmun(2) + t0
code_lines[6] = lib + yfmun(1) + t0
code_lines[7] = sad + yfmun(2) + t0
code_lines[8] = ria + yfmun(3) + t0
code_lines[9] = lib + yfmun(0) + t0
code_lines[10] = jin + yfmun(12) + t0
code_lines[11] = jump + yfmun(2) + t0
code_lines[12] = ria + yfmun(3) + t0
code_lines[13] = rib + yfmun(1) + t0
code_lines[14] = sad + yfmun(3) + t0
code_lines[15] = ria + yfmun(2) + t0
code_lines[16] = lib + yfmun(1) + t0
code_lines[17] = ssu + yfmun(2) + t0
code_lines[18] = halt + t0 + t0
```

### Turing machine

```py
import numpy as np
```

```py
tape = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
```

```py
h = 0
```

```py
states = np.array([[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]],[["H"],["H"]]]
```

```py
state = 0
```

```py
while True:
  instructions = states[state][tape[h]]
  for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction == "H":
      break
    elif instruction[0] == "t":
      h = int(instruction[2])
    elif instruction[0] == "s":
      state = int(instruction[2])
    elif instruction[0] == "w":
      tape = int(instruction[2])
    else:
      print(f"error: {instruction} is not defined.")
      break
```

### all the groups (run at your own (computer's) risk)

```py
import itertools
```

```py
import numpy as np
```

```py
def permutation(n):
  return [list(_) for _ in itertools.permutations(np.arange(n))]
```

```py
from itertools import chain, combinations
```

```py
def powerlist(L):
  """generate power set from iterable input"""
  (list(subset) for subset in chain.from_iterable(combinations(L, r) for r in range(len(L) + 1)))
```

```py
def mult(p, L):
  return L[p]
```

Do not run this next code that my dad wrote for an input more than $4$.

```py
for _ in powerlist(permutation(4)):
  if len(_) == 0:
    continue
  b = True
  for i in _:
    for j in _:
      k = list(mult(np.array(i), np.array(j)))
      if not k in _:
        b = False
#         print(f'found {k} not in {_}')
        break
    if not b:
      break
  if b:
    print(f'{_}')
    print()
```

### project mu

Mine is project mu ($\mu$), my dad's is project nu ($\nu$) (he's been working on is pretty much all weekend), and together, it is project kappa ($\kappa$), a project that should be able to do lambda calculus. I know what you're thinking: why can't you just use the built-in words `lambda` and `:`? 'Cause that's boring! (Also, get it? $\kappa \lambda \mu \nu$?)

Syntax: $f(x)$ is denoted as `[f x]`

```py
def reduce(string):
  for i in range(len(string)):
    if string[i] == "[" and string[i + 1] == "λ":
      bound_varable = string[i + 2]
      j = i + 4
      runc = 0
      s1 = ""
      s2 = ""
      split = False
      while True:
        term = string[j]
        if term == "[":
          runc += 1
        if term == "]":
          runc -= 1
          if runc == -1:
            break
        if runc == 0 and term == " ":
          split = True
          si = j
        else:
          if not split:
            s1 += term
          else:
            s2 += term
        j += 1
      result = ""
      for k in range(0, i):
        result += string[k]
      for k in range(i + 4, si):
        if string[k] == bound_varable:
          result += s2
        else:
          result += string[k]
      for k in range(j + 1, len(string)):
        result += string[k]
      return [result, "needs another!"]
  return [string, "done!"]
```

```py
def fullreduce(string):
  prev_result = string
  result = reduce(string)
  for i in range(100):
    if result == prev_result:
       return result
    prev_result = result
    result = reduce(result)
  print(f"recursion depth limit exceeded, the furthest I got was {result}")
  return result
```

But there's a problem: capture of free variables. I'll explain with an example:

$$ \text{[} \lambda f. \lambda g. \lambda x. \text{[} f \text{ } \text{[} g \text{ } x \text{]} \text{]} \text{ } g \text{]} = \lambda g. \lambda x. \text{[} g \text{ } \text{[} g \text{ } x \text{]} \text{]} $$

### project xi

Apparently, I just found another method for doing lambda calculus is python, so I subdivided again into project mu ($\mu$) and project xi ($\xi$).

$1000$ Lines, wow.

(Get it? $\kappa \lambda \mu \nu \xi$?)

The method supports functions as arguments, currying, and even (I think) capture of free variables. I'll explain with some examples:

```py
def mult(x):
  def mult1(y):
    return x * y
  return mult1
```

```py
mult(1)(2)
```

```py
def B(f):
  def B1(g):
    def B2(x):
      return f(g(x))
    return B2
  return B1
```

```py
def inc(x):
  return x + 1
```

```py
def dec(x):
  return x - 1
```

```py
B(inc)(dec)(5)
```

### xi

```py
def B(f):
  def B1(g):
    def B2(x):
      return f(g(x))
    return B2
  return B1
```

```py
comp = B
```

```py
def C(f):
  def C1(x):
    def C2(y):
      return f(y)(x)
    return C2
  return C1
```

```py
swap = C
```

```py
def K(x):
  def K1(y):
    return x
  return K1
```

```py
fstin = K
```

```py
const = K
```

```py
def W(f):
  def W1(x):
    return f(x)(x)
  return W1
```

```py
I = B(C)(C)
```

```py
Th = c(I)
```

```py
Ki = K(I)
```

```py
sndin = Ki
```

```py
T = K
```

```py
F = Ki
```

```py
xibool = C(Th("T / K"))("F / Ki")
```

```py
AND = W(C)
```

```py
OR = W(I)
```

```py
NOT = C
```

```py
beq = B(W)(B(C(B)(C))(C))
```

```py
n0 = Ki
```

```py
n1 = I
```

```py
n2 = W(B)
```

```py
n3 = W(B(B)(W(B)))
```

```py
n4 = W(B(B)(W(B(B)(W(B)))))
```

```py
n5 = W(B(B)(W(B(B)(W(B(B)(W(B)))))))
```

```py
n6 = W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B)))))))))
```

```py
n7 = W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B)))))))))))
```

```py
n8 = W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B)))))))))))))
```

```py
n9 = W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B)))))))))))))))
```

```py
n10 = W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B(B)(W(B)))))))))))))))))
```

```py
xinum = C(Th(lambda x: x + 1))(0)
```

```py
inc = B(W)(B(B))
```

```py
add = B(B(W))(B(C)(B(B(B))(B(B))))
```

```py
mult = B
```

```py
exp = Th
```

```py
is0 = C(Th(K(F)))(T)
```

```py
pair = B(C)(Th)
```

```py
fst = Th(K)
```

```py
snd = Th(Ki)
```

```py
def xipair(p):
  return f"({fst(p)}, {snd(p)})"
```

```py
Phi = W(C(B(B)(B(pair)(snd)))(B(inc)(snd))
```

```py
dec = B(fst)(C(Th(Phi))(pair(n0)(n0)))
```

```py
sub = Th(dec)
```

```py
dcomp = B(B)(B)
```

```py
leq = dcomp(is0)(sub)
```

```py
geq = C(leq)
```

```py
gt = dcomp(NOT)(leq)
```

```py
lt = C(gt)
```

```py
def eq(n):
  def eq1(k):
    return AND(leq(n)(k))(geq(n)(k))
  return eq1
```

```py
neq = dcomp(NOT)(eq)
```

```py

```
