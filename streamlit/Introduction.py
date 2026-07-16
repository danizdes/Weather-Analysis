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
st.image("media/weather_meme.jpg")

# Caption for the meme
st.caption("Who doesn't love the weather lol")

# read `2019_extremes.json` file
with open("dataset/extremes.json", "r") as file:
    extremes = json.load(file)

# Hottest temperature & date
hottest_temp = extremes["Hottest Day"]["Temperature"]
hottest_date = extremes["Hottest Day"]["Day"]

# Windiest speed & dat
windiest_speed = extremes["Windiest Day"]["Speed"]
windiest_date = extremes["Windiest Day"]["Day"]

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
        st.metric(label="Windiest Registered Day", value=f"{windiest_speed} km/h", delta=f"Recorded on a {windiest_date}", delta_color="off")