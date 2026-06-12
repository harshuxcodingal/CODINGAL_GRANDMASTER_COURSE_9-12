class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def area(self):
        return 0.5 * self.width * self.height

# Rectangle
r = Rectangle(10, 5)
print("Rectangle Area =", r.area())

# Triangle
t = Triangle(10, 5)
print("Triangle Area =", t.area())