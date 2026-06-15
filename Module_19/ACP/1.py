from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Classification Model
classifier = KNeighborsClassifier(n_neighbors=3)

# Train Model
classifier.fit(X_train, y_train)

# Predict
predictions = classifier.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Sample Prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
result = classifier.predict(sample)

print("\nPredicted Class:", iris.target_names[result[0]])