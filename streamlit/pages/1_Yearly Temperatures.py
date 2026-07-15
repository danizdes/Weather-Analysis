# Importing streamlit
import streamlit as st

# Import Pandas
import pandas as pd

# Import plotly for them interactive plots
import plotly.express as px

# Main intro
st.write("""
         # Yearly Temperature Analysis

This page aims to understand the yearly temperature trends. 
## Regression Plot
         
The way this plot is calculated is by taking the base dataset and then the mean of the total mean temperatures for each year

""")

# Read dataset
df = pd.read_csv("dataset/temperature_yearly_summary.csv")

# Setting up the figure
fig = px.scatter(
    df,
    x="Year",
    y="Mean Mean Temperature (°C)",
    trendline="ols",
    title="Temperature Trajectory(1983-2019)",
    labels={
        "Mean Mean Temperature (°C)": "Mean Temperature (°C)"
    },
    template="plotly_white",
    trendline_color_override="#ca5504"
)

# Show the plot
fig.update_traces(marker=dict(color="#ca5507", size=8))
fig.update_layout(height=500)
st.plotly_chart(fig, use_container_width=True)

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

# Second figure details
fig2 = px.area(
    df,
    x="Year",
    y=[
        "Mean Maximum Temperature (°C)",
        "Mean Mean Temperature (°C)",
        "Mean Minimum Temperature (°C)",
    ],
    title="Yearly Temperature Area chart",
    labels={"value": "Temperature (°C)", "variable": "Metric"},
    template="plotly_white",
    color_discrete_map={
        "Mean Mean Temperature (°C)": "#293c50",
        "Mean Maximum Temperatures (°C)": "#b43729",
        "Mean Mean Temperature (°C)": "#4278ae", 
    }
)

# Show plot
fig2.update_layout(height=500)
st.plotly_chart(fig2, use_container_width=True)

# Continuing
st.write("""
While the line of best fit leads us to the same conclusion of warming. One more thing to realize with this data
is the "base" minimum values(the ones in blue) have been steadily increasing. In addition the maximum temperature is increasing as well.

Looking at the gray shaded area, looking at it's thickness, you can see that the weather isn't really
erratic, but the entire graph is moving cohesively. This means that nothing crazy or bazzare is happening
but instead the "normal" weather of today is just hotter.
         """)
