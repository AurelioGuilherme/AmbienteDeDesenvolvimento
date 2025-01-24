import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium


# Layout
layout_indicium.layout_custom()
streamlit_utils.titulo_personalizado("Deploy - Produto", color="#0081BE")
st.divider()