# ---------------------------------------------------------
# 🧠 What are map(), filter(), and reduce() in Python?
# ---------------------------------------------------------
# These are *higher-order functions* that work with iterables (like lists).
# They help apply a function to each element of an iterable easily.
# ---------------------------------------------------------

# 🟩 Example list
numbers = [1, 2, 3, 4, 5]

# ---------------------------------------------------------
# 🔹 map(function, iterable)
# ---------------------------------------------------------
# → Applies a function to each element of an iterable.
# → Returns a map object (which can be converted to a list).
# ---------------------------------------------------------

def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))
print("Squares using map():", squared_numbers)
# Output: [1, 4, 9, 16, 25]

# 💡 Same thing using lambda:
squared_lambda = list(map(lambda x: x ** 2, numbers))
print("Squares using lambda + map():", squared_lambda)


# ---------------------------------------------------------
# 🔹 filter(function, iterable)
# ---------------------------------------------------------
# → Filters elements from the iterable based on a condition.
# → The function should return True or False.
# ---------------------------------------------------------

def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers using filter():", even_numbers)
# Output: [2, 4]

# 💡 Same thing using lambda:
even_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda + filter():", even_lambda)


# ---------------------------------------------------------
# 🔹 reduce(function, iterable)
# ---------------------------------------------------------
# → Performs a rolling computation on all items in an iterable.
# → Example: sum all numbers, multiply all numbers, etc.
# ---------------------------------------------------------
# 🧩 Note: reduce() is in functools module.

from functools import reduce

def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)
print("Sum using reduce():", sum_of_numbers)
# Output: 15

# 💡 Same thing using lambda:
sum_lambda = reduce(lambda x, y: x + y, numbers)
print("Sum using lambda + reduce():", sum_lambda)


# ---------------------------------------------------------
# ✅ Summary:
# ---------------------------------------------------------
# map()   → Transforms each element (e.g., square, double, etc.)
# filter() → Selects elements that meet a condition (e.g., even, > 10)
# reduce() → Combines all elements into one value (e.g., sum, product)
# ---------------------------------------------------------
