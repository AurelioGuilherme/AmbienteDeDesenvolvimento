from utils import streamlit_utils,layout_indicium
import streamlit as st
import pandas as pd

layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Data Preparation", color="#0081BE",anchor='inicio_data_preparation')
st.divider()

st.write('''
            O processo de tratamento de dados foi detalhado no arquivo Jupyter Notebook 
            :orange[data_preparation.ipynb]. Além disso, uma classe foi implementada no 
            arquivo :orange[tratamento_de_dados.py], a qual encapsula todas as etapas de 
            tratamento, automatizando todo o processo de preparação dos dados.
         
         ''')


if "data" in st.session_state:
    df = st.session_state["data"]
else:
    st.warning("Nenhum arquivo foi carregado. Volte para a página de Upload.")

streamlit_utils.titulo_personalizado("Descrição do Tratamento", text_align='left', color="#0081BE", size='h2')

streamlit_utils.titulo_personalizado("Dados de Treinamento", text_align='left'  ,color="#0081BE", size='h2')



st.write('A baixo você pode conferir o Jupyter Notebook.')

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