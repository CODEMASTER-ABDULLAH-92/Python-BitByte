# for_loop.py
# 💡 Understanding the 'for' loop in Python

# ✅ A 'for' loop is used to iterate (loop) over a sequence
#    such as a list, tuple, string, or range of numbers.

# Example 1: Looping through a list
fruits = ["apple", "banana", "cherry"]

print("🍎 Example 1: Looping through a list")
for fruit in fruits:
    print(f"I like {fruit}")

# Example 2: Using range() to loop through numbers
print("\n🔢 Example 2: Looping through numbers using range()")
for i in range(5):  # range(5) gives 0,1,2,3,4
    print(i)

# Example 3: Using range(start, stop, step)
print("\n➡️ Example 3: Using start, stop, and step values in range()")
for num in range(2, 11, 2):  # start=2, stop=11, step=2
    print(num)

# Example 4: Looping through a string
print("\n🔤 Example 4: Looping through a string")
for letter in "Python":
    print(letter)

# Example 5: Using else with for loop
print("\n✅ Example 5: Using else with for loop")
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("Loop completed successfully!")

# Example 6: Nested for loop
print("\n🔁 Example 6: Nested for loop")
colors = ["red", "green", "blue"]
items = ["pen", "book"]

for color in colors:
    for item in items:
        print(f"{color} {item}")



# output 


"""
🍎 Example 1: Looping through a list
I like apple
I like banana
I like cherry

🔢 Example 2: Looping through numbers using range()
0
1
2
3
4
...

"""