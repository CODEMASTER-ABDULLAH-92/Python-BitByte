# ---------------------------------------------------
# ✅ In Python, both 'for' and 'while' loops can have an 'else' block.
# The 'else' part runs when the loop completes normally
# (i.e., it is NOT terminated by a 'break' statement).
# ---------------------------------------------------

# 🟢 Example 1: for loop with else
print("🟢 Example 1: for loop with else")

for num in range(1, 6):
    print(num)
else:
    print("Loop completed successfully ✅")

# Output:
# 1
# 2
# 3
# 4
# 5
# Loop completed successfully ✅


# 🔴 Example 2: for loop with break (else will NOT execute)
print("\n🔴 Example 2: for loop with break")

for i in range(1, 6):
    if i == 3:
        print("Breaking the loop at", i)
        break
    print("Number:", i)
else:
    print("This will NOT print because loop was broken ❌")

# Output:
# Number: 1
# Number: 2
# Breaking the loop at 3


# 🟡 Example 3: while loop with else
print("\n🟡 Example 3: while loop with else")

count = 0
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("While loop finished normally ✅")

# Output:
# Count: 0
# Count: 1
# Count: 2
# While loop finished normally ✅


# 🟣 Example 4: while loop with break (else skipped)
print("\n🟣 Example 4: while loop with break")

num = 0
while num < 5:
    if num == 2:
        print("Breaking at:", num)
        break
    print("Number:", num)
    num += 1
else:
    print("This will NOT print ❌")

# Output:
# Number: 0
# Number: 1
# Breaking at: 2


# ---------------------------------------------------
# 🧠 Summary:
# ---------------------------------------------------
# ✅ 'else' runs ONLY if the loop ends normally (no 'break')
# ✅ Works with both 'for' and 'while' loops
# ✅ Commonly used for searching tasks
