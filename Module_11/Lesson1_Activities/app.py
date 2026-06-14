# ==================================
# IMPLEMENT BITWISE OPERATIONS
# ==================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBitwise Operations")
print("AND (&) =", a & b)
print("OR (|) =", a | b)
print("XOR (^) =", a ^ b)
print("Left Shift (a << 1) =", a << 1)
print("Right Shift (a >> 1) =", a >> 1)

# ==================================
# ODD OR EVEN USING BITWISE
# ==================================

num = int(input("\nEnter a number to check Odd/Even: "))

if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")

# ==================================
# NUMBER OF BITS
# ==================================

n = int(input("\nEnter a number to count bits: "))

bits = len(bin(n)) - 2

print("Binary Representation:", bin(n))
print("Number of Bits:", bits)