class Expression:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition =", self.a + self.b)

    def subtract(self):
        print("Subtraction =", self.a - self.b)

    def multiply(self):
        print("Multiplication =", self.a * self.b)

    def divide(self):
        if self.b != 0:
            print("Division =", self.a / self.b)
        else:
            print("Cannot divide by zero")

# Creating object
e1 = Expression(10, 5)

e1.add()
e1.subtract()
e1.multiply()
e1.divide()