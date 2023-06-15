from pages.Data import *
import pandas as pd
import streamlit as st

uploaded_file = get_data()



def corridors():
    df = pd.read_csv(uploaded_file)
    return df

if uploaded_file is not None:
    corridors = corridors()
    st.write(corridors)
