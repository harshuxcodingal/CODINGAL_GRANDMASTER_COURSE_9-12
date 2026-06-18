# Seaborn Library in Python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Create Bar Plot
sns.barplot(x="Name", y="Marks", data=df)

# Add title
plt.title("Student Marks using Seaborn")

# Display graph
plt.show()