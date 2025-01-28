import streamlit as st
from utils import streamlit_utils,layout_indicium


layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Modeling e Evaluation", 
                                     color="#0081BE")
st.divider()


modelos_nome = ('Regressão Linear Múltipla','SVR', 'XGBoost')

streamlit_utils.titulo_personalizado("Modelagem", 
                                     text_align="left",
                                     color="#0081BE", 
                                     size='h2')

st.write('''
         A etapa de modelagem utilizei Jupyters Notebooks para 
         testar os modelos: Regressão linear, SVR e XGboost.

         Foi feito o trackeamento usando o MlFlow e o Dagshub para 
         registrar os testes e comparar a performance dos modelos.

         No menu abaixo você pode selecionar uma das opçoes e 
         verificar a implementação do código, ao clicar no botão :orange[MLFlow],
         será redirecionado para o :orange[MlFlow UI] contendo todas as experimentações.
         ''')

option_models = st.selectbox('Opções de Modelos: ', modelos_nome, key='models')
if option_models == 'Regressão Linear Múltipla':
    streamlit_utils.titulo_personalizado("Modelo Regressão Linear", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    
    with st.expander('**Notebook Jupyter**'):
        streamlit_utils.load_notebook('./Notebooks/Models-Notebooks/modelo_regressao_linear_multipla.ipynb')
    
    st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")


if option_models == 'SVR':
    streamlit_utils.titulo_personalizado("Modelo SVR", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    
    with st.expander('**Notebook Jupyter**'):
        streamlit_utils.load_notebook('./Notebooks/Models-Notebooks/modelo_svr.ipynb')
    
    st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")

if option_models == 'XGBoost':
    streamlit_utils.titulo_personalizado("Modelo XGBoost", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    
    with st.expander('**Notebook Jupyter**'):
        streamlit_utils.load_notebook('./Notebooks/Models-Notebooks/modelo_xgboost.ipynb')
    
    st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")

        

