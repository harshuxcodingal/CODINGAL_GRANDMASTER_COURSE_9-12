# Visualization Using Histogram

import matplotlib.pyplot as plt

# Student Marks Data
marks = [45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 78, 68, 88, 72, 59]

# Create Histogram
plt.hist(marks, bins=5)

# Add Title and Labels
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Display Graph
plt.show()