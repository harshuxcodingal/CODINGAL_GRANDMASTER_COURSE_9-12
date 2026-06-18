# Housing Rent Prediction

import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Area": [500, 700, 900, 1100, 1300],
    "Rent": [8000, 12000, 15000, 18000, 22000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input (Area)
X = df[["Area"]]

# Output (Rent)
y = df["Rent"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict rent for a new house
new_area = [[1000]]
predicted_rent = model.predict(new_area)

print("Predicted Rent for area", new_area[0][0], "sq.ft is Rs.", round(predicted_rent[0], 2))