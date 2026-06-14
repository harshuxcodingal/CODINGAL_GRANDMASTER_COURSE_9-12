# ==================================
# POWER OF 2
# ==================================

n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    print(n, "is a Power of 2")
else:
    print(n, "is NOT a Power of 2")


# ==================================
# POWER OF 4
# ==================================

m = int(input("\nEnter another number: "))

if m > 0 and (m & (m - 1)) == 0 and (m - 1) % 3 == 0:
    print(m, "is a Power of 4")
else:
    print(m, "is NOT a Power of 4")


# ==================================
# LOG(N) POWER
# ==================================

base = int(input("\nEnter base: "))
exp = int(input("Enter exponent: "))

result = 1

while exp > 0:
    if exp % 2 == 1:
        result *= base

    base *= base
    exp //= 2

print("Answer =", result)