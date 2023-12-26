import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader
import pdfplumber

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    st.title("file upload")

    menu = ["Home", "Dataset", "Documents", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":
        st.subheader("Home")
        image_file = st.file_uploader("upload images", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            #st.write(type(image_file))
            file_details = {"filename": image_file.name, 
                            "filetype": image_file.type, "filesize": image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width=250)
        
    elif choice=="Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df)
    
    elif choice == "Documents":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", 'txt'])
        if st.button("Process"):
            if docx_file is not None:
                if docx_file.type == "text/plain":
                    raw_text = str(docx_file.read(), "utf-8")
                    st.text(raw_text)
                
                elif docx_file.type == "application/pdf":
                    pass

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
    
    else:
        st.subheader("About")




if __name__=="__main__":
    main()