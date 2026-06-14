# ==================================
# REVERSE BITS
# ==================================

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    bit = n & 1          # Get last bit
    reverse = (reverse << 1) | bit
    n = n >> 1           # Remove last bit

print("Reversed Number =", reverse)
print("Binary =", bin(reverse))