# comparison_operators.py
# -----------------------
# 🎯 In this file, we’ll learn about Comparison (Relational) Operators in Python.

# Comparison operators are used to compare two values.
# The result of a comparison operation is always a Boolean value: True or False.


# ----------------------------------------------------------
# 🧠 List of Comparison Operators
# ----------------------------------------------------------
# Operator | Description                 | Example
# -------- | --------------------------- | ---------------------
# ==       | Equal to                    | 5 == 5 → True
# !=       | Not equal to                | 5 != 3 → True
# >        | Greater than                | 10 > 5 → True
# <        | Less than                   | 2 < 5 → True
# >=       | Greater than or equal to    | 5 >= 5 → True
# <=       | Less than or equal to       | 3 <= 5 → True


# ----------------------------------------------------------
# 🔹 Examples
# ----------------------------------------------------------

a = 10
b = 5

print("🔹 a =", a)
print("🔹 b =", b)
print("------------------------------")

# Equal to
print("Equal to (a == b):", a == b)

# Not equal to
print("Not equal to (a != b):", a != b)

# Greater than
print("Greater than (a > b):", a > b)

# Less than
print("Less than (a < b):", a < b)

# Greater than or equal to
print("Greater than or equal to (a >= b):", a >= b)

# Less than or equal to
print("Less than or equal to (a <= b):", a <= b)


# ----------------------------------------------------------
# 💡 Example: Using comparison in a condition
# ----------------------------------------------------------
age = 18

if age >= 18:
    print("\n✅ You are eligible to vote.")
else:
    print("\n❌ You are not eligible to vote.")


# ----------------------------------------------------------
# 🎯 Summary:
# == → checks if values are equal
# != → checks if values are not equal
# >  → checks if left value is greater
# <  → checks if left value is smaller
# >= → checks if left value is greater or equal
# <= → checks if left value is smaller or equal
# ----------------------------------------------------------
