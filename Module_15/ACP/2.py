# Visualization using Line Plot

import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1800, 1700, 2100, 2500]

# Create Line Plot
plt.plot(months, sales, marker='o')

# Add Title and Labels
plt.title("Monthly Sales Analysis")
plt.xlabel("Months")
plt.ylabel("Sales")

# Add Grid
plt.grid(True)

# Display Graph
plt.show()