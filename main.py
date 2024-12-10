import pandas as pd
import streamlit as st


with open( "assets/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



st.title("Este Titulo esta Titilium")
st.write("Este texto está sendo usado a fonte ROBOTO")




