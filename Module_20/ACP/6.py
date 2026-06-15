import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Load dataset
df = pd.read_csv("Pokemon.csv")

# Drop unnecessary columns (adjust if needed)
df = df.drop(['#', 'Name'], axis=1)

# Convert categorical column (if any)
le = LabelEncoder()
if df['Type 1'].dtype == 'object':
    df['Type 1'] = le.fit_transform(df['Type 1'])
if 'Type 2' in df.columns:
    df['Type 2'] = le.fit_transform(df['Type 2'].astype(str))

# Target variable
X = df.drop('Legendary', axis=1)
y = df['Legendary']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# ANN model
model = Sequential()

model.add(Dense(12, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # classification

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)

# Predictions
y_pred = (model.predict(X_test) > 0.5)

print(y_pred[:10])