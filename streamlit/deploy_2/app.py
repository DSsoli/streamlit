import streamlit as st


def main():
    menu = ["Home","other","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.title("Hello this is home to test deploy")
    elif choice == "other":
        st.title("Hello this is other to test deploy")
    else:
        st.title("hello this is About to test deploy")

if __name__ == "__main__":
    main()