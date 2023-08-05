
print("Number Data Type in Python\n######################################")
a = 5
print(type(a))
print(type(5.0))
c = 5 + 3j
print(c + 3)
print(type(c))
print(isinstance(c, complex))

print("Binary, Hexadecimals & Octals\n######################################")
# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)

print("Type Conversion\n######################################")
print(1 + 2.0)
print(int(2.3))
print(int(-2.5))
print(float(5))
print(complex(3+5j))

print("Python Hexadecimals\n######################################")
from decimal import Decimal as D

print(D(1.1) + D(2.2))
print(D('1.2') * D('2.5'))

print("Python Fraction\n######################################")
import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1,3))

# This is due to the imperfect binary floating point number representation as discussed in the previous section.
# While creating Fraction from float, we might get some unusual results.
# Fortunately, Fraction allows us to instantiate with string as well. This is the preferred option when using decimal numbers.

# As float # Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string # Output: 11/10
print(fractions.Fraction('1.1'))

#This data type supports all basic operations. Here are a few examples.
from fractions import Fraction as F

print(F(1, 3) + F(1, 3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)

print("Python Maths\n######################################")
# Python offers modules like math and random to carry out different mathematics like trigonometry, logarithms, probability and statistics, etc.

import math
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))
print(math.ceil(2.0))
print(math.ceil(-2.0))
print(math.ceil(2.56))
print(math.ceil(-2.56))
print(math.log10(1))
print(math.log(math.e))
print(math.modf(1.5))
print(math.hypot(3,4))

print("Python random\n######################################")
import random
print(random.randrange(10, 20))
x = ['a', 'b', 'c', 'd', 'e']
# Get random choice
print(random.choice(x))
# Shuffle x
random.shuffle(x)
# Print the shuffled x
print(x)
# Print random element
print(random.random())
