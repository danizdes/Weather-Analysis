# Import streamlit
import streamlit as st

# Main intro
st.write("""
# Temperature vs Rainfall
         
It is commonly believed that on rainy days, the temperature naturally is lower. While this looks like common sense,
I wanted to test this hypothesis. So I took the Daily Rainfall and the Maximum Temperature and see if there
any correlation
         """)

# Show graph
st.image("media/rainfall_vs_temp.png", caption="Correlation between rainfall and temperature", use_container_width=True)

# Interpreting the results
st.write("""
## Interpreting the results

Well the theory was **CORRECT!**. As you can see rainy days have a lower median temperature than dry days. 

There is something else though which is pretty interesting, the trail of open circles (i.e the outliers) are 
quite cold compared to the rest of the dataset. And *both* categories have these cold anamolies. What this shows is 
while rain is pretty affective at lowering temperatures, other things play a role as well.
         """)