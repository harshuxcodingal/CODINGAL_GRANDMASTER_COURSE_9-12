# Visualization to Check Relation Between Variables

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 60, 65, 75, 85, 95]

# Create Scatter Plot
plt.scatter(study_hours, marks)

# Add Title and Labels
plt.title("Relation Between Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Display Graph
plt.show()