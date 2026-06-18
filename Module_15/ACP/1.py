# Handling Null Values using Pandas

import pandas as pd

# Create DataFrame with null values
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha"],
    "Marks": [85, None, 78, 92],
    "Age": [18, 19, None, 21]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Check null values
print("\nNull Values:")
print(df.isnull())

# Count null values
print("\nNumber of Null Values:")
print(df.isnull().sum())

# Fill null values with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Display updated DataFrame
print("\nDataFrame after Handling Null Values:")
print(df)