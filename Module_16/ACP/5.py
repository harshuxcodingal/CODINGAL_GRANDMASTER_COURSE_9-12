# Data Transformation and Data Association

import pandas as pd

# Create Dataset
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Gender": ["Male", "Male", "Female", "Female", "Male"],
    "Marks": [85, 90, 78, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Original Data
print("Original Dataset:")
print(df)

# Data Transformation
df["Gender_Code"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

print("\nDataset After Transformation:")
print(df)

# Data Association (Correlation)
correlation = df["Gender_Code"].corr(df["Marks"])

print("\nCorrelation between Gender_Code and Marks:")
print(correlation)