import streamlit as st

def main():
    st.title("streamlit app")
    st.subheader("hello streamlit")

    st.help(st.form)

    with st.form(key="myform", clear_on_submit=True):
        firstname = st.text_input("first name")
        lastname = st.text_input("last name")
        message = st.text_area("message")
        submit_button = st.form_submit_button("submit")
    
    if submit_button:
        st.info("results")
        result = firstname + lastname + "@gmail.com"
        st.write(result)


if __name__=="__main__":
    main()