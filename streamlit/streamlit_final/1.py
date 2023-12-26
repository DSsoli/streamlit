import streamlit as st
import pandas as pd

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

def main():
    st.title("hello streamlit lovers")
    st.text("text")
    name = "asdf"
    st.text(f"{name}")
    st.header("header")
    st.title("title")
    st.markdown("markdown")
    st.markdown("## markdown")
    st.subheader("subheader")

    st.success("success")
    st.warning("warning")
    st.info("info")
    st.error("error")
    st.exception("exception")

    st.write("normal text")
    st.write("## markdown")
    st.write(1+2)
    st.help(range)

    df = pd.read_csv("/home/soli/Desktop/streamlit/first_virtualenv_project/data/iris.csv")
    st.dataframe(df.style.highlight_max(axis=0))
    #st.table(df)
    st.write(df.head())

    st.json({"data": "name"})

    name = "Jesse"

    if st.button("submit"):
        st.write(f"name: {name.lower()}")
    
    if st.button("submit", key="2"):
        st.write(f"name: {name.upper()}")

    status = st.radio("whats your status", ("active", "inactive"))
    if status == "active":
        st.success("you're active")
    elif status == "inactive":
        st.warning("inactive")
    
    if st.checkbox("show/hide"):
        st.text("showing sth")

    if st.expander("python"):
        st.text("hello python")

    my_lang = ["A", "B", "C"]
    choice = st.selectbox("language", my_lang)
    st.write(choice)

    spoken_lang = ("eng", "french", "span")
    my_spoken_lang = st.multiselect("spoken lang", spoken_lang, default="eng")

    age = st.slider("age", 1, 100)

    color = st.select_slider("choose color", options=["a", "b", "c", "d"], value=("a", "d"))

if __name__=="__main__":
    main()