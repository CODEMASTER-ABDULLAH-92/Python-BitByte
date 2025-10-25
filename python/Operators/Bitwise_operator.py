# bitwise_operators.py
# --------------------
# 🎯 In this file, we’ll learn about Bitwise Operators in Python.

# Bitwise operators are used to perform operations on binary (bit-level) data.
# They work directly on bits — the 0s and 1s that make up numbers.


# ----------------------------------------------------------
# 🧠 List of Bitwise Operators
# ----------------------------------------------------------
# Operator | Name           | Description                                      | Example
# -------- | -------------- | ------------------------------------------------ | -------------------------
# &        | AND            | Sets each bit to 1 if both bits are 1            | 5 & 3 → 1
# |        | OR             | Sets each bit to 1 if one of the bits is 1       | 5 | 3 → 7
# ^        | XOR            | Sets each bit to 1 if bits are different         | 5 ^ 3 → 6
# ~        | NOT            | Inverts all bits (flips 0s to 1s, and vice versa)| ~5 → -6
# <<       | Left Shift     | Shifts bits to the left (adds zeros on right)    | 5 << 1 → 10
# >>       | Right Shift    | Shifts bits to the right (removes right bits)    | 5 >> 1 → 2


# ----------------------------------------------------------
# 🔹 Example Numbers (in binary)
# ----------------------------------------------------------

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("🔹 a =", a, "→ Binary:", bin(a))
print("🔹 b =", b, "→ Binary:", bin(b))
print("------------------------------")

# AND
print("AND (a & b):", a & b, "→ Binary:", bin(a & b))

# OR
print("OR (a | b):", a | b, "→ Binary:", bin(a | b))

# XOR
print("XOR (a ^ b):", a ^ b, "→ Binary:", bin(a ^ b))

# NOT
print("NOT (~a):", ~a, "→ Binary:", bin(~a))

# Left Shift
print("Left Shift (a << 1):", a << 1, "→ Binary:", bin(a << 1))

# Right Shift
print("Right Shift (a >> 1):", a >> 1, "→ Binary:", bin(a >> 1))


# ----------------------------------------------------------
# 💡 Explanation of Binary Operations (example: a = 5, b = 3)
# ----------------------------------------------------------
# a = 0101
# b = 0011
#
# a & b = 0001 → 1
# a | b = 0111 → 7
# a ^ b = 0110 → 6
# ~a   = Inverts bits → -(a+1) → -6
# a << 1 = 1010 → 10
# a >> 1 = 0010 → 2
# ----------------------------------------------------------


# ----------------------------------------------------------
# 🎯 Summary:
# &  → Bitwise AND
# |  → Bitwise OR
# ^  → Bitwise XOR
# ~  → Bitwise NOT
# << → Left Shift
# >> → Right Shift
# ----------------------------------------------------------
