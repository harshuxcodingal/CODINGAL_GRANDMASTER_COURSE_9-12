import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Marks": [85, 90, 78, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average marks
average_marks = df["Marks"].mean()

print("Student Data:")
print(df)
print("\nAverage Marks =", average_marks)

# Line Graph
plt.figure(figsize=(6, 4))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Bar Graph
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()