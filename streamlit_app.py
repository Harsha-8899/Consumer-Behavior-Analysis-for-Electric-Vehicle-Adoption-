import streamlit as st
st.subheader('I am Harsha!')
st.text('My First Streamlit Project')

import numpy as np
import pickle
import streamlit as st  # Added import statement for Streamlit
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Title and description
st.title("Electric Vehicle Data Analysis")
st.write("An interactive web app to analyze and visualize electric vehicle data.")

# Load the data
data = pd.read_csv('https://github.com/Harsha-8899/Consumer-Behavior-Analysis-for-Electric-Vehicle-Adoption-/blob/main/Electric_Vehicle_Population_Data.xlsx')

# Display the data
st.write(data.head())
