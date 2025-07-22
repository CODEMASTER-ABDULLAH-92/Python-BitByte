# ========================
# 🐍 Python Basics for Beginners
# ========================

# ----- 📤 Output and Comments -----
print("Abdullah")              # Prints a string
print(23)                      # Prints an integer
print("23 + 25 =", 23 + 25)    # Prints the result of addition

# ----- 🔡 Variables and Data Types -----
name = "Abdullah"              # String (text)
age = 22                       # Integer (whole number)
price = 24.99                  # Float (decimal number)

print("Name:", name)
print("Age:", age)
print("Price:", price)

# Check and print data types
print("Type of name:", type(name))     # <class 'str'>
print("Type of age:", type(age))       # <class 'int'>
print("Type of price:", type(price))   # <class 'float'>

# ----- 🧵 Different Ways to Declare Strings -----
name1 = "ab"
name2 = 'ab'
name3 = '''ab'''
print(name1)
print(name2)
print(name3)

# ----- ❌ None Type -----
nothing = None                  # None means no value assigned
print("Nothing:", nothing)
print("Type of nothing:", type(nothing))  # <class 'NoneType'>

# ----- ➕ Arithmetic Operators -----
num1 = 23
num2 = 25
sum_result = num1 + num2        # Addition
print("Sum:", sum_result)

a1 = 10
b1 = 2
print("Addition:", a1 + b1)
print("Subtraction:", a1 - b1)
print("Multiplication:", a1 * b1)
print("Division:", a1 / b1)
print("Modulus:", a1 % b1)
print("Exponent:", a1 ** b1)    # a^b (a raised to the power b)

# ----- 🧮 Relational (Comparison) Operators -----
rel_a = 50
rel_b = 20

# These return True or False
print("rel_a == rel_b:", rel_a == rel_b)
print("rel_a != rel_b:", rel_a != rel_b)
print("rel_a >= rel_b:", rel_a >= rel_b)
print("rel_a <= rel_b:", rel_a <= rel_b)
print("rel_a < rel_b:", rel_a < rel_b)
print("rel_a > rel_b:", rel_a > rel_b)

# ----- 🧷 Assignment Operators -----
x = 5
x += 10
print("x after += 10:", x)

y = 20
y -= 10
print("y after -= 10:", y)

z = 100
z /= 10
print("z after /= 10:", z)

m = 25
m %= 10
print("m after %= 10:", m)

n = 7
n *= 10
print("n after *= 10:", n)

p = 2
p **= 10
print("p after **= 10:", p)

# ----- 🔗 Logical Operators -----
logic_a = True
logic_b = False

# AND returns True only if both are True
result_and = logic_a and logic_b
print("Result of AND:", result_and)

# OR returns True if at least one is True
result_or = logic_a or logic_b
print("Result of OR:", result_or)

# NOT reverses the condition
logic_c = False
result_not = not logic_c
print("Result of NOT:", result_not)

# ----- 🧾 Input from User -----
# input() always returns a string, use type conversion when needed

user_name = input("Enter your name: ")
print("Welcome,", user_name)

user_age = int(input("Enter your age: "))
print("Your age is:", user_age)
print("Type of age:", type(user_age))

user_marks = float(input("Enter your marks: "))
print("Your marks:", user_marks)

# ----- 🧠 Practice Questions -----

# 1️⃣ Add Two Numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Sum =", n1 + n2)

# 2️⃣ Area of a Square
side = int(input("Enter the side of the square: "))
area = side * side
print("Area of Square =", area)

# 3️⃣ Calculate Average of Two Numbers
val1 = float(input("Enter number 1 for average: "))
val2 = float(input("Enter number 2 for average: "))
average = (val1 + val2) / 2
print("Average =", average)

# 4️⃣ Relational Check
check1 = int(input("Enter number 1: "))
check2 = int(input("Enter number 2: "))
print("Is number 1 >= number 2?", check1 >= check2)
