def getSum(a, b):
    return a + b

def getDifference(a, b):
    return a - b

def getProduct(a, b):
    return a * b

def getDivision(a, b):
    return a / b

firstNumber = float(input("Enter first value: "))
secondNumber = float(input("Enter second value: "))

print("Addition:", getSum(firstNumber, secondNumber))
print("Subtraction:", getDifference(firstNumber, secondNumber))
print("Multiplication:", getProduct(firstNumber, secondNumber))
print("Division:", getDivision(firstNumber, secondNumber))