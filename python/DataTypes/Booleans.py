# 🟩 Booleans in Python

# ==============================================
# ✅ Definition:
# ==============================================
# Booleans represent one of two values: True or False.
# They are used for decision-making (conditional statements, loops, etc.)

# Example:
is_active = True
is_logged_in = False

print(is_active)       # True
print(is_logged_in)    # False

# Type of Boolean
print(type(is_active))  # <class 'bool'>



# ==============================================
# ✅ Boolean Values from Expressions
# ==============================================
# Boolean values often result from comparisons.

x = 10
y = 5

print(x > y)   # True
print(x == y)  # False
print(x < y)   # False



# ==============================================
# ✅ Using bool() Function
# ==============================================
# The bool() function converts values into True or False.

print(bool(1))        # True
print(bool(0))        # False
print(bool("Hello"))  # True (non-empty string)
print(bool(""))       # False (empty string)
print(bool([]))       # False (empty list)
print(bool([1, 2]))   # True (non-empty list)



# ==============================================
# ✅ Boolean Operators
# ==============================================
# Used to combine multiple conditions.

# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses the boolean value

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False



# ==============================================
# ✅ Example Usage in Conditional Statements
# ==============================================

age = 18
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("Access denied.")


# ==============================================
# 🧠 Summary Table
# ==============================================

| Expression            | Result  | Description                               |
| ---------------------- | ------- | ----------------------------------------- |
| `10 > 5`              | True    | Comparison result                         |
| `bool(0)`             | False   | 0 is considered False                     |
| `bool("Python")`      | True    | Non-empty string → True                   |
| `bool([])`            | False   | Empty list → False                        |
| `True and False`      | False   | Both must be True                         |
| `True or False`       | True    | Only one needs to be True                 |
| `not True`            | False   | Reverses the value                        |
