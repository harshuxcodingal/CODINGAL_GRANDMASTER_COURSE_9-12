# ==========================================
# RECOMMENDATION ENGINE
# ==========================================

print("Welcome to the Recommendation Engine")

# Categories and Recommendations
recommendations = {
    "Movies": [
        "Avatar",
        "Avengers",
        "Interstellar",
        "Titanic"
    ],

    "Books": [
        "Harry Potter",
        "The Alchemist",
        "Rich Dad Poor Dad",
        "Atomic Habits"
    ],

    "Music": [
        "Shape of You",
        "Believer",
        "Perfect",
        "Senorita"
    ],

    "Games": [
        "Minecraft",
        "Free Fire",
        "PUBG",
        "Valorant"
    ]
}

# Display Categories
print("\nAvailable Categories:")

for category in recommendations:
    print("-", category)

# User Choice
choice = input("\nEnter a category: ")

# Recommendation
if choice in recommendations:

    print("\nRecommended Items:")

    for item in recommendations[choice]:
        print(item)

else:
    print("Category not found.")

print("\nThank you for using the Recommendation Engine!")