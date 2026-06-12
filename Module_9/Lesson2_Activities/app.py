# Create file
file = open("demo.txt", "w")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")
file.write("Line 4\n")
file.write("Line 5\n")
file.close()

# Read file
file = open("demo.txt", "r")
print(file.read())
file.close()

# Print odd lines
file = open("demo.txt", "r")
lines = file.readlines()

print("\nOdd Lines:")
for i in range(len(lines)):
    if i % 2 == 0:
        print(lines[i], end="")

file.close()