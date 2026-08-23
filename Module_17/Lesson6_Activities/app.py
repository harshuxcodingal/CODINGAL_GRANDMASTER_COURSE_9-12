import random

# Puppies Data Sampling
puppies = [2.1, 2.5, 3.0, 2.8, 3.2, 2.9, 2.4, 3.1]

sample = random.sample(puppies, 3)

print("Population:", puppies)
print("Sample:", sample)

# Central Limit Theorem
data = [10, 20, 30, 40, 50]

means = []

for _ in range(100):
    sample = random.choices(data, k=3)

    mean = sum(sample) / len(sample)

    means.append(mean)

print("\nFirst 10 Sample Means:")
print(means[:10])