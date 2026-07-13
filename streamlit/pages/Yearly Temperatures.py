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

