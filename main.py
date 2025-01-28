import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium


# Layout
layout_indicium.layout_custom()
df = streamlit_utils.carrega_dados_cache()


streamlit_utils.titulo_personalizado("Precificação de Aluguéis em Nova York", color="#0081BE")
st.divider()

# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Descrição do Projeto","Estrutura"],
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
    
    st.divider()
    streamlit_utils.titulo_personalizado("Objetivo", size="h3", text_align='left', color="#0081BE")
    st.write(""" 
                Definirei os seguintes objetivos:   
                      
                - Experiênciação de ferramentas usadas para desenvolver um modelo de previsão 
                de preços a partir do dataset oferecido contendo a ducumentação, histórico de desevolvimento 
                e avaliação dos modelos testados utilizando frameworks de MLOps para garantir a eficiência, 
                reprodutibilidade e escalabilidade. 

                - Uso do framework Streamlit para criar a aplicação Web garantindo uma visualização interativa,
                diferente de um Jupyter Notebook, contendo todas as etapas do desenvolvimento seguindo 
                o framework CRISP-DM como metodologia. 
             
                - Desenvolver um processo de preparação de dados que permita a experimentação de diferentes features, 
                possibilitando defini-las de maneira simples e intuitiva, além de facilitar sua utilização na etapa de modelagem.  

                - Desenvolver uma aplicação interativa que funcione como um "produto", onde o usuário preenche um formulário
                 com as características desejadas e, com base nos dados fornecidos, o sistema retorna a previsão do preço de forma rápida.     

            """)
    st.divider()
    
    
    with st.expander("Fontes"):
        st.write("""
                    [Exame - 8.set.2023: Crise de aluguel? Entenda por que Nova York proibiu reservas curtas no Airbnb](https://exame.com/mundo/crise-de-aluguel-entenda-por-que-nova-york-proibiu-reservas-curtas-no-airbnb/)
                    
                    [Folha de São Paulo - 16.jan.2025: NY teve 2º maior número de visitantes em 2024 e prevê recorde em 2025](https://www1.folha.uol.com.br/turismo/2025/01/ny-teve-2o-maior-numero-de-visitantes-em-2024-e-preve-quebrar-recorde-em-2025.shtml)
                """)
    


if selected == "Estrutura":

    streamlit_utils.titulo_personalizado("Estrutura", size="h3", text_align='left', color="#0081BE")

    st.write('''
                  **Business Understanding:**
                Trata-se da descrição geral do projeto e a contextualização sobre o problema proposto. 
                 - Descrição do Projeto
                    - Sobre Nova York.
                    - Mercado imobiliário.
                    - Objetivo
            ''')
    
    st.divider()
    st.write("""
                **Data Understanding:** 
                Análise dos dados fornecidos, identificando os problemas, testando e hipóteses.
                - Descrição dos Dados
                    - Dicionário de Dados
                    - Visualização Inicial dos Dados
                - Análise Descritiva
                    - Dados Faltantes
                    - Dados Duplicados
                    - Análise de Dados Contínuos
                    - Valores Discrepantes
                    - Exploração Individual das Variáveis Contínuas
                        - price
                        - minimo_noites
                        - numero_de_reviews 
                        - reviews_por_mes
                        - calculado_host_listings_count
                        - disponibilidade_365
                    - Análise de Dados Categóricos
                        - host_id
                        - bairro_group
                        - bairro
                        - room_type
                    - Exploração Multivariada
                        - Correlação
                    - Analisando a relação entre variáveis
                        - Relação de preço com os bairros
                        - Relação de preço com o tipo de espaço
                        - Relação de preço com o mínimo de noites de forma agrupada
                        - Relação de preço com o numero de reviews de forma agrupada
                        - Relação de preço com o a quantidade de imoveis por host de forma agrupada
                        - Relação de preço com o a variável disponibilidade_365 de forma agrupada
                    - Dados Geoespaciais
                    - Análise Temporal
                    - Análise de Dados Textuais.
                        - Comparação de Palavras-Chave por Faixa de Preço
                        - Palavras presentes somente em imóveis de alto valor
                    - Conclusão
                - Análise Inferencial
                    - Hipóteses
                        - Existe diferença entre os preços dos imóveis de acordo com o tipo de espaço?
                        - Existem diferenças significativas entre o preço nos grupos de bairros?
                        - Existe associação entre o tipo de espaço e o bairro?
            """)
    st.divider()
    st.write('''
                **Data Preparation:**
             Estratégia de tratamento de dados para limpar, transformar e organizar os dados brutos 
             para torná-los adequados para análise e modelagem. 
             - Abordagem de Experimentação
             - 1ª experimentação - Abordagem com Features Continuas Transformadas em Categóricas
              - Divisão dos Dados Para Treino, Teste e Calibração
              - Enconding e Padronização
             - 2ª experimentação - Abordagem com Features Continuas Padronizadas.
              - Escolha de Features
            ''')
    st.divider()
    st.write('''
                **Modeling:**
             A etapa de modelagem e avaliação do Modelo.
             - Modelagem
                - Modelo Regressão Linear
                - Modelo SVR
                - Modelo XGBoost
             - MLFlOW
             - Avaliação
             - Metricas
                ''')
    st.divider()
    st.write('''
                **Deploy - Produto:**
             Aplicação do Modelo treinado
                - Prevendo o Valor
                    - Valor Previsto
                    - Localização
             ''')
