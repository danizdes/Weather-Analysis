# Import Streamlit
import streamlit as st

# Need to import joblib for the model
import joblib

# need pandas to format input
import pandas as pd

# Import model
model = joblib.load("models/tmr_temp.joblib")

# Introduction
st.write("""
# Predicting Tommorows Temperature
         
Give todays weather conditions and get a prediction!
         """)

# Widgets for selecting weather
max_temp = st.sidebar.slider("Max Temperature", min_value=15.0, max_value=40.0, step=0.1)
min_temp = st.sidebar.slider("Minimum Temperature", min_value=10.0, max_value=30.0, step=0.1)
mean_wind = st.sidebar.slider("Today's Mean Wind Speed", min_value=0.0, max_value=50.0, step=0.1)
yestureday_rain = st.sidebar.number_input("Yesterday's Rainfall", min_value=0.0, max_value=300.0, step=0.1)
yestureday_wind = st.sidebar.slider("Yesterday's Mean Wind Speed", min_value=0.0, max_value=50.0, step=0.1)

# Calculate mean temp from these values
mean_temp = (max_temp + min_temp) / 2

# We need to format the data so we can feed it to the model

features = pd.DataFrame([{
    "Yestureday_Rainfall": yestureday_rain, 
    "Yestureday_Wind": yestureday_wind,
    "Mean Temperature (°C)": mean_temp, 
    "Maximum Temperature (°C)": max_temp, 
    "Minimum Temperature (°C)": min_temp, 
    "Mean Wind Speed (km/h)": mean_temp, 
}])

#Make the prediction
prediction = model.predict(features)[0]

# Show the predition
st.metric(
    label="Predicted Temperature",
    value=f"{prediction:.2f}°C"
)