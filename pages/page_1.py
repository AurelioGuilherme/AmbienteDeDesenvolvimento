import streamlit as st
from utils import streamlit_utils,layout_indicium

layout_indicium.layout_custom()
streamlit_utils.titulo_centralizado("Bussines e Data Understanding")

st.write("Fornecer possiveis KPIs")
st.write("Incluir um resumo estatístico")

st.write("")
with st.expander("show code"):
    st.write("Incluir sempre ó código para fornecer tal gráfico, ou tal analise")
    st.code("print('Hello world!')")

st.write("Incluir testes estatísticos relevantes para responder as perguntas de negócios.")


with st.expander('**Notebook Jupyter**'):
    st.write("Teste notebook")
    streamlit_utils.load_notebook('./Notebooks/notebook.ipynb')



