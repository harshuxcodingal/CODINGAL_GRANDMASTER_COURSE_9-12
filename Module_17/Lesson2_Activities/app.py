# Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union =", A | B)

# Intersection
print("Intersection =", A & B)

# Addition Rule
PA = float(input("Enter P(A): "))
PB = float(input("Enter P(B): "))
PAB = float(input("Enter P(A and B): "))

print("P(A Union B) =", PA + PB - PAB)