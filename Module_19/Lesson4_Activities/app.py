import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Iris Dataset
iris = datasets.load_iris()

# Features and Target
X = iris.data
y = iris.target

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Classification Model
classifier = DecisionTreeClassifier()

# Train the model
classifier.fit(X_train, y_train)

# Make Predictions
y_pred = classifier.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Plot first two features
plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=y_pred
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Data Classification using Decision Tree")

plt.show()