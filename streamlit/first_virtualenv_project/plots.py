import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

def main():
    st.title("plotting with plotly")
    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df, values="Sum", names="lang", title="pie chart of langs")
    st.plotly_chart(fig)

    fig2 = px.bar(df, x="lang", y="Sum")
    st.plotly_chart(fig2)


    fig3, ax = plt.subplots()
    ax.hist(df.Sum)
    st.pyplot(fig3)

if __name__ == "__main__":
    main()