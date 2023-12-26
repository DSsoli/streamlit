import streamlit as st
import pandas as pd

df = pd.read_csv("asdf.csv")
csv = df.to_csv().encode()

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv', 
)