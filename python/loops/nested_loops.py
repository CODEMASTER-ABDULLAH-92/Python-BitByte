# ✅ A nested loop means a loop inside another loop.
# The inner loop runs completely for each iteration of the outer loop.
# ---------------------------------------------------

# 🟢 Example 1: Basic nested for loop
print("🟢 Example 1: Basic nested for loop")

for i in range(1, 4):           # Outer loop
    for j in range(1, 4):       # Inner loop
        print(f"i = {i}, j = {j}")
    print("End of inner loop for i =", i)
    print("---")

# Output:
# i = 1, j = 1
# i = 1, j = 2
# i = 1, j = 3
# End of inner loop for i = 1
# ---
# i = 2, j = 1
# ...
# i = 3, j = 3


# 🟡 Example 2: Nested loops for pattern printing
print("\n🟡 Example 2: Printing a simple pattern")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")  # Print on same line
    print()  # Newline after each row

# Output:
# *
# **
# ***
# ****
# *****


# 🟣 Example 3: Nested while loops
print("\n🟣 Example 3: Nested while loops")

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# Output:
# i = 1, j = 1
# i = 1, j = 2
# i = 2, j = 1
# i = 2, j = 2
# i = 3, j = 1
# i = 3, j = 2


# 🔵 Example 4: Using nested loops with lists
print("\n🔵 Example 4: Iterating over 2D list")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Newline after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# ---------------------------------------------------
# 🧠 Summary:
# ---------------------------------------------------
# ✅ Nested loops = loop inside another loop
# ✅ Used for patterns, 2D lists, and grid-based logic
# ✅ Be careful — too many nested loops can slow down performance
