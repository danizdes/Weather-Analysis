# Import streamlit
import streamlit as st

# Import pandas as pd
import pandas as pd

# Import main dataframe
df = pd.read_csv("dataset/weather_clean.csv")

# Import json to read predictions
import json

# Main introductions
st.write("""
# Making Predictions

Moving from basic analysis, I want to move onto **predictions**.
So why not create a model that predicts the **temperature**?
                  
Thats what I decided to do!
         """)

# Going a little deeper into the methods 
st.write("""
## Methods

### Setting the data up chronologically
First, I set up the data chronologically. The data from the CSV file is currently 
in descending order:
         """)

# Show the first couple values from the dataframe
st.dataframe(df)

# Converting date so we can sort it
df["Date"] = pd.to_datetime(df["Date"])

# Get the dataframe in asending order
df_sorted = df.sort_values("Date").reset_index(drop=True)

# Introduce descending dataframe
st.write("""
The issue with this is that this makes the model look "backwards" for the prediction.
So we sort the data to be ascending:
         """)

# Show dataframe
st.dataframe(df_sorted)

# Introduce Features
st.write("""
## "Lag" features
So we need the AI to know what is "Yeturedays" and what is "Todays" temperature,
the model doesn't really understand time. So we purposefully shift our data to create
this affect:
         
```python
    # Shift mean temperature back by 1 day
    df["tmr_temp"] = df["Mean Temperature (°C)"].shift(-1)

    # Create some lag features ("yestureday")
    df["Yestureday_Rainfall"] = df["Daily Rainfall Total (mm)"].shift(1)
    df["Yestureday_Wind"] = df["Mean Wind Speed (km/h)"]
         
```


## Features

Now I need to feed the model *input data*, this is the data the model uses to make the predictions:
         
* Yestureday_Rainfall
* Yestureday_Wind
* Mean Temperature (°C) 
* Maximum Temperature (°C) 
* Minimum Temperature (°C) 
* Mean Wind Speed (km/h)
         
The model uses this data to make predictions of the temperature.
         
## Evaluation
         
After training the model, we use 2 evaluation metrics to see how good are model is:
         
### R2
         
This is basically how much more accurate the model is than just guessing the value
         
### Mean Absolute Error (MAE)
This calculated the average rate of deviation from the actual answer. So how close
was it to the actual answer?
         
The Evaluations are displayed below:
         

         """)

# Read predictions
with open("dataset/predictions.json", "r") as file:
    predictions = json.load(file)

# Display Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Mean Absolute Error(MAE)",
        value=f"{predictions['MAE']:.2f}",
    )
with col2:
    st.metric(
        label="Model Accuracy(R2 Score)",
        value=f"{predictions['R2'] * 100:.1f}%",
    )

# Introducing graph
st.write("""
## Graph

Heres also a graph that can show how the model compares with the true answers:
""")

st.image("media/prediction.png")