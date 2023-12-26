import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import docx2txt
import pdfplumber
from PIL import Image
import time

def main():

    st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    st.sidebar.selectbox("Menu", ["Home", "About", "Applications"])

    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df, width=800, height=150)

    fig = px.bar(df, x='lang', y="Sum")
    st.plotly_chart(fig)

    st.write("text")
    st.write("## text")

    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("first name")
        age = st.number_input("age", 1, 100)
        message = st.text_area("Message")
    
    with col2:
        lname = st.text_input("first name", key="1")
        contact = st.text_input("contact", key='2')
    
    st.write(f"{fname}, {age}, {message}, {lname}")

    with st.expander("lee"):
        st.text("hello lee")


    uploaded_file = st.file_uploader("upload files", type=["txt", 'pdf', 'docx', 'csv'])
    file_type = st.selectbox("select file type", ['txt', 'pdf', 'docx', 'csv'])
    if st.button("submit"):
        if file_type=='txt':
            processed_file = uploaded_file.read().decode('utf-8')
        elif file_type=='docx':
            processed_file = docx2txt.process(uploaded_file)
        elif file_type=='pdf':
            with pdfplumber.open(uploaded_file) as pdf_file:
                pages = pdf_file.pages[0]
                processed_file = pages.extract_text()
        elif file_type == 'csv':
            processed_file = pd.read_csv(uploaded_file)
        st.write(processed_file)

    img = Image.open("data/image_03.jpg")
    st.image(img, use_column_width=True)


    uploaded_files = st.file_uploader("upload files", type=['png', 'jpg'],
                                      accept_multiple_files=True)
    
    for file in uploaded_files:
        img = Image.open(file)
        st.image(img)


    # bar = st.progress(0)
    # for pc in range(50):
    #     time.sleep(0.1)
    #     bar.progress(pc + 1)
    
    # with st.spinner("processing"):
    #     time.sleep(5)
    # st.success("finished")

    my_lang = ['a', 'b', 'c']
    choice = st.selectbox("language", my_lang)
    st.write(f"you selected {choice}")

    

if __name__=="__main__":
    main()