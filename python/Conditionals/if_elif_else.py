# if_elif_else.py
# ----------------
# 🎯 In this file, we’ll learn about Conditional Statements in Python.
# Conditional statements are used to make decisions in code.
# They allow your program to execute certain blocks of code only when a condition is True.


# ----------------------------------------------------------
# 🧠 Basic Structure
# ----------------------------------------------------------
# if condition:
#     # code block executes if condition is True
# elif another_condition:
#     # code block executes if previous conditions are False and this is True
# else:
#     # code block executes if all conditions are False


# ----------------------------------------------------------
# 🔹 Example 1: Simple if statement
# ----------------------------------------------------------

x = 10

if x > 5:
    print("x is greater than 5")  # This will run because condition is True


# ----------------------------------------------------------
# 🔹 Example 2: if-else statement
# ----------------------------------------------------------

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ----------------------------------------------------------
# 🔹 Example 3: if-elif-else ladder
# ----------------------------------------------------------

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# ----------------------------------------------------------
# 🔹 Example 4: Nested if statements
# ----------------------------------------------------------

number = 10

if number > 0:
    print("\nNumber is positive")
    if number % 2 == 0:
        print("It is also even")
    else:
        print("It is odd")
else:
    print("Number is zero or negative")


# ----------------------------------------------------------
# 🔹 Example 5: Using Logical Operators in conditions
# ----------------------------------------------------------

temperature = 25

if temperature > 20 and temperature < 30:
    print("\nWeather is pleasant 🌤️")
else:
    print("Weather is too hot or too cold ❄️🔥")


# ----------------------------------------------------------
# 🔹 Example 6: Short-hand if (one-line if)
# ----------------------------------------------------------

x = 15
if x > 10: print("\nThis is a one-line if statement ✅")


# ----------------------------------------------------------
# 🔹 Example 7: Short-hand if-else (Ternary Operator)
# ----------------------------------------------------------

age = 18
status = "Adult" if age >= 18 else "Minor"
print("\nYou are an:", status)


# ----------------------------------------------------------
# 🎯 Summary:
# if → Executes block when condition is True
# elif → Checks next condition if previous ones fail
# else → Executes when all conditions are False
#
# ✅ You can use logical operators (and, or, not) inside conditions.
# ✅ You can nest if statements for complex decision-making.
# ✅ Python supports one-line conditional expressions.
# ----------------------------------------------------------
