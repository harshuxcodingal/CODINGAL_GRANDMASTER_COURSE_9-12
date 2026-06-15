import random

# Conditional Probability
PAB = float(input("Enter P(A and B): "))
PB = float(input("Enter P(B): "))

print("P(A|B) =", PAB / PB)

# Multiplication Rule
PA_given_B = float(input("Enter P(A|B): "))
PB2 = float(input("Enter P(B): "))

print("P(A and B) =", PA_given_B * PB2)

# Pick a Shirt
shirts = [
    "Red", "Red", "Red",
    "Blue", "Blue",
    "Black"
]

print("Picked Shirt:", random.choice(shirts))