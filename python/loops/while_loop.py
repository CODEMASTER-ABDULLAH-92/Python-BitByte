
# ✅ The 'while' loop executes a block of code
#    as long as the given condition is True.

# Example 1: Basic while loop
print("🔁 Example 1: Basic while loop")

count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment to avoid infinite loop

# Example 2: Using break to exit the loop early
print("\n⛔ Example 2: Using 'break' to stop the loop")

num = 1
while num <= 10:
    if num == 5:
        print("Breaking at 5")
        break
    print(num)
    num += 1

# Example 3: Using continue to skip an iteration
print("\n➡️ Example 3: Using 'continue' to skip a value")

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skip printing 3
    print(x)

# Example 4: Using else with while loop
print("\n✅ Example 4: Using 'else' with while loop")

i = 1
while i <= 3:
    print(f"Iteration {i}")
    i += 1
else:
    print("Loop ended normally (no break used)")

# Example 5: Infinite loop with condition control
# ⚠️ Uncomment carefully — it runs forever unless stopped manually!
# print("\n♾️ Example 5: Infinite loop (use Ctrl+C to stop)")
# while True:
#     print("This will run forever!")
