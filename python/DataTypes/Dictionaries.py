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
# 🧩 Creating and Accessing Dictionaries
# ------------------------------------------------------------

# Creating a dictionary
student = {
    "name": "Ali",
    "age": 21,
    "department": "Software Engineering"
}

# Accessing values using keys
print("Name:", student["name"])  # Output: Ali

# Using get() method (safe access, avoids error if key not found)
print("Age:", student.get("age"))  # Output: 21
print("GPA:", student.get("gpa", "Not Available"))  # Default message


# ------------------------------------------------------------
# ✍️ Modifying and Updating Dictionary
# ------------------------------------------------------------
# Adding a new key-value pair
student["semester"] = 3
print("After adding semester:", student)

# Modifying existing value
student["age"] = 22
print("After modifying age:", student)

# Removing a key-value pair using pop()
student.pop("department")
print("After removing department:", student)

# Removing all items
# student.clear()


# ------------------------------------------------------------
# ⚙️ Common Dictionary Methods
# ------------------------------------------------------------
# dict.keys()     → returns all keys
# dict.values()   → returns all values
# dict.items()    → returns all key-value pairs
# dict.get(key)   → returns value of key (no error if missing)
# dict.pop(key)   → removes item by key
# dict.update()   → updates dictionary with another dictionary
# dict.clear()    → removes all items

# Example
info = {
    "name": "Sara",
    "age": 19
    }

print("Keys:", info.keys())
print("Values:", info.values())
print("Items:", info.items())

# Updating dictionary
info.update({"city": "Lahore", "age": 20})
print("After update:", info)


# ------------------------------------------------------------
# 🔁 Iterating Through Dictionary
# ------------------------------------------------------------

person = {"name": "Usman", "age": 25, "country": "Pakistan"}

# Loop through keys
for key in person.keys():
    print("Key:", key)

# Loop through values
for value in person.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key} → {value}")


# ------------------------------------------------------------
# 📦 Nested Dictionary Example
# ------------------------------------------------------------
students = {
    "std1": {"name": "Ali", "age": 21},
    "std2": {"name": "Sara", "age": 20}
}
print("Nested Dictionary Example:", students["std1"]["name"])  # Output: Ali


# ------------------------------------------------------------
# 🧮 Dictionary Comprehension
# ------------------------------------------------------------
# Just like list comprehension, you can create dictionaries in one line.

# Example 1: Square of numbers
squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Example 2: Filtering even numbers only
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print("Even Squares Dictionary:", even_squares)

# Example 3: Convert two lists into dictionary
keys = ["name", "age", "city"]
values = ["Ahsan", 23, "Lahore"]
combined = {k: v for k, v in zip(keys, values)}
print("Combined Dictionary:", combined)


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
# ✅ Perfect for representing JSON-like data.


# ------------------------------------------------------------
# 🌍 Python Dictionary vs JavaScript Object
# ------------------------------------------------------------
# You can say that a Python dictionary is very similar to a JavaScript object —
# both store data in key-value pairs.

# 🔸 JavaScript Example:
# const person = {
#     name: "Abdullah",
#     age: 20,
#     city: "Faisalabad"
# };

# console.log(person.name);  // Access value using dot notation
# person.country = "Pakistan";  // Add new property

# 🔸 Python Equivalent:
py_person = {
    "name": "Abdullah",
    "age": 20,
    "city": "Faisalabad"
}
print(py_person["name"])
py_person["country"] = "Pakistan"
print(py_person)

# ✅ Both are dynamic, mutable, and store key-value data.
# ⚠️ But Python dictionaries use square brackets [] for access,
# while JS objects use dot notation (.) or brackets.
