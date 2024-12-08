import streamlit as st
from utils import notebook_view





with st.expander('**Notebook Jupyter**'):
    st.write("Teste notebook")
    notebook_view.load_notebook('./Notebooks/notebook.ipynb')
 