import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mario Lasić")
    content="""I'm a Python developer with a solid foundation in HTML and CSS, 
        specializing in creating dynamic websites using Django. I am 29 years old, 
        I bring both experience and innovation to my work."""
    st.info(content)