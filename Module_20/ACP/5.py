import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5, 7, 8, 9])

# Create Regression Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Values
y_pred = model.predict(X)

# Model Statistics
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# Plot Original Data
plt.scatter(X, y, label="Actual Data")

# Plot Regression Line
plt.plot(X, y_pred, linewidth=2, label="Regression Line")

plt.title("Regression Analysis with Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

plt.show()