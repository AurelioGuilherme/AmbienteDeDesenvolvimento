from utils import streamlit_utils,layout_indicium
import streamlit as st
import pandas as pd

layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Data Preparation", color="#0081BE",anchor='inicio_data_preparation')
st.divider()


if "data" in st.session_state:
    df = st.session_state["data"]
    st.dataframe(df)
else:
    st.warning("Nenhum arquivo foi carregado. Volte para a página de Upload.")






with st.expander('**Notebook Jupyter**'):
    streamlit_utils.titulo_personalizado("Data Preparation Notebook", size="h3", text_align='left',color="#F7A600")

    streamlit_utils.load_notebook('./Notebooks/data_preparation.ipynb')
st.markdown("""
             <style>
             .scroll-button {
                 position: fixed;
                 bottom: 20px;
                 right: 20px;
                 background-color: #0081BE;
                 color: white;
                 border: none;
                 padding: 10px 20px;
                 border-radius: 5px;
                 cursor: pointer;
                 font-size: 16px;
                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
             }
             .scroll-button:hover {
                 background-color: #005f8b;
             }
             </style>
             <a href="#inicio_data_preparation">
                 <button class="scroll-button">Voltar ao Início.</button>
             </a>
            """,unsafe_allow_html=True)