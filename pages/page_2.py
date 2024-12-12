from utils import streamlit_utils,layout_indicium
import streamlit as st


layout_indicium.layout_custom()


streamlit_utils.titulo_centralizado("Data Preparation")

st.write("Detalhar todo o processo de tratamento de dados e enriquecimento")
st.write("Fornecer amostras do antes e depois")

st.write("No fim fazer uma classe que faz toda a tarefa de processamento de dados exibindo o código detalhado")



with st.expander('**Notebook Jupyter**'):
    st.write("Teste notebook")
    streamlit_utils.load_notebook('./Notebooks/notebook.ipynb')
 