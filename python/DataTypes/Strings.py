# 🟩 Strings in Python

# ==> A string is a sequence of characters enclosed in quotes — single ('), double (") or triple (''' / """).
# ==> Strings are used to store text data.

# 🔹 Examples:
name = "Abdullah"
greeting = 'Hello'
message = """This is
a multiline string."""

# --------------------------------------------------
# 🔹 Accessing Characters:
# --------------------------------------------------
# You can access characters using indexing (starting from 0).

word = "Python"
print(word[0])   # Output: P
print(word[5])   # Output: n

# 🧠 Negative indexing works too:
print(word[-1])  # Output: n
print(word[-2])  # Output: o


# --------------------------------------------------
# 🔹 String Slicing:
# --------------------------------------------------
# You can extract parts of a string using slicing.
# Syntax: string[start:end] → end index not included

text = "Programming"
print(text[0:6])    # Output: Progra
print(text[:6])     # Output: Progra
print(text[3:])     # Output: gramming


# --------------------------------------------------
# 🔹 String Concatenation & Repetition:
# --------------------------------------------------
a = "Hello"
b = "World"

print(a + " " + b)     # Output: Hello World
print(a * 3)           # Output: HelloHelloHello


# ============================================================
# 🐍 STRINGS IN PYTHON
# Description: A complete and aesthetic guide covering
#              ➤ String Methods
#              ➤ String Formatting (f-strings & .format)
# ============================================================


# ============================================================
# 🧩 PART 1: STRING METHODS
# ============================================================

# ------------------------------------------------------------
# 1️⃣ upper()
# ------------------------------------------------------------
# Converts all characters in the string to uppercase.
# ------------------------------------------------------------
text = "hello world"
print("🔹 upper():", text.upper())   # Output: HELLO WORLD


# ------------------------------------------------------------
# 2️⃣ lower()
# ------------------------------------------------------------
# Converts all characters in the string to lowercase.
# ------------------------------------------------------------
text = "Hello World"
print("🔹 lower():", text.lower())   # Output: hello world


# ------------------------------------------------------------
# 3️⃣ title()
# ------------------------------------------------------------
# Converts the first letter of each word to uppercase.
# ------------------------------------------------------------
text = "hello world from python"
print("🔹 title():", text.title())   # Output: Hello World From Python


# ------------------------------------------------------------
# 4️⃣ capitalize()
# ------------------------------------------------------------
# Converts the first character to uppercase and others to lowercase.
# ------------------------------------------------------------
text = "python programming"
print("🔹 capitalize():", text.capitalize())  # Output: Python programming


# ------------------------------------------------------------
# 5️⃣ replace(old, new)
# ------------------------------------------------------------
# Replaces all occurrences of a substring with another substring.
# ------------------------------------------------------------
text = "I love JavaScript"
print("🔹 replace():", text.replace("JavaScript", "Python"))  # Output: I love Python


# ------------------------------------------------------------
# 6️⃣ strip(), lstrip(), rstrip()
# ------------------------------------------------------------
# Removes extra spaces from start and/or end of the string.
# ------------------------------------------------------------
text = "   Python is fun!   "
print("🔹 strip():", text.strip())   # Output: Python is fun!
print("🔹 lstrip():", text.lstrip()) # Output: 'Python is fun!   '
print("🔹 rstrip():", text.rstrip()) # Output: '   Python is fun!'


# ------------------------------------------------------------
# 7️⃣ split(separator)
# ------------------------------------------------------------
# Splits a string into a list using the given separator.
# ------------------------------------------------------------
text = "Python is awesome"
print("🔹 split():", text.split())   # Output: ['Python', 'is', 'awesome']

# ------------------------------------------------------------
# 8️⃣ join(iterable)
# ------------------------------------------------------------
# Joins elements of a list (or tuple) into a single string.
# ------------------------------------------------------------
words = ["Python", "is", "fun"]
print("🔹 join():", " ".join(words))  # Output: Python is fun


# ------------------------------------------------------------
# 9️⃣ find(substring)
# ------------------------------------------------------------
# Returns index of first occurrence of substring, or -1 if not found.
# ------------------------------------------------------------
text = "I love Python programming"
print("🔹 find('Python'):", text.find("Python"))  # Output: 7
print("🔹 find('Java'):", text.find("Java"))      # Output: -1


# ------------------------------------------------------------
# 🔟 count(substring)
# ------------------------------------------------------------
# Counts how many times a substring appears in the string.
# ------------------------------------------------------------
text = "apple apple mango apple"
print("🔹 count('apple'):", text.count("apple"))  # Output: 3


# ------------------------------------------------------------
# 1️⃣1️⃣ startswith(prefix), endswith(suffix)
# ------------------------------------------------------------
# Checks if the string starts or ends with a specific substring.
# ------------------------------------------------------------
text = "Masah Dev"
print("🔹 startswith('Masah'):", text.startswith("Masah"))  # True
print("🔹 endswith('Dev'):", text.endswith("Dev"))          # True


# ------------------------------------------------------------
# 1️⃣2️⃣ isalpha(), isdigit(), isalnum()
# ------------------------------------------------------------
# Check if characters are alphabetic, numeric, or alphanumeric.
# ------------------------------------------------------------
print("🔹 isalpha():", "Hello".isalpha())     # True
print("🔹 isdigit():", "1234".isdigit())      # True
print("🔹 isalnum():", "Hello123".isalnum())  # True


# ------------------------------------------------------------
# 1️⃣3️⃣ swapcase()
# ------------------------------------------------------------
# Swaps uppercase letters to lowercase and vice versa.
# ------------------------------------------------------------
text = "PyThOn"
print("🔹 swapcase():", text.swapcase())    # Output: pYtHoN


# ------------------------------------------------------------
# 1️⃣4️⃣ center(width, fillchar)
# ------------------------------------------------------------
# Centers the string and fills empty space with the given character.
# ------------------------------------------------------------
text = "Python"
print("🔹 center():", text.center(12, "-"))  # Output: ---Python---


# ------------------------------------------------------------
# 1️⃣5️⃣ len()
# ------------------------------------------------------------
# Built-in function that returns string length.
# ------------------------------------------------------------
text = "Python"
print("🔹 len():", len(text))  # Output: 6


# ------------------------------------------------------------
# ✅ SUMMARY OF STRING METHODS
# ------------------------------------------------------------
# upper()      → Convert to uppercase
# lower()      → Convert to lowercase
# replace()    → Replace substring
# strip()      → Remove spaces
# split()      → Split into list
# join()       → Join list into string
# find()       → Find substring index
# count()      → Count occurrences
# startswith() → Check start of string
# endswith()   → Check end of string
# isalpha()    → Letters only
# isdigit()    → Digits only
# isalnum()    → Letters + digits
# swapcase()   → Swap cases
# capitalize() → First letter uppercase
# title()      → Each word uppercase
# len()        → Get string length
# ------------------------------------------------------------

print("\n✅ String methods demonstrated successfully!\n")


# ============================================================
# 🎨 PART 2: STRING FORMATTING
# ============================================================

# ------------------------------------------------------------
# 1️⃣ f-Strings (Formatted String Literals)
# ------------------------------------------------------------
# Modern and clean method to format strings using {}
# ------------------------------------------------------------
name = "Muhammad Abdullah"
age = 21
language = "Python"

# Example 1: Insert variables
print(f"👋 Hello, my name is {name} and I am {age} years old.")

# Example 2: Using expressions
print(f"🎂 Next year, I’ll be {age + 1} years old.")

# Example 3: Using string methods inside f-strings
print(f"💬 My name in uppercase: {name.upper()}")

# Example 4: Formatting floating-point numbers
price = 1999.45678
print(f"💰 Price: ${price:.2f}")  # 2 decimal places

# Example 5: Alignment
print(f"|{name:<20}| Left aligned")
print(f"|{name:^20}| Center aligned")
print(f"|{name:>20}| Right aligned")

# ------------------------------------------------------------
# ✨ f-STRING QUICK NOTES
# ------------------------------------------------------------
# {variable}      → Insert variable
# {expr}          → Insert expression
# {var:.2f}       → Format decimal numbers
# {var:<, >, ^}   → Align left, right, center
# {var:10}        → Reserve width of 10 chars



# 🟩===========================================================

# 📚 Topic: String Slicing and Indexing in Python

# 🟩===========================================================

# 🧠 In Python, strings are sequences of characters.
# Each character has a specific position (index) — starting from 0.
# We can access individual characters or parts of a string using:
#   🔹 Indexing → to access single characters
#   🔹 Slicing  → to access a range (portion) of characters


# ============================================================
# 🟦 INDEXING
# ============================================================

# 👉 Indexing means accessing individual characters in a string.
# The index starts from 0 (left to right) and -1 (right to left).

text = "Python"

# ✅ Positive Indexing
print("Character at index 0:", text[0])   # 'P'
print("Character at index 1:", text[1])   # 'y'
print("Character at index 5:", text[5])   # 'n'

# ✅ Negative Indexing (starts from end)
print("Last character:", text[-1])        # 'n'
print("Second last character:", text[-2]) # 'o'


# ============================================================
# 🟨 SLICING
# ============================================================

# 👉 Slicing allows extracting a part (substring) of a string.
# Syntax: string[start:end:step]
#  - start → starting index (included)
#  - end → ending index (excluded)
#  - step → jump (optional)

# Example string
word = "Programming"

# ✅ Basic slicing
print("word[0:6] →", word[0:6])      # 'Progra' (index 0 to 5)
print("word[3:9] →", word[3:9])      # 'grammi'

# ✅ Omitting start or end index
print("word[:7] →", word[:7])        # from start → 'Program'
print("word[4:] →", word[4:])        # from index 4 to end → 'ramming'

# ✅ Using step value
print("word[::2] →", word[::2])      # every 2nd character → 'Pormig'
print("word[::-1] →", word[::-1])    # reversed string → 'gnimmargorP'


# ============================================================
# 🟩 PRACTICAL EXAMPLES
# ============================================================

sentence = "I love Python Programming"

# ✅ Extract a word using slicing
print("Extract 'Python' →", sentence[7:13])

# ✅ Reverse the sentence
print("Reversed Sentence →", sentence[::-1])

# ✅ Get the last 3 characters
print("Last 3 chars →", sentence[-3:])

# ✅ Skip characters
print("Every 2nd char →", sentence[::2])


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
