# Automotive Agentic AI Prototype 🚗🤖
A "Show and Tell" prototype demonstrating a **Master-Worker Agent Architecture** for the automotive industry. This application visualizes how an AI system detects vehicle faults, coordinates with specialized sub-agents, and automates service bookings.
## 🌟 Features
*   **Telematics Simulator**: Real-time visualization of sensor data (Engine Temperature) with capability to simulate critical faults.
*   **Agent Brain**: Visual log of the "Master Agent" analyzing data and delegating tasks to a "Voice Agent".
*   **Service Dashboard**: Live view of service bay availability and automated booking management.
*   **Mocked Voice Interaction**: Simulates customer outreach via UI alerts.
## 🛠️ Tech Stack
*   **Python**
*   **Streamlit** (Frontend & State Management)
*   **Pandas & NumPy** (Data Simulation)
## 🚀 Getting Started
### Prerequisites
*   Python 3.8+
### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automotive-agentic-prototype.git
    cd automotive-agentic-prototype
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Running the App
Execute the Streamlit application:
```bash
streamlit run app.py
```
## 📸 Usage Scenarios
1.  **Monitor**: Watch the live engine temperature graph.
2.  **Trigger Fault**: Click **"Simulate Critical Fault"** to see the system react.
3.  **Agent Action**: Observe the Master Agent diagnosis and Voice Agent prompt.
4.  **Resolve**: Click **"Accept Booking"** to update the Service Dashboard and view the Root Cause Analysis.
## 📄 License
MIT
