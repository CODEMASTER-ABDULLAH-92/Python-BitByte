# assignment_operators.py
# -----------------------
# 🎯 In this file, we’ll learn about Assignment Operators in Python.

# Assignment operators are used to assign values to variables.
# They can also be combined with arithmetic operators to perform operations and assignment in one step.


# ----------------------------------------------------------
# 🧠 List of Assignment Operators
# ----------------------------------------------------------
# Operator | Description                        | Example
# -------- | ---------------------------------- | --------------------
# =        | Assigns value                      | x = 10
# +=       | Add and assign                     | x += 5 → x = x + 5
# -=       | Subtract and assign                | x -= 3 → x = x - 3
# *=       | Multiply and assign                | x *= 2 → x = x * 2
# /=       | Divide and assign (float result)   | x /= 4 → x = x / 4
# %=       | Modulus and assign                 | x %= 3 → x = x % 3
# **=      | Exponent and assign                | x **= 2 → x = x ** 2
# //=      | Floor divide and assign            | x //= 3 → x = x // 3


# ----------------------------------------------------------
# 🔹 Examples
# ----------------------------------------------------------

x = 10
print("Initial value of x:", x)
print("------------------------------")

x += 5
print("After x += 5:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)

x %= 3
print("After x %= 3:", x)

x **= 2
print("After x **= 2:", x)

x //= 2
print("After x //= 2:", x)


# ----------------------------------------------------------
# 💡 Example Use Case
# ----------------------------------------------------------

score = 50
bonus = 10

# Add bonus points to score
score += bonus
print("\n🎯 Final Score after bonus:", score)


# ----------------------------------------------------------
# 🎯 Summary:
# =   → Assigns value
# +=  → Add and assign
# -=  → Subtract and assign
# *=  → Multiply and assign
# /=  → Divide and assign
# %=  → Remainder and assign
# **= → Power and assign
# //= → Floor divide and assign
# ----------------------------------------------------------
