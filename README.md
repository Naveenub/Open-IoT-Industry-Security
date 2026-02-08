# **🔐 OpenIoTIndustrySecurity**

**OpenIoTIndustrySecurity** is a clean-room, open-source **Industrial IoT Security & Environmental Monitoring platform** designed for **real-time sensing, alerting, and live dashboards** in industrial and safety-critical environments.

It is built end-to-end in the open using **FastAPI, React, and containerized infrastructure,** with a strong focus on **live data, threshold-based safety automation,** and **production-ready system design**.

This is not a basic sensor demo.

It is a **full IoT system** with ingestion, storage, alerting, dashboards, simulation, and deployment — designed the way **real industrial monitoring platforms are built**.

---

🚀 **Why OpenIoTIndustrySecurity Exists**

Most IoT “projects” online suffer from one or more of the following:

* Hard-coded demos
* No live data flow
* No real dashboard
* No alert logic
* No deployment story
* No system architecture

Industrial security systems don’t work like that.

**OpenIoTIndustrySecurity fills that gap** by providing:

* Live sensor ingestion (real or simulated)
* Threshold-based industrial safety alerts
* Real-time monitoring dashboard
* Clean backend architecture
* Dockerized, cloud-ready deployment
* Raspberry Pi–compatible design

All built in a **clean-room, reproducible, open-source** way.

---

🧠 **Core Design Goals**

* **Real-time first** – live data, not static charts
* **Industry-oriented** – safety, alerts, thresholds
* **Hardware-agnostic** – works with real sensors or simulators
* **Explainable flows** – clear data → decision → alert path
* **Infra-ready** – Docker, EC2, cloud-deployable
* **Fully open** – Apache-2.0 license

---

📐 **System Overview**

OpenIoTIndustrySecurity follows a **stream-based IoT pipeline**, inspired by how industrial telemetry systems actually operate.

| Stage                          | Description                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| Sensing                        | Flame, CO, Smoke, Temp, Humidity                                                       |
| Ingestion                      | HTTP, edge device, simulator                                                           |
| Validation & Threshold Checks  | Schema validation, Range checks, Threshold evaluation                                  |
| Persistence                    | High-frequency writes, Historical analysis, Trend detection, Auditing & compliance     |
| Alerting                       | Dashboard notifications, Logs / events, Webhooks (SMS, email, Slack-ready)             |
| Live Visualization             | Live sensor graphs, Zone-wise status indicators, Alert timelines, Historical playback  |

---

🔩 **Tech Stack**

| Layer	        | Choice
| ------------- | -------------------------- |
| Backend	      | FastAPI (Python)           |
| Frontend	    | React                      |
| Charts	      | Recharts / Live polling    |
| Database	    | SQLite (pluggable)         |
| Simulation	  | Python (sensor emulator)   |
| Deploy	      | Docker + Docker Compose    |
| Hardware	    | Raspberry Pi compatible    |

---

🏗️ **Repository Structure**

```
Open-IoT-Industry-Security/
├── backend/                         # Backend services (API + processing)
│   ├── app/
│   │   ├── main.py                  # FastAPI application entrypoint
│   │   ├── api/
│   │   │   └── routes.py            # Sensor ingestion & query endpoints
│   │   ├── core/
│   │   │   ├── config.py            # Environment & app configuration
│   │   │   └── thresholds.py        # Safety limits & alert rules
│   │   ├── db/
│   │   │   └── database.py          # Time-series data persistence layer
│   │   ├── models/
│   │   │   └── sensor.py            # Sensor data models & schemas
│   │   ├── ml/
│   │   |   └── anomaly_detector.py
│   │   ├── rag/
│   │   |   ├── vector_store.py        # LangChain + embeddings
│   │   |   └── advisor.py             # RAG reasoning
│   │   ├── llm/
│   │   |   └── incident_reporter.py   # LLM summaries
│   │   ├── aws/
│   │   |   ├── iot.py                 # AWS IoT ingestion
│   │   |   ├── sns.py                 # SMS alerts
│   │   |   └── ses.py                 # Email alerts
│   │   ├── realtime/
│   │   |   └── websocket.py           # Live push to UI
│   │   └── services/
│   │       ├── alert_service.py     # Alerting & notification logic
│   │       └── notifier/               # NEW
│   │           ├── __init__.py
│   │           ├── email.py
│   │           ├── sms.py
│   │           └── webhook.py
│   ├── core/
│   │   └── config.py               # extended
│   ├── requirements.txt             # Backend dependencies
│   └── Dockerfile                   # Backend container definition
├── dashboard/                       # Live monitoring dashboard (UI)
│   ├── src/
│   │   ├── App.jsx                  # Dashboard root component
│   │   ├── api.js                   # Backend API client
│   │   ├── components/
│   │   │   ├── Dashboard.jsx        # Main dashboard view
│   │   │   ├── SensorCard.jsx       # Real-time sensor widgets
│   │   │   └── Alerts.jsx           # Alerts & warnings panel
│   │   └── main.jsx                 # Frontend bootstrap
│   ├── package.json                 # Frontend dependencies
│   └── Dockerfile                   # Dashboard container definition
├── simulator/                       # Sensor data simulator
│   └── sensor_simulator.py          # Generates live test telemetry
├── infrastructure/                  # Deployment & orchestration
│   └── docker-compose.yml           # Full stack deployment (API + UI)
├── docs/                            # Documentation & assets
│   ├── architecture.png             # System architecture diagram
│   └── project_report.pdf           # Detailed project report
├── .env.example                     # Environment variable template
├── README.md                        # Project documentation
├── LICENSE                          # Open-source license
└── .gitignore                       # Git ignore rules
```

---

🧩 **How This Maps to the System Pipeline**

```
Sensors → Simulator → Backend API → Validation → Storage → Alerts → Dashboard
```

* **backend/** → ingestion, validation, persistence, alerting
* **dashboard/** → real-time visualization & operator view
* **simulator/** → live data generation for testing & demos
* **infrastructure/** → production-ready deployment

---

🧱 **ASCII Architecture Diagram (README-friendly)**

                       ┌──────────────────────────────────────────────┐
                       │                Industrial Sensors            │
                       │  Flame | CO | Smoke | Temperature | Humidity │
                       └───────────────────────┬──────────────────────┘
                                               │
                                               ▼
                             ┌───────────────────────────────────┐
                             │         Edge / Device Layer       │
                             │  Raspberry Pi / ESP32 / Simulator │
                             │  • Sampling & normalization       │
                             │  • JSON telemetry                 │
                             └─────────────────┬─────────────────┘
                                               │ HTTP / MQTT
                                               ▼
                                ┌─────────────────────────────┐
                                | Cloud Ingestion (Optional)  │
                                │ AWS IoT Core                │
                                │ • Device auth (certs)       │
                                │ • Secure ingestion          │
                                └──────────────┬──────────────┘
                                               │
                                               ▼
          ┌─────────────────────────────────────────────────────────────────────────┐
          │                               Backend (FastAPI)                         │
          │                                 backend/app                             │
          │                                                                         │
          │                     ┌───────────────────────────────────┐               │
          │                     │ API Layer (api/routes.py)         │               │
          │                     │ • /ingest  • /sensors  • /alerts  │               │ 
          │                     └─────────────────┬─────────────────┘               │
          │                                       │                                 │
          │                        ┌──────────────▼─────────────┐                   │
          │                        │ Validation & Rules Engine  │                   |
          │                        │ (core/thresholds.py)       │                   │
          │                        │ • Schema validation        │                   │
          │                        │ • Safety thresholds        │                   │
          │                        └────────────┬───────────────┘                   │
          │                                     │                                   │
          │                       ┌─────────────▼──────────────┐                    │
          │                       │ ML Anomaly Detection       │                    │
          │                       │ (ml/anomaly_detector.py)   │                    │
          │                       │ • Trend deviation          │                    │
          │                       │ • Early hazard detection   │                    │
          │                       └─────────────┬──────────────┘                    │
          │                                     │                                   │
          │                   ┌─────────────────▼──────────────────┐                │
          │                   │ RAG Intelligence Layer             │                │
          │                   │ (rag/vector_store.py, advisor.py)  │                │
          │                   │ • LangChain                        │                │
          │                   │ • Vector DB (FAISS)                │                │
          │                   │ • SOPs, manuals, incident history  │                │
          │                   └─────────────────┬──────────────────┘                │
          │                                     │                                   │
          │                   ┌─────────────────▼─────────────────┐                 │
          │                   │ LLM Incident Reporter             │                 │
          │                   │ (llm/incident_reporter.py)        │                 │
          │                   │ • Root-cause explanation          │                 |
          │                   │ • Human-readable incident reports │                 │
          │                   └─────────────────┬─────────────────┘                 │
          │                                     │                                   │
          │                      ┌──────────────▼────────────┐                      │
          │                      │ Time-Series Persistence   │                      │
          │                      │ (db/database.py)          │                      │
          │                      │ • In-memory / DB-ready    │                      │
          │                      └──────────────┬────────────┘                      │
          │                                     │                                   │
          │          ┌──────────────────────────▼──────────────────────────┐        │
          │          │                    Alert Service                    │        │
          │          │             (services/alert_service.py)             │        │
          │          │          Warning / Critical classification          │        │
          │          └───────┬───────────────┬─────────────────────┬───────┘        │
          │                  │               │                     │                │
          │                  ▼               ▼                     ▼                │
          │     ┌─────────────────┐  ┌─────────────────┐   ┌──────────────────┐     │
          │     │  Email (SES)    │  │   SMS (SNS)     │   │ Webhooks         │     │
          │     │ notifier/email  │  │ notifier/sms    │   │ notifier/webhook │     │
          │     └─────────┬───────┘  └─────────┬───────┘   └─────────┬────────┘     │
          │               ▼                    ▼                     ▼              │
          │        Ops / SRE Team         On-call Phone         SIEM / Slack        │
          │                                                          │              │
          │       ┌─────────────────────────────────────────────┐    │              │
          │       │ WebSocket Server (realtime/websocket.py)    │◄───┘              │
          │       │ • Push live sensor + alerts                 │                   │
          │       └───────────────────────────┬─────────────────┘                   │
          |                                   ▼                                     |
          └───────────────────────────────────┬─────────────────────────────────────┘
                                              │
                                              ▼
                            ┌────────────────────────────────────────┐
                            │    Live Monitoring Dashboard (React)   │
                            │              dashboard/                │
                            │  • Real-time graphs                    │
                            │  • AI recommendations                  │
                            │  • Alert stream                        │
                            │  • Incident summaries                  │
                            └────────────────────────────────────────┘

---

🧪 **Sensor Simulation (Acts Like Real Hardware)**

For development and demos, a **sensor simulator** continuously pushes live data to the backend — exactly like a Raspberry Pi would.

Run it:
```
python simulator/sensor_simulator.py
```

Simulated sensors:

🔥 Flame
💨 CO (MQ-7)
🌫 Smoke (MQ-2)
🌡 Temperature
💧 Humidity

---

🚨 **Threshold-Based Industrial Alerts**

This system is **safety-first**, not visualization-first.

Threshold logic is built directly into the backend:

* CO concentration limits
* Smoke density limits
* Temperature danger zones
* Flame detection (binary)
* Humidity thresholds

Alerts are:
* Computed server-side
* Logged alongside sensor data
* Displayed live on the dashboard
* Ready to integrate with SMS / email / IoT actuators

---

🌐 **Live Dashboard**

The React dashboard provides:
* Live sensor updates (polling / push-ready)
* Clear, readable status indicators
* Alert visibility
* Expandable charts

Once running:
```
http://localhost:3000
```

This is **not a static UI** — it updates continuously with live data.

---

🐳 **Running the Full System**

**Start everything**
```
docker-compose up --build
```

**Start sensor feed**
```
python simulator/sensor_simulator.py
```

Access
* Backend: ```http://localhost:8000```
* Dashboard: ```http://localhost:3000```

---

🔌 **Hardware Compatibility**

Designed to work with:
* Raspberry Pi
* MQ-2 / MQ-7 gas sensors
* DHT11 temperature & humidity sensor
* Flame sensor modules
* Buzzers / LEDs / actuators (future extension)

Only the ingestion layer changes — **the rest of the system stays the same**.

---

📚 **Documentation**

📊 System Architecture Diagram: `docs/architecture.png`

📄 Detailed Project Report: `docs/project_report.pdf`

---

⚖️ **License**

**Apache License 2.0**

---

⚠️ **Disclaimer**

This project is a **clean-room, independent open-source implementation**.
0
* Not affiliated with any industrial vendor
* Not tied to proprietary SCADA systems
* No restricted or private datasets used

---

🎯 **Who This Is For**

* IoT & Embedded Engineers
* Industrial Automation Engineers
* Cloud & DevOps Engineers
* Students building real, not toy, IoT systems
* Anyone tired of “hello-sensor” demos

---

🛣️ **Roadmap**

* MQTT / AWS IoT Core support
* WebSockets (true push-based live updates)
* Grafana integration
* Actuator control (relays, shutdown triggers)
* Cloud deployment reference (AWS EC2)

---

⭐ **Final Note**

**OpenIoTIndustrySecurity** is meant to be:

* Practical
* Readable
* Deployable
* Honest

If you build on it — **ship it** 🔐🚀
