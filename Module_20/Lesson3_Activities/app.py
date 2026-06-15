import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Sample Dataset
X = np.random.rand(500, 2)
y = np.random.randint(0, 2, 500)

# 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Neural Network
model = Sequential()

# Hidden Layer 1 (4 neurons)
model.add(Dense(
    4,
    activation="sigmoid",
    input_shape=(2,)
))

# Hidden Layer 2 (6 neurons)
model.add(Dense(
    6,
    activation="sigmoid"
))

# Output Layer
model.add(Dense(
    1,
    activation="sigmoid"
))

# Compile
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X_train,
    y_train,
    epochs=20,
    verbose=1
)

# Test
loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print("Testing Loss:", loss)
print("Testing Accuracy:", accuracy)