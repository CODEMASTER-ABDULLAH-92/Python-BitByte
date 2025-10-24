# 🟩 Lists in Python

# ==============================================
# ✅ Definition:
# ==============================================
# A list is a collection of items stored in a single variable.
# It is ordered, mutable (can be changed), and can contain different data types.

# Example:
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "mango"]
mixed = [25, "Abdullah", 3.14, True]



# ==============================================
# ✅ Syntax:
# ==============================================
# Lists are created using square brackets [] with items separated by commas.
my_list = [1, 2, 3, 4, 5]



# ==============================================
# ✅ Accessing List Elements:
# ==============================================
# Indexing starts from 0.

fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
print(fruits[2])   # mango

# 🧠 Negative Indexing:
print(fruits[-1])  # mango (last item)
print(fruits[-2])  # banana



# ==============================================
# ✅ List Slicing:
# ==============================================
# You can extract parts of a list using slicing syntax.
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# Syntax: list[start:end] → end index not included



# ==============================================
# ✅ List Methods:
# ==============================================

fruits = ["apple", "banana", "mango"]

fruits.append("grape")         # Adds element at the end
fruits.insert(1, "orange")     # Inserts at specific position
fruits.remove("banana")        # Removes first occurrence
fruits.pop()                   # Removes last element
fruits.sort()                  # Sorts in ascending order
fruits.reverse()               # Reverses order

print(fruits)
print(len(fruits))             # Returns number of elements



# ==============================================
# ✅ Lists Are Mutable:
# ==============================================
# You can change items after creation.

fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'mango']



# ==============================================
# ✅ Example Program:
# ==============================================

numbers = [5, 10, 15, 20]
print("Original List:", numbers)

numbers.append(25)
print("After append:", numbers)

numbers.remove(10)
print("After remove:", numbers)

print("Length of list:", len(numbers))



# ==============================================
# 🧾 Summary Table:
# ==============================================

| Property               | Description             |
| ---------------------- | ----------------------- |
| **Type**               | Collection (list)       |
| **Ordered**            | ✅ Yes                   |
| **Mutable**            | ✅ Yes (can change)      |
| **Duplicates allowed** | ✅ Yes                   |
| **Data type**          | Can hold multiple types  |
