import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Config
st.set_page_config(page_title="Automotive Agentic AI", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .big-font {
        font-size:20px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Automotive Agentic AI System")
st.markdown("### Master-Worker Architecture Prototype")
st.divider()

# Session State Initialization
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(np.random.normal(80, 2, size=(20,)), columns=["Engine Temperature"])
if 'fault_triggered' not in st.session_state:
    st.session_state.fault_triggered = False
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []
if 'bay_status' not in st.session_state:
    st.session_state.bay_status = [True, True, True, False] # True = Free, False = Booked
if 'service_booked' not in st.session_state:
    st.session_state.service_booked = False

# --- LAYOUT ---
col1, col2, col3 = st.columns(3)

# --- SECTION 1: TELEMATICS SIMULATOR ---
with col1:
    st.subheader("1. Telematics Simulator")
    st.caption("Monitoring real-time vehicle sensor data")
    
    # Placeholder for the chart
    chart_placeholder = st.empty()
    
    # Display the current chart state
    st.line_chart(st.session_state.data, color="#29b5e8", height=250)
    
    st.markdown("---")
    
    # Simulate Critical Fault Button
    if st.button("🚨 Simulate Critical Fault", key="sim_fault", type="primary"):
        st.session_state.fault_triggered = True
        # Add spike
        new_data = pd.DataFrame([110.0, 125.0, 138.0, 142.0], columns=["Engine Temperature"]) # Spike data
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        # Add log
        if not any("CRITICAL" in msg for msg in st.session_state.chat_log):
             st.session_state.chat_log.append("⚠️ CRITICAL EVENT: Engine Temperature > 120°C")
        st.rerun()

    # Normal "background" simulation button (or just manual refresh)
    if st.button("🔄 Generate Normal Telematics"):
        new_val = np.random.normal(80, 2)
        new_row = pd.DataFrame([new_val], columns=["Engine Temperature"])
        st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
        # Keep window size reasonable
        if len(st.session_state.data) > 30:
            st.session_state.data = st.session_state.data.iloc[1:]
        st.rerun()

# --- SECTION 2: AGENT BRAIN ---
with col2:
    st.subheader("2. Agent Brain (Logic)")
    st.caption("Master Agent orchestrating worker agents")
    
    chat_container = st.container(height=300, border=True)
    
    if st.session_state.fault_triggered:
        # Simulate thinking logic
        if len(st.session_state.chat_log) < 4:
             st.session_state.chat_log.append("🔍 Analyzing sensor data stream...")
             st.session_state.chat_log.append("🤖 Master Agent: Anomaly Detected. Probability of failure: 98%.")
             st.session_state.chat_log.append("📞 Delegating to Voice Agent for customer outreach.")
        
        # Display Logs
        for msg in st.session_state.chat_log:
            chat_container.text(msg)
            
        # Voice Agent Simulation
        st.error("🗣️ VOICE AGENT SPEAKING: \n\n'Hello, we detected a potential issue with your engine cooling system. I can book you a service appointment immediately. Shall I proceed?'")
        
    else:
        chat_container.info("System Normal. Monitoring protocols active...")

# --- SECTION 3: SERVICE DASHBOARD ---
with col3:
    st.subheader("3. Service Dashboard")
    st.caption("Service Center Management System")
    
    # Grid of Service Bays
    st.write("**Service Bay Live Status:**")
    
    # simple 2x2 grid attempt with columns
    b1, b2 = st.columns(2)
    b3, b4 = st.columns(2)
    bays = [b1, b2, b3, b4]
    
    for i, bay in enumerate(bays):
        is_free = st.session_state.bay_status[i]
        color = "#28a745" if is_free else "#dc3545" # Green vs Red
        status_text = "FREE" if is_free else "BOOKED"
        bay.markdown(f"""
        <div style="background-color: {color}; padding: 15px; border-radius: 5px; text-align: center; color: white; margin-bottom: 10px;">
            <small>Bay {i+1}</small><br><strong>{status_text}</strong>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.fault_triggered and not st.session_state.service_booked:
        if st.button("✅ Accept Booking (User Action)", type="secondary"):
            st.session_state.service_booked = True
            # Find first free bay and book it
            booked_bay = -1
            for i in range(len(st.session_state.bay_status)):
                if st.session_state.bay_status[i]:
                    st.session_state.bay_status[i] = False
                    booked_bay = i + 1
                    break
            
            st.session_state.chat_log.append(f"✅ Customer accepted. Service Bay {booked_bay} booked.")
            st.rerun()

    if st.session_state.service_booked:
        st.success("Appointment Confirmed.")
        st.text_area("📋 Quality Agent - Root Cause Analysis", 
                     "Generating Report...\n\n- Error Code: P0117\n- Component: Coolant Temperature Sensor\n- Severity: High\n- Action: Inspect connector and harness. Replace sensor if necessary.",
                     height=150)
