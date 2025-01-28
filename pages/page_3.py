import streamlit as st
from utils import streamlit_utils,layout_indicium


layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Modeling e Evaluation", color="#0081BE", anchor="Modeling e Evaluation")
st.divider()


modelos_nome = ('Regressão Linear','Ensemble', 'Arvore')

option_models = st.selectbox('Opções de Modelos: ', modelos_nome, key='models')
if option_models == 'Regressão Linear':
    streamlit_utils.titulo_personalizado("Modelo Regressão Linear", text_align="left" ,color="#0081BE", size='h3')
    with st.expander('**Notebook Jupyter**'):
        st.write("Regression_model.ipynb")
        streamlit_utils.load_notebook('./Notebooks/Models-Notebooks/regression_model.ipynb')
    
    st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")

        

