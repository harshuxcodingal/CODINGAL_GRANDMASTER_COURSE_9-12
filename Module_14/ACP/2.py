# Manipulation using Pandas

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha"],
    "Age": [18, 19, 20, 21],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df["Grade"] = ["A", "A+", "B", "A+"]

# Update a value
df.loc[2, "Marks"] = 80

# Delete a column
df = df.drop("Age", axis=1)

# Display modified DataFrame
print("\nModified DataFrame:")
print(df)