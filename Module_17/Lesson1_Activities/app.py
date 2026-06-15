import random

# Ball Picking Machine
balls = ["Red", "Blue", "Green", "Yellow", "White"]
print("Machine Picked:", random.choice(balls))

# Probability as Fraction
fav = int(input("Favorable Outcomes: "))
total = int(input("Total Outcomes: "))
print("Probability =", fav, "/", total)

# Pick a Ball
bag = ["Red", "Red", "Red",
       "Blue", "Blue",
       "Green"]

print("Ball Picked From Bag:", random.choice(bag))