# telemetry_generator.py
# This file creates fake spacecraft telemetry data for us to analyse

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_telemetry(num_readings=20):
    """
    Generates a list of fake telemetry readings from a spacecraft.
    Each reading represents one snapshot in time.
    """

    readings = []
    base_time = datetime.now()

    for i in range(num_readings):
        # Every reading is 5 minutes apart
        timestamp = base_time + timedelta(minutes=i * 5)

        # Normal values with occasional spikes to simulate anomalies
        reading = {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "battery_percent": round(random.uniform(60, 100), 1),
            "temperature_celsius": round(random.uniform(-10, 40), 1),
            "altitude_km": round(random.uniform(490, 510), 2),
            "signal_strength_dbm": round(random.uniform(-90, -50), 1),
            "cpu_usage_percent": round(random.uniform(10, 70), 1),
        }

        # Randomly inject anomalies into ~20% of readings
        if random.random() < 0.2:
            anomaly_type = random.choice(["battery", "temperature", "signal"])
            if anomaly_type == "battery":
                reading["battery_percent"] = round(random.uniform(5, 20), 1)
            elif anomaly_type == "temperature":
                reading["temperature_celsius"] = round(random.uniform(60, 90), 1)
            elif anomaly_type == "signal":
                reading["signal_strength_dbm"] = round(random.uniform(-120, -100), 1)

        readings.append(reading)

    # Convert to a pandas DataFrame (like a spreadsheet in Python)
    df = pd.DataFrame(readings)
    return df


if __name__ == "__main__":
    # Test it by running this file directly
    df = generate_telemetry()
    print(df)