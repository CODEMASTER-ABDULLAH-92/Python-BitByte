
# Logical operators are used to combine multiple conditional statements.
# They return a Boolean value: True or False.


# ----------------------------------------------------------
# 🧠 List of Logical Operators
# ----------------------------------------------------------
# Operator | Description                                       | Example
# -------- | ------------------------------------------------- | -------------------------
# and      | Returns True if both conditions are True          | (5 > 2 and 3 < 4) → True
# or       | Returns True if at least one condition is True    | (5 > 10 or 4 == 4) → True
# not      | Reverses the result of a condition                | not(5 > 2) → False


# ----------------------------------------------------------
# 🔹 Examples
# ----------------------------------------------------------

a = 10
b = 5
c = 3

print("🔹 a =", a)
print("🔹 b =", b)
print("🔹 c =", c)
print("------------------------------")

# AND operator → True only if both are True
print("AND Operator (a > b and b > c):", a > b and b > c)

# OR operator → True if at least one is True
print("OR Operator (a < b or b > c):", a < b or b > c)

# NOT operator → Reverses the result
print("NOT Operator not(a > b):", not (a > b))


# ----------------------------------------------------------
# 💡 Example: Logical Operators in Conditions
# ----------------------------------------------------------

age = 20
has_id = True

if age >= 18 and has_id:
    print("\n✅ Access Granted.")
else:
    print("\n❌ Access Denied.")

# ----------------------------------------------------------
# 🎯 Summary:
# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses (negates) the condition
# ----------------------------------------------------------
