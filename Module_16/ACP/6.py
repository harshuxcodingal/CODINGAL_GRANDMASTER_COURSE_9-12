# Exploratory Data Analysis (EDA)

import pandas as pd

# Create Dataset
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Age": [18, 19, 20, 21, 22],
    "Marks": [85, 90, 78, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset:")
print(df)

# First 5 Records
print("\nFirst 5 Records:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())