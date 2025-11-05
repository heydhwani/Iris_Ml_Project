import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load dataset
df = pd.read_csv("Dataset/iris.csv")

# Add column names
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

#Separate features and target
X = df.drop("species", axis=1)
y = df["species"]

# Label Encode target column
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

#  Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

print("✅ Model trained successfully!")
print(f"\n📈 Accuracy: {accuracy * 100:.2f}%")
print("\n📋 Classification Report:\n")
print(report)

# Save model and label encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅ Model and LabelEncoder saved successfully!")

