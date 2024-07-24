import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Electric Vehicle Data Analysis")
st.write("An interactive web app to analyze and visualize electric vehicle data.")

import streamlit as st
import pandas as pd

# Load the dataset from GitHub
data_url = "https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx"
data = pd.read_csv(data_url)

# Streamlit app title
st.title("Electric Vehicle Data Analysis")
