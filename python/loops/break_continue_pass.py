# loop_control_statements.py
# 💡 Understanding loop control statements in Python:
#    break, continue, and pass

# ---------------------------------------------------
# 🟥 1. break statement
# ---------------------------------------------------
# The 'break' statement is used to exit the loop immediately,
# even if the loop condition is still True.

print("🟥 Example 1: break statement")

for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at:", i)
        break  # Exits the loop when i == 5
    print("Current number:", i)

# Output:
# Current number: 1
# Current number: 2
# Current number: 3
# Current number: 4
# Breaking the loop at: 5


# ---------------------------------------------------
# 🟧 2. continue statement
# ---------------------------------------------------
# The 'continue' statement skips the current iteration
# and moves to the next iteration of the loop.

print("\n🟧 Example 2: continue statement")

for num in range(1, 6):
    if num == 3:
        print("Skipping number:", num)
        continue  # Skip the rest of the code for this iteration
    print("Number:", num)

# Output:
# Number: 1
# Number: 2
# Skipping number: 3
# Number: 4
# Number: 5


# ---------------------------------------------------
# 🟨 3. pass statement
# ---------------------------------------------------
# The 'pass' statement is a null operation — it does nothing.
# It is used as a placeholder where code is required syntactically
# but you don't want to execute anything yet.

print("\n🟨 Example 3: pass statement")

for letter in "Python":
    if letter == 'h':
        pass  # Do nothing (placeholder)
        print("(pass executed here)")
    print("Current letter:", letter)

# Output:
# Current letter: P
# Current letter: y
# (pass executed here)
# Current letter: h
# Current letter: o
# Current letter: n


# ---------------------------------------------------
# 🧠 Summary:
# ---------------------------------------------------
# break    → Exit the loop completely.
# continue → Skip current iteration and continue to next.
# pass     → Do nothing (placeholder).
