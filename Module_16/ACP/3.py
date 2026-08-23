# Quartiles, Quantiles and Interquartile Range

import numpy as np

# Dataset
data = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)  # Median
Q3 = np.percentile(data, 75)

# Interquartile Range
IQR = Q3 - Q1

# Quantiles
quantiles = np.quantile(data, [0.25, 0.50, 0.75])

# Display Results
print("Data:", data)
print("Q1 (First Quartile):", Q1)
print("Q2 (Median):", Q2)
print("Q3 (Third Quartile):", Q3)
print("Interquartile Range (IQR):", IQR)
print("Quantiles:", quantiles)