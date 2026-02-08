🔐 OpenIoTIndustrySecurity

OpenIoTIndustrySecurity is a clean-room, open-source Industrial IoT Security & Environmental Monitoring platform designed for real-time sensing, alerting, and live dashboards in industrial and safety-critical environments.

It is built end-to-end in the open using FastAPI, React, and containerized infrastructure, with a strong focus on live data, threshold-based safety automation, and production-ready system design.

This is not a basic sensor demo.

It is a full IoT system with ingestion, storage, alerting, dashboards, simulation, and deployment — designed the way real industrial monitoring platforms are built.

🚀 Why OpenIoTIndustrySecurity Exists

Most IoT “projects” online suffer from one or more of the following:

🟢 Hard-coded demos

🟢 No live data flow

🟢 No real dashboard

🟢 No alert logic

🟢 No deployment story

🟢 No system architecture

Industrial security systems don’t work like that.

OpenIoTIndustrySecurity fills that gap by providing:

🟢 Live sensor ingestion (real or simulated)

🟢 Threshold-based industrial safety alerts

🟢 Real-time monitoring dashboard

🟢 Clean backend architecture

🟢 Dockerized, cloud-ready deployment

🟢 Raspberry Pi–compatible design

All built in a clean-room, reproducible, open-source way.

🧠 Core Design Goals

🟢 Real-time first – live data, not static charts
🟢 Industry-oriented – safety, alerts, thresholds
🟢 Hardware-agnostic – works with real sensors or simulators
🟢 Explainable flows – clear data → decision → alert path
🟢 Infra-ready – Docker, EC2, cloud-deployable
🟢 Fully open – Apache-2.0 license

📐 System Overview

OpenIoTIndustrySecurity follows a stream-based IoT pipeline, inspired by how industrial telemetry systems actually operate.

Stages

Sensing (Flame, CO, Smoke, Temp, Humidity)

Ingestion (HTTP / edge device / simulator)

Validation & Threshold Checks

Persistence (time-series storage)

Alerting

Live Visualization

🧱 ASCII Architecture Diagram (README-friendly)
                    ┌──────────────────────────┐
                    │    Sensors / Edge Node   │
                    │ (Raspberry Pi / Sim)     │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │     FastAPI Backend      │
                    │  Ingestion + Validation  │
                    └─────────────┬────────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
                ▼                 ▼                 ▼
     ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
     │ Threshold Engine │ │   SQLite / DB   │ │  Alert Service  │
     │ (Safety Logic)   │ │ (Time-Series)   │ │ (Events)        │
     └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │   Live React Dashboard   │
                    │  Charts + Alerts + UI   │
                    └──────────────────────────┘

🔩 Tech Stack
Layer	Choice
Backend	FastAPI (Python)
Frontend	React
Charts	Recharts / Live polling
Database	SQLite (pluggable)
Simulation	Python (sensor emulator)
Deploy	Docker + Docker Compose
Hardware	Raspberry Pi compatible
🏗️ Repository Structure
Open-IoT-Industry-Security/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   └── services/
│   ├── requirements.txt
│   └── Dockerfile
├── dashboard/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── package.json
│   └── Dockerfile
├── simulator/
│   └── sensor_simulator.py
├── infrastructure/
│   └── docker-compose.yml
├── docs/
│   └── project_report.pdf
├── README.md
├── LICENSE
└── .gitignore

🧪 Sensor Simulation (Acts Like Real Hardware)

For development and demos, a sensor simulator continuously pushes live data to the backend — exactly like a Raspberry Pi would.

Run it:

python simulator/sensor_simulator.py


Simulated sensors:

🔥 Flame

💨 CO (MQ-7)

🌫 Smoke (MQ-2)

🌡 Temperature

💧 Humidity

🚨 Threshold-Based Industrial Alerts

This system is safety-first, not visualization-first.

Threshold logic is built directly into the backend:

CO concentration limits

Smoke density limits

Temperature danger zones

Flame detection (binary)

Humidity thresholds

Alerts are:

Computed server-side

Logged alongside sensor data

Displayed live on the dashboard

Ready to integrate with SMS / email / IoT actuators

🌐 Live Dashboard

The React dashboard provides:

Live sensor updates (polling / push-ready)

Clear, readable status indicators

Alert visibility

Expandable charts

Once running:

http://localhost:3000


This is not a static UI — it updates continuously with live data.

🐳 Running the Full System
Start everything
docker-compose up --build

Start sensor feed
python simulator/sensor_simulator.py

Access

Backend: http://localhost:8000

Dashboard: http://localhost:3000

🔌 Hardware Compatibility

Designed to work with:

Raspberry Pi

MQ-2 / MQ-7 gas sensors

DHT11 temperature & humidity sensor

Flame sensor modules

Buzzers / LEDs / actuators (future extension)

Only the ingestion layer changes — the rest of the system stays the same.

⚖️ License

Apache License 2.0

You are free to:

Use commercially

Modify

Deploy

Extend

Embed in real systems

⚠️ Disclaimer

This project is a clean-room, independent open-source implementation.

Not affiliated with any industrial vendor

Not tied to proprietary SCADA systems

No restricted or private datasets used

🎯 Who This Is For

IoT & Embedded Engineers

Industrial Automation Engineers

Cloud & DevOps Engineers

Students building real, not toy, IoT systems

Anyone tired of “hello-sensor” demos

🛣️ Roadmap

MQTT / AWS IoT Core support

WebSockets (true push-based live updates)

Grafana integration

Actuator control (relays, shutdown triggers)

Cloud deployment reference (AWS EC2)

⭐ Final Note

OpenIoTIndustrySecurity is meant to be:

Practical

Readable

Deployable

Honest

If you build on it — ship it 🔐🚀
