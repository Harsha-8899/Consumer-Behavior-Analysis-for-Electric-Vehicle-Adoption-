import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Electric Vehicle Data Analysis")
st.write("An interactive web app to analyze and visualize electric vehicle data.")

url = 'https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx'
df = pd.read_xlsx(url,index_col=0,parse_dates=[0])

st.write(df.head())
