
# 💡 Understanding Lambda (Anonymous) Functions in Python

# ---------------------------------------------------
# ✅ A lambda function is a small, anonymous (nameless) function.
# ✅ It can take any number of arguments but has only ONE expression.
# ✅ Syntax:
#       lambda arguments : expression
# ---------------------------------------------------

# 🟢 Example 1: Simple lambda function
add = lambda a, b: a + b
print("Sum:", add(5, 3))  # Output: 8


# 🟡 Example 2: Lambda with one argument
square = lambda x: x ** 2
print("Square:", square(4))  # Output: 16


# 🟣 Example 3: Lambda with no arguments
say_hello = lambda: "Hello from Lambda 👋"
print(say_hello())


# ---------------------------------------------------
# 🔵 Using lambda with built-in functions
# ---------------------------------------------------

# 🧩 Example 4: Using lambda with map()
# map() applies the function to every element in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("\nSquared numbers using map():", squared)

# Output: [1, 4, 9, 16, 25]


# 🧩 Example 5: Using lambda with filter()
# filter() selects elements based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# Output: [2, 4]


# 🧩 Example 6: Using lambda with sorted()
# sorted() can use a key function for custom sorting
students = [("Ali", 18), ("Ahmed", 22), ("Sara", 20)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Students sorted by age:", sorted_students)

# Output: [('Ali', 18), ('Sara', 20), ('Ahmed', 22)]


# ---------------------------------------------------
# 🧠 Comparison: lambda vs def
# ---------------------------------------------------
# 'lambda' is best for short, simple functions
# 'def' is best for complex or reusable functions

# Using def
def cube(x):
    return x ** 3

# Using lambda
cube_lambda = lambda x: x ** 3

print("\nCube using def:", cube(3))
print("Cube using lambda:", cube_lambda(3))


# ---------------------------------------------------
# 🧾 Summary:
# ---------------------------------------------------
# ✅ 'lambda' creates small anonymous functions
# ✅ Syntax → lambda arguments : expression
# ✅ Commonly used with map(), filter(), and sorted()
# ✅ Suitable for one-line functions
# ✅ Not ideal for large or complex logic
