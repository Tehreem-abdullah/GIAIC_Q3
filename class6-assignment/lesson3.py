# Operators keywords and variables

# 1.OPerators
#1.1 ARthmetic operators

# +, -, *, /, %, **, //

# 1.2 Assigment operators
# =, +=, -=, *=, /=, %=, **=, //=

# 1.3 comparison operators
# ==, !=, >, <, >=, <=

# 1.4 logical operators
# and, or , not

# 1.5 identity operators
# is, is not

# 1.6 membership operators
# in, not in

# 1.7 bitwise operators 
# &, |, ^, ~`, <<, >>`


# Variables
a = 10
b = 3
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("=== Arithmetic Operators ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

print("\n=== Assignment Operators ===")
a += 2
print("a += 2:", a)
a *= 3
print("a *= 3:", a)

print("\n=== Comparison Operators ===")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)

print("\n=== Logical Operators ===")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

print("\n=== Identity Operators ===")
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not y:", x is not y)

print("\n=== Membership Operators ===")
print("2 in x:", 2 in x)
print("5 not in x:", 5 not in x)

print("\n=== Bitwise Operators ===")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
