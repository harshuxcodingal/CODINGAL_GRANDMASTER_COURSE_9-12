import pandas as pd

# Sample User Data
data = {
    "User": ["A", "B", "C", "D", "E"],
    "Movie": ["Avatar", "Avatar", "Avengers", "Avatar", "Interstellar"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Count Movie Popularity
movie_count = df["Movie"].value_counts()

print("\nRecommended Movies:")
print(movie_count)

# Most Recommended Movie
print("\nTop Recommendation:")
print(movie_count.index[0])