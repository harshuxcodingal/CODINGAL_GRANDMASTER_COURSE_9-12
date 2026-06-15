import random

data = [10, 20, 30, 40, 50]

sample_means = []

for i in range(100):
    sample = random.choices(data, k=3)
    mean = sum(sample) / len(sample)
    sample_means.append(mean)

print("First 10 Sample Means:")
print(sample_means[:10])

overall_mean = sum(sample_means) / len(sample_means)

print("Average of Sample Means =", overall_mean)