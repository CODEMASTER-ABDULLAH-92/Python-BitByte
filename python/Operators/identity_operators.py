# identity_operators.py
# ---------------------
# 🎯 In this file, we’ll learn about Identity Operators in Python.

# Identity operators are used to compare the **memory location** of two objects.
# They check whether two variables refer to the same object in memory — not just if their values are equal.


# ----------------------------------------------------------
# 🧠 List of Identity Operators
# ----------------------------------------------------------
# Operator | Description                                              | Example
# -------- | -------------------------------------------------------- | --------------------------
# is       | Returns True if both variables refer to the same object  | a is b
# is not   | Returns True if they do NOT refer to the same object     | a is not b


# ----------------------------------------------------------
# 🔹 Example 1: Comparing Integers
# ----------------------------------------------------------

a = 10
b = 10
print("a =", a, ", b =", b)

print("a == b →", a == b)   # Compares values
print("a is b →", a is b)   # Compares identity (same memory?)

# Note: In Python, small integers (-5 to 256) are cached,
# so 'a' and 'b' may actually point to the same memory location.


# ----------------------------------------------------------
# 🔹 Example 2: Comparing Lists
# ----------------------------------------------------------

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nlist1 =", list1)
print("list2 =", list2)
print("list3 = list1 →", list3)

print("list1 == list2 →", list1 == list2)   # Same values → True
print("list1 is list2 →", list1 is list2)   # Different memory → False
print("list1 is list3 →", list1 is list3)   # Same object → True


# ----------------------------------------------------------
# 🔹 Example 3: Using 'is not'
# ----------------------------------------------------------

x = "Python"
y = "Java"

print("\n'x is not y' →", x is not y)
print("'x is y' →", x is y)


# ----------------------------------------------------------
# 💡 Example Use Case
# ----------------------------------------------------------

value = None

if value is None:
    print("\n✅ Value is None")
else:
    print("\n❌ Value is not None")


# ----------------------------------------------------------
# 🎯 Summary:
# ==      → Compares values (contents)
# is      → Compares identities (memory location)
# is not  → True if objects are different in memory
# ----------------------------------------------------------
