# 🟩 What is a Tuple in Python?

# A tuple is a collection (like a list) that can store multiple items in a single variable.
# Tuples are immutable, meaning you cannot change, add, or remove elements after creation.


# 🧠 Key Features of Tuples
# Feature	Description
# Ordered	Elements have a defined order that doesn’t change.
# Immutable	You can’t modify (update, delete, or append) items.
# Allow Duplicates	Tuples can store repeated values.
# Multiple Data Types	Can hold integers, strings, floats, lists, or even other tuples.

# -----------------------------------

# 🧩 Syntax

# ------------------------------------
# my_tuple = (1, 2, 3, 4)


# ✅ Use parentheses () instead of square brackets [] (used in lists).

# 📘 Examples
# # Creating a tuple
# fruits = ("apple", "banana", "cherry")
# print(fruits)

# # Accessing elements
# print(fruits[1])  # Output: banana

# # Nested tuple
# nested = (1, 2, (3, 4))
# print(nested[2][1])  # Output: 4

# # Tuple with mixed data types
# mixed = (10, "Hello", 3.14, True)

# ----------------------------------

# 💡 When to Use Tuples

# ----------------------------------

# When data should remain fixed (e.g., coordinates, dates, config values).
# When you need faster performance compared to lists.

# ✅ Summary:
# Tuples are ordered, immutable collections used to store data that should not change throughout the program.