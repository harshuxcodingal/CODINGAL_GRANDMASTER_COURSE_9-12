# Visualization using Matplotlib

import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 95, 88]

# Create Bar Graph
plt.bar(subjects, marks)

# Add title and labels
plt.title("Student Marks Visualization")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display graph
plt.show()