import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "Age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
    "Buy": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Age"]]
y = df["Buy"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LogisticRegression()

# Train Model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# New Prediction
age = [[40]]

prediction = model.predict(age)

print("\nPrediction for Age 40:")

if prediction[0] == 1:
    print("Will Buy")
else:
    print("Will Not Buy")