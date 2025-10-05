import streamlit as st
import folium
from streamlit_folium import st_folium
from scipy.spatial import distance
import plotly.express as px

# Page configuration
st.set_page_config(page_title="MediDrone Dashboard", layout="wide")

# Title
st.title("🩺 MediDrone Control Center")

# Sidebar for navigation
menu = st.sidebar.radio("Select a Module", ["Drone Path", "Bird Detection", "Teleconsultation", "Vitals Monitoring", "Medicine Dispenser"])

# 1️⃣ Drone Path
if menu == "Drone Path":
    st.subheader("🚁 Real-Time Drone Path Tracking")

    m = folium.Map(location=[12.9716, 77.5946], zoom_start=13)
    folium.Marker([12.9716, 77.5946], popup="Start Point").add_to(m)
    folium.Marker([12.9816, 77.6046], popup="Destination").add_to(m)
    folium.PolyLine([[12.9716, 77.5946], [12.9816, 77.6046]], color="blue", weight=3).add_to(m)

    st_folium(m, width=700, height=450)

# 2️⃣ Bird Detection
elif menu == "Bird Detection":
    st.subheader("🕊️ Bird Detection Module")
    st.info("This module simulates real-time bird detection to prevent drone collision.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Red-tailed_Hawk_Buteo_jamaicensis_Full_Body_1880px.jpg", caption="Detected Bird: Red-tailed Hawk")

# 3️⃣ Teleconsultation
elif menu == "Teleconsultation":
    st.subheader("📞 Teleconsultation Interface")
    st.markdown("Video call module placeholder. (This can be connected to Twilio or WebRTC APIs for live consultation.)")
    st.button("Start Video Call")

# 4️⃣ Vitals Monitoring
elif menu == "Vitals Monitoring":
    st.subheader("💓 Patient Vitals Monitoring")

    vitals = {
        "Heart Rate (bpm)": 78,
        "Blood Pressure (mmHg)": "120/80",
        "Oxygen Saturation (%)": 98,
        "Temperature (°C)": 36.7
    }

    st.table(vitals)

    fig = px.line(x=["Heart Rate", "Oxygen", "Temperature"], y=[78, 98, 36.7], markers=True, title="Vitals Overview")
    st.plotly_chart(fig, use_container_width=True)

# 5️⃣ Medicine Dispenser
elif menu == "Medicine Dispenser":
    st.subheader("💊 Automated Medicine Dispenser")
    st.markdown("MediDrone dispenser simulation for emergency supply.")
    st.success("Medicine Dispenser Ready ✅")
    if st.button("Dispense Medicine"):
        st.balloons()
        st.success("Medicine dispensed successfully!")
