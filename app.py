# Importing streamlit
import streamlit as st
import pandas as pd

# Add CSV file
df = pd.read_csv("weather_clean.csv")

# Filter out the dataset to only get the data for the year 2019
df19 = df[df["Year"] == 2019]

# Getting the row with the hottest day
hottest_day_row_19 = df.loc[df["Maximum Temperature (°C)"].idxmax()]

# Getting hottest date & temperature
hottest_date_19 = hottest_day_row_19["Date"]
hottest_temp = hottest_day_row_19["Maximum Temperature (°C)"]

# Getting the windiest day
windiest_day_row_19 = df.loc[df["Max Wind Speed (km/h)"].idxmax()]

# Getting windiest date & temperature
windiest_date_19 = windiest_day_row_19["Date"]
windiest_temp_19 = windiest_day_row_19["Max Wind Speed (km/h)"]

# Naming the naviation "navigation" (duh)
st.sidebar.title("Navigation")

# Sidebar with a Home button
if st.sidebar.button("Home"):
    # Introduction section!s
    st.title("weatherAnalysis")
    st.subheader("Heyo! my names Daniyal. TBD")