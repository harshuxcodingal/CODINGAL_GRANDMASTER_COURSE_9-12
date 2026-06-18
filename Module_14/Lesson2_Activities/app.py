# DataFrame using Pandas

import pandas as pd

# Create a dictionary
data = {
    "Name": ["Harshal", "Rahul", "Priya", "Sneha"],
    "Age": [18, 19, 20, 21],
    "Marks": [85, 90, 88, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)