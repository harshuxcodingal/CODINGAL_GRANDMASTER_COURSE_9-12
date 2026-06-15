# Guess the Event

probability = float(input("Enter probability (0 to 1): "))

if probability == 0:
    print("Impossible Event")
elif probability == 1:
    print("Certain Event")
elif 0 < probability < 1:
    print("Possible Event")
else:
    print("Invalid Probability")