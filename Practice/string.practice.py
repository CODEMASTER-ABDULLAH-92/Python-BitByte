# 1. Create a string and access individual characters

name = 'abdullah'
for i in name:
    print(i)

# 2. Slice a string to get substrings
# print(name[:4])

# 3. Convert a string to uppercase and lowercase
print(name.upper())
print(name.lower())

str1 = "PY is fun"

# 4. Check if a string starts/ends with specific substring
print(str1.startswith("PY"))
print(str1.endswith("fun"))

# 5. Find the index of a substring in a string
print(str1.index("i"))

# 6. Replace substrings in a string
print(str1.replace("PY", "CPP"))

# 7. Split a string into a list of words
print(str1.split())

# 8. Join a list of strings into a single string
str2 = ["My", "Name", "Is", "Abdulah"]
print(" ".join(str2)) 

# 9. Remove whitespace from the beginning and end of a string

str3 = "   abdullah    "
print(str3.strip())

# 10. Check if a string contains only alphabets/numbers
print(str3.isalpha())
print(str3.isnumeric())

# 11. Count occurrences of a character in a string
print(str3.count("a"))

# 12. Reverse a string using slicing
print(name[::1]) # This prints the complete string 
print(name[::-1]) # This reverse the string


# 14. Capitalize the first letter of each word in a string

str4 = '''my name is abdullah and what's your name'''
print(str4.title())

# 18. Create a multi-line string with triple quotes
str5 = '''Learn PY is easy'''

# 16. Create a string with special characters and escape sequences

# \n → New line
# \t → Tab space
# \' → Single quote
# \" → Double quote
# \\ → Backslash
# \b → Backspace
# \r → Carriage return

# Example string containing different escape sequences
text = "Hello!\nMy name is Abdullah.\tI\'m learning Python.\nHe said, \"Python is fun!\"\\"

# Printing the string to see the output
print(text)

# ----------------------------------------
# Example of raw string (r"")
# A raw string ignores escape sequences and prints them as they are
path = r"C:\Users\Abdullah\Documents\Python"
print(path)

# Output Explanation:
# - \n creates a new line
# - \t adds a tab space
# - \" and \' allow quotes inside the string
# - \\ prints a single backslash
# - Raw string prints backslashes as normal characters
