import streamlit as st
from PIL import Image

img = Image.open('/home/soli/Desktop/streamlit/first_virtualenv_project/data/image_03.jpg')
st.set_page_config(
    page_title="hello",
    page_icon=img,
    layout='centered',
    initial_sidebar_state='auto'
)

#st.set_page_config(layout="centered")
img = Image.open("/home/soli/Desktop/streamlit/first_virtualenv_project/data/image_03.jpg")
st.image(img, use_column_width=True)
st.image("https://rare-gallery.com/thumbs/324508-Nezuko-Cute-Kimetsu-no-Yaiba-4K-iphone-wallpaper.jpg",
         use_column_width=True)

video_file = open('../first_virtualenv_project/data/secret_of_success.mp4', 'rb').read()
st.video(video_file, start_time=3)

audio_file = open("../first_virtualenv_project/data/song.mp3", 'rb')
st.audio(audio_file.read(), format="mp3")

fname = st.text_input("enter firstname")
password = st.text_input("enter password", type='password')
st.title(fname)

message = st.text_area("enter message", height=100)
st.write(message)

number = st.number_input('enter number', 1, 25)

myappointment = st.date_input("appointment")

mytime = st.time_input("my time")

color = st.color_picker("select color")

def main():
    st.title("hello streamlit lovers")
    st.sidebar.success("Menu")

if __name__=='__main__':
    main()