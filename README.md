Anomaly Detection in IoT for Wind Turbine Component Production

This project demonstrates a system for detecting anomalies in IoT sensor data collected during the production cycle of wind turbine components. The system includes data simulation, anomaly detection, and a RESTful API for serving predictions in real-time.
Project Overview
Objective

To develop a decision-support system that identifies patterns in sensor data, highlighting potential issues during production. The project focuses on:

    Real-time data ingestion and processing.
    Anomaly detection using machine learning.
    Deploying the model as a service accessible via a standardized API.

Key Features

    Simulated Sensor Data: Generates realistic factory sensor data for attributes like temperature, humidity, and sound volume.
    Anomaly Detection Model: Uses an Isolation Forest model to identify anomalies.
    RESTful API: Allows real-time prediction and easy integration into production systems.

Project Structure

Anomaly_Detection_Project/
├── app.py               # Flask API code
├── model_training.py    # Model training script
├── data_simulation.py   # Data simulation script
├── requirements.txt     # Python dependencies
├── Procfile             # For Heroku deployment
├── README.md            # Project documentation
└── example_requests    # Example API request payloads

Getting Started
1. Prerequisites

    Python 3.9+
    Flask
    Scikit-learn
    (Optional) Heroku CLI for deployment

2. Install Dependencies

Run the following command to install dependencies:

pip install -r requirements.txt

3. Simulate Data

To simulate sensor data:

python data_simulation.py

This generates a dataset (simulated_sensor_data.csv) with sensor readings, including random anomalies.
4. Train the Model

Train the Isolation Forest anomaly detection model using:

python model_training.py

The trained model will be saved as anomaly_model.pkl and used in the API.
5. Run the API

Start the Flask API:

python app.py

The API will be available at http://127.0.0.1:5000.
6. Test the API

Use tools like Postman or curl to test the /predict endpoint.

Example Request:

curl -X POST -H "Content-Type: application/json" \
-d '{"Temperature_C": 72.5, "Humidity_%": 40, "Sound_Volume_dB": 62, "Vibration_mm_s": 5.3}' \
http://127.0.0.1:5000/predict

Example Response:

{
  "Anomaly_Score": -0.12,
  "Is_Anomaly": 1
}

Deployment
Deploying to Heroku

    Log in to Heroku:

heroku login

Create a Heroku App:

heroku create your-app-name

Deploy to Heroku:

git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main

Open the Deployed App:

    heroku open

    Access the API using the Heroku-provided URL (e.g., https://your-app-name.herokuapp.com).

Monitoring and Maintenance
Monitoring

    Use Heroku logs for basic API uptime and error tracking:

    heroku logs --tail

    Implement alerts for high anomaly rates using monitoring tools like Datadog or Prometheus.

Scalability

    Deploy on scalable cloud platforms (e.g., AWS, GCP, Azure).
    Use a production WSGI server like gunicorn for better performance:
        Add gunicorn to requirements.txt:

gunicorn==20.1.0

Update Procfile:

        web: gunicorn app:app
