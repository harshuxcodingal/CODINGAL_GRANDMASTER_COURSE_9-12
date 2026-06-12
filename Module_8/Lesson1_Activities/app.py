# =========================
# Operations on List
# =========================

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Add element
fruits.append("Orange")
print("After Append:", fruits)

# Insert element
fruits.insert(1, "Grapes")
print("After Insert:", fruits)

# Remove element
fruits.remove("Banana")
print("After Remove:", fruits)

# Access element
print("First Fruit:", fruits[0])

# Length of list
print("Number of Fruits:", len(fruits))

# =========================
# List to Dictionary
# =========================

keys = ["name", "age", "city"]
values = ["Harshal", 22, "Nagpur"]

student = dict(zip(keys, values))

print("\nDictionary Created from Lists:")
print(student)

# =========================
# Operations on Dictionary
# =========================

# Add new key-value pair
student["course"] = "Python"
print("\nAfter Adding Course:")
print(student)

# Update value
student["age"] = 23
print("\nAfter Updating Age:")
print(student)

# Access value
print("\nStudent Name:", student["name"])

# Remove item
student.pop("city")
print("\nAfter Removing City:")
print(student)

# Display keys and values
print("\nKeys:", student.keys())
print("Values:", student.values())

# Loop through dictionary
print("\nDictionary Items:")
for key, value in student.items():
    print(key, ":", value)