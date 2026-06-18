# Visualization Using Bar Chart

import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 95, 88]

# Create Bar Chart
plt.bar(subjects, marks)

# Add Title and Labels
plt.title("Student Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display Graph
plt.show()