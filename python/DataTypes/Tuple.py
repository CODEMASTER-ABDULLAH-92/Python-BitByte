# 🟩 What is a Tuple in Python?

# A tuple is a collection (like a list) that can store multiple items in a single variable.
# Tuples are immutable, meaning you cannot change, add, or remove elements after creation.


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





# ==========================================
# 🟣 TUPLES IN PYTHON — ADVANCED CONCEPTS
# ==========================================

# -------------------------------------------------
# 🧩 Tuple Packing & Unpacking
# -------------------------------------------------
# 📦 Tuple Packing means putting multiple values together into a single tuple.
# 📤 Tuple Unpacking means extracting those values back into individual variables.

# Example: Tuple Packing
person = ("Abdullah", 20, "Software Engineer")  # Packing values into a tuple
print("Packed Tuple:", person)

# Example: Tuple Unpacking
name, age, profession = person  # Unpacking tuple values into variables
print("Unpacked Values:")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# 💡 Note: Number of variables must match the number of tuple elements.


# -------------------------------------------------
# 🆚 Tuple vs List
# -------------------------------------------------
# Both tuples and lists can store multiple items, but they have key differences.

# Example
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)

print("\nTuple vs List:")
print("List:", my_list)
print("Tuple:", my_tuple)

# 🧠 Key Differences:

# | Feature           | Tuple                      | List                    |
# | ----------------- | -------------------------- | ----------------------- |
# | **Syntax**        | ()                         | []                      |
# | **Mutable**       | ❌ No (Cannot change)       | ✅ Yes (Can change)     |
# | **Performance**   | ✅ Faster (fixed size)      | ❌ Slower (flexible)    |
# | **Use Case**      | Fixed data (e.g., coords)  | Dynamic data            |

# Example of mutability difference
my_list[0] = 99
print("\nModified List:", my_list)

# my_tuple[0] = 99  # ❌ This will raise an error (Tuples are immutable)


# -------------------------------------------------
# 🔒 Immutable Nature of Tuples
# -------------------------------------------------
# Tuples cannot be changed after creation — no item assignment, no addition, or removal.

immutable_tuple = (10, 20, 30)

print("\nImmutable Tuple:", immutable_tuple)

# Trying to modify a tuple
try:
    immutable_tuple[1] = 200  # ❌ This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# ✅ However, if a tuple contains a mutable element (like a list), that element can be changed.
mixed_tuple = (1, [2, 3], 4)
print("\nBefore modification:", mixed_tuple)

mixed_tuple[1][0] = 99  # We modify the list inside the tuple
print("After modification:", mixed_tuple)

# -------------------------------------------------
# 🧠 Summary
# -------------------------------------------------
# ✔ Tuple Packing — Combine values into a tuple.
# ✔ Tuple Unpacking — Extract values from a tuple.
# ✔ Tuple vs List — Tuples are immutable and faster; Lists are mutable and flexible.
# ✔ Immutable Nature — Tuples cannot be modified, but mutable elements inside them can.

