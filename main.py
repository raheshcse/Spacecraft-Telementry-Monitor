# main.py
# This is the main entry point - it ties everything together
# Run this file to execute the full spacecraft monitoring pipeline

import os
from datetime import datetime
from telemetry_generator import generate_telemetry
from anomaly_detector import detect_anomalies
from ai_analyst import analyse_with_ai

def save_report(report, anomalies):
    """
    Saves the mission health report to a text file.
    Creates a 'reports' folder if it doesn't exist.
    """
    # Create reports folder if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Create a filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/mission_report_{timestamp}.txt"

    # Write the report to the file
    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("       ROCKET LAB SPACECRAFT HEALTH REPORT\n")
        f.write(f"       Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"ANOMALIES DETECTED: {len(anomalies)}\n")
        f.write("-" * 60 + "\n")
        for a in anomalies:
            f.write(f"[{a['severity']}] {a['timestamp']} | {a['sensor']} = {a['value']}\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("AI MISSION ANALYSIS\n")
        f.write("=" * 60 + "\n\n")
        f.write(report)

    return filename


def run_pipeline():
    """
    Runs the full spacecraft monitoring pipeline:
    1. Generate telemetry data
    2. Detect anomalies
    3. Analyse with AI
    4. Save report to file
    """

    print("\n" + "=" * 60)
    print("   🛰️  ROCKET LAB SPACECRAFT MONITOR v1.0")
    print("=" * 60)

    # Step 1 - Generate telemetry
    print("\n[1/4] Generating telemetry data...")
    df = generate_telemetry(num_readings=20)
    print(f"      ✅ {len(df)} readings generated")

    # Step 2 - Detect anomalies
    print("\n[2/4] Scanning for anomalies...")
    anomalies = detect_anomalies(df)
    if anomalies:
        print(f"      ⚠️  {len(anomalies)} anomalies found:")
        for a in anomalies:
            print(f"         [{a['severity']}] {a['sensor']} = {a['value']} at {a['timestamp']}")
    else:
        print("      ✅ All systems nominal")

    # Step 3 - AI analysis
    print("\n[3/4] Sending to AI for analysis...")
    report = analyse_with_ai(df, anomalies)
    print("      ✅ AI report generated")

    # Step 4 - Save report
    print("\n[4/4] Saving report to file...")
    filename = save_report(report, anomalies)
    print(f"      ✅ Report saved to: {filename}")

    # Print the report to terminal too
    print("\n" + "=" * 60)
    print("   📋 MISSION HEALTH REPORT")
    print("=" * 60)
    print(report)
    print("=" * 60)
    print("\n✅ Pipeline complete!\n")


if __name__ == "__main__":
    run_pipeline()