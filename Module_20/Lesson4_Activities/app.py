import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load Dataset
data = pd.read_csv("housing_data.csv")

print(data.head())

# Features and Target
target = data["AboveMedianPrice"]
features = data.drop("AboveMedianPrice", axis=1)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

# Build Neural Network
model = Sequential()

model.add(Dense(
    12,
    activation="relu",
    input_shape=(X_train.shape[1],)
))

model.add(Dense(
    8,
    activation="relu"
))

model.add(Dense(
    1,
    activation="linear"
))

# Compile Model
model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

# Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=8,
    verbose=1
)

# Model Summary
print(model.summary())

# Predictions
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", mae)

accuracy = (1 - mae) * 100
print("Approximate Accuracy:", accuracy, "%")