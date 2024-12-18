from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest

# Initialize Flask app
app = Flask(__name__)

# Load trained model and feature columns
feature_columns = ["Temperature_C", "Humidity_%", "Sound_Volume_dB", "Vibration_mm_s"]
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)

# Dummy training for demonstration (replace with actual trained model)
def train_model():
    global model
    sample_data = pd.DataFrame({
        "Temperature_C": [70, 65, 75, 200, 30],
        "Humidity_%": [40, 42, 38, 80, 20],
        "Sound_Volume_dB": [60, 62, 58, 120, 10],
        "Vibration_mm_s": [5, 4, 6, 20, 2]
    })
    model.fit(sample_data)

def predict_anomaly(input_data):
    input_df = pd.DataFrame([input_data])
    anomaly_score = model.decision_function(input_df[feature_columns])[0]
    is_anomaly = int(model.predict(input_df[feature_columns])[0] == -1)
    return {"Anomaly_Score": anomaly_score, "Is_Anomaly": is_anomaly}

# Train the model during initialization
train_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided."}), 400

        missing_features = [col for col in feature_columns if col not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        prediction = predict_anomaly(data)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

