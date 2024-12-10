from utils import notebook_view
import streamlit as st



with open( "assets/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

with st.expander('**Notebook Jupyter**'):
    st.write("Teste notebook")
    notebook_view.load_notebook('./Notebooks/notebook.ipynb')
 