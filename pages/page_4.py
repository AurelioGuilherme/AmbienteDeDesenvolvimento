import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium, valida_dados_deploy, tratamento_de_dados
import pandas as pd



# Layout
layout_indicium.layout_custom()
streamlit_utils.titulo_personalizado("Deploy - Produto", color="#0081BE")
st.divider()


with st.form(key='formulario_nome'):
    col_1, col_2, col_3 =  st.columns(3)
    with col_1:
        id = st.text_input("**id:**")
        nome = st.text_input("**nome**")
        host_id = st.text_input("host_id:")
        host_name = st.text_input("**host_name:**")
        # Selectbox para grupo de bairros
        bairro_group = st.selectbox("**bairro_group:**",options=["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"])
    with col_2:
        # Campo de texto para o bairro
        bairro = st.text_input("**bairro:**")

        # Campos de latitude e longitude
        latitude = st.text_input("**latitude:**")
        longitude = st.text_input("**longitude:**")
        # Selectbox para tipo de quarto
        room_type = st.selectbox("**room_type:**", options=["Entire home/apt", "Private room", "Shared room", "Hotel room"])
        minimo_noites = st.text_input("**minimo_noites**")

    with col_3:
        numero_de_reviews = st.text_input("**numero_de_reviews:**")
        ultima_review = st.text_input("**ultima_review**")
        reviews_por_mes = st.text_input("**reviews_por_mes:**")
        calculado_host_listings_count = st.text_input("**calculado_host_listings_count**")
        disponibilidade_365 = st.text_input("**disponibilidade_365**")
    
    # Botão de envio
    submit_button = st.form_submit_button(label='Enviar')  

    ## Verifica se o botão foi pressionado
    if submit_button:
        erros = []

        # Validação para cada campo
        if not valida_dados_deploy.texto_valido(nome):
            erros.append("Nome do anúncio inválido.")
        if not valida_dados_deploy.texto_valido(host_name):
            erros.append("Nome do anfitrião inválido.")
        if not bairro_group:
            erros.append("Grupo do bairro deve ser selecionado.")
        if not valida_dados_deploy.texto_valido(bairro):
            erros.append("Nome do bairro inválido.")
        if not minimo_noites.isdigit():
            erros.append("Mínimo de noites deve conter apenas números.")
        if not numero_de_reviews.isdigit():
            erros.append("Número de reviews deve conter apenas números.")
        if ultima_review:
            try:
                pass
            except ValueError:
                erros.append("Data da última review deve estar no formato YYYY-MM-DD.")
        if not reviews_por_mes.replace('.', '', 1).isdigit():
            erros.append("Reviews por mês deve ser um número válido.")
        if not disponibilidade_365.isdigit() or not (0 <= int(disponibilidade_365) <= 365):
            erros.append("Disponibilidade deve ser um número entre 0 e 365.")

        # Exibe mensagens de erro
        if erros:
            for erro in erros:
                st.error(erro)
            
        else:
             dados = {
                "id": [int(id)],
                "nome": [str(nome)],
                "host_id":[int(host_id)],
                "host_name": [str(host_name)],
                "bairro_group": [str(bairro_group)],
                "bairro":[str(bairro)],
                "latitude":[float(latitude)],
                "longitude":[float(longitude)],
                "room_type":[str(room_type)],
                "minimo_noites": [int(minimo_noites)],
                "numero_de_reviews": [int(numero_de_reviews)],
                "ultima_review": [str(ultima_review)],
                "reviews_por_mes": [float(reviews_por_mes)],
                "calculado_host_listings_count": [int(calculado_host_listings_count)],
                "disponibilidade_365": [float(disponibilidade_365)],
                'price': 0}
             
             df_previsao = pd.DataFrame(dados)
             st.dataframe(df_previsao)


             st.success("Dados enviados com sucesso!")

        
        features_numericas = ['numero_de_reviews',
                              'reviews_por_mes',
                              'calculado_host_listings_count']

        features_categoricas = [
            'room_type',
            'bairro_group',
            'minimo_noites_categorico',
            'disponibilidade_365_categorico',
            'ultima_review_semestre',
            'valor_preenchido']
        

     
        cleaner_data = tratamento_de_dados.TransformData(df_previsao, features_categoricas, features_numericas, treino=False)

        X_predict, _ = cleaner_data.fit_transform()
        st.write(X_predict)
