import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import codecs
import os
import pandas as pd


def load_notebook(path_notebook):
    # Carregando o notebook
    with codecs.open(path_notebook, 'r', 'utf-8') as notebook_file:
        notebook_content = notebook_file.read()
        notebook = nbformat.reads(notebook_content, as_version=4)

    # Convertendo o notebook para HTML
    html_exporter = HTMLExporter(template_name='classic')
    html_body, _ = html_exporter.from_notebook_node(notebook)

    # Exibindo o conteúdo do notebook como HTML
    st.components.v1.html(html_body, height=600,scrolling=True)


         
def titulo_personalizado(texto_de_titulo, size='h1', color=None, text_align="center", anchor=None):
    style = f"text-align: {text_align};{f' color: {color};' if color else ''}"
    if anchor:
        st.markdown(f"""<a id="{anchor}"></a>""", unsafe_allow_html=True)
    st.markdown(f"""<{size} style="{style}">{texto_de_titulo}</{size}>""", unsafe_allow_html=True)


def carrega_dados_cache():
    DATA_DIR = "./Data"
    POLLUTION_DATASET_FILE_NAME = "teste_indicium_precificacao.csv"
    file_path = os.path.join(DATA_DIR, POLLUTION_DATASET_FILE_NAME)
    df = pd.read_csv(file_path)
    st.session_state["data"] = df
    return df  