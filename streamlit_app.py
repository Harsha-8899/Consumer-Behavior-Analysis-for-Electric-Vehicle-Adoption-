import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Electric Vehicle Data Analysis")
st.write("An interactive web app to analyze and visualize electric vehicle data.")

def load_original_data():
    data = 'https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx'
    response = requests.get(data)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None

st.write(data.head())
