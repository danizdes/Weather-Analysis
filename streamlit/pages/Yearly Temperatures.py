# Importing streamlit
import streamlit as st

# Import Pandas
import pandas as pd

# Main intro
st.write("""
         # Yearly Temperature Analysis

This page aims to understand the yearly temperature trends. 
## Regression Plot
         
The way this plot is calculated is by taking the base dataset and then the mean of the total mean temperatures for each year

"""
)

# Show regression plot
st.image("media/regression_plot_summary.png", caption="Temperature Trajectory (1983-2019)", use_container_width=True)

# Information based on the plot
st.write("""
We can see one clear trend with this data: The line of best fit is increasing, hence meaning year-on-year around temperatures are **increasing**. Proving statistical
evidence of long-term climate warming in Singapore.
         """)


# Area Chart Introduction
st.write("""
## Diving a little deeper
         
Let's include the maximum and minimun data values and create an Area Chart
         """)

# Show graph
st.image("media/yearly_temp_range_chart.png", caption="Yearly Temperature Envelope (1983-2019)", use_container_width=True)

# Continuing
st.write("""
While the line of best fit leads us to the same conclusion of warming. One more thing to realize with this data
is the "base" minimum values(the ones in blue) have been steadily increasing. In addition the maximum temperature is increasing as well.

Looking at the gray shaded area, looking at it's thickness, you can see that the weather isn't really
erratic, but the entire graph is moving cohesively. This means that nothing crazy or bazzare is happening
but instead the "normal" weather of today is just hotter.
         """)