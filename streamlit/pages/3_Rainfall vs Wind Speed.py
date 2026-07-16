# import streamlit
import streamlit as st

# import plotly for graphs
import plotly.express as px

# impot pandas for data science stuff
import pandas as pd

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

# Get dataset
df=pd.read_csv("dataset/weather_clean.csv")

fig = px.scatter(
    df,
    x="Daily Rainfall Total (mm)",
    y="Max Wind Speed (km/h)",
    trendline="ols",
    title="Daily Rainfall vs Maximum Wind Speed",
    labels={
        "Daily Rainfall Total (mm)": "Daily Rainfall Total (mm)",
        "Max Wind Speed (km/h)": "Max Wind Speed (km/h)",
    },
    template="plotly_white",
    opacity=0.6,
    color_discrete_sequence=["#226d9f"],
    trendline_color_override="#d63d2d",
)
fig.update_traces(marker=dict(size=5, line=dict(color="white", width=0.5)))
fig.update_layout(height=500)
st.plotly_chart(fig, use_container_width=True)


# Interpreting results
st.write("""
## Interpreting the results

As you can see from the graph, there is a slight correlation. But emphasis on the *slight*. There is a positive trend shown
meaning wind speeds generally are higher when there is more total rainfall. However, the trend isn't the **strongest**. 
This points towards there being other likely factors that might affect this relationship.
         """)
