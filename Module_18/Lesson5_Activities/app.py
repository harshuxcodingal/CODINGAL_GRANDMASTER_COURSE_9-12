import numpy as np
import matplotlib.pyplot as plt

# Function to minimize
def cost_function(x):
    return x ** 2

# Derivative of the function
def gradient(x):
    return 2 * x

# Gradient Descent
def gradient_descent(start, learning_rate, iterations):
    
    x = start
    x_history = []
    y_history = []

    for i in range(iterations):

        y = cost_function(x)

        x_history.append(x)
        y_history.append(y)

        print(f"Iteration {i+1}: x = {x:.5f}, f(x) = {y:.5f}")

        x = x - learning_rate * gradient(x)

    return x_history, y_history

# Parameters
starting_point = 0.8
learning_rate = 0.1
iterations = 30

# Run Gradient Descent
x_points, y_points = gradient_descent(
    starting_point,
    learning_rate,
    iterations
)

# Plot original function
x = np.linspace(-1, 1, 100)
y = cost_function(x)

plt.plot(x, y, label="f(x)=x²")

# Plot descent path
plt.plot(
    x_points,
    y_points,
    'o-',
    label="Gradient Descent"
)

plt.title("Gradient Descent Example")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()