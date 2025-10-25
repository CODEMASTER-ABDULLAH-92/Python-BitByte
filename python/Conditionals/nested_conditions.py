# 🟨 Nested Conditions in Python

# ✅ A nested condition means putting one if statement inside another if statement.
# ✅ It is used when you want to check multiple conditions in stages — i.e., only check the inner condition if the outer one is true.

# syntax 

"""
if condition1:
    if condition2:
        # Code runs if both condition1 and condition2 are True
    else:
        # Code runs if condition1 is True but condition2 is False
else:
    # Code runs if condition1 is False

"""

# nested_conditions.py
# 💡 Example of Nested Conditions in Python

age = 20
country = "Pakistan"

# Outer condition
if country == "Pakistan":
    print("You are from Pakistan 🇵🇰")

    # Inner condition
    if age >= 18:
        print("You are eligible to vote in Pakistan.")
    else:
        print("You are under 18, not eligible to vote.")
else:
    print("You are not from Pakistan.")


# Another Example
temperature = 35
is_raining = False

if temperature > 30:
    print("\nIt's a hot day! ☀️")
    if is_raining:
        print("Take an umbrella too! ☔")
    else:
        print("Stay hydrated and avoid going out in the sun.")
else:
    print("\nIt's not too hot today.")

"""

You are from Pakistan 🇵🇰
You are eligible to vote in Pakistan.

It's a hot day! ☀️
Stay hydrated and avoid going out in the sun.

"""