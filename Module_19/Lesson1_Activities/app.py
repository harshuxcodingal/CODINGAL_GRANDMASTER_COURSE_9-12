#Activity_1
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

# Load Dataset
cancer_data = load_breast_cancer()

# Display Target Classes
print("Classes:", cancer_data.target_names)

# Count class occurrences
unique_values, class_counts = np.unique(
    cancer_data.target,
    return_counts=True
)

print("\nUnique Labels:", unique_values)
print("Number of Samples:", class_counts)

# Plot Class Distribution
sns.set_style("whitegrid")

plt.figure(figsize=(8, 5))

sns.barplot(
    x=cancer_data.target_names,
    y=class_counts
)

plt.title("Breast Cancer Dataset Classification")
plt.xlabel("Class")
plt.ylabel("Count")

plt.show()



#Activity_2

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.linear_model import SGDClassifier

# Generate Sample Data
X, y = make_blobs(
    n_samples=60,
    centers=2,
    random_state=42,
    cluster_std=0.8
)

# Create Model
model = SGDClassifier(
    loss="hinge",
    alpha=0.01,
    max_iter=500
)

# Train Model
model.fit(X, y)

# Create Grid
x_range = np.linspace(
    X[:, 0].min() - 1,
    X[:, 0].max() + 1,
    100
)

y_range = np.linspace(
    X[:, 1].min() - 1,
    X[:, 1].max() + 1,
    100
)

XX, YY = np.meshgrid(x_range, y_range)

grid = np.c_[XX.ravel(), YY.ravel()]

Z = model.decision_function(grid)
Z = Z.reshape(XX.shape)

# Plot Hyperplane
plt.contour(
    XX,
    YY,
    Z,
    levels=[-1, 0, 1],
    linestyles=["dashed", "solid", "dashed"]
)

# Plot Data Points
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    edgecolors="black"
)

plt.title("Maximum Margin Separating Hyperplane")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()