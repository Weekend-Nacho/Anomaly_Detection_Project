import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate simulated sensor data
def generate_sensor_data(start_time, num_records, num_sensors=5):
    data = []
    for _ in range(num_records):
        timestamp = start_time + timedelta(seconds=np.random.randint(1, 60))
        sensor_id = np.random.choice(range(1, num_sensors + 1))
        temperature = np.random.normal(70, 10)
        humidity = np.random.normal(40, 5)
        sound_volume = np.random.normal(60, 15)
        vibration = np.random.normal(5, 2)

        if np.random.rand() < 0.1:
            temperature += np.random.uniform(30, 50)
            humidity += np.random.uniform(20, 30)
            sound_volume += np.random.uniform(40, 60)
            vibration += np.random.uniform(10, 20)

        data.append({
            "Timestamp": timestamp,
            "Sensor_ID": sensor_id,
            "Temperature_C": round(temperature, 2),
            "Humidity_%": round(humidity, 2),
            "Sound_Volume_dB": round(sound_volume, 2),
            "Vibration_mm_s": round(vibration, 2)
        })

    return pd.DataFrame(data)

# Generate and save simulated data
start_time = datetime.now()
simulated_data = generate_sensor_data(start_time, num_records=1000)
simulated_data.to_csv("simulated_sensor_data.csv", index=False)

print("Simulated sensor data saved as 'simulated_sensor_data.csv'.")

