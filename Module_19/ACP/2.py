from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pandas as pd

# Generate Dataset
X, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0,
    random_state=42
)

# Scatter Plot
plt.scatter(X, y, c=y, cmap="rainbow")
plt.title("Scatter Plot of Logistic Regression")
plt.xlabel("Feature")
plt.ylabel("Class")
plt.show()

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=1
)

# Create Logistic Regression Model
log_reg = LogisticRegression()

# Train Model
log_reg.fit(X_train, y_train)

# Show Coefficient and Intercept
print("Coefficient:")
print(log_reg.coef_)

print("\nIntercept:")
print(log_reg.intercept_)

# Predict Values
y_pred = log_reg.predict(X_test)

print("\nPredicted Values:")
print(y_pred)

# Actual Values
print("\nActual Values:")
print(y_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Comparison Table
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print("\nComparison Table:")
print(results)