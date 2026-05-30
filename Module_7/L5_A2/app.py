def calculateFactorial(value):
    if value <= 1:
        return 1
    return value * calculateFactorial(value - 1)

numberValue = int(input("Enter a number: "))

if numberValue < 0:
    print("Factorial cannot be found for negative numbers.")
else:
    print("Factorial =", calculateFactorial(numberValue))