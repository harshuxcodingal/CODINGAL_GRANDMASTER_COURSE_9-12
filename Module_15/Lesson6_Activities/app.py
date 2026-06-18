# Iris Dataset Analysis

import pandas as pd
from sklearn.datasets import load_iris

# Load Iris Dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add Species Column
df["Species"] = iris.target

# Display First 5 Records
print("First 5 Records:")
print(df.head())

# Statistical Analysis
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())