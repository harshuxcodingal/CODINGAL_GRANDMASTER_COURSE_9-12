class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee(101, "Harshal", 50000)

e1.display()