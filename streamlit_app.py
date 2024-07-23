import streamlit as st
st.subheader('I am Harsha!')
st.text('My First Streamlit Project')

import numpy as np
import pickle
import streamlit as st  # Added import statement for Streamlit
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def load_original_data():
    data = 'https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx'
    response = requests.get(data)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None

st.write(data.head())
