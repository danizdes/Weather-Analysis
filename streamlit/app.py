# Importing streamlit
import streamlit as st

# Import JSON
import json

# Introductory Markdown
st.write("""
# Singapores Weather Analysis!
### (How does Singapores Weather change? Well thats what we'll find out!)
         
Hi everyone! My names [Daniyal](https://www.instagram.com/mohdaniyaldes/). I made this project to 
showcase how Singapores weather changes. I choose Singapore as its irony with [Horiaons Arcana](https://horizons.hackclub.com/) 
is just too funny not to miss.
         """)

# Weather Meme
st.image("media/weather_meme.png")

# Caption for the meme
st.caption("Who doesn't love the weather lol")

# read `2019_extremes.json` file
with open("dataset/2019_extremes.json", "r") as file:
    extremes_2019 = json.load(file)

# Hottest temperature & date
hottest_temp = extremes_2019["Hottest Day"]["Temperature"]
hottest_date = extremes_2019["Hottest Day"]["Day"]

# Windiest speed & dat
windiest_speed = extremes_2019["Windiest Day"]["Speed"]
windiest_date = extremes_2019["Windiest Day"]["Day"]

# "Data at a glance" section
st.write("""
## Data at a glance
""")

# Created 2 columns
col1, col2 = st.columns(2)
    
# Col 1 = Hottest Day & Temperature
with col1:
        st.metric(label="Hottest Registered Day", value=f"{hottest_temp}°C", delta=f"Recorded on {hottest_date}", delta_color="off")
# Col 2 = Windiest Day & Speed
with col2:
        # Displays wind speed as the main number, and the date cleanly beneath it
        st.metric(label="Windiest Registered Day", value=f"{windiest_speed} km/h", delta=f"Recorded on a {windiest_date}", delta_color="off")

st.write("Presented above is the Hottest Temperature and Speeds along with their respective dates. This maximum is for the year **2019** ")