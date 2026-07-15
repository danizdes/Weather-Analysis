# import streamlit
import streamlit as st

# intro
st.write("""
# Rainfall vs Wind Speed
Do Rainstorms Bring High Winds? Well we'll find out!
         """)

# Introduction
st.write("""
## Introduction
         
I wanted to test a hypothesis: Does more rainfall lead to higher winds? To test this out I decided to create
a graph using matplotlib and seaborn. The points were plotted and then I created a line of best fit to showcase
the trend of the data
         """)

# display image
st.image("media/rainfall_vs_wind_speed.png", use_container_width=True)

# Interpreting results
st.write("""
## Interpreting the results

As you can see from the graph, there is a slight correlation. But emphasis on the *slight*. There is a positive trend shown
meaning wind speeds generally are higher when there is more total rainfall. However, the trend isn't the **strongest**. 
This points towards there being other likely factors that might affect this relationship.
         """)