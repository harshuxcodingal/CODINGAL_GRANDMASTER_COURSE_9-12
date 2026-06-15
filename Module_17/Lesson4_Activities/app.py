import random

# Step Throat Part 1
total_steps = int(input("Enter total steps: "))
favorable_steps = int(input("Enter favorable steps: "))

print("Probability =", favorable_steps / total_steps)

# Step Throat Part 2
step1 = float(input("Probability of Step 1: "))
step2 = float(input("Probability of Step 2: "))

print("Combined Probability =", step1 * step2)

# Dice Roll
print("Dice Roll =", random.randint(1, 6))

# Coin PMF
print("Head Probability =", 0.5)
print("Tail Probability =", 0.5)