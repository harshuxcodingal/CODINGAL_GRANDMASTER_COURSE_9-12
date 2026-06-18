# Capstone Project - Student Performance Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Marks": [85, 90, 78, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Student Data:")
print(df)

# Calculate statistics
average = df["Marks"].mean()
highest = df["Marks"].max()
lowest = df["Marks"].min()

print("\nAverage Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Bar Graph
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()