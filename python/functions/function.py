# 💡 Understanding Functions in Python

# ---------------------------------------------------
# ✅ A function is a reusable block of code that performs a specific task.
# ✅ It helps to organize code, reduce repetition, and improve readability.
# ---------------------------------------------------

# 🟢 Defining a Function:
# Use the 'def' keyword followed by the function name and parentheses ().
# Then write the indented block of code (the function body).

def greet():
    """A simple function with no parameters."""
    print("Hello! Welcome to Python functions 😊")


# 🟢 Calling a Function:
# Just use the function name followed by parentheses.

greet()


# ---------------------------------------------------
# 🟡 Function Arguments (Parameters)
# ---------------------------------------------------
# Python supports different types of arguments:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable-length Arguments (*args, **kwargs)


# 🧩 Example 1: Positional Arguments
def add(a, b):
    """Takes two numbers and prints their sum."""
    print("Sum is:", a + b)

add(10, 20)  # 10 and 20 are positional arguments


# 🧩 Example 2: Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=20, name="Abdullah")  # Order doesn’t matter when using keywords


# 🧩 Example 3: Default Arguments
def greet_person(name="Guest"):
    print(f"Hello, {name}! 👋")

greet_person("Ali")
greet_person()  # Uses default value "Guest"


# 🧩 Example 4: Variable-length Arguments (*args)
def print_numbers(*args):
    """Accepts any number of positional arguments as a tuple."""
    print("Numbers:", args)

print_numbers(1, 2, 3, 4, 5)


# 🧩 Example 5: Variable-length Keyword Arguments (**kwargs)
def user_info(**kwargs):
    """Accepts keyword arguments as a dictionary."""
    for key, value in kwargs.items():
        print(f"{key} → {value}")

user_info(name="Abdullah", age=20, city="Faisalabad")


# ---------------------------------------------------
# 🟣 Return Values
# ---------------------------------------------------
# Functions can return values using the 'return' keyword.

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

result = multiply(5, 6)
print("\nReturned Value:", result)  # Output: 30


# ---------------------------------------------------
# 🔵 Scope and Lifetime of Variables
# ---------------------------------------------------
# ✅ Scope: The area where a variable is accessible.
#    - Local scope: Defined inside a function.
#    - Global scope: Defined outside all functions.
#
# ✅ Lifetime: The period during which a variable exists in memory.
#    - Local variables are destroyed when the function ends.


# Global variable
language = "Python"

def show_scope():
    # Local variable
    version = 3.14
    print("\nInside Function:")
    print("Language:", language)  # Can access global variable
    print("Version:", version)    # Local variable (only inside function)

show_scope()

print("\nOutside Function:")
print("Language:", language)
# print(version)  # ❌ Error: version is not defined (local variable destroyed)


# 🧠 Using 'global' keyword to modify global variables inside a function
count = 0

def increase_count():
    global count
    count += 1
    print(f"\nCount increased to: {count}")

increase_count()
increase_count()


# ---------------------------------------------------
# 🧠 Summary:
# ---------------------------------------------------
# ✅ Functions = reusable blocks of code
# ✅ Arguments types:
#    → Positional, Keyword, Default, Variable-length (*args, **kwargs)
# ✅ 'return' sends data back to caller
# ✅ Variables have:
#    → Scope (where they are accessible)
#    → Lifetime (how long they exist)
# ✅ 'global' keyword allows modifying global variables inside functions
