# ==================================
# POWER OF 8
# ==================================

n = int(input("Enter a number: "))

while n > 1 and n % 8 == 0:
    n = n // 8

if n == 1:
    print("Power of 8")
else:
    print("Not a Power of 8")