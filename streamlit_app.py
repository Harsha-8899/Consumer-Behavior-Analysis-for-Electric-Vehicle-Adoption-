import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Electric Vehicle Data Analysis")
st.write("An interactive web app to analyze and visualize electric vehicle data.")

# Load the data
data = pd.read_csv('H:/Harsha/Study/Data Mining/Project/Electric_Vehicle_Population_Data.csv')

# Display the data
st.write("### Dataset")
st.write(data.head())
