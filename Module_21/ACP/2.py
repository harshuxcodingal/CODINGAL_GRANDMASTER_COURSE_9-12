import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Create CNN Model
model = Sequential()

# Convolution Operation
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3,3),
        activation='relu',
        input_shape=(28,28,1)
    )
)

# Pooling Operation
model.add(
    MaxPooling2D(pool_size=(2,2))
)

# Flatten Operation
model.add(
    Flatten()
)

# Fully Connected Layer
model.add(
    Dense(units=128, activation='relu')
)

# Output Layer
model.add(
    Dense(units=10, activation='softmax')
)

# Display Model Summary
model.summary()