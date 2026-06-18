# Statistics for Categorical Variables and Data Transformation

import pandas as pd

# Create Dataset
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha", "Amit"],
    "Gender": ["Male", "Male", "Female", "Female", "Male"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Original Dataset:")
print(df)

# Frequency Count
print("\nGender Frequency:")
print(df["Gender"].value_counts())

print("\nDepartment Frequency:")
print(df["Department"].value_counts())

# Data Transformation
df["Gender_Code"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

print("\nDataset After Transformation:")
print(df)