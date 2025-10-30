# -----------------------------------------------------------
# 1. Create a variable `name` and assign your name to it
# -----------------------------------------------------------

# name = "Muhammad Abdullah"
# print(name)





# -----------------------------------------------------------
# 2. Create variables for your age, height, and favorite color
# -----------------------------------------------------------

# age = int(input())
# height = float(input())
# color = input()

# print(age)
# print(height)
# print(color)

# 2nd Way 

# Taking input from the user
# age = int(input("Enter your age: "))        # int() converts the input into an integer
# height = float(input("Enter your height: ")) # float() converts the input into a decimal value
# color = input("Enter your favorite color: ") # input() by default gives a string

# # Displaying the values
# print("Your age:", age)
# print("Your height:", height)
# print("Your favorite color:", color)


# ------------------------------------------------------------------
# 3. Swap the values of two variables without using a third variable
# ------------------------------------------------------------------

# number1 = 10
# number2 = 20

# # name, age, profession = person
# number1, number2 = number2,number1

# print(number1)
# print(number2)


# ------------------------------------------------------------------
# 4. Convert a string to integer and float data types
# ------------------------------------------------------------------

# name = "Muhammad Abdullah"
num_str="123" #The functions int() and float() can only convert strings that represent numbers, like "123" or "3.14".
# str_into_int= int(num_str) 
# str_into_float= float(num_str)

# print(type(str_into_int))
# print(type(str_into_float))


# ------------------------------------------------------------------
# 5. Create a complex number variable
# ------------------------------------------------------------------

num = 5 + 3j   # 'j' represents the imaginary part in Python

# print(num)
# print(type(num))

# ------------------------------------------------------------------
# 6. Check the data type of a variable using `type()`
# ------------------------------------------------------------------

num = 22
# print(type(num))


# ------------------------------------------------------------------
# 7. Create a multi-line string variable
# ------------------------------------------------------------------

# student_dec="""
# My name is abdullah,
# I'm studing in GCUF,
# I'm Full stack Dev"""

# print(student_dec)

# ------------------------------------------------------------------
# 9. Create a boolean variable and perform logical operations
# ------------------------------------------------------------------

# isLoggedIn = True
# age=18
# if(age >= 18 and isLoggedIn == True):
#     print("Access Granted")
# else:
#     print("Access Denied")


# ------------------------------------------------------------------
# 10. Use `input()` to get user input and store it in a variable
# ------------------------------------------------------------------


# user_name = input("Enter User Name ")
# user_age=int(input("Enter The Age "))
# user_percenatge = float(input("Enter Percentage "))

# print("User name ", user_name)
# print("User Age: ",user_age)
# print("User Percentage: ", user_percenatge)


# ------------------------------------------------------------------
# 11. Create variables using different naming conventions
# ------------------------------------------------------------------

# 1️⃣ snake_case (most common in Python)
user_name = "Abdullah"

# 2️⃣ camelCase (used often in JavaScript)
userName = "Muhammad"

# 3️⃣ PascalCase (used for class names)
UserName = "Abdullah Peerzada"

# 4️⃣ UPPER_CASE (used for constants)
USER_AGE = 20

# print(user_name)
# print(userName)
# print(UserName)
# print(USER_AGE)



# ------------------------------------------------------------------
# 12. Demonstrate variable reassignment
# ------------------------------------------------------------------

color = "Black"
print("Original color:", color)

# Reassigning a new value
color = "Blue"
print("Updated color:", color)

# Reassigning another data type
color = 123
print("Color variable now holds:", color)

# ------------------------------------------------------------------
# 13. Create NoneType variable and check its value
# ------------------------------------------------------------------

vari = None
print(type(vari))

# ------------------------------------------------------------------
# 14. Use `id()` function to check memory address of variables
# ------------------------------------------------------------------

color = 123
print("Address of Variable: ", id(color))

# ------------------------------------------------------------------
# 15. Create formatted strings using f-strings
# ------------------------------------------------------------------

# Syntax of f-strings here 

# f"your text {expression}"

name = "Muhammad Abdullah"
age =22
marks = 1082

print(f"My name is {name}. I'm {age} years old and I got {marks} marks in 2nd Year Exam.")


# ------------------------------------------------------------------
# 18. Show the difference between `is` and `==` operators
# ------------------------------------------------------------------

# Example 1: With numbers
a = 10
b = 10

print(a == b)   # ✅ True → values are equal
print(a is b)   # ✅ True → both refer to the same memory location (for small integers)

# Example 2: With lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # ✅ True → values inside both lists are the same
print(list1 is list2)  # ❌ False → they are stored in different memory locations


# ✅ In short:
# is → compares memory address (object identity)
# == → compares values (object content)



# ------------------------------------------------------------
# 🔹 Variable Scope in Python
# ------------------------------------------------------------
# A variable's *scope* determines where it can be accessed.

x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print("Inside function (local x):", x)

my_function()
print("Outside function (global x):", x)




# ------------------------------------------------------------
# 🔹 Using the 'global' Keyword
# ------------------------------------------------------------
# You can modify a global variable inside a function using 'global'

count = 0  # Global variable

def increment():
    global count
    count += 1
    print("Inside function (count):", count)

increment()
increment()
increment()
print("Outside function (global count):", count)
