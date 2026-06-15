from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create classifier
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Predict results
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Predicted Values:")
print(predictions)

print("\nActual Values:")
print(y_test)

print("\nAccuracy:", accuracy * 100, "%")