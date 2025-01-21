import streamlit as st
from utils import streamlit_utils,layout_indicium


layout_indicium.layout_custom()

streamlit_utils.titulo_personalizado("Modeling, Evaluation e Deployment")

st.write("Elaborar uma forma de utilizar multiplos modelos e exibir os resultados")

st.write("Exibir as métricas ex. Cross Validation")

st.write("Posso fazer multiplas paginas e dividir por framework")
st.write("""ex:
         
        - pag_1 scikit learn
        - pag_2 PyTorch e tensorboard(pre treinado e construção de um modelo, multiplas formas de customizar um modelo) 
        - pag_3 Mlflow
        - pag_4 Resumo e conclusões de todos os modelos testados, compartivos de performance.
        """)

st.write("Talvez o streamlit não de conta de utilizar tudo em nuvem, neste caso,sera necessário buscar uma solução viável")


with st.expander('**Notebook Jupyter**'):
    st.write("Teste notebook")
    streamlit_utils.load_notebook('./Notebooks/notebook.ipynb')
 