# ------------------------------------------------------
# 1. Print numbers from 1 to 10 using a for loop
# ------------------------------------------------------
# for i in range(1,11):
#     print(i)

# -----------------------------------------------------
# 2. Print even numbers from 1 to 20 using a for loop
# -----------------------------------------------------

for i in range(1, 21):  # starts from 1, ends at 20
    if i % 2 == 0:      # checks if number is divisible by 2
        print(i)


# --------------------------------------------------------
# 3. Print the multiplication table of 5 using a for loop
# --------------------------------------------------------

for i in range(1, 11):   # Start from 1, not 0
    print(f"5 * {i} = {5 * i}")




# 6. Print a pattern of stars using nested for loops

for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()
    

    
# 7. Find the factorial of a number using a for loop
"""
num = int(input("Enter the number"))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial * i
    
print(f"The factorial of {num} is {factorial}")

"""

# 8. Reverse a string using a for loop


str = "mara name abdullah hai "
chars = list(str)
Reverse=""
left = 0
right = len(chars) - 1

while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left+=1
    right-=1

Reverse = "".join(chars)
print(Reverse)


# 9. Count vowels in a string using a for loop
text = "mara name abdullah hai"
count = 0

for i in text:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Total Vowels:", count)



# 10. Print numbers from 10 to 1 using a while loop
i = 10
while i >=1:
    print(i)
    i -=1
    
    
# 12. Use `continue` to skip even numbers in a loop

for i in range(100):
    if i % 2 == 0:
        continue    
    else:
        print(i)

# 13. Use `else` clause with a for loop


for i in range(5):
    print(i)
else:
    print("Loop completed Successfully")
    
# 🧠 Concept:
# In Python, a for loop can have an else block.
# 👉 The code inside the else block runs only if the loop completes normally (i.e., no break statement is used).

# 15. Find the largest number in a list using a loop

my_list = [2, 4, 5, 6, 8, 10, 14]

maxValue = my_list[0]
for num in my_list:
    if num > maxValue:
        maxValue = num

print("Maximum Value:", maxValue)


# 20. Create a password checker with limited attempts using a while loop

password = "abdullah92"
count = 0

while count < 3:
    usersPassword = input("Enter the password: ")
    
    if usersPassword == password:
        print("✅ Logged in successfully!")
        break
    else:
        print("❌ Incorrect password, try again.")
        count += 1

else:
    # This else runs only if the while loop completes (no break)
    print("🚫 You attempted 3 wrong passwords. Try again after 5 hours.")
