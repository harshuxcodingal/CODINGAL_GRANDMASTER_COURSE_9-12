# ==================================
# POWER SET
# ==================================

arr = [1, 2, 3]

n = len(arr)

print("Power Set:")

for i in range(1 << n):
    subset = []

    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])

    print(subset)


# ==================================
# FLIP BITS
# ==================================

num = int(input("\nEnter a number: "))

bits = num.bit_length()

mask = (1 << bits) - 1

flipped = num ^ mask

print("Original Binary :", bin(num))
print("Flipped Binary  :", bin(flipped))
print("Flipped Number  :", flipped)