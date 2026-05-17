import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset path
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "machine_failure.csv")

# Load dataset
df = pd.read_csv(DATASET_PATH)

# Features
X = df[[
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]'
]]

# Failure Type Target
# Priority based labeling

def get_failure_type(row):
    if row['TWF'] == 1:
        return 'Tool Wear Failure'
    elif row['HDF'] == 1:
        return 'Heat Dissipation Failure'
    elif row['PWF'] == 1:
        return 'Power Failure'
    elif row['OSF'] == 1:
        return 'Overstrain Failure'
    elif row['RNF'] == 1:
        return 'Random Failure'
    else:
        return 'No Failure'


# Create target column

df['Failure Type'] = df.apply(get_failure_type, axis=1)

y = df['Failure Type']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Save model
MODEL_DIR = os.path.join(BASE_DIR, 'model')
print("Model saved successfully!")