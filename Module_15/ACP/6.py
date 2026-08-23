# Capstone Project - Student Performance Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Marks": [85, 90, 78, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Student Data:")
print(df)

# Calculate Statistics
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("\nAverage Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Create Bar Chart
plt.bar(df["Name"], df["Marks"])

# Add Title and Labels
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display Graph
plt.show()