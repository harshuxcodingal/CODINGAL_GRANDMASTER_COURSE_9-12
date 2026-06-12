# Create and Write to a file
file = open("student.txt", "w")
file.write("Name: Harshal\n")
file.write("Course: Python\n")
file.write("Marks: 90\n")
file.close()

print("Data written successfully!")

# Read the file
file = open("student.txt", "r")
data = file.read()
print("\nFile Content:")
print(data)
file.close()