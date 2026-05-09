# anomaly_detector.py
# This file checks telemetry data and flags anything that looks wrong

def detect_anomalies(df):
    """
    Checks each telemetry reading against safe thresholds.
    Returns a list of anomalies found.
    """

    anomalies = []

    # Define what "normal" looks like for each sensor
    thresholds = {
        "battery_percent":      {"min": 25,   "max": 100},
        "temperature_celsius":  {"min": -20,  "max": 50},
        "altitude_km":          {"min": 480,  "max": 520},
        "signal_strength_dbm":  {"min": -100, "max": -40},
        "cpu_usage_percent":    {"min": 0,    "max": 90},
    }

    # Loop through every reading
    for index, row in df.iterrows():
        for sensor, limits in thresholds.items():
            value = row[sensor]

            # Check if value is outside safe range
            if value < limits["min"] or value > limits["max"]:
                anomalies.append({
                    "timestamp": row["timestamp"],
                    "sensor": sensor,
                    "value": value,
                    "min_allowed": limits["min"],
                    "max_allowed": limits["max"],
                    "severity": get_severity(sensor, value, limits)
                })

    return anomalies


def get_severity(sensor, value, limits):
    """
    Returns HIGH, MEDIUM, or LOW based on how far out of range the value is.
    """
    if sensor == "battery_percent" and value < 15:
        return "HIGH"
    elif sensor == "temperature_celsius" and value > 70:
        return "HIGH"
    elif sensor == "signal_strength_dbm" and value < -110:
        return "HIGH"
    else:
        return "MEDIUM"


if __name__ == "__main__":
    # Test it with generated data
    from telemetry_generator import generate_telemetry

    df = generate_telemetry()
    anomalies = detect_anomalies(df)

    if anomalies:
        print(f"⚠️  {len(anomalies)} anomalies detected:\n")
        for a in anomalies:
            print(f"[{a['severity']}] {a['timestamp']} | {a['sensor']} = {a['value']}")
    else:
        print("✅ All systems nominal. No anomalies detected.")