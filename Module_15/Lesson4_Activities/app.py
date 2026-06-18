# Analysis of Blood Sugar Level

import pandas as pd

# Create dataset
data = {
    "Patient": ["P1", "P2", "P3", "P4", "P5"],
    "Blood_Sugar": [90, 120, 140, 110, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Blood Sugar Data:")
print(df)

# Statistical Analysis
print("\nAverage Blood Sugar Level:", df["Blood_Sugar"].mean())
print("Highest Blood Sugar Level:", df["Blood_Sugar"].max())
print("Lowest Blood Sugar Level:", df["Blood_Sugar"].min())