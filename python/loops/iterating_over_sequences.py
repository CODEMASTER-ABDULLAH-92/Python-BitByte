# 💡 Understanding how to iterate over sequences in Python

# ---------------------------------------------------
# ✅ In Python, "sequences" include data types like:
#    → string, list, tuple, set, and dictionary
# ✅ You can use loops (mostly 'for') to iterate (go through) each element.
# ---------------------------------------------------


# 🟢 Example 1: Iterating over a string
print("🟢 Example 1: Iterating over a string")

word = "Python"
for char in word:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n


# 🟡 Example 2: Iterating over a list
print("\n🟡 Example 2: Iterating over a list")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry


# 🟣 Example 3: Iterating over a tuple
print("\n🟣 Example 3: Iterating over a tuple")

numbers = (10, 20, 30)
for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30


# 🔵 Example 4: Iterating over a set
print("\n🔵 Example 4: Iterating over a set")

colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# ⚠️ Sets are unordered, so output order may vary.


# 🟠 Example 5: Iterating over a dictionary (keys, values, items)
print("\n🟠 Example 5: Iterating over a dictionary")

person = {
    "name": "Abdullah",
    "age": 20,
    "city": "Faisalabad"
}

# Iterating over keys
print("Keys:")
for key in person:
    print(key)

# Iterating over values
print("\nValues:")
for value in person.values():
    print(value)

# Iterating over key-value pairs
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"{key} → {value}")


# 🧩 Example 6: Using range() with for loop
print("\n🧩 Example 6: Using range() with for loop")

for i in range(1, 6):
    print(f"Number: {i}")

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


# ---------------------------------------------------
# 🧠 Summary:
# ---------------------------------------------------
# ✅ You can iterate over any iterable (string, list, tuple, set, dict)
# ✅ Use `for` loop for direct access to each element
# ✅ Use `range()` when you need numeric sequences
# ✅ Dictionary supports iteration over keys, values, and key-value pairs
