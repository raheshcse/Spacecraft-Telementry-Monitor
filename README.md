## Spacecraft Telemetry Monitor

An AI-powered spacecraft health monitoring system that automatically detects anomalies in telemetry data and generates professional mission health reports using Large Language Models (LLM).

## Overview

This system simulates a real spacecraft operations pipeline:
1. Collects telemetry data from a spacecraft in Low Earth Orbit (LEO)
2. Automatically detects anomalies across key sensors
3. Uses AI to analyse anomalies and generate a mission health report
4. Saves timestamped reports for mission record keeping

## Features

- Real-time telemetry simulation (battery, temperature, altitude, signal strength, CPU)
- Automatic anomaly detection with HIGH/MEDIUM severity classification
- AI-generated mission health reports with root cause analysis
- Timestamped report saving system
- Clean pipeline with step-by-step progress output

## Tech Stack

- **Python** — core programming language
- **Pandas** — telemetry data processing
- **Groq API (LLaMA 3.1)** — AI mission report generation
- **python-dotenv** — secure API key management

<<<<<<< HEAD

## Project Structure

spacecraft-telemetry-monitor/
├── telemetry_generator.py  # Simulates spacecraft telemetry data
├── anomaly_detector.py     # Detects and classifies anomalies
├── ai_analyst.py           # AI-powered mission report generation
├── main.py                 # Main pipeline entry point
├── reports/                # Auto-generated mission reports
├── .env                    # API keys (not committed to git)
└── README.md               # Project documentation

## 🔭 Future Improvements

- Live telemetry ingestion from real spacecraft APIs
- Web dashboard for real-time monitoring
- Alert notifications via email or Slack
- Historical anomaly trend analysis
- Multi-spacecraft fleet monitoring

## 👨‍💻 Author

Rahesh — Software Engineering Student  
Built as a portfolio project for spacecraft operations roles
>>>>>>> 3341831018374abb2407a5bc248b2504ff37eb10
