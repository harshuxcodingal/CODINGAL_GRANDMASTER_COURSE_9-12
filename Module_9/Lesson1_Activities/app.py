# Write
file = open("sample.txt", "w")
file.write("Python\n")
file.write("Java\n")
file.close()

# Append
file = open("sample.txt", "a")
file.write("C++\n")
file.close()

# Read
file = open("sample.txt", "r")
print(file.read())
file.close()

# Count Lines
file = open("sample.txt", "r")
count = len(file.readlines())
print("Total Lines:", count)
file.close()