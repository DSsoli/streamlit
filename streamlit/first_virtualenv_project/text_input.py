import streamlit as st

fname = st.text_input("enter firstname", max_chars=10)

password = st.text_input("enter password", type='password')
st.title(fname)

message = st.text_area("enter message", height=200)
st.write(message)

number = st.number_input("enter number", min_value=1, max_value=25, step=5)

myappointment = st.date_input("appointment")

mytime = st.time_input("my time")

color = st.color_picker("select color")