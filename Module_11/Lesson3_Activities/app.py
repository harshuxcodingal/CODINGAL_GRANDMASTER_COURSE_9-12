# ==================================
# 2 EQUAL NUMBERS
# ==================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are Equal")
else:
    print("Numbers are Not Equal")


# ==================================
# ONE ODD OCCURRING NUMBER
# ==================================

arr1 = [4, 3, 4, 4, 4, 5, 5]

result = 0

for num in arr1:
    result ^= num

print("\nOne Odd Occurring Number:", result)


# ==================================
# TWO ODD OCCURRING NUMBERS
# ==================================

arr2 = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]

xor = 0

for num in arr2:
    xor ^= num

rightmost_set_bit = xor & -xor

res1 = 0
res2 = 0

for num in arr2:
    if num & rightmost_set_bit:
        res1 ^= num
    else:
        res2 ^= num

print("Two Odd Occurring Numbers:", res1, "and", res2)