# Population Growth using Matplotlib

import matplotlib.pyplot as plt

# Years
years = [2018, 2019, 2020, 2021, 2022, 2023]

# Population
population = [50000, 55000, 60000, 68000, 75000, 82000]

# Create Line Graph
plt.plot(years, population, marker='o')

# Add Title and Labels
plt.title("Population Growth")
plt.xlabel("Year")
plt.ylabel("Population")

# Show Grid
plt.grid(True)

# Display Graph
plt.show()