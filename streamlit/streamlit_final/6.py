import streamlit as st
import pandas as pd


def main():
    st.title("streamlit forms & salary calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":
        st.subheader("Forms Tutorial")

        with st.form(key="salaryform"):
            col1, col2, col3 = st.columns([3,2,1])
            with col1:
                amount = st.number_input("rate in $")
            with col2:
                hour_per_week = st.number_input("hours per week", 1, 120)
            
            with col3:
                st.text("salary")
                submit_salary = st.form_submit_button(label="calculate")

        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hour_per_week]
                df = pd.DataFrame({"hourly":amount, "daily":daily, "weekly":weekly})
                st.dataframe(df)


        with st.form(key='form1'):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("lastname")
            dob = st.date_input("date of birth")

            submit_button = st.form_submit_button(label="sign up")
        
        if submit_button:
            st.success(f"hello {firstname} you've created an account")
        
        form2 = st.form(key="form2")
        username = form2.text_input("username")
        jobtype = form2.selectbox("job", ['dev', 'data scientist', 'doctor'])
        submit_button2 = form2.form_submit_button("Log in")
        if submit_button2:
            st.write(f"hi {username}")

    else:
        st.subheader("About")

if __name__=="__main__":
    main()