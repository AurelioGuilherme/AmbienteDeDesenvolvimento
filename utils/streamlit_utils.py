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
    html_exporter = HTMLExporter(template_name='classic')
    html_body, _ = html_exporter.from_notebook_node(notebook)

    # Exibindo o conteúdo do notebook como HTML
    st.components.v1.html(html_body, height=600,scrolling=True)


         
def titulo_personalizado(texto_de_titulo, size='h1', color=None, text_align="center"):
    style = f"text-align: {text_align};{f' color: {color};' if color else ''}"
    st.markdown(f"""<{size} style="{style}">{texto_de_titulo}</{size}>""", unsafe_allow_html=True)  