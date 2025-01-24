from utils import streamlit_utils,layout_indicium
import streamlit as st
import pandas as pd

layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Data Preparation")
st.divider()


if "data" in st.session_state:
    df = st.session_state["data"]
    st.dataframe(df)
else:
    st.warning("Nenhum arquivo foi carregado. Volte para a página de Upload.")






#with st.expander('**Notebook Jupyter**'):
#    st.write("Teste notebook")
#    streamlit_utils.load_notebook('./Notebooks/notebook.ipynb')
 