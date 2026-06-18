# Time Velocity Line Graph

import matplotlib.pyplot as plt

# Time in seconds
time = [0, 1, 2, 3, 4, 5]

# Velocity in m/s
velocity = [0, 10, 20, 30, 40, 50]

# Create line graph
plt.plot(time, velocity, marker='o')

# Add title and labels
plt.title("Time vs Velocity Graph")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")

# Show grid
plt.grid(True)

# Display graph
plt.show()