class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print("Hello!")
        print("My name is", self.name)
        print("My model is", self.model)

# Create an object
r1 = Robot("Robo", "X100")

# Call method
r1.introduce()