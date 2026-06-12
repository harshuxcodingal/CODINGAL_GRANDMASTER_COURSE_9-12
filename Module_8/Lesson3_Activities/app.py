class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

class Bird:
    def fly(self):
        print("Bird can fly")

    def sound(self):
        print("Bird makes a sound")

class Parrot(Bird):
    def speak(self):
        print("Parrot can speak")

    def sound(self):
        print("Parrot says Hello!")

# Student Objects
s1 = Student("Harshal", 90)
s2 = Student("Rahul", 85)

s1.display()
print()
s2.display()

print("\n--- Bird Example ---")

p = Parrot()
p.fly()      # Inherited method
p.speak()    # Parrot method
p.sound()    # Overridden method