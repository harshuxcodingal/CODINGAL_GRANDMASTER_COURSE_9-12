# ==================================
# ONES AND ZEROS
# ==================================

num = int(input("Enter a number: "))

binary = bin(num)[2:]

ones = binary.count("1")
zeros = binary.count("0")

print("\nBinary:", binary)
print("Number of 1s:", ones)
print("Number of 0s:", zeros)

# ==================================
# NTH BIT SET OR NOT
# ==================================

n = int(input("\nEnter position of bit to check: "))

if num & (1 << (n - 1)):
    print(f"{n}th bit is SET")
else:
    print(f"{n}th bit is NOT SET")