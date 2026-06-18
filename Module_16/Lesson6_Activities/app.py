# Titanic Survival Prediction Analysis

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "Pclass": [1, 3, 2, 1, 3, 2, 1, 3],
    "Age": [22, 38, 26, 35, 28, 19, 45, 30],
    "Fare": [7.25, 71.28, 10.50, 53.10, 8.05, 13.00, 80.00, 7.90],
    "Survived": [0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Titanic Dataset:")
print(df)

# Features and Target
X = df[["Pclass", "Age", "Fare"]]
y = df["Survived"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")



# Iris Data Survey

import pandas as pd
from sklearn.datasets import load_iris

# Load Iris Dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add Species Column
df["Species"] = iris.target

# Display Data
print("First 5 Records:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())