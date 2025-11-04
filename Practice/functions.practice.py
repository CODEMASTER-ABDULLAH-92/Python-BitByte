# 1. Create a function that greets a user by name


def greets(name):
    print(f"Helo {name}")
    
greets("Abdullah")

# 2. Write a function that returns the square of a number

def squareOfNumber(num):
    return num*num

result = squareOfNumber(5)
print("Result", result)


# ------------------------------------------------------------
# 🔹 Function with Multiple Parameters
# ------------------------------------------------------------
# You can define a function that takes multiple parameters.
# Each parameter acts as a variable inside the function.

def student_info(name, age, course):
    print("Student Name:", name)
    print("Age:", age)
    print("Course:", course)

# ------------------------------------------------------------
# 🔹 Calling the Function
# ------------------------------------------------------------
# You must pass arguments in the same order as parameters.

student_info("Abdullah", 20, "Software Engineering")



def greet(name, message="Welcome to Python!"):
    print(f"Hello {name}, {message}")

greet("Abdullah")               # Uses default message
greet("Ali", "How are you?")    # Custom message


# 6. Write a recursive function to calculate factorial

def calculateTheFactorial(num):
    if num == 0:
        return 1
    else:
       return num * calculateTheFactorial(num - 1)
res =  calculateTheFactorial(5)
print(res)


# 8. Use `*args` to create a function that takes any number of arguments

def takeNumbers(*args):
    res = 0
    for i in args:
        res += i
    return res
response = takeNumbers(1,2,3,4,5)
print(response)

# 9. Use `**kwargs` to create a function that takes keyword arguments

def keyWordFunction(**kwarg):
    for key,value in kwarg.items():
        print(f"{key} -> {value}")

keyWordFunction(user_name = "abdullah", age=22, roll_number=123456)


# 10. Write a function that has both positional and keyword arguments


# def intr(name, age, country="Pakistan"):
#     print(f"My name is {name} and i'm {age} years old. I'm from {country}")

# intr("abdullah", 22, country="Multan")



# 🟨 Python Function with Both Positional and Keyword Arguments

# ------------------------------------------------------------
# 🔹 What are Positional Arguments?
# ------------------------------------------------------------
# Positional arguments are passed to the function in order.
# Their position determines which parameter they correspond to.

# Example:
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")
# greet("Abdullah", 20)   # name="Abdullah", age=20


# ------------------------------------------------------------
# 🔹 What are Keyword Arguments?
# ------------------------------------------------------------
# Keyword arguments are passed using parameter names.
# The order doesn’t matter because each argument is explicitly labeled.

# Example:
# greet(age=20, name="Abdullah")


# ------------------------------------------------------------
# ✅ Function Example: Using Both Positional and Keyword Arguments
# ------------------------------------------------------------
def introduce(person, city, country="Pakistan", hobby="coding"):
    """
    This function introduces a person with both positional and keyword arguments.
    
    Parameters:
    - person (str): Person's name (positional)
    - city (str): Person's city (positional)
    - country (str): Country name (keyword, default = "Pakistan")
    - hobby (str): Hobby name (keyword, default = "coding")
    """
    print(f"Hi, I'm {person} from {city}, {country}. I love {hobby}!")


# ------------------------------------------------------------
# 🧪 Function Calls
# ------------------------------------------------------------
# 1️⃣ Using only positional arguments (default keyword values will apply)
introduce("Abdullah", "Faisalabad")

# 2️⃣ Mixing positional and keyword arguments
introduce("Sara", "Lahore", hobby="reading")

# 3️⃣ Using all keyword arguments (order doesn’t matter)
introduce(person="Ali", city="Karachi", country="UAE", hobby="traveling")

# ------------------------------------------------------------
# 🧾 Expected Output:
# ------------------------------------------------------------
# Hi, I'm Abdullah from Faisalabad, Pakistan. I love coding!
# Hi, I'm Sara from Lahore, Pakistan. I love reading!
# Hi, I'm Ali from Karachi, UAE. I love traveling!


# 11. Create a function inside another function (closure)


def adding(number1 , number2):
    number3 = number1 + number2
    def inner_fun():
        return number3
    return inner_fun

result = adding(5,5)
print(result())

