# Data Distribution Measures

import statistics

# Dataset
data = [10, 20, 30, 40, 50, 60, 70]

# Mean
mean = statistics.mean(data)

# Median
median = statistics.median(data)

# Mode
# (Using a dataset with a repeated value)
data_mode = [10, 20, 20, 30, 40, 50]
mode = statistics.mode(data_mode)

# Range
data_range = max(data) - min(data)

# Variance
variance = statistics.variance(data)

# Standard Deviation
std_dev = statistics.stdev(data)

# Display Results
print("Data:", data)
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Range =", data_range)
print("Variance =", variance)
print("Standard Deviation =", std_dev)