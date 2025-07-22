# ========================
# Python Basics for Beginners
# ========================

# ----- Output and Comments -----
# print("Abdullah")      # Prints a string
# print(23)              # Prints an integer
# print(23 + 25)         # Prints the result of addition

# ----- Variables and Data Types -----
name = "Abdullah"       # String (text)
age = 22                # Integer (whole number)
price = 24.99           # Float (decimal number)

# print(name)
# print(age)
# print(price)

# Check and print data types
# print(type(name))     # <class 'str'>
# print(type(age))      # <class 'int'>
# print(type(price))    # <class 'float'>

# ----- Different Ways to Declare Strings -----
name1 = "ab"
name2 = 'ab'
name3 = '''ab'''
# print(name1)
# print(name2)
# print(name3)

# ----- None Type -----
name = None             # None means no value
# print(name)           # Output: None
# print(type(name))     # <class 'NoneType'>

# ----- Arithmetic Operators -----
num1 = 23
num2 = 25
num3 = num1 + num2      # Addition
# print("Sum:", num3)

a = 10
b = 2
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)
# print("Exponent:", a ** b)   # a raised to the power b

# ----- Relational (Comparison) Operators -----
a = 50
b = 20

# These return True or False
# print("a == b:", a == b)
# print("a != b:", a != b)
# print("a >= b:", a >= b)
# print("a <= b:", a <= b)
# print("a < b:", a < b)
# print("a > b:", a > b)

# ----- Assignment Operators -----
a = 5
a += 10
print("a after += 10:", a)  # 15

b = 20
b -= 10
print("b after -= 10:", b)  # 10

c = 100
c /= 10
print("c after /= 10:", c)  # 10.0

d = 25
d %= 10
print("d after %= 10:", d)  # 5

e = 7
e *= 10
print("e after *= 10:", e)  # 70

f = 2
f **= 10
print("f after **= 10:", f)  # 1024

# ----- Logical Operators -----
# Logical operators are used to combine conditional statements

a = True
b = False

# AND returns True only if both are True
result_and = a and b
print("Result of a AND b:", result_and)  # False

# OR returns True if at least one is True
x = True
y = False
result_or = x or y
print("Result of x OR y:", result_or)    # True

# NOT reverses the condition
z = False
result_not = not z
print("Result of NOT z:", result_not)    # True
