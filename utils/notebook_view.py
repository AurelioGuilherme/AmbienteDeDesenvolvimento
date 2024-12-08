import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import codecs


def load_notebook(path_notebook):
    # Carregando o notebook
    with codecs.open(path_notebook, 'r', 'utf-8') as notebook_file:
        notebook_content = notebook_file.read()
        notebook = nbformat.reads(notebook_content, as_version=4)

    # Convertendo o notebook para HTML
    html_exporter = HTMLExporter()
    html_body, _ = html_exporter.from_notebook_node(notebook)

    # Exibindo o conteúdo do notebook como HTML
    st.components.v1.html(html_body, height=600,scrolling=True)#width=1100, height=600, scrolling=True)