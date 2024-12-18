import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Simulate some sensor data for training
sensor_data = pd.DataFrame({
    "Temperature_C": [70, 65, 75, 200, 30, 68, 72, 64, 150, 85],
    "Humidity_%": [40, 42, 38, 80, 20, 39, 41, 43, 75, 45],
    "Sound_Volume_dB": [60, 62, 58, 120, 10, 65, 63, 59, 110, 70],
    "Vibration_mm_s": [5, 4, 6, 20, 2, 5.5, 4.8, 5.2, 18, 7]
})

# Initialize and train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(sensor_data)

# Save the model to a file
joblib.dump(model, "anomaly_model.pkl")

print("Model trained and saved as 'anomaly_model.pkl'.")

