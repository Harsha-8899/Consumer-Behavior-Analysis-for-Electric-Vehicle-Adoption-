import streamlit as st
st.subheader('I am Harsha!')
st.text('My First Streamlit Project')


# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:42:13 2024

@author: supre
"""


import numpy as np
import pickle
import streamlit as st  # Added import statement for Streamlit
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def load_original_data():
    url = 'https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None


st.write("### Dataset")
st.write(data.head())
