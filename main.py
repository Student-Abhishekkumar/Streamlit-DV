import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   


st.set_page_config(
    page_title="Data Visualisation with streamlit",
    page_icon="💀"
)
st.title('Data Visualisation with streamlit')

# with st.sidebar():
#     st.title('Sidebar')
#     st.write('This is a sidebar')
#     st.write('You can add widgets here')

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.read_csv(uploaded_file)