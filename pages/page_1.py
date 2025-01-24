import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium

layout_indicium.layout_custom()
streamlit_utils.titulo_personalizado("Data Understanding", color="#0081BE")

st.divider()
streamlit_utils.titulo_personalizado("Descrição dos Dados", text_align="left" ,color="#0081BE", size='h2')
# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Análise Descritiva","Análise Inferencial"],
                       icons=["house", "list-task"],
                       orientation="horizontal")








#with st.expander('**Notebook Jupyter**'):
#    st.write("Teste notebook")
#    streamlit_utils.load_notebook('./Notebooks/notebook.ipynb')