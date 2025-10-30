# ============================================
# 📘 list.py — Lists in Python (Detailed Guide)
# ============================================

# 🟩 What is a List?
# A list is a collection (sequence) of items that are:
# - Ordered
# - Mutable (can be changed)
# - Can store different data types (int, string, float, etc.)

# Example:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']


# ====================================================
# 🟨 INDEXING and SLICING
# ====================================================

# 🧩 Indexing:
# Each element in a list has an index (position) starting from 0.
# Syntax: list[index]

print(fruits[0])   # First element → apple
print(fruits[1])   # Second element → banana
print(fruits[-1])  # Last element → cherry (negative index counts from end)

# 🧩 Slicing:
# Used to access a range of elements.
# Syntax: list[start:end:step]
# (start is inclusive, end is exclusive)

print(fruits[0:2])   # ['apple', 'banana']
print(fruits[:2])    # ['apple', 'banana'] → same as above (start defaults to 0)
print(fruits[1:])    # ['banana', 'cherry'] → end defaults to last
print(fruits[::-1])  # Reverse the list


# ====================================================
# 🟨 LIST METHODS
# ====================================================

# Lists come with several built-in methods for manipulation.


# Initial list
numbers = [1, 2, 9, 4, 2]

# 1️⃣ append() → Adds an item to the end
numbers.append(7)
print("After append:", numbers)
# Output: After append: [1, 2, 9, 4, 2, 7]

# 2️⃣ extend() → Adds multiple items at once like the append adding the only one item but the extend adds the multiple items 
numbers.extend([3, 8])
print("After extend:", numbers)
# Output: After extend: [1, 2, 9, 4, 2, 7, 3, 8]

# 3️⃣ insert() → Adds item at a specific index
numbers.insert(2, 10)

# Here 2 is the index number while 10 is the value you needs to insert 

print("After insert:", numbers)
# Output: After insert: [1, 2, 10, 9, 4, 2, 7, 3, 8]

# 4️⃣ remove() → Removes the first occurrence of a value
numbers.remove(9)
# Here remove function takes the value instead of the index number 
print("After remove:", numbers)
# Output: After remove: [1, 2, 10, 4, 2, 7, 3, 8]

# 5️⃣ pop() → Removes item from the last 
removed_item = numbers.pop()
print("Popped item:", removed_item)
print("After pop:", numbers)
# Output:
# Popped item: 8
# After pop: [1, 2, 10, 4, 2, 7, 3]

# 6️⃣ sort() → Sorts list in ascending order
numbers.sort()
print("After sort:", numbers)
# Output: After sort: [1, 2, 2, 3, 4, 7, 10]

# 7️⃣ reverse() → Reverses the order of elements
numbers.reverse()
print("After reverse:", numbers)
# Output: After reverse: [10, 7, 4, 3, 2, 2, 1]

# 8️⃣ count() → Counts occurrences of a value
print("Count of 2:", numbers.count(2))
# Output: Count of 2: 2

# 9️⃣ index() → Returns the first index of a value
print("Index of 10:", numbers.index(10))
# Output: Index of 10: 0

# 🔟 clear() → Removes all items from the list
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)
# Output: After clear: []



# ====================================================
# 🟨 LIST COMPREHENSION
# ====================================================

# List comprehension provides a short way to create new lists.

# Example 1: Squares of numbers

# --------------------------------------------------
# Syntax 
# --------------------------------------------------

# new_list = [expression for item in iterable if condition (stoping point)]

squares = [x**2 for x in range(5)]
print("\nSquares:", squares)

# Example 2: Convert all fruits to uppercase
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase Fruits:", upper_fruits)

# Example 3: Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)


# ====================================================
# 🟨 NESTED LISTS (List within a List)
# ====================================================

# You can store lists inside other lists.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in nested lists:
print("\nMatrix:")
for row in matrix:
    print(row)

print("Element at row 1, col 2:", matrix[0][1])  # 2
print("Element at row 3, col 3:", matrix[2][2])  # 9

# Flattening a nested list using list comprehension
flat = [num for row in matrix for num in row]
print("Flattened list:", flat)


