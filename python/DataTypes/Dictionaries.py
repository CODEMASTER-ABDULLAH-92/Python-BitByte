# 🟨 Python Dictionaries — Complete Notes

# ------------------------------------------------------------
# 🔹 What is a Dictionary?
# ------------------------------------------------------------
# A dictionary is a collection of key–value pairs.
# Each key is unique and used to access its corresponding value.
# Dictionaries are unordered, mutable, and dynamic.

# Example of a dictionary
my_dict = {
    "name": "Abdullah",
    "age": 20,
    "city": "Faisalabad"
}
print("My Dictionary:", my_dict)


# ------------------------------------------------------------
# 🧠 Key Features of Dictionaries
# ------------------------------------------------------------
# 1. Stores data as key–value pairs.
# 2. Mutable – can be changed after creation.
# 3. No duplicate keys allowed.
# 4. Keys must be immutable (like strings, numbers, tuples).
# 5. Values can be of any data type.


# ------------------------------------------------------------
# 🧩 Syntax and Basic Examples
# ------------------------------------------------------------

# Creating a dictionary
student = {
    "name": "Ali",
    "age": 21,
    "department": "Software Engineering"
}

# Accessing values using key
print("Name:", student["name"])  # Output: Ali

# Using get() method to safely access values
print("Age:", student.get("age"))  # Output: 21

# Adding a new key-value pair
student["semester"] = 3
print("After adding semester:", student)

# Modifying existing value
student["age"] = 22
print("After modifying age:", student)

# Removing a key-value pair using pop()
student.pop("department")
print("After removing department:", student)

# Looping through dictionary items
for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# ⚙️ Common Dictionary Methods
# ------------------------------------------------------------
# dict.keys()     → returns all keys
# dict.values()   → returns all values
# dict.items()    → returns all key-value pairs
# dict.get(key)   → returns value of key (no error if missing)
# dict.pop(key)   → removes item by key
# dict.update()   → updates dictionary with another
# dict.clear()    → removes all items

# Example
info = {"name": "Sara", "age": 19}
print("Keys:", info.keys())
print("Values:", info.values())
print("Items:", info.items())


# ------------------------------------------------------------
# 📦 Nested Dictionary Example
# ------------------------------------------------------------
students = {
    "std1": {"name": "Ali", "age": 21},
    "std2": {"name": "Sara", "age": 20}
}
print("Nested Dictionary Example:", students["std1"]["name"])  # Output: Ali


# ------------------------------------------------------------
# ⚖️ Comparison Table
# ------------------------------------------------------------
# | Feature        | Dictionary     | List      | Tuple     | Set       |
# |----------------|----------------|-----------|-----------|-----------|
# | Syntax         | {key: value}   | []        | ()        | {}        |
# | Ordered        | ✅ (3.7+)       | ✅         | ✅         | ❌        |
# | Mutable        | ✅              | ✅         | ❌         | ✅        |
# | Duplicates     | ❌ (keys only)  | ✅         | ✅         | ❌        |
# | Access By      | Key            | Index     | Index     | No index  |


# ------------------------------------------------------------
# 💡 When to Use Dictionaries
# ------------------------------------------------------------
# ✅ When you want to store data with meaningful keys.
# ✅ When fast lookups are required.
# ✅ When data should be structured (like records, configs, etc.).


# --------------------------------------

# Both JS object and PY Dictionary same 

# --------------------------------------

# You can say that a Python dictionary is very similar to a JavaScript object — both store data in key-value pairs.