import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("Titanic.csv")

# Display first 5 rows
print(data.head())

# Dataset shape
print("Dataset Shape:", data.shape)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualize missing values
sns.heatmap(data.isnull(), cmap="viridis")
plt.show()

# Drop deck column (contains many null values)
data = data.drop("deck", axis=1)

# Remove remaining null values
data.dropna(inplace=True)

# Verify no missing values remain
print("\nAfter Cleaning:")
print(data.isnull().sum())

# Convert categorical columns into numerical form
gender = pd.get_dummies(data["sex"], drop_first=True)

embark = pd.get_dummies(data["embarked"], drop_first=True)

ticket_class = pd.get_dummies(data["pclass"], drop_first=True)

# Merge new columns with dataset
data = pd.concat([data, gender, embark, ticket_class], axis=1)

# Display updated dataset
print("\nProcessed Dataset:")
print(data.head())