class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create objects
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Rectangle Area =", r.area())
print("Triangle Area =", t.area())