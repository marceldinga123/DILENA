
import streamlit as st
import joblib
import pandas as pd
import numpy as np
from utils import preprocess_user_input

# Load trained model
model = joblib.load("flight_price_model_global_rf.joblib")

st.title("🌍 Global Flight Price Predictor")

# Input fields
airline = st.selectbox("Airline", ['Delta Air Lines', 'Emirates', 'Qatar Airways', 'United Airlines', 'Lufthansa', 'British Airways', 'Air France', 'Singapore Airlines', 'Turkish Airlines', 'ANA'])
source_country = st.selectbox("Source Country", ['USA', 'UK', 'UAE', 'France', 'Germany', 'India', 'Japan', 'Singapore', 'Qatar', 'Turkey', 'Nigeria', 'South Africa', 'Kenya', 'Egypt', 'Ethiopia', 'Ghana', 'Morocco'])
source_city = st.text_input("Source City")
destination_country = st.selectbox("Destination Country", ['USA', 'UK', 'UAE', 'France', 'Germany', 'India', 'Japan', 'Singapore', 'Qatar', 'Turkey', 'Nigeria', 'South Africa', 'Kenya', 'Egypt', 'Ethiopia', 'Ghana', 'Morocco'])
destination_city = st.text_input("Destination City")

date = st.date_input("Travel Date")
time = st.time_input("Departure Time")
stops = st.slider("Number of Stops", 0, 2, 0)
duration = st.number_input("Duration (minutes)", min_value=30, max_value=1440, value=120)

# Prediction
if st.button("Predict Flight Price"):
    try:
        X_input = preprocess_user_input(airline, source_country, source_city, destination_country, destination_city, date, time, stops, duration)
        prediction = model.predict(X_input)
        st.success(f"Estimated Ticket Price: ${round(prediction[0], 2)}")
    except Exception as e:
        st.error(f"Error: {e}")
