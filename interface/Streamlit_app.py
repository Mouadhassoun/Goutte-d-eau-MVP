import streamlit as st
import requests

st.title("🌧️ Prédiction du risque de pluie {Rennes}")

temperature = st.number_input("Température (°C)")
humidite = st.number_input("Humidité (%)")
pression = st.number_input("Pression (hPa)")
vent = st.number_input("Vitesse du vent (m/s)")

if st.button("Prédire"):
    data = {
        "temperature": temperature,
        "humidite": humidite,
        "pression": pression,
        "vent": vent
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    st.write("Probabilité de pluie :", response.json()["probabilite_pluie"])