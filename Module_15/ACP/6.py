# Advanced Plots using Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "Marks": [85, 90, 78, 92, 88, 95, 80, 87]
}

df = pd.DataFrame(data)

# Histogram Plot
sns.histplot(df["Marks"], bins=5)

# Add title
plt.title("Histogram of Student Marks")

# Display graph
plt.show()