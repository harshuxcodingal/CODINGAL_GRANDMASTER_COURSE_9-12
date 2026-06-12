# Write Mode (w)
file = open("sample.txt", "w")
file.write("Hello Python\n")
file.close()

# Read Mode (r)
file = open("sample.txt", "r")
print("Read Mode:")
print(file.read())
file.close()

# Append Mode (a)
file = open("sample.txt", "a")
file.write("Welcome to File Handling\n")
file.close()

# Read Again
file = open("sample.txt", "r")
print("\nAfter Append:")
print(file.read())
file.close()