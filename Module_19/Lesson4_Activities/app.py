import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Iris Dataset
iris = load_iris()

# Select Features and Target
X = iris.data[:, [0, 2]]   # Sepal Length and Petal Length
y = iris.target

# Check Classification Type
classes = np.unique(y)

if len(classes) > 2:
    print("This is a Multi-Class Classification Dataset")
else:
    print("This is a Binary Classification Dataset")

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Logistic Regression Model
model = LogisticRegression(
    multi_class="multinomial",
    max_iter=200
)

# Train Model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("\nAccuracy:", accuracy_score(y_test, predictions))

# Create Decision Boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.05),
    np.arange(y_min, y_max, 0.05)
)

Z = model.predict(
    np.c_[xx.ravel(), yy.ravel()]
)

Z = Z.reshape(xx.shape)

# Plot Decision Regions
plt.contourf(xx, yy, Z, alpha=0.3)

# Plot Original Data
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    edgecolors="black"
)

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Multi-Class Logistic Regression")

plt.show()