# ==================================
# IMPLEMENT CIRCUIT (LOGIC GATES)
# ==================================

a = int(input("Enter first bit (0 or 1): "))
b = int(input("Enter second bit (0 or 1): "))

print("\nLogic Gate Outputs:")
print("AND  =", a & b)
print("OR   =", a | b)
print("XOR  =", a ^ b)
print("NOT a =", 1 - a)
print("NOT b =", 1 - b)