import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium

# Layout
layout_indicium.layout_custom()


streamlit_utils.titulo_personalizado("Precificação de Aluguéis em Nova York", color="#0081BE")
st.divider()

# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Descrição do Projeto","Objetivos e Estrutura"],
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
        st.image("imgs/ny.jpg", caption="Empire State Building e Estatua da Liberdade - Charly Triballeau/AFP")

    streamlit_utils.titulo_personalizado("Mercado imobiliário", size="h3", text_align='left', color="#0081BE")

    st.write("""
                O mercado imobiliário nova-iorquino oferece uma ampla variedade de opções para compradores 
                e investidores, com propriedades que atendem a diferentes perfis e necessidades. 
                Entre os principais tipos de imóveis, destacam-se os apartamentos de luxo, as residências 
                familiares, os lofts e os imóveis comerciais.
                Investir no mercado imobiliário de Nova York oferece diversas oportunidades, mas também 
                apresenta desafios que devem ser pontuados. Isto é, desde os preços elevados até as rígidas 
                regulamentações imobiliárias. A cidade é conhecida por ter alguns dos imóveis mais caros do mundo, 
                especialmente em áreas como Manhattan e Brooklyn, onde os valores por metro quadrado podem, facilmente, 
                ultrapassar a marca de milhões de dólares. 

                Além disso, especificamente tratando-se do mercado de locações de curto prazo, mudanças recentes
                na legislação local impactaram diretamente. Desde setembro de 2023, :blue[uma lei exige que os imóveis 
                não sejam alugados por períodos inferiores a 30 dias], a menos que os proprietários estejam 
                presentes durante toda a estadia, com um limite máximo de dois hóspedes. Também é proibida a 
                locação de cômodos separados, e os proprietários precisam pagar uma taxa de regularização de **US\\$ 145,00**. 
                Infrações às regras podem resultar em multas de até **US\\$ 7.500,00**.
             
                Essas mudanças representam um desafio adicional para o projeto que precisa se adaptar enquanto explora 
                as oportunidades de um dos mercados imobiliários mais atrativos e competitivos do mundo.""")
    
    with st.expander("Fontes"):
        st.write("""
                    [Exame - 8.set.2023: Crise de aluguel? Entenda por que Nova York proibiu reservas curtas no Airbnb](https://exame.com/mundo/crise-de-aluguel-entenda-por-que-nova-york-proibiu-reservas-curtas-no-airbnb/)
                    
                    [Folha de São Paulo - 16.jan.2025: NY teve 2º maior número de visitantes em 2024 e prevê recorde em 2025](https://www1.folha.uol.com.br/turismo/2025/01/ny-teve-2o-maior-numero-de-visitantes-em-2024-e-preve-quebrar-recorde-em-2025.shtml)
                """)
    


if selected == "Objetivos e Estrutura":
    streamlit_utils.titulo_personalizado("Objetivo", size="h3", text_align='left', color="#0081BE")
    st.write("""             
                O principal objetivo é a experiênciação das ferramentas usadas com fim de 
                :blue-background[**desenvolver um modelo de previsão de preços a partir 
                do dataset oferecido**] contendo a ducumentação, histórico de desevolvimento 
                e avaliação dos modelos testados utilizando frameworks de MLOps para 
                garantir a eficiência, reprodutibilidade e escalabilidade. 

                Vale ressaltar justamente o uso do framework Streamlit para criar a aplicação Web interativa, 
                contendo todas as etapas do desenvolvimento seguindo o framework CRISP-DM como metodologia. 


             

            """)
    st.divider()
    streamlit_utils.titulo_personalizado("Estrutura", size="h3", text_align='left', color="#0081BE")
    st.write("""
                **Entendimento do Negócio:**
                Trata-se da descrição geral do projeto e a contextualização sobre o problema proposto. 

                    - Sobre Nova York.
                    - Mercado imobiliário.

                **Entendimento dos Dados:** 
                Análise dos dados fornecidos, identificando os problemas

                    - Analise inicial (Estudo das variáveis)
                    - Dicionário dos dados
                    - Outliers
                    - Dados Ausentes
                    - Dados duplicados 
                    - Hipóteses de negócio relacionadas (Propostas pelo desafio e criadas)
        
                **Data Preparation:**
                 Descrição e motivação para as transformações nos dados.

                    - Dados categoricos 
                    - Dados contínuos

                **Modelagem:**
                 Descrição dos modelos testados e etapas do desenvolvimento e avalição dos modelos.

                    - MlFlow UI
                    - Conformal Prediction
                    - Métricas        
            """)


#st.link_button("MLFLOW","https://dagshub.com/AurelioGuilherme/AmbienteDeDesenvolvimento.mlflow")