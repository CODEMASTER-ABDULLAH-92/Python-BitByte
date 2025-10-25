# 🟦 Python Sets — Complete Notes

# ------------------------------------------------------------
# 🔹 What is a Set?
# ------------------------------------------------------------
# A set is a collection of unique and unordered items.
# It is used to store multiple values in a single variable
# without duplicates.
# Sets are mutable (you can add or remove elements),
# but elements themselves must be immutable (like numbers, strings, or tuples).

# Example of a set
my_set = {1, 2, 3, 4}
print("My Set:", my_set)


# ------------------------------------------------------------
# 🧠 Key Features of Sets
# ------------------------------------------------------------
# 1. Unordered – You can’t access elements by index.
# 2. No duplicates – All elements are unique.
# 3. Mutable – You can add or remove elements.
# 4. Heterogeneous – Can store different data types.


# ------------------------------------------------------------
# 🧩 Syntax and Basic Examples
# ------------------------------------------------------------

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Fruits:", fruits)

# No duplicates allowed
numbers = {1, 2, 2, 3, 3, 3}
print("Numbers (duplicates removed):", numbers)  # Output: {1, 2, 3}

# Adding elements
fruits.add("mango")
print("After adding mango:", fruits)

# Removing elements
fruits.remove("banana")   # Removes 'banana' (throws error if not found)
print("After removing banana:", fruits)

fruits.discard("pear")    # Removes 'pear' if found, no error otherwise
print("After discarding pear:", fruits)

# Creating an empty set
empty = set()
print("Type of empty variable:", type(empty))  # <class 'set'>


# ------------------------------------------------------------
# ⚙️ Set Operations (Mathematical)
# ------------------------------------------------------------
# Python sets support union, intersection, difference, and symmetric difference.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union → combines all unique elements
print("Union (A | B):", A | B)

# Intersection → common elements
print("Intersection (A & B):", A & B)

# Difference → elements in A but not in B
print("Difference (A - B):", A - B)

# Symmetric Difference → elements not common in both sets
print("Symmetric Difference (A ^ B):", A ^ B)


# ------------------------------------------------------------
# ⚖️ Comparison: Set vs List vs Tuple
# ------------------------------------------------------------
# | Feature        | Set ({} )   | List ([])   | Tuple (())   |
# | -------------- | ------------| ------------| -------------|
# | Order          | ❌ Unordered| ✅ Ordered  | ✅ Ordered   |
# | Duplicates     | ❌ No       | ✅ Yes      | ✅ Yes       |
# | Mutable        | ✅ Yes      | ✅ Yes      | ❌ No        |
# | Indexing       | ❌ No       | ✅ Yes      | ✅ Yes       |


# ------------------------------------------------------------
# 💡 When to Use Sets
# ------------------------------------------------------------
# ✅ When you need to store only unique values.
# ✅ When performing mathematical operations (union, intersection, etc.).
# ✅ When order of elements doesn’t matter.
