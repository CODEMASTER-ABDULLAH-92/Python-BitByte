# ----------------------------------------------
# 1. Create a list of 5 favorite fruits
# ----------------------------------------------

fruits = ['Banana','Apple','Orange']
print(fruits)

# ----------------------------------------------
# 2. Access the first, last, and middle elements of a list
# ----------------------------------------------

fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[0])     # First element
print(fruits[-1])    # Last element
print(fruits[len(fruits)//2])  # Middle element


# ----------------------------------------------
# 3. Add an element to the end of a list using `append()`
# ----------------------------------------------

fruits.append('WaterMelon')
print(fruits)


# ----------------------------------------------
# 4. Insert an element at a specific position using `insert()`
# ----------------------------------------------

fruits.insert(1,'Mango 2')
print(fruits)

# ---------------------------------------------
# 5. Remove an element by value using `remove()`
# ---------------------------------------------

fruits.remove("Mango 2")
print(fruits)


# ---------------------------------------------
# 6. Remove an element by index using `pop()`
# ---------------------------------------------

fruits.pop(1)
print(fruits)


# ---------------------------------------------
# 7. Create a list with mixed data types
# ---------------------------------------------

new_list = [1,2,3,4.5,'Abdullah','Abdur Rehman', 98.3333]


# ---------------------------------------------
# 8. Slice a list to get specific portions
# ---------------------------------------------

print(new_list[1:6])


# ---------------------------------------------
# 9. Reverse a list using slicing and `reverse()`
# ---------------------------------------------

print(new_list[::-1]) # using the slicing

new_list.reverse()
print(new_list)


# ---------------------------------------------
# 10. Sort a list in ascending and descending order
# ---------------------------------------------

new_numeric_list = [32, 75, 31, 65, 22, 76]

new_numeric_list.sort()       # Sorts in ascending order
print("Ascending:", new_numeric_list)
# Output: Ascending: [22, 31, 32, 65, 75, 76]

new_numeric_list.reverse()    # Reverses to descending order
print("Descending:", new_numeric_list)
# Output: Descending: [76, 75, 65, 32, 31, 22]

# ---------------------------------------------
# 11. Find the length of a list using `len()`
# ---------------------------------------------

# print(len(new_numeric_list))


# ---------------------------------------------
# 12. Check if an element exists in a list using `in`
# ---------------------------------------------

fruits = ["apple", "banana", "cherry", "mango"]

if "banana" in fruits:
    print("✅ Banana is in the list!")
else:
    print("❌ Banana is not in the list.")

# Another example:
if "grape" in fruits:
    print("✅ Grape is in the list!")
else:
    print("❌ Grape is not in the list.")



# 💡 Explanation:
# The in operator checks membership in a list (or any iterable).
# It returns True if the element exists, otherwise False.



# ---------------------------------------------
# 13. Concatenate two lists using `+` and `extend()`
# ---------------------------------------------

print(fruits + new_numeric_list)

fruits.extend(["Apple 2", 'Mango 2'])
print(fruits)

# ---------------------------------------------
# 14. Create a nested list (list of lists)
# ---------------------------------------------

nested = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(nested)

# ---------------------------------------------
# 17. Count occurrences of an element in a list
# ---------------------------------------------

new_list_2 = [1,2,2,2,2,4,5,3]
print(new_list_2.count(2)) 

# ---------------------------------------------
# 18. Create a list comprehension that squares numbers 1-10
# ---------------------------------------------

new_li = [x*x for x in range(11)]
print(new_li)
