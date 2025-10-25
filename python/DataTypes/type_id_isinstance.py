# type_id_isinstance.py
# ---------------------
# This file demonstrates three important Python built-in functions:
# 1. type()
# 2. id()
# 3. isinstance()

# ----------------------------------------------------------
# 🧠 1️⃣ type() — Used to find the data type of a variable
# ----------------------------------------------------------

x = 10
y = "Hello"
z = [1, 2, 3]
a = 3.14

print("🔹 type(x):", type(x))   # <class 'int'>
print("🔹 type(y):", type(y))   # <class 'str'>
print("🔹 type(z):", type(z))   # <class 'list'>
print("🔹 type(a):", type(a))   # <class 'float'>


# ----------------------------------------------------------
# 💡 2️⃣ id() — Returns a unique ID (memory address) of an object
# ----------------------------------------------------------

num1 = 100
num2 = 100
num3 = 200

print("\n🔹 id(num1):", id(num1))
print("🔹 id(num2):", id(num2))  # May be same as num1 (Python reuses small integers)
print("🔹 id(num3):", id(num3))  # Usually different ID


# ----------------------------------------------------------
# 🧩 3️⃣ isinstance() — Checks if an object is of a given type
# ----------------------------------------------------------

name = "Abdullah"
age = 21
marks = [90, 95, 88]
info = {"name": "Abdullah", "age": 21}

print("\n🔹 isinstance(name, str):", isinstance(name, str))      # True
print("🔹 isinstance(age, int):", isinstance(age, int))          # True
print("🔹 isinstance(marks, list):", isinstance(marks, list))    # True
print("🔹 isinstance(info, dict):", isinstance(info, dict))      # True
print("🔹 isinstance(info, list):", isinstance(info, list))      # False


# ----------------------------------------------------------
# ✅ Summary:
# type() → tells what type of data a variable holds
# id() → gives unique identity (memory address) of object
# isinstance() → checks if variable belongs to specific data type
# ----------------------------------------------------------
