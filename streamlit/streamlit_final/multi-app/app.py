import streamlit as st

# no_sidebar_style = """
#     <style>
#         div[data-testid="stSidebarNav"] {display: none;}
#     </style>
# """
# st.markdown(no_sidebar_style, unsafe_allow_html=True)


#st.set_page_config(initial_sidebar_state="collapsed")
# st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

my_variable = "From Main App.py Page"


def main():
    st.title("Streamlit Multi-Page")
    st.subheader("Main Page")

    choice = st.sidebar.selectbox("Submenu", ["a", "b"])
    if choice == "a":
        st.subheader("A")

if __name__=="__main__":
    main()