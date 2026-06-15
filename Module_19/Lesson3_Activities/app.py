import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math

# Load Dataset
data = pd.read_csv("insurance_data.csv")

# Display first few records
print(data.head())

# Visualize Dataset
plt.scatter(
    data["age"],
    data["bought_insurance"],
    color="blue",
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Bought Insurance")
plt.title("Insurance Purchase Dataset")
plt.show()

# Features and Target
X = data[["age"]]
y = data["bought_insurance"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Logistic Regression Model
classifier = LogisticRegression()

# Train Model
classifier.fit(X_train, y_train)

# Predictions
predicted = classifier.predict(X_test)

# Probability Predictions
probability = classifier.predict_proba(X_test)

print("\nPredicted Values:")
print(predicted)

print("\nPrediction Probabilities:")
print(probability)

# Model Accuracy
accuracy = classifier.score(X_test, y_test)
print("\nAccuracy:", accuracy)

# Model Parameters
print("\nCoefficient:", classifier.coef_)
print("Intercept:", classifier.intercept_)

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Custom Prediction Function
def insurance_prediction(age):
    
    coefficient = classifier.coef_[0][0]
    intercept = classifier.intercept_[0]

    z = coefficient * age + intercept

    return sigmoid(z)

# Test Predictions
print("\nProbability for Age 35:")
print(insurance_prediction(35))

print("\nProbability for Age 43:")
print(insurance_prediction(43))