import streamlit as st

st.set_page_config(
page_title="Ex-stream-ly Cool App",
page_icon="🧊",
#layout="wide",
#initial_sidebar_state="expanded",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.text("hello world. this is a text")

asdf = "fuck"
st.text(f"this is so {asdf}")

st.header("this is a header")
st.subheader("this is a subheader")
st.markdown("this is a markdown")

st.success("successful")
st.warning("this is danger")
st.info("this is information")
st.error("this is an error")
st.exception("this is an exception")

#superfunction
st.write("normal text")
st.write("## this is a markdown text")
st.write(1+2)

st.write(dir(st))
st.help(range)


def main():
	"""all your code goes here"""
	st.title("Hello Streamlit")
	pass


if __name__ == '__main__':
	main()

