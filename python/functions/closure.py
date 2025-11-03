# 🟩 Python Closures — Function Inside Another Function

# ------------------------------------------------------------
# 🔹 What is a Closure?
# ------------------------------------------------------------
# A closure is a function that:
#   1. Is defined inside another function (nested function)
#   2. Accesses variables from the outer function
#   3. Remembers those variables even after the outer function has finished executing

# ------------------------------------------------------------
# ✅ Example: Function Inside Another Function
# ------------------------------------------------------------

def outer_function(name):
    """
    Outer function that defines and returns an inner function.
    """

    # Variable defined in the outer function
    greeting = f"Hello, {name}!"

    def inner_function():
        """
        Inner function that uses variable from the outer function.
        This inner function forms a closure.
        """
        return f"{greeting} Welcome to Python Closures!"

    # Return the inner function (not calling it yet)
    return inner_function


# ------------------------------------------------------------
# 🧪 Using the Closure
# ------------------------------------------------------------

# Call outer_function() and store its returned inner function
welcome_message = outer_function("Abdullah")

# Now call the inner function
print(welcome_message())

# ------------------------------------------------------------
# 🧾 Expected Output:
# ------------------------------------------------------------
# Hello, Abdullah! Welcome to Python Closures!
