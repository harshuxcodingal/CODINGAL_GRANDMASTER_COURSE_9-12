import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Load Dataset
data = pd.read_csv("petrol_consumption.csv")

print("First 5 Records")
print(data.head())

# Features and Target
X = data[
    [
        "Petrol_tax",
        "Average_income",
        "Paved_Highways",
        "Population_Driver_licence(%)"
    ]
]

y = data["Petrol_Consumption"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Regression Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Coefficients
print("\nModel Coefficients")
for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)

# Compare Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nPrediction Results")
print(results.head(10))

# Evaluation Metrics
print("\nEvaluation Metrics")
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("Root Mean Squared Error:",
      np.sqrt(mean_squared_error(y_test, y_pred)))

print("R2 Score:",
      r2_score(y_test, y_pred))

# Plot
plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Regression Analysis")

plt.show()