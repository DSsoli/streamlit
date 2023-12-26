import streamlit as st

import pandas as pd

df = pd.read_csv("data/iris.csv")

#method 1
#st.dataframe(df, 200, 100)

#adding a color style
st.dataframe(df.style.highlight_max(axis=0), 900, 800)

#static table
#st.table(df)

#method3: suing superfunction st.write
st.write(df.head())

st.json({"data":"name"})

mycode = """
def sayhello():
    print("hello")
"""
st.code(mycode, language="python")

