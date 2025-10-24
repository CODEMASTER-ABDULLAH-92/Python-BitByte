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


# --------------------------------------------------
# 🔹 Common String Functions/Methods:
# --------------------------------------------------
# These are some of the most useful built-in string methods in Python.

# | Function        | Description              | Example                            |
# | --------------- | ------------------------ | ---------------------------------- |
# | `len()`         | Returns length           | `len("Python") → 6`                |
# | `.upper()`      | Convert to uppercase     | `"hi".upper() → "HI"`              |
# | `.lower()`      | Convert to lowercase     | `"HI".lower() → "hi"`              |
# | `.title()`      | First letter capital     | `"python language".title()`        |
# | `.strip()`      | Removes spaces           | `" hello ".strip()`                |
# | `.replace(a,b)` | Replace text             | `"Hello".replace("H","J") → Jello` |
# | `.find(sub)`    | Finds index of substring | `"hello".find("e") → 1`            |
