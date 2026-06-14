# ==================================
# SWAP 2 NUMBERS
# ==================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore Swap:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swap:")
print("a =", a)
print("b =", b)


# ==================================
# DIVIDE WITHOUT DIVIDE OPERATOR
# ==================================

dividend = int(input("\nEnter dividend: "))
divisor = int(input("Enter divisor: "))

quotient = 0
temp = dividend

while temp >= divisor:
    temp -= divisor
    quotient += 1

print("Quotient =", quotient)
print("Remainder =", temp)