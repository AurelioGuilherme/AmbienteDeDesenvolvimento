import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium


# Layout 
layout_indicium.layout_custom()


streamlit_utils.titulo_centralizado("NOME DO PROJETO")
_, cent_co,_ = st.columns(3)
with cent_co:
    st.image('imgs/64998fedf721c1b76821baf2_glob-logo-indicium.svg')


# Menu horizontal
selected = option_menu(menu_title=None,
                     options=["HOME","PROJECTS"],
                     orientation="horizontal")
if selected =="HOME":
    st.write("Home")
if selected == "PROJECTS":
    st.write("Projects")

st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")

# BACKLOG
st.divider()
st.title("Teste de projeto de Ciência de Dados")
st.write(":rainbow-background[O teste a seguir contera todos os passos para estruturar este projeto assim que receber o desafio real]")
st.subheader("Esta pagina sera uma pagina 'sobre' com um resumo.")



st.divider()
st.write("### BACKLOG")
st.write("- incluir uma box com o texto descrevendo o projeto.")
st.write("- incluir um botão para download do resumo contendo as respostas do desafio")
st.write("- Links uteis para acessar o Linkedin e Github")
st.write("- Mudar o fundo de alguns elementos para amarelo com a fonte na cor branca")

