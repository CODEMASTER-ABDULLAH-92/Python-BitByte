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

print("\nSet A:", A)
print("Set B:", B)

# Union → combines all unique elements
print("Union (A | B):", A | B)
print("Union using method:", A.union(B))

# Intersection → common elements
print("Intersection (A & B):", A & B)
print("Intersection using method:", A.intersection(B))

# Difference → elements in A but not in B
print("Difference (A - B):", A - B)
print("Difference using method:", A.difference(B))

# Symmetric Difference → elements not common in both sets
print("Symmetric Difference (A ^ B):", A ^ B)
print("Symmetric Difference using method:", A.symmetric_difference(B))


# ------------------------------------------------------------
# 🧰 Common Set Methods
# ------------------------------------------------------------
# Below are some of the most used methods for manipulating sets.

colors = {"red", "green", "blue"}

# add() → Adds a new element
colors.add("yellow")
print("\nAfter add():", colors)

# update() → Adds multiple elements
colors.update(["purple", "black"])
print("After update():", colors)

# remove() → Removes element (error if not found)
colors.remove("red")
print("After remove():", colors)

# discard() → Removes element (no error if not found)
colors.discard("white")
print("After discard():", colors)

# pop() → Removes and returns a random element
removed = colors.pop()
print("Removed element using pop():", removed)
print("After pop():", colors)

# clear() → Removes all elements
colors.clear()
print("After clear():", colors)  # Output: set()

# copy() → Creates a shallow copy of the set
set1 = {"a", "b", "c"}
set2 = set1.copy()
print("Copied set:", set2)

# issubset() → Checks if all elements of one set are in another
print("Is {1,2} subset of {1,2,3}? :", {1, 2}.issubset({1, 2, 3}))

# issuperset() → Checks if a set contains all elements of another
print("Is {1,2,3} superset of {1,2}? :", {1, 2, 3}.issuperset({1, 2}))

# isdisjoint() → Checks if sets have no common elements
print("Are {1,2} and {3,4} disjoint? :", {1, 2}.isdisjoint({3, 4}))


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
# ✅ When checking membership efficiently (fast lookups).

# Example: Removing duplicates from a list
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("\nUnique numbers from list:", unique_numbers)
