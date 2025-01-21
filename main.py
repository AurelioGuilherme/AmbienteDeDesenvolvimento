import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium

# Layout 
st.set_page_config(layout="wide")
layout_indicium.layout_custom()


streamlit_utils.titulo_personalizado("Precificação de Aluguéis em Nova York", color="#0081BE")
st.divider()

# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Descrição do Projeto","Objetivo"],
                       icons=["house", "list-task"],
                       orientation="horizontal")

if selected =="Descrição do Projeto":
    st.write("""
             Este projeto foi desenvolvido na etapa do case técncico para a posição de
             Cientista de Dados Trainee no programa Lighthouse da Indicium Academy, 
             para testar os conhecimentos sobre a resolução de problemas de negócios, 
             análise de dados e aplicação de modelos preditivos. 
             
             O desafio simula minha alocação em um time de ciência de dados, 
             trabalhando com um cliente no desenvolvimento de uma estratégia de 
             precificação para uma plataforma de aluguéis temporários na cidade de Nova York.
             
             """)
    streamlit_utils.titulo_personalizado("Sobre Nova York", size="h3", text_align='left', color="#0081BE")
    left_colum, righ_column = st.columns(2)
    with left_colum:
         st.write("""
                    Nova York (New York City) é a cidade mais populosa dos Estados Unidos e um dos 
                    principais centros urbanos possui uma população superior a 8,2 milhões de 
                    habitantes em uma área de apenas 778 km², o que a torna a cidade mais densamente 
                    povoada do país. 
             
                    A cidade é composta por cinco *boroughs* (divisões administrativas/distritos): 
                    Bronx, Brooklyn, Manhattan, Queens e Staten Island, cada um com sua própria 
                    identidade cultural e histórica. Manhattan, em particular, é amplamente 
                    reconhecido como o coração financeiro da cidade. É em Manhattan, mais 
                    precisamente em Lower Manhattan, que se encontra Wall Street, o principal 
                    centro financeiro de Nova York, onde está localizada a Bolsa de Valores de 
                    Nova York (NYSE), a maior do mundo em capitalização de mercad
              
                    Também se destaca como um centro global de cultura, gastronomia e inovação. 
                    Em 2024, a cidade consolidou sua posição como :blue[um dos destinos turísticos 
                    mais populares do mundo, recebendo impressionantes 64,3 milhões de visitantes], 
                    desse total, 700 mil foram brasileiros. No total, os turistas movimentaram cerca 
                    de US$ 51 bilhões em gastos diretos, para fins de comparação, esse valor é maior 
                    que o PIB do Paraguai.
                  
                    Tratando-se de mobilidade, Nova York possui um dos mais antigos e extensos 
                    sistemas de transporte público do mundo. O metrô da cidade conta com 472 
                    estações e opera ininterruptamente, funcionando 24 horas por dia, 7 dias por semana.    
             """)
    with righ_column:
        st.image("imgs/ny.jpg")

    streamlit_utils.titulo_personalizado("Mercado imobiliário", size="h3", text_align='left', color="#0081BE")
    
#    responder: 
# - Sobre Nova York
# - Mercado de precificação
# - Economia 


if selected == "Objetivo":
    st.write("Objetivo")




#st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")




