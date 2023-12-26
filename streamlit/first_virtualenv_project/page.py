import streamlit as st
from PIL import Image

img = Image.open("data/image_03.jpg")

# st.set_page_config(page_title="hello",
#                    page_icon=img,
#                    layout="wide",
#                    initial_sidebar_state="expanded")

PAGE_CONFIG = {"page_title":"hello", "page_icon":img, "layout":"wide",
               "initial_sidebar_state":"expanded"}

st.set_page_config(**PAGE_CONFIG)


def main():
    st.title("hello streamlit lovers")
    st.sidebar.success("Menu")

if __name__=="__main__":
    main()