from sklearn.tree import DecisionTreeClassifier

# Sample data
X = [
    [25, 50000],
    [35, 80000],
    [45, 100000],
    [20, 30000]
]

y = ["No", "Yes", "Yes", "No"]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[30, 60000]])

print("Prediction:", prediction[0])