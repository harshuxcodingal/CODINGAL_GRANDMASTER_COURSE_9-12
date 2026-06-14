# ==================================
# FIRST SET BIT
# ==================================

n = int(input("Enter a number: "))

position = 1

while n > 0:
    if n & 1:
        print("First Set Bit Position =", position)
        break

    n = n >> 1
    position += 1
else:
    print("No set bit found")