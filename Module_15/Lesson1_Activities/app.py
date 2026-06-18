# Data Cleaning using Pandas

import pandas as pd

# Create DataFrame with missing values
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha"],
    "Marks": [85, None, 78, 92],
    "Age": [18, 19, None, 21]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove duplicate rows (if any)
df = df.drop_duplicates()

# Display cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)