# Create a file and write initial data
file = open("student.txt", "w")
file.write("Harshal\n")
file.write("Rahul\n")
file.close()

# Append new data
file = open("student.txt", "a")
file.write("Priya\n")
file.close()

# Read one line
file = open("student.txt", "r")
print("First Line:")
print(file.readline())
file.close()

# Read all lines
file = open("student.txt", "r")
print("\nAll Lines:")
print(file.readlines())
file.close()