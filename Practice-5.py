# Numbers

# There are three numeric types in Python:
# 1. int (integer)
# 2. float
# 3. complex

x = 1
y = 1.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

# 1. int (integer)

x = 1
y = 15347834934
z = -323344
print(type(x))
print(type(y))
print(type(z))

# 2. float

x = 1.4
y = 15.347834934
z = -32.3344
print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 1e4
y = 15.e347834934
z = -32.E3344

print(type(x))
print(type(y))
print(type(z))

# 3. complex
# Complex numbers are written with a "j" as the imaginary part:

x = 1j
y = 15 + 5j
z = -32j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1
y = 2.5
z = 0j
print(type(x))
print(type(y))
print(type(z))

a = float(x)
print(a)
print(type(a))

b = int(y)
print(b)
print(type(b))

c = complex(x)
print(c)
print(type(c))

# Random Number
import random
print(random.randrange(9, 99))
print(random.randrange(0, 100, 5))
print(random.uniform(1.5, 5.5))

choices = ["a", "b", "c"]
print(random.choice(choices))

# Python Casting
a = int(1) 
b = int(2.8) 
c = float(1)  
d = float(2.8)
e = str("s1") # x will be 's1'
f = str(2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
