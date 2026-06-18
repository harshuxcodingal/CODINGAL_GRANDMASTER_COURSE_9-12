# Travel Itinerary Planner

import pandas as pd

# Create travel data
data = {
    "Place": ["Mumbai", "Pune", "Goa", "Delhi", "Jaipur"],
    "Days": [2, 1, 3, 2, 2],
    "Budget": [5000, 3000, 8000, 7000, 6000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Travel Itinerary")
print(df)

# Total Days and Budget
print("\nTotal Days:", df["Days"].sum())
print("Total Budget: Rs.", df["Budget"].sum())


# IMDB Rating Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Movie Data
data = {
    "Movie": ["3 Idiots", "Dangal", "PK", "Sholay", "Lagaan"],
    "Rating": [8.4, 8.3, 8.1, 8.2, 8.1]
}

# Create DataFrame
df = pd.DataFrame(data)

print("IMDB Ratings")
print(df)

# Average Rating
print("\nAverage Rating:", df["Rating"].mean())

# Bar Chart
plt.bar(df["Movie"], df["Rating"])

plt.title("IMDB Movie Ratings")
plt.xlabel("Movies")
plt.ylabel("Ratings")

plt.show()