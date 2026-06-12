class Student:
    # Constructor
    def __init__(self, name):
        self.name = name
        print("Constructor Called")
        print("Student Name:", self.name)

    # Destructor
    def __del__(self):
        print("Destructor Called")
        print("Object Destroyed")

s1 = Student("Harshal")

del s1