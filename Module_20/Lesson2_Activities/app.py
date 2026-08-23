import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Sample Dataset
X = np.array([
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [6,7],
    [7,8],
    [8,9]
])

y = np.array([0,0,0,1,1,1,1,1])

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Neural Network Model
model = Sequential()

# Input + Hidden Layer 1
model.add(Dense(
    3,
    activation="relu",
    input_shape=(2,)
))

# Hidden Layer 2
model.add(Dense(
    3,
    activation="relu"
))

# Hidden Layer 3
model.add(Dense(
    3,
    activation="relu"
))

# Output Layer
model.add(Dense(
    1,
    activation="sigmoid"
))

# Compile Model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train Model
model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=1
)

# Evaluate
loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print("\nTesting Loss:", loss)
print("Testing Accuracy:", accuracy)

# Prediction
prediction = model.predict([[5,6]])

print("\nPrediction:")
print(prediction)