import streamlit as st
from PIL import Image


img = Image.open("data/image_03.jpg")
st.image(img, use_column_width=True)

st.image("https://rare-gallery.com/thumbs/324508-Nezuko-Cute-Kimetsu-no-Yaiba-4K-iphone-wallpaper.jpg",
         use_column_width=True)


video_file = open("data/secret_of_success.mp4", "rb").read()
st.video(video_file, start_time=3)

audio_file = open("data/song.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")