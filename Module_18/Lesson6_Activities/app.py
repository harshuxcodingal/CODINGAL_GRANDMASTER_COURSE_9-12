import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load Dataset
data = pd.read_csv("petrol_consumption.csv")

# Display basic information
print(data.head())
print("\nDataset Summary:")
print(data.describe())

# Select Features and Target
features = data[
    ['Petrol_tax',
     'Average_income',
     'Paved_Highways',
     'Population_Driver_licence(%)']
]

target = data['Petrol_Consumption']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Coefficients
coef_table = pd.DataFrame({
    "Feature": features.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients:")
print(coef_table)

# Predictions
predictions = model.predict(X_test)

# Compare Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nPredictions:")
print(results.head())

# Evaluation Metrics
print("\nModel Performance")
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("Root Mean Squared Error:",
      np.sqrt(mean_squared_error(y_test, predictions)))