# Import streamlit
import streamlit as st

# Import plotly for them cool plots
import plotly.express as px

# Import pandas 
import pandas as pd

# Main intro
st.write("""
# Temperature vs Rainfall
         
Comparing Temperature and Rainfall!
         
## Introductions
It is commonly believed that on rainy days, the temperature naturally is lower. While this looks like common sense,
I wanted to test this hypothesis. So I took the Daily Rainfall and the Maximum Temperature and see if there
any correlation. I made a box plot using matplot lib and seaborn.
        
## Graph
         """)

# Import the csv file
df = pd.read_csv("dataset/weather_clean.csv")

# Classify rainy vs dry
df["Rainy Day"] = df["Daily Rainfall Total (mm)"].apply(lambda x: "Rainy" if x > 5 else "Dry")

# Plot graph
fig = px.box(
    df,
    x="Rainy Day",
    y="Maximum Temperature (°C)",
    title="Rainfall vs Maximum Temperature",
    color="Rainy Day",
    color_discrete_map={"Rainy": "#267eb9", "Dry": "#d07321"},
    template="plotly_white",
    points="outliers",
)

fig.update_layout(height=500, showlegend=True)
st.plotly_chart(fig, use_container_width=True)

# Interpreting the results
st.write("""
## Interpreting the results

Well the theory was **CORRECT!**. As you can see rainy days have a lower median temperature than dry days. 

There is something else though which is pretty interesting, the trail of open circles (i.e the outliers) are 
quite cold compared to the rest of the dataset. And *both* categories have these cold anamolies. What this shows is 
while rain is pretty affective at lowering temperatures, other things play a role as well.
         """)
