# import streamlit

import streamlit as st

# intro
st.write("""
# Rainfall vs Wind Speed

The hypothesis here is major rain events usually lead
to higher winds. 
         
Do Rainstorms Bring High Winds? Well we'll find out!
         """)

# display image
st.image("media/rainfall_vs_wind_speed.png", use_container_width=True)

# Interpreting results
st.write("""
## Interpreting the results

Now this one is actually pretty interesting, the graph suggests that while there is a 
slight correlation (the line of best fit gradually increasing), It's not really THAAT
strong, providing evidence that maybe there are more variables at play here.
         """)