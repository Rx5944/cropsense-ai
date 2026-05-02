import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

BASE_DIR = os.path.dirname(__file__)

data_path = os.path.join(BASE_DIR, "../data/crop_data.csv")
model_path = os.path.join(BASE_DIR, "crop_model.pkl")
encoder_path = os.path.join(BASE_DIR, "label_encoder.pkl")

df = pd.read_csv(data_path)

X = df.drop("label", axis=1)
y = df["label"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("Accuracy:", round(acc*100,2), "%")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(encoder_path, "wb") as f:
    pickle.dump(le, f)

print("Model saved successfully.")