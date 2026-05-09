# ai_analyst.py
# This file sends telemetry anomalies to Groq AI for analysis

import os
from dotenv import load_dotenv
from groq import Groq

# Load your API key from the .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyse_with_ai(df, anomalies):
    """
    Sends telemetry data and anomalies to Groq AI.
    Returns a mission health report as text.
    """

    # Build a summary of the telemetry to send to AI
    telemetry_summary = df.describe().round(2).to_string()

    # Format anomalies into readable text
    if anomalies:
        anomaly_text = "\n".join([
            f"- [{a['severity']}] {a['timestamp']} | {a['sensor']} = {a['value']}"
            for a in anomalies
        ])
    else:
        anomaly_text = "No anomalies detected."

    # This is the prompt we send to the AI
    prompt = f"""
You are an expert spacecraft operations engineer at Rocket Lab.
You have just received telemetry data from a spacecraft in Low Earth Orbit.

TELEMETRY STATISTICS (last 20 readings):
{telemetry_summary}

ANOMALIES DETECTED:
{anomaly_text}

Please provide a mission health report that includes:
1. Overall mission status (NOMINAL / CAUTION / CRITICAL)
2. Summary of anomalies and their potential causes
3. Recommended actions for the operations team
4. Risk assessment

Keep the report professional and concise, as if writing for a real mission operations team.
"""

    # Send to Groq and get response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an expert spacecraft operations engineer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    from telemetry_generator import generate_telemetry
    from anomaly_detector import detect_anomalies

    print("🛰️  Generating telemetry data...")
    df = generate_telemetry()

    print("🔍 Detecting anomalies...")
    anomalies = detect_anomalies(df)
    print(f"   Found {len(anomalies)} anomalies\n")

    print("🤖 Sending to AI for analysis...\n")
    report = analyse_with_ai(df, anomalies)

    print("=" * 60)
    print("         MISSION HEALTH REPORT")
    print("=" * 60)
    print(report)
    print("=" * 60)