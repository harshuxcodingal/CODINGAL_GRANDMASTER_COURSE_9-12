age = int(input("Enter your age: "))
attendance = int(input("Enter attendance percentage: "))

if age >= 18 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")