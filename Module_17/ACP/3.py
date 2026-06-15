# What Are Your Winning Chances?

winning_outcomes = int(input("Enter number of winning outcomes: "))
total_outcomes = int(input("Enter total outcomes: "))

probability = winning_outcomes / total_outcomes

print("Winning Chance =", probability)
print("Winning Chance (%) =", probability * 100)