# 🟩 Type Casting (Type Conversion)
# 🔹 Definition:

# Type casting (or type conversion) means changing the data type of a variable from one type to another.

# For example, converting a string into an integer, or a float into a string.

# 🔹 Types of Type Casting:
# 🧠 1. Implicit Type Casting (Automatic)

# Done automatically by Python.

# Python converts smaller data types to larger ones to avoid data loss.

# -------------------------------

# Example 
a = 5        # int
b = 2.5      # float
result = a + b   # int + float → float
print(result)     # Output: 7.5
print(type(result))  # <class 'float'>

# -------------------------------





# 🧠 2. Explicit Type Casting (Manual)

# Done manually by the programmer using type conversion functions.


# String to int
num = int("10")
print(num + 5)     # Output: 15

# Float to int
x = int(9.8)
print(x)           # Output: 9

# Int to float
y = float(7)
print(y)           # Output: 7.0

# Int to string
s = str(123)
print(s + "4")     # Output: 1234



