import pandas as pd
import matplotlib.pyplot as plt

# Create weather data
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [30, 32, 31, 33, 35, 34, 32]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Weather Data:")
print(df)

# Plot Line Graph
plt.figure(figsize=(8, 5))
plt.plot(df["Day"], df["Temperature"], marker="o")

# Add title and labels
plt.title("Weather Data Visualization")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Show graph
plt.show()