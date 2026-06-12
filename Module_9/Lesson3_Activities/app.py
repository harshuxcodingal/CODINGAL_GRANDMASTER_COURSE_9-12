# ==========================
# 1. CREATE AND WRITE FILES
# ==========================

file1 = open("file1.txt", "w")
file1.write("Python\n")
file1.write("Java\n")
file1.write("Python\n")
file1.close()

file2 = open("file2.txt", "w")
file2.write("C++\n")
file2.write("Java\n")
file2.write("HTML\n")
file2.close()

# ==========================
# 2. READ FILE 1
# ==========================

print("Contents of File1:")
file1 = open("file1.txt", "r")
print(file1.read())
file1.close()

# ==========================
# 3. APPEND CONTENT
# ==========================

file1 = open("file1.txt", "a")
file1.write("Machine Learning\n")
file1.close()

print("\nAfter Appending:")
file1 = open("file1.txt", "r")
print(file1.read())
file1.close()

# ==========================
# 4. READLINES()
# ==========================

file1 = open("file1.txt", "r")
lines = file1.readlines()

print("Readlines Output:")
print(lines)

file1.close()

# ==========================
# 5. FIND DUPLICATE LINES
# ==========================

print("\nDuplicate Lines:")

duplicates = set()

for line in lines:
    if lines.count(line) > 1:
        duplicates.add(line.strip())

for item in duplicates:
    print(item)

# ==========================
# 6. MERGE TWO FILES
# ==========================

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
merged = open("merged.txt", "w")

merged.write(file1.read())
merged.write(file2.read())

file1.close()
file2.close()
merged.close()

# ==========================
# 7. DISPLAY MERGED FILE
# ==========================

print("\nMerged File Content:")

merged = open("merged.txt", "r")
print(merged.read())
merged.close()