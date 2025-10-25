# Membership operators are used to test if a value or variable
# is present in a sequence (like a list, tuple, set, string, or dictionary).


# ----------------------------------------------------------
# 🧠 List of Membership Operators
# ----------------------------------------------------------
# Operator | Description                                 | Example
# -------- | ------------------------------------------- | ---------------------
# in       | Returns True if the value is found          | 3 in [1, 2, 3] → True
# not in   | Returns True if the value is NOT found      | 4 not in [1, 2, 3] → True


# ----------------------------------------------------------
# 🔹 Examples with Lists
# ----------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

print("🔹 Fruits List:", fruits)
print("------------------------------")

# 'in' operator
print("'apple' in fruits →", "apple" in fruits)

# 'not in' operator
print("'mango' not in fruits →", "mango" not in fruits)


# ----------------------------------------------------------
# 🔹 Examples with Strings
# ----------------------------------------------------------

name = "Python Programming"

print("\n🔹 String:", name)
print("------------------------------")

print("'Python' in name →", "Python" in name)
print("'Java' not in name →", "Java" not in name)


# ----------------------------------------------------------
# 🔹 Examples with Dictionaries
# ----------------------------------------------------------

student = {"name": "Ali", "age": 20, "grade": "A"}

print("\n🔹 Dictionary:", student)
print("------------------------------")

# Checks only keys, not values
print("'name' in student →", "name" in student)
print("'Ali' in student →", "Ali" in student)  # False (values not checked)
print("'roll_no' not in student →", "roll_no" not in student)


# ----------------------------------------------------------
# 💡 Example Use Case
# ----------------------------------------------------------

email = "test@example.com"

if "@" in email and "." in email:
    print("\n✅ Valid Email Format")
else:
    print("\n❌ Invalid Email Format")


# ----------------------------------------------------------
# 🎯 Summary:
# in → Checks if value exists in a sequence
# not in → Checks if value does NOT exist in a sequence
# ----------------------------------------------------------
