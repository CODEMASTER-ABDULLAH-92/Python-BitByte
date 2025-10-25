# recursion.py
# ==========================
# 🔁 RECURSION IN PYTHON
# ==========================

# 🧠 Definition:
# Recursion is a process where a function calls itself directly or indirectly.
# It is used to solve problems that can be broken down into smaller, similar sub-problems.
#
# Every recursive function must have a **base case** (to stop recursion)
# and a **recursive case** (where the function calls itself).


# --------------------------
# 🧩 Example 1: Factorial of a Number
# --------------------------
# factorial(n) = n * factorial(n - 1)
# Base Case: factorial(0) = 1

def factorial(n):
    if n == 0:            # Base case (stopping condition)
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print("Factorial of 5:", factorial(5))
# Output: 120


# --------------------------
# 🧩 Example 2: Fibonacci Sequence
# --------------------------
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...
# fib(n) = fib(n-1) + fib(n-2)
# Base Cases: fib(0) = 0, fib(1) = 1

def fibonacci(n):
    if n <= 1:            # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print("Fibonacci(6):", fibonacci(6))
# Output: 8


# --------------------------
# 🧩 Example 3: Sum of Natural Numbers
# --------------------------
# sum(n) = n + sum(n - 1)
# Base Case: sum(0) = 0

def recursive_sum(n):
    if n == 0:           # Base case
        return 0
    else:
        return n + recursive_sum(n - 1)  # Recursive call

print("Sum of first 5 natural numbers:", recursive_sum(5))
# Output: 15


# --------------------------
# ⚙️ Key Points about Recursion
# --------------------------
# ✅ Every recursive function must have a base case, otherwise it leads to infinite recursion.
# ✅ Python has a recursion depth limit (~1000 by default). 
#    You can check it with:
#       import sys
#       print(sys.getrecursionlimit())
# ✅ Recursion is often used in:
#    - Mathematical problems (factorial, Fibonacci)
#    - Divide and conquer algorithms (merge sort, quick sort)
#    - Tree and graph traversal (DFS)

