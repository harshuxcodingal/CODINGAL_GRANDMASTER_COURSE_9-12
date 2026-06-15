from sklearn.datasets import make_blobs
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Generate sample dataset
features, labels = make_blobs(
    n_samples=1000,
    centers=2,
    random_state=42
)

# Display dataset information
print("Feature Shape:", features.shape)
print("Label Shape:", labels.shape)

# Count observations in each class
class_count = Counter(labels)

print("\nClass Distribution:")
print(class_count)

# Display first 10 records
print("\nFirst 10 Samples:")
for i in range(10):
    print("Features:", features[i], "Class:", labels[i])

# Plot classified data
for cls in class_count.keys():
    index = np.where(labels == cls)
    
    plt.scatter(
        features[index, 0],
        features[index, 1],
        label=f"Class {cls}"
    )

plt.title("Binary Classification Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()