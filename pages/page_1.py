import streamlit as st



with open( "assets/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# Agora você pode usar a fonte Roboto no seu aplicativo
st.title("Aplicativo com Fonte Roboto")
st.write("Este texto está usando a fonte Roboto.")
