# =========================
# Operations on Tuple
# =========================

colors = ("Red", "Green", "Blue", "Yellow")

print("Tuple:", colors)

# Access element
print("First Color:", colors[0])

# Length of tuple
print("Length of Tuple:", len(colors))

# Count occurrences
numbers = (10, 20, 10, 30, 10)
print("Count of 10:", numbers.count(10))

# Find index
print("Index of Green:", colors.index("Green"))

# =========================
# Operations on Set
# =========================

set1 = {10, 20, 30, 40}
print("\nOriginal Set:", set1)

# Add element
set1.add(50)
print("After Add:", set1)

# Remove element
set1.remove(20)
print("After Remove:", set1)

# Check membership
print("Is 30 present?", 30 in set1)

# =========================
# Set Union
# =========================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A.union(B)
print("\nSet A:", A)
print("Set B:", B)
print("Union:", union_set)

# =========================
# Set Intersection
# =========================

intersection_set = A.intersection(B)
print("Intersection:", intersection_set)