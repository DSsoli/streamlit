import streamlit as st

name = "lee"

if st.button("submit"):
    st.write(f"name: {name.upper()}")

if st.button("submit", key="new02"):
    st.write(f"name: {name.lower()}")


status = st.radio("what is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
elif status == "Inactive":
    st.warning("Inactive")

if st.checkbox("Show/Hide"):
    st.text("Showing something")

with st.expander("asdf"):
    st.text("hello asdf")


my_lang = ["python", "go", "rust"]

choice = st.selectbox("language", my_lang)
st.write(f"you selected {choice}")

spoken_lang = ("eng", "kor", "jpn")
my_spoken_lang = st.multiselect("spoken lang", spoken_lang, default="eng")

age = st.slider("age", 1, 100)

color = st.select_slider("choose color", options=["yellow", 'black', 'green', 'blue'],
                         value=("yellow", "blue"))
