import streamlit as st
from utils import streamlit_utils,layout_indicium
import pandas as pd


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

streamlit_utils.titulo_personalizado("Avaliação", 
                                      text_align="left",
                                      color="#0081BE", 
                                      size='h2')

st.write('''
            As abordagens de modelagem não alcançaram resultados satisfatórios, com o melhor modelo 
         apresentando um R² de 0,1054. No entanto, o objetivo principal foi atingido: criar um ambiente 
         que possibilite a experimentação de diferentes features de maneira simples, além de facilitar 
         a inclusão de novos tratamentos no pipeline de limpeza de dados.

            A performance limitada do modelo pode ser atribuída à alta quantidade de outliers, que 
         impactam significativamente os modelos de regressão mais simples. Modelos como XGBoost e 
         SVR oferecem uma vasta gama de hiperparâmetros que podem ser explorados, e o ambiente também 
         permite o registro dessas experimentações por meio do MLFlow, o que facilita o acompanhamento e 
         a análise dos resultados.

        ''')

streamlit_utils.titulo_personalizado("Metricas", 
                                      text_align="left",
                                      color="#0081BE", 
                                      size='h2')
dados = [
    ("LinearRegression", "1 - Categorizadas", "R²", 0.089570),
    ("LinearRegression", "1 - Categorizadas", "MAE", 74.192615),
    ("LinearRegression", "1 - Categorizadas", "MSE", 52733.150074),
    ("LinearRegression", "1 - Categorizadas", "RMSE", 229.636996),
    
    ("LinearRegression", "2 - Padronizadas", "R²", 0.105432),
    ("LinearRegression", "2 - Padronizadas", "MAE", 72.067135),
    ("LinearRegression", "2 - Padronizadas", "MSE", 46035.071870),
    ("LinearRegression", "2 - Padronizadas", "RMSE", 214.557852),
    
    ("SVR", "1 - Categorizadas", "R²", -0.005694),
    ("SVR", "1 - Categorizadas", "MAE", 74.143550),
    ("SVR", "1 - Categorizadas", "MSE", 51753.684786),
    ("SVR", "1 - Categorizadas", "RMSE", 227.494362),
    
    ("SVR", "2 - Padronizadas", "R²", 0.002902),
    ("SVR", "2 - Padronizadas", "MAE", 72.674731),
    ("SVR", "2 - Padronizadas", "MSE", 51311.349438),
    ("SVR", "2 - Padronizadas", "RMSE", 226.520086),
    
    ("XGBoost", "1 - Categorizadas", "R²", -0.095115),
    ("XGBoost", "1 - Categorizadas", "MAE", 72.319155),
    ("XGBoost", "1 - Categorizadas", "MSE", 56355.345496),
    ("XGBoost", "1 - Categorizadas", "RMSE", 237.392808),
    
    ("XGBoost", "2 - Padronizadas", "R²", 0.030136),
    ("XGBoost", "2 - Padronizadas", "MAE", 67.769217),
    ("XGBoost", "2 - Padronizadas", "MSE", 49909.858860),
    ("XGBoost", "2 - Padronizadas", "RMSE", 223.405145)
]


df_metricas = pd.DataFrame(dados, columns=["Modelo", "Abordagem", "Métrica", "Valor"])
st.dataframe(df_metricas)
