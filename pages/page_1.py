import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium, stats_utils,tratamento_de_dados
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter
import re
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols



layout_indicium.layout_custom()
df = streamlit_utils.carrega_dados_cache()
df_copia = df.copy()


streamlit_utils.titulo_personalizado("Data Understanding", 
                                     color="#0081BE", 
                                     anchor="inicio")
st.divider()

# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Descrição dos Dados",
                                "Análise Descritiva",
                                "Análise Inferencial"],
                       icons=["list-task", "list-task", "list-task"],
                       orientation="horizontal")

if selected == "Descrição dos Dados":
    streamlit_utils.titulo_personalizado("Descrição dos Dados", text_align="left" ,color="#0081BE", size='h2')
    st.write('''
             A base de dados fornecida contém :blue[16 colunas] e :blue[48.894 linhas], 
             abaixo estão as descrições detalhadas juntamente com a tipagem dos dados:

             **:orange[id]** – Atua como uma chave exclusiva para cada anúncio nos dados do aplicativo (Tipo: :green[int64])  
             **:orange[nome]** - Representa o nome do anúncio (Tipo: :green[object])  
             **:orange[host_id]** - Representa o id do usuário que hospedou o anúncio (Tipo: :green[int64])  
             **:orange[host_name]** – Contém o nome do usuário que hospedou o anúncio (Tipo: :green[object])  
             **:orange[bairro_group]** - Contém o nome do bairro onde o anúncio está localizado (Tipo: :green[object])  
             **:orange[bairro]** - Contém o nome da área onde o anúncio está localizado (Tipo: :green[object])  
             **:orange[latitude]** - Contém a latitude do local (Tipo: :green[float64])  
             **:orange[longitude]** - Contém a longitude do local (Tipo: :green[float64])  
             **:orange[room_type]** – Contém o tipo de espaço de cada anúncio (Tipo: :green[object])  
             **:orange[price]** - Contém o preço por noite em dólares listado pelo anfitrião (Tipo: :green[int64])  
             **:orange[minimo_noites]** - Contém o número mínimo de noites que o usuário deve reservar (Tipo: :green[int64])  
             **:orange[numero_de_reviews]** - Contém o número de comentários dados a cada listagem (Tipo: :green[int64])  
             **:orange[ultima_review]** - Contém a data da última revisão dada à listagem (Tipo: :green[object])  
             **:orange[reviews_por_mes]** - Contém o número de avaliações fornecidas por mês (Tipo: :green[float64])  
             **:orange[calculado_host_listings_count]** - Contém a quantidade de listagens por host (Tipo: :green[int64])  
             **:orange[disponibilidade_365]** - Contém o número de dias em que o anúncio está disponível para reserva (Tipo: :green[int64])  
            ''')
    st.divider()
    st.dataframe(df)



if selected =="Análise Descritiva":
    streamlit_utils.titulo_personalizado("Dados Faltantes", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    st.write('''
                O conjunto de dados apresenta a seguinte quantidade de dados faltantes, 
                conforme detalhado abaixo:


            ''')
    st.write(pd.DataFrame({"Quantidade_Dados_Faltantes" : df.isnull().sum()[df.isnull().sum() > 0],
                           "Porcentagem_Dados_Faltantes" : round((df.isnull().sum()[df.isnull().sum() > 0] / len(df) * 100),2)
                           }))
    st.write('''
                Como a quantidade de dados faltantes nas colunas :orange[reviews_por_mes] e :orange[ultima_review]
             é igual, realizei a verificação confirmando que os valores ausentes correspondem às mesmas 
             linhas em ambas as colunas.
            ''')
    with st.expander('Mostrar código'):
         st.code('''
                # Selecionei as colunas e realizei a comparação, após isso utilizei o tipo `set()` 
                # para exibir os valores únicos, desta forma retornou apenas um valor (True).
                 #Caso houvessem diferença retornaria dois valores (True e False) por exemplo.

                 set(df[df["ultima_review"].isnull()].index == df[df["reviews_por_mes"].isnull()].index) 
                ''')
         st.write('{np.True_}')


    streamlit_utils.titulo_personalizado("Dados Duplicados", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    st.write('''
               Não identifiquei valores duplicados no conjunto de dados, 
               e as colunas que apresentam duplicações não indicam erros.
            ''')
    with st.expander('Mostrar código'):
        st.code('''
                # Verificando se existem linhas em que todos os dados são duplicados
                df[df.duplicated()]
                
                # Verifica em loop se existe valores duplicados
                lista_colunas_com_valores_duplicados = []
                for col in df.columns:
                    if len(set(df[col].duplicated())) == 2:
                        lista.append(col)
                
                print(lista_colunas_com_valores_duplicados)
                ''')      
    st.divider()


    streamlit_utils.titulo_personalizado("Análise de Dados Contínuos", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    st.write('''
             Para analisar os dados contínuos, selecionarei as seguintes colunas:
              - :orange[price]
              - :orange[minimo_noites]
              - :orange[numero_de_reviews] 
              - :orange[reviews_por_mes]
              - :orange[calculado_host_listings_count]
              - :orange[disponibilidade_365]
             ''')
    
    valores_continuos = ['price', 'minimo_noites', 'numero_de_reviews', 
                         'reviews_por_mes', 'calculado_host_listings_count',
                         'disponibilidade_365']
    valores_continuos_df = df[valores_continuos].describe().T
    valores_continuos_df['Valores únicos'] = df[valores_continuos].nunique()
    
    st.write(valores_continuos_df)

    st.write('''
                Com o método :blue[**pd.describe()**] é possivel identificar algumas possíveis discrepancias:
             
             - A média está distante da mediana (50%) em todas as colunas, isso indica uma **distribuição assimétrica**.
             - A valores máximos discrepantes em todas as colunas exceto pela coluna :orange[disponibilidade_365]
             - Os dados possuem alta variabilidade
             - A coluna :orange[price] possui valores mínimos :blue[**"0"**], possivelmente um erro.
            ''')


    streamlit_utils.titulo_personalizado("Valores Discrepantes", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    
    with st.expander('Gráficos Boxplot'):
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                streamlit_utils.titulo_personalizado("price", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                fig = px.box(df, y='price')
                st.plotly_chart(fig)

            with col_2:
                streamlit_utils.titulo_personalizado("minimo_noites", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                # Plot minimo noites
                fig = px.box(df, y='minimo_noites')
                st.plotly_chart(fig)
            with col_3:
                
                streamlit_utils.titulo_personalizado("numero_de_reviews", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                # Plot numero de reviews
                fig = px.box(df, y='numero_de_reviews')
                st.plotly_chart(fig)

            col_4, col_5, col_6 = st.columns(3)
            with col_4:
                streamlit_utils.titulo_personalizado("reviews_por_mes", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                # Plot reviews por mes
                fig = px.box(df, y='reviews_por_mes')
                st.plotly_chart(fig)

            with col_5:
                streamlit_utils.titulo_personalizado("calculado_host_listings_count", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.box(df, y='calculado_host_listings_count')
                st.plotly_chart(fig)

            with col_6:
                streamlit_utils.titulo_personalizado("disponibilidade_365", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.box(df, y='disponibilidade_365')
                st.plotly_chart(fig)

    with st.expander('Gráficos Histograma'):
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                streamlit_utils.titulo_personalizado("price", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='price', nbins=50)
                st.plotly_chart(fig)

            with col_2:
                streamlit_utils.titulo_personalizado("minimo_noites", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='minimo_noites', nbins=50 )
                st.plotly_chart(fig)
            with col_3:
                
                streamlit_utils.titulo_personalizado("numero_de_reviews", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='numero_de_reviews', nbins=50)
                st.plotly_chart(fig)

            col_4, col_5, col_6 = st.columns(3)
            with col_4:
                streamlit_utils.titulo_personalizado("reviews_por_mes", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='reviews_por_mes', nbins=50)
                st.plotly_chart(fig)

            with col_5:
                streamlit_utils.titulo_personalizado("calculado_host_listings_count", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='calculado_host_listings_count', nbins=50)
                st.plotly_chart(fig)
                
            with col_6:
                streamlit_utils.titulo_personalizado("disponibilidade_365", 
                                                     text_align="left",
                                                     color="#0081BE", 
                                                     size='h3')
                
                fig = px.histogram(df, x='disponibilidade_365')
                st.plotly_chart(fig)
        
    st.write('''
                Ao analisar os gráficos apresentados acima, é possível comprovar a presença de 
                outliers nos dados. Para compreender melhor essas discrepâncias, será realizada 
                uma análise detalhada de cada coluna individualmente.
             ''')
    st.divider()
    
    
    streamlit_utils.titulo_personalizado("Exploração Individual das Variáveis Contínuas", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')       
    st.write(':orange[**Selecione uma das opções de análise abaixo para visualiza-la.**]') 

    opcoes_analise_individual = ('price', 
                                 'minimo_noites',
                                 'numero_de_reviews',
                                 'reviews_por_mes',
                                 'calculado_host_listings_count',
                                 'disponibilidade_365'
                                 )


    option = st.selectbox('Opções de Análise', opcoes_analise_individual, key='1')
    if option == 'price':
        streamlit_utils.titulo_personalizado("price", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')
        
        with st.expander('Exibir Análise'):
            st.write('**price menor do que 1**')
            st.dataframe(df.query('price < 1'))
            st.write('''
                     - São imóveis diferentes de acordo com a latitude e longitude.
                     - Há imóveis que pertencem ao mesmo proprietário neste grupo de dados.

                     :red[**Esses valores serão tratados na etapa de Data Preparation, 
                     podendo ser removidos ou preenchidos**]

                     ''')
            st.divider()


            stats_utils.exibe_analise_q3_outliers(df, df.price)

    elif option == 'minimo_noites': 
        streamlit_utils.titulo_personalizado("minimo_noites", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')
        
        with st.expander('Exibir Análise'):
            stats_utils.exibe_analise_q3_outliers(df, df.minimo_noites)

    elif option == 'numero_de_reviews':
        streamlit_utils.titulo_personalizado("numero_de_reviews", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')
        with st.expander('Exibir Análise'):
            stats_utils.exibe_analise_q3_outliers(df,df.numero_de_reviews)
    
    elif option == 'reviews_por_mes':
        streamlit_utils.titulo_personalizado("reviews_por_mes", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')

        with st.expander('Exibir Análise'):
            stats_utils.exibe_analise_q3_outliers(df, df.reviews_por_mes)

    elif option == 'calculado_host_listings_count':
        streamlit_utils.titulo_personalizado("calculado_host_listings_count", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')
        with st.expander('Exibir Análise'):
            stats_utils.exibe_analise_q3_outliers(df, df.calculado_host_listings_count)

            streamlit_utils.titulo_personalizado("Será que a contagem host está correta?", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            
            st.write('A resposta para esta pergunta é não.')
            # Separei as colunas necessárias para essa análise, criei uma lista com os valores únicos 
            # em "calculado_host_listings_count" e criei um dataframe vazio.
            df_problema = df_copia[['host_id', 'calculado_host_listings_count']]
            ids = list(df_problema['calculado_host_listings_count'].unique())
            df_teste = pd.DataFrame()

            # loop com os valores únicos armazenando o resultado do tamanho do objeto set
            for i in ids:
                tamanho_teste = len(set(df_problema.query(f'calculado_host_listings_count == {i}')\
                                                   .value_counts('host_id')))

                # Compara se o valor é diferente de 1
                if tamanho_teste != 1:
                    # Calcula a quantidade de host_ids verdadeira
                    host_ids_counts_df = pd.DataFrame(df_copia.query(f'calculado_host_listings_count == {i}')\
                                                              .value_counts('host_id'))\
                                                              .reset_index()

                    # Filtra somente os valores incosistentes
                    host_ids_counts = host_ids_counts_df[host_ids_counts_df['count'] != i]

                    # Concatena os valores ao DataFrame. 
                    df_teste = pd.concat([df_teste, host_ids_counts])
            # Dados incorretos
            df_teste = df_teste.rename({'count': 'calculado_host_listings_count'}, axis = 1)

            st.write('Dados corrigidos:')
            st.dataframe(df_teste)

            st.write('Filtrando dados originais incorretos.')
            st.dataframe(df.query('host_id == 2787'))

            st.write('''Código para esta análise:''')
            st.code('''
            # Separei as colunas necessárias para essa análise, criei uma lista com os valores únicos 
            # em "calculado_host_listings_count" e criei um dataframe vazio.
            df_problema = df_copia[['host_id', 'calculado_host_listings_count']]
            ids = list(df_problema['calculado_host_listings_count'].unique())
            df_teste = pd.DataFrame()

            # loop com os valores únicos armazenando o resultado do tamanho do objeto set
            for i in ids:
                tamanho_teste = len(set(df_problema.query(f'calculado_host_listings_count == {i}')\\
                                                   .value_counts('host_id')))

                # Compara se o valor é diferente de 1
                if tamanho_teste != 1:
                    # Calcula a quantidade de host_ids verdadeira
                    host_ids_counts_df = pd.DataFrame(df_copia.query(f'calculado_host_listings_count == {i}')\\
                                                              .value_counts('host_id'))\\
                                                              .reset_index()

                    # Filtra somente os valores incosistentes
                    host_ids_counts = host_ids_counts_df[host_ids_counts_df['count'] != i]

                    # Concatena os valores ao DataFrame. 
                    df_teste = pd.concat([df_teste, host_ids_counts])
            # Dados incorretos
            df_teste = df_teste.rename({'count': 'calculado_host_listings_count'}, axis = 1)

                ''')
    
    elif option == 'disponibilidade_365':
        streamlit_utils.titulo_personalizado("disponibilidade_365", 
                                             text_align="left",
                                             color="#F7A600", 
                                             size='h3')
        
        with st.expander('Exibir Análise'):
            stats_utils.exibe_analise_q3_outliers(df, df.disponibilidade_365)

    st.write('''
             Os valores de :red[price que são menores que 1] serão removidos ou preenchidos na etapa 
             de Data Preparation, julgo esses dados como valores incorretos devido algum erro de coleta.

             Embora exista a presença de :red[outliers], a remoção ou corte desses valores 
             julgo como não necessária, :red[*neste momento], pois os dados permanecem dentro 
             de uma faixa aceitável e condizente com a realidade, não aparentando um erro de coleta. 
             
             No entanto, na etapa de Data Preparation, a normalização deve ser realizada 
             considerando a presença desses valores para a escolha do algoritmo de normalização.

             As variáveis :orange[minimo_noites], :orange[numero_de_reviews], :orange[calculado_host_listings_count], 
             :orange[disponibilidade_365] podem ser classificadas ou transformadas em variáveis categóricas 
             com agrupamentos melhorando a homogeneidade na etapa de Data Preparation.

             A variável :orange[calculado_host_listings_count] possui um erro de atribuição no host_id: 2787, 
             onde a quantidade de anúncios informada está divergente da presente do conjunto de dados, desta forma 
             será necessária a atribuição do valor correto.

             - :red[**Neste momento:**] Caso seja constatado que a performance do modelo é insulficiente 
             na etapa de evaluation, pode ser considerado algum tratamento de dados adicional nos valores outliers
             para a melhoria do modelo. 
             ''')
    st.divider()

    streamlit_utils.titulo_personalizado("Análise de Dados Categóricos", 
                                         text_align="left", 
                                         color="#0081BE", 
                                         size='h2')

    st.write('''
            Para analisar os dados categóricos, selecionarei as seguintes colunas:
             - :orange[host_id]
             - :orange[bairro_group] 
             - :orange[bairro]
             - :orange[room_type]
            ''') 
    st.divider() 
    streamlit_utils.titulo_personalizado("Exploração Individual das Variáveis Categóricas", 
                                         text_align="left", 
                                         color="#0081BE", 
                                         size='h3')

    col_1, col_2 = st.columns(2)
    with col_1:

        st.write(':blue-background[host_id]')
        st.write(f'O conjunto de dados possui um total de {df["host_id"].nunique()} host distintos.')

        host_counts = pd.DataFrame(df.groupby('host_id')['id'].count())\
                                     .rename({'id': 'Quantidade de anuncios'}, axis=1)\
                                     .sort_values('Quantidade de anuncios', ascending=False)
        
        st.write('Top 5 Hosts com Mais Anúncios')
        st.write(host_counts.head(5))

 

    with col_2:
        st.write(':blue-background[bairro_group]')
        
        st.write(f'''
                 O conjunto de dados possui um total de {df["bairro_group"].nunique()} grupos de bairros.
                 ''')
        st.write(pd.DataFrame(df.groupby('bairro_group')['id'].count())\
                                .rename({'id': 'Quantidade de anuncios'}, axis=1))


    col_3, col_4 = st.columns(2) 
    with col_3:
        st.write(':blue-background[bairro]')

        st.write(f'O conjunto de dados possui um total de {df["bairro"].nunique()} grupos de bairros.')

        bairro_counts = pd.DataFrame(df.groupby('bairro')['id'].count())\
                                       .rename({'id': 'Quantidade de anuncios'}, axis=1)\
                                       .sort_values('Quantidade de anuncios', ascending=False)
        st.write('Top 5 Bairros com Mais Anúncios')
        st.write(bairro_counts.head(5))
   
    with col_4:
        st.write(':blue-background[room_type]')

        st.write(f'O conjunto de dados possui um total de {df["room_type"].nunique()} tipos de espaço distintos.')
        room_type_counts = pd.DataFrame(df.groupby('room_type')['id'].count())\
                                          .rename({'id': 'Quantidade de anuncios'}, axis=1)\
                                          .sort_values('Quantidade de anuncios', ascending=False)  
        st.write(room_type_counts)

        st.write('''
                    A definição para os tipos:
                    
                 - **Entire home/apt**: Apartamento ou casa individual (o hóspede não precisará compartilhar 
                 os espaços com outros inquilinos ou proprietários).
                 - **Private room**: Quarto individual (o hospede compartilha espaços como cozinha 
                 com outros inquilinos ou proprietarios, porem o quarto é individual).
                 - **Shared room**: Quarto compartilhado.
                 ''')
    

    st.divider()
    streamlit_utils.titulo_personalizado("Exploração Multivariada", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    
    streamlit_utils.titulo_personalizado("Correlação", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    st.write('''
                Para analisar a correlação entre as variáveis selecionei as seguintes features:
                - :orange[price]
                - :orange[minimo_noites]
                - :orange[numero_de_reviews]
                - :orange[reviews_por_mes]
                - :orange[calculado_host_listings_count]
                - :orange[disponibilidade_365]

                As demais variáveis não foram consideradas devido à sua natureza categórica, descritiva, geoespacial 
                (como latitude e longitude) ou temporal. Dessa forma, a utilização da correlação de Pearson 
                não seria adequada para essas características.
            ''')
    correlacao_features = ['price', 
                           'minimo_noites', 
                           'numero_de_reviews', 
                           'reviews_por_mes', 
                           'calculado_host_listings_count', 
                           'disponibilidade_365']
    
    correlation_matrix = df[correlacao_features].corr()
    fig = px.imshow(correlation_matrix,  text_auto=True, aspect="auto")
    fig.update_layout(title=dict(text="Matriz de Correlação", x=0.4),
                      width=750, 
                      height=500) 
    st.plotly_chart(fig)

    st.write('''
             As únicas váriaveis que apresentam correlação ao menos moderada são: 
             :orange[reviews_por_mes] :orange[numero_de_reviews], as demais apresentam correlção fraca.
             ''')
    st.divider()

    streamlit_utils.titulo_personalizado("Analisando a relação entre variáveis", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    
    st.write(':orange[**Selecione uma das opções de análise abaixo para visualiza-la.**]')
    option_relacao_entre_variaveis = ('Relação de preço com os bairros',
                                      'Relação de preço com o tipo de espaço',
                                      'Relação de preço com o mínimo de noites de forma agrupada',
                                      'Relação de preço com o numero de reviews de forma agrupada',
                                      'Relação de preço com o a quantidade de imoveis por host de forma agrupada',
                                      'Relação de preço com o a variável disponibilidade_365 de forma agrupada'                                      
                                      )
                                   

    option_2 = st.selectbox('Opções de Análise: ', option_relacao_entre_variaveis, key=2)
    if option_2 == 'Relação de preço com os bairros':
        streamlit_utils.titulo_personalizado("Relação de preço com os bairros", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        
        with st.expander('Exibir Análise'):
            streamlit_utils.titulo_personalizado("price X bairro_group", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            st.write('''
                        Fazedo um agrupamento por preço por grupo de bairros, considerando somente os 
                     alugueis com valor diferentes de 0 é possivel concluir que:

                     - Manhattan pode ser considerado o melhor conjunto de bairros, 
                     pois é o mais popular e com maior média de preço.
                     - Bronx é o bairro menos rentavel.
                     - State Island é o bairro menos popular.
                    ''')

            st.write('''
                    Criei uma função chamada :green[agrupamento_estilizado] que está 
                    disponível em :green[utils.stats_utils.py] para auxiliar 
                    na replicação desses agrupamentos.
                    ''')    
            stats_utils.agrupamento_estilizado(df=df, 
                                               query='price != 0', 
                                               agrupamento='bairro_group', 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)


            st.divider()    
            streamlit_utils.titulo_personalizado("price x bairro", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            
            manhattan_col, brooklyn_col,  = st.columns(2)
            Queens_col, statenisland_col = st.columns(2)
            bronx_col, analise_bairros = st.columns(2)

            with manhattan_col:
                st.write(':orange[**Manhattan**]')

                stats_utils.agrupamento_estilizado(df=df, 
                                                  query='price != 0 & bairro_group == "Manhattan"', 
                                                  agrupamento='bairro', 
                                                  coluna_valor='price',
                                                  porcentagem_do_total=True)
            with brooklyn_col:
                st.write(':orange[**Brooklyn**]')
                stats_utils.agrupamento_estilizado(df=df, 
                                                  query='price != 0 & bairro_group == "Brooklyn"', 
                                                  agrupamento='bairro', 
                                                  coluna_valor='price',
                                                  porcentagem_do_total=True)


            with Queens_col:
                st.write(':orange[**Queens**]')
                stats_utils.agrupamento_estilizado(df=df, 
                                                  query='price != 0 & bairro_group == "Queens"', 
                                                  agrupamento='bairro', 
                                                  coluna_valor='price',
                                                  porcentagem_do_total=True)

            with statenisland_col:
                st.write(':orange[**Staten Island**]')
                stats_utils.agrupamento_estilizado(df=df, 
                                                  query='price != 0 & bairro_group == "Staten Island"', 
                                                  agrupamento='bairro', 
                                                  coluna_valor='price',
                                                  porcentagem_do_total=True)


            with bronx_col:
                st.write(':orange[**Bronx**]')
                stats_utils.agrupamento_estilizado(df=df, 
                                                  query='price != 0 & bairro_group == "Bronx"', 
                                                  agrupamento='bairro', 
                                                  coluna_valor='price',
                                                  porcentagem_do_total=True)

            with analise_bairros:
                streamlit_utils.titulo_personalizado("Conclusão", 
                                                     text_align="left" ,
                                                     color="#F7A600", 
                                                     size='h3')
                st.write('''
                         Após fazer uma análise interativa em cada coluna considerando o preço, é possivel inferir
                         as seguintes suposições:

                         - O bairro Fort Wadsworth em Staten Island é o que tem maior média de preços, US\$ 800.00, 
                         porem conta somente com um anúncio no conjunto de dados.
                         - O bairro mais popular fica no Brooklyn, Williamsburg com 3919 anúncios e um total 
                         acumulado de US\$ 563.707.
                         - Manhattan possui um valor acumulado 70.55% maior que o segundo colocado que é Brooklyn.
                         - O valor acumulado de Manhattan é maior que a soma de todos os grupos de bairros em 33,15%.
                         ''')

    
        
    elif option_2 == 'Relação de preço com o tipo de espaço':         
        streamlit_utils.titulo_personalizado("Relação de preço com o tipo de espaço", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        
        with st.expander('Exibir análise'):
            streamlit_utils.titulo_personalizado("price x room_type", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            
            stats_utils.agrupamento_estilizado(df=df, 
                                               query='price != 0', 
                                               agrupamento='room_type', 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            
            bairro_grupo_filtro = st.selectbox('Bairro:', list(df['bairro_group'].unique()))
            
            stats_utils.agrupamento_estilizado(df=df.query('bairro_group == @bairro_grupo_filtro'), 
                                               query='price != 0', 
                                               agrupamento='room_type', 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            streamlit_utils.titulo_personalizado("Conclusão", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            
            st.write('''
                        - O tipo de espaço mais rentavel em todos os grupos de bairros é "Entire home/apt".
                        - Analisando os tipos de espaço considerando o grupo de bairro, o mais popular é "Private Room"
                        em quase todos os bairros. Porem, em Manhattan, o tipo mais comum é "Entire home/apt", devido 
                        Manhattan possuir a maioria dos anúncios, torna "Entire home/apt" o mais popular no conjunto de dados.
                  ''')
    
    elif option_2 == 'Relação de preço com o mínimo de noites de forma agrupada':
        streamlit_utils.titulo_personalizado("Relação de preço com o mínimo de noites de forma agrupada", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        
        st.write('''
                    Como a feature minimo_noites possui 109 valores únicos, para reduzir a cardinalidade e 
                     facilitar a análise efetuei o agrupamento da seguinte maneira.
                    
                     - Entre 1 a 3 dias
                     - Entre 3 a 7 dias
                     - Entre 1 e 2 Semanas
                     - Entre 2 Semanas e 1 Mes 
                     - Mais de 1 Mes
                     - Mais de 2 Meses
                     - Mais de 6 Meses
                     - Mais de 1 Ano
                     ''')
        with st.expander('Exibir análise'):
            streamlit_utils.titulo_personalizado("price x minimo_noites", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')

            

            df_copia['minimo_noites_grupo'] = pd.cut(df_copia['minimo_noites'],
                                                     bins=[0, 3, 7, 14, 30, 60, 180, 365 ,float('inf')],
                                                     labels=['Entre 1 a 3 dias',
                                                             'Entre 3 a 7 dias', 
                                                             'Entre 1 e 2 Semanas', 
                                                             'Entre 2 Semanas e 1 Mes',   
                                                             'Mais de 1 Mes',
                                                             'Mais de 2 Meses',
                                                             'Mais de 6 Meses',
                                                             'Mais de 1 Ano']).astype('object')


            stats_utils.agrupamento_estilizado(df=df_copia, 
                                               query='price != 0', 
                                               agrupamento=['minimo_noites_grupo'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            bairro_grupo_filtro = st.selectbox('Bairro:', list(df['bairro_group'].unique()))
            
            stats_utils.agrupamento_estilizado(df=df_copia.query('bairro_group == @bairro_grupo_filtro'), 
                                               query='price != 0', 
                                               agrupamento=['minimo_noites_grupo'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            streamlit_utils.titulo_personalizado("Conclusão", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            st.write('''
                        - O único grupo de bairro que torna-se mais barato, considerando a média, conforme maior o tempo
                        de hospedagem é o Bronx. 
                        - Manhattan é o único grupo de bairro que mantem a média acima de US\$100,00 
                        independente do periodo.

                    ''')
      
    elif option_2 == 'Relação de preço com o numero de reviews de forma agrupada':
        streamlit_utils.titulo_personalizado("Relação de preço com o numero de reviews de forma agrupada", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        st.write('''
                    Como a variável numero_de_reviews possui 394 valores únicos, para reduzir a cardinalidade e 
                     facilitar a análise efetuei o agrupamento da seguinte maneira:
                 
                    - Poucos Reviews (0-99) 
                    - Quantidade Moderada de Reviews (100-199)
                    - Alta Quantidade de Reviews (200 - 299)
                    - Quantidade Muito Alta de Reviews (300+)


                ''')
        with st.expander('Exibir análise'):
            streamlit_utils.titulo_personalizado("price x numero_de_reviews", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            
            df_copia['numero_de_reviews_grupo'] = pd.cut(df_copia['numero_de_reviews'],
                                                     bins=[0, 100, 200, 300,float('inf')],
                                                     labels=['Poucos Reviews (0-99)', 
                                                             'Quantidade Moderada de Reviews (100-199)', 
                                                             'Alta Quantidade de Reviews (200 - 299)', 
                                                             'Quantidade Muito Alta de Reviews (300+)']).astype('object')

            stats_utils.agrupamento_estilizado(df=df_copia, 
                                               query='price != 0', 
                                               agrupamento=['numero_de_reviews_grupo'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            bairro_grupo_filtro = st.selectbox('Bairro:', list(df['bairro_group'].unique()))
            stats_utils.agrupamento_estilizado(df=df_copia.query('bairro_group == @bairro_grupo_filtro'), 
                                               query='price != 0', 
                                               agrupamento=['numero_de_reviews_grupo'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
            
            streamlit_utils.titulo_personalizado("Conclusão", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
            st.write('''
                        - O grupo de bairro Broklyn é o único que quanto maior a quantidade 
                        de reviews, maior a média de valor, os demais grupos de bairros 
                        segue a lógica contrária.
                        - Em Manhattan a alta quantidade de reviews inpacta em 51.05% no preço médio.
                    ''')

        

    elif option_2 == 'Relação de preço com o a quantidade de imoveis por host de forma agrupada':

        streamlit_utils.titulo_personalizado("""
                                             Relação de preço com o a quantidade de imoveis 
                                             por host de forma agrupada""", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        
        st.write('''
                    Para reduzir a cardinalidade e  facilitar a análise efetuei o agrupamento 
                 variável calculado_host_listings_count da seguinte maneira:

                 - Somente 1
                 - Entre 2 e 5
                 - De 5 a 10
                 - De 10 a 50
                 - Mais de 50               
                ''')
        
        with st.expander('Exibir análise'):
        
           streamlit_utils.titulo_personalizado("price x calculado_host_listings_count", 
                                                text_align="left",
                                                color="#F7A600", 
                                                size='h3')
           
           df_copia['calculado_host_listings_count_group'] = pd.cut(df_copia['calculado_host_listings_count'],
                                                                    bins=[0, 1, 5, 10, 50,float('inf')],
                                                                    labels=['Somente 1', 
                                                                            'Entre 2 e 5', 
                                                                            'De 5 a 10', 
                                                                            'De 10 a 50',
                                                                            'Mais de 50']).astype('object')

           stats_utils.agrupamento_estilizado(df=df_copia, 
                                               query='price != 0', 
                                               agrupamento=['calculado_host_listings_count_group'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
           
           bairro_grupo_filtro = st.selectbox('Bairro:', list(df['bairro_group'].unique()))
           stats_utils.agrupamento_estilizado(df=df_copia.query("bairro_group == @bairro_grupo_filtro"), 
                                               query='price != 0', 
                                               agrupamento=['calculado_host_listings_count_group'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
          
           streamlit_utils.titulo_personalizado("Conclusão", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
           
           st.write('''
                    - 66,08% Possui somente 1 imovel listado.
                    - Em Manhattan e Bronx possuir mais do que 10 imóveis listados émais vantajoso, 
                    consideradando média de preços.
                    ''')
           


           
    elif option_2 == 'Relação de preço com o a variável disponibilidade_365 de forma agrupada':
        streamlit_utils.titulo_personalizado("Relação de preço com o a variável disponibilidade_365 de forma agrupada", 
                                             text_align="left",
                                             color="#0081BE", 
                                             size='h3')
        st.write('''
                    Para reduzir a cardinalidade e  facilitar a análise efetuei o agrupamento 
                 variável disponibilidade_365 da seguinte maneira:

                  - 0 Dias
                  - Entre 1 a 3 dias
                  - Entre 3 a 7 dias
                  - Entre 1 e 2 Semanas
                  - Entre 2 Semanas e 1 Mes
                  - Mais de 1 Mes
                  - Mais de 2 Meses
                  - Mais de 6 Meses
                  - 1 Ano

                ''')
        
        with st.expander('Exibir análise'):
           streamlit_utils.titulo_personalizado("price x disponibilidade_365", 
                                                text_align="left",
                                                color="#F7A600", 
                                                size='h3')
           
           df_copia['disponibilidade_365_group'] = pd.cut(df_copia['disponibilidade_365'],
                                                                    bins=[-1, 0, 3, 7, 14, 30, 60, 180, 364 , float('inf')],
                                                                    labels=['0 Dias',
                                                                            'Entre 1 a 3 dias',
                                                                            'Entre 3 a 7 dias', 
                                                                            'Entre 1 e 2 Semanas', 
                                                                            'Entre 2 Semanas e 1 Mes',   
                                                                            'Mais de 1 Mes',
                                                                            'Mais de 2 Meses',
                                                                            'Mais de 6 Meses',
                                                                            '1 Ano']).astype('object')
           stats_utils.agrupamento_estilizado(df=df_copia, 
                                               query='price != 0', 
                                               agrupamento=['disponibilidade_365_group'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
           
           bairro_grupo_filtro = st.selectbox('Bairro:', list(df['bairro_group'].unique()))
           stats_utils.agrupamento_estilizado(df=df_copia.query('bairro_group == @bairro_grupo_filtro'), 
                                               query='price != 0', 
                                               agrupamento=['disponibilidade_365_group'], 
                                               coluna_valor='price',
                                               porcentagem_do_total=True)
           
           streamlit_utils.titulo_personalizado("Conclusão", 
                                                 text_align="left",
                                                 color="#F7A600", 
                                                 size='h3')
           st.write('''
                        - 35,86\% dos imóveis não estão disponiveis para locação.
                        - Os imóveis que possuem disponibilidade de 1 ano tem a maior média 
                        de valor no conjunto de dados.
                        - Brooklyn é o único grupo de bairros que os imóveis indisponíveis 
                        tem a pior média de valor.
                    ''')


    streamlit_utils.titulo_personalizado("Dados Geoespaciais", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    
    exibir_filtros = st.checkbox('Exibir filtros', value=False)
    if exibir_filtros:
        col_filtro_price, col_filtro_localizacao,kpi_cols = st.columns(3)

        with col_filtro_localizacao:
            bairro_grupo_filtror = st.selectbox('Bairro:', ["Todos"] + list(df['bairro_group'].unique()))
            room_type_filter = st.selectbox('Tipo de espaço:', ["Todos"] + list(df['room_type'].unique()))

        with col_filtro_price:
            min_price = st.slider('Preço mínimo:', 
                                  min_value=int(df['price'].min()),
                                  max_value=int(df['price'].max()),
                                  value=int(df['price'].min()))

            max_price = st.slider('Preço máximo:',
                                  min_value=min_price,
                                  max_value=int(df['price'].max()),
                                  value=int(df['price'].max()))
            
        if bairro_grupo_filtror == 'Todos' and room_type_filter == 'Todos':
              dados_filtrados = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

        elif bairro_grupo_filtror == 'Todos'and room_type_filter != 'Todos':
              dados_filtrados = df[(df['room_type'] == room_type_filter) &
                                   (df['price'] >= min_price) & 
                                   (df['price'] <= max_price)]

        elif bairro_grupo_filtror != 'Todos' and room_type_filter == 'Todos':
             dados_filtrados = df[(df['bairro_group'] == bairro_grupo_filtror) &                                
                                  (df['price'] >= min_price) & 
                                  (df['price'] <= max_price)]

        elif bairro_grupo_filtror != 'Todos' and room_type_filter != 'Todos':
            dados_filtrados = df[(df['bairro_group'] == bairro_grupo_filtror) & 
                                 (df['room_type'] == room_type_filter) &
                                 (df['price'] >= min_price) & 
                                 (df['price'] <= max_price)]
        else:
            dados_filtrados = df
        with kpi_cols:
            st.metric('Quantidade de Anúncios', value=len(dados_filtrados), border=True)
            st.metric('Valor Médio dos Anuncios', value=round(dados_filtrados.price.mean(), 2), border=True)
    else:
        dados_filtrados = df
    st.map(dados_filtrados, latitude='latitude', longitude='longitude', color='#01aaff80')
    
    
    
    streamlit_utils.titulo_personalizado("Análise Temporal", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')

    st.write('''
             A variável ultima_review é a única no conjunto de dados que apresenta 
             valores compatíveis com uma série temporal.

             Após convertê-la para o formato de data, visto que inicialmente o tipo 
             de dado era texto, foi possível realizar as seguintes análises:            
            ''')
    

    df_copia['ultima_review'] = pd.to_datetime(df_copia['ultima_review'])
    df_copia['ultima_review_ano'] = df_copia['ultima_review'].dt.year
    df_ano_agrupado = df_copia.groupby('ultima_review_ano')[['id']].count()
    df_ano_agrupado['% do total'] = (df_ano_agrupado['id'] / df_ano_agrupado['id'].sum()*100)
    df_ano_agrupado['% do total'] = df_ano_agrupado['% do total'].apply(lambda x: f"{x:.2f}")
    df_ano_agrupado = df_ano_agrupado.rename({'id': 'count'}, axis=1)
    
    
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(df_ano_agrupado.style.highlight_max(subset=['count'], color='#59deba')\
                                          .highlight_min(subset=['count'], color='#de5959'))

    with col_2:
        st.dataframe(pd.DataFrame({'minimo': [df_copia['ultima_review'].min()],
                                   'máximo': [df_copia['ultima_review'].max()]}))
        

 


    streamlit_utils.titulo_personalizado("Gráfico de Linha: ultima review", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h3')
    fig = px.line(df.groupby(['ultima_review'])['id'].count())
    st.plotly_chart(fig)

    st.divider()

    streamlit_utils.titulo_personalizado("Análise de Dados Textuais.", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    
    col_1_analise_palavras, col_2_analise_palavras = st.columns(2)
    with col_1_analise_palavras:
        streamlit_utils.titulo_personalizado("Nuvem de palavras", 
                                         text_align="center",
                                         color="#0081BE", 
                                         size='h3')
        st.write('Nuvem de palavras gerada a partir de todo o conjunto de dados. ')
  
        nome_text = ' '.join(df['nome'].dropna().values)
        wordcloud = WordCloud(width=800, height=400, background_color="white",colormap='Blues').generate(nome_text)
        st.image(wordcloud.to_array())

    with col_2_analise_palavras:
        streamlit_utils.titulo_personalizado("20 Palavras Mais Comuns nos Nomes", 
                                         text_align="center",
                                         color="#0081BE", 
                                         size='h3')

        words = re.findall(r'\w+', nome_text.lower())
        stopwords = set(['the', 'in', 'of', 'and', 'to', 'a', 'at', 'for', 'on', 'with', 'room', 'rooms', 'nyc', 'new', 'york'])
        words = re.findall(r'\w+', nome_text.lower())
        filtered_words = [word for word in words if word not in stopwords and len(word) > 2]
        word_counts = Counter(filtered_words).most_common(20)
    
        df_words = pd.DataFrame(word_counts, columns=['Palavra', 'Frequência'])
        fig = px.bar(df_words, 
                     x='Frequência', 
                     y='Palavra', 
                     orientation='h',
                     color='Frequência',
                     color_continuous_scale='Blues')
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig)
    
    streamlit_utils.titulo_personalizado("Comparação de Palavras-Chave por Faixa de Preço", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')

    
    preco_medio = df['price'].median()
    alto_valor = df[df['price'] > preco_medio]
    baixo_valor = df[df['price'] <= preco_medio]

    col1, col2 = st.columns(2)
    with col1:
        palavras_comuns_alto_valor = tratamento_de_dados.obtem_palavras_comuns(alto_valor, top=10, stopwords=stopwords)
        df_high = pd.DataFrame(palavras_comuns_alto_valor, columns=['Palavra', 'Frequência'])
        fig = px.bar(df_high,
                     x='Frequência',
                     y='Palavra',
                     orientation='h',
                     title='Imóveis de Alto Valor',
                     color='Frequência',
                     color_continuous_scale='Blues')
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=500)
        st.plotly_chart(fig, use_container_width=True)

    with col2:  
        palavras_comuns_baixo_valor = tratamento_de_dados.obtem_palavras_comuns(baixo_valor,top=10, stopwords=stopwords)
        df_low = pd.DataFrame(palavras_comuns_baixo_valor, columns=['Palavra', 'Frequência'])
        fig = px.bar(df_low,
                     x='Frequência',
                     y='Palavra',
                     orientation='h',
                     title='Imóveis de Baixo Valor',
                     color='Frequência',
                     color_continuous_scale='Blues')
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=500)
        st.plotly_chart(fig, use_container_width=True)

    streamlit_utils.titulo_personalizado("Palavras presentes somente em imóveis de alto valor", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    palavras_comuns_alto_valor = tratamento_de_dados.obtem_palavras_comuns(alto_valor, top=5000,stopwords=stopwords)
    palavras_comuns_baixo_valor = tratamento_de_dados.obtem_palavras_comuns(baixo_valor, top=5000, stopwords=stopwords)

    set_palavras_alto = set()
    set_palavras_baixo = set()

    for palavra, _ in palavras_comuns_alto_valor:
        set_palavras_alto.add(palavra)

    for palavra, _ in palavras_comuns_baixo_valor:
        set_palavras_baixo.add(palavra)


    palavras_exclusivas_alto = set_palavras_alto - set_palavras_baixo

    frequencias_exclusivas_alto = []
    for palavra, qtd in palavras_comuns_alto_valor:
        if palavra in palavras_exclusivas_alto:
            frequencias_exclusivas_alto.append((palavra, qtd))

    nome_text = ' '.join([word * freq for word, freq in frequencias_exclusivas_alto])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(nome_text)
    st.image(wordcloud.to_array())

    st.dataframe(df[df['nome'].str.contains('2block', case=False, na=False)])
    

    streamlit_utils.titulo_personalizado("Conclusão", 
                                         text_align="left" ,
                                         color="#F7A600", 
                                         size='h3')
    st.write('''
            - Somente com a análise descritiva é difícil confirmar um padrão claro de diferença 
             entre os grupos de imóveis de baixo e alto padrão, porem os imóveis de alto padrão tem 
             uma incidencia maior de palavras que indicam luxo.
            - É comum a descrição incluir a localização do imóvel ou 
             o tipo de espaço como loft ou apartarment. 
            - Subtraindo as 5000 palavras mais frequentes nos dois conjuntos para assim obter as palavras
             únicas, é possivel identificar que os imóveis de alto padrão possuem palavras que indicam estar
             em Manhattan, como "MAG" e "UPW".
            - Outra palavra que pode indicar que é um imóvel de alto padrão é "2block", que indica
             que o imóvel está a 2 quadras de algum ponto importante ou metro.          
              
            ''')



if selected =="Análise Inferencial":
    streamlit_utils.titulo_personalizado("Análise Inferencial", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h1')

    streamlit_utils.titulo_personalizado("Hipóteses", 
                                         text_align="left",
                                         color="#0081BE", 
                                         size='h2')
    
    option_analise_inferencial = ['Existe diferença entre os preços dos imóveis de acordo com o tipo de espaço?',
                                  'Existem diferenças significativas entre o preço nos grupos de bairros?',
                                  'Existe associação entre o tipo de espaço e o bairro?'                                  
                                  ]
    
    options = st.selectbox('Opções de Análise: ', option_analise_inferencial, key=3)

    if options == 'Existe diferença entre os preços dos imóveis de acordo com o tipo de espaço?':
        st.write('''
                 Compara as médias de preços entre diferentes tipos de quarto para verificar se há diferença 
                 estatisticamente significativa
                 
                 - Hipótese Nula: Não há diferença significativa nos preços médios entre os diferentes tipos de quarto.
                 - Hipótese Alternativa: Existe uma diferença significativa nos preços médios entre os diferentes tipos de quarto.

                 ''')
      
        groups = df[df['room_type'].isin(['Entire home/apt', 'Private room'])].groupby('room_type')['price']
        group1 = groups.get_group('Entire home/apt')
        group2 = groups.get_group('Private room')

        t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
        streamlit_utils.titulo_personalizado("Resultado do Teste t", 
                                         text_align="left",
                                         color="#F7A600", 
                                         size='h3')
        
        st.write(f"Estatística t: {t_stat:.2f}")
        st.write(f"Valor p: {p_value:.4f}")
        st.write("Existe diferença significativa entre os preços" if p_value < 0.05 
                 else "Não há evidência de diferença significativa")

        st.code('''
                # Divisão do conjunto de dados por room_type diferentes agrupados por preço
                groups = df[df['room_type'].isin(['Entire home/apt', 'Private room'])].groupby('room_type')['price']
                group1 = groups.get_group('Entire home/apt')
                group2 = groups.get_group('Private room')

                # Aplicação do Teste T para comparar os dois grupos
                t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)

                # Exibindo os resultados.
                print("Resultado do Teste t")
                print(f"Estatística t: {t_stat:.2f}")
                print(f"Valor p: {p_value:.4f}")
                print("Existe diferença significativa entre os preços" if p_value < 0.05 
                else "Não há evidência de diferença significativa")
            ''') 


    if options =='Existem diferenças significativas entre o preço nos grupos de bairros?':
            numerical_var = 'price'
            categorical_var = 'bairro_group'
            anova_data = df[[numerical_var, categorical_var]].dropna()
            model = ols(f'{numerical_var} ~ C({categorical_var})', data=anova_data).fit()
            anova_resultado = sm.stats.anova_lm(model, typ=2)
            streamlit_utils.titulo_personalizado('ANOVA: "price" por "bairro_group"', 
                                         text_align="left",
                                         color="#F7A600", 
                                         size='h3')
            
            st.write('''
                    Avalia se existe diferença significativa nos preços médios entre os diferentes grupos de bairro.
                     
                    - Hipótese Nula: Não há diferença significativa nos preços médios entre os diferentes grupos de bairro.
                    - Hipótese Alternativa: Existe pelo menos uma diferença significativa nos preços médios entre os 
                     diferentes grupos de bairro.
                ''')
            
            f_value = anova_resultado['F'][0]
            p_value = anova_resultado['PR(>F)'][0]

            st.write(f'**F-value:** {f_value:.2f}, **Valor-p:** {p_value:.4f}\n\n'
                     'Há diferenças significativas entre os distritos nos preços.' if p_value < 0.05 
                     else 'Não foram encontradas diferenças significativas entre os distritos nos preços.')
            
            st.code('''
                    # Definição de variáveis para análise                  
                    numerical_var = 'price'
                    categorical_var = 'bairro_group'

                    # Aplicação do teste ANOVA - Soma de quadrados parciais 
                    anova_data = df[[numerical_var, categorical_var]].dropna()
                    model = ols(f'{numerical_var} ~ C({categorical_var})', data=anova_data).fit()
                    anova_resultado = sm.stats.anova_lm(model, typ=2)
                    f_value = anova_resultado['F'][0]
                    p_value = anova_resultado['PR(>F)'][0]

                    # Exibição do resultado   
                    print(f'**F-value:** {f_value:.2f},**Valor-p:** {p_value:.4f}'
                         'Há diferenças significativas entre os distritos nos preços.' if p_value < 0.05 
                         else 'Não foram encontradas diferenças significativas entre os distritos nos preços.')
                ''')
            
    if options == 'Existe associação entre o tipo de espaço e o bairro?':

        tabela_cruzada = pd.crosstab(df['room_type'], df['bairro_group'])
        chi2, p, _, _ = stats.chi2_contingency(tabela_cruzada)

        streamlit_utils.titulo_personalizado('Teste Qui-quadrado (room_type e bairro_group', 
                                            text_align="left",
                                            color="#F7A600", 
                                            size='h3')
        st.write('''
                    Verifica associação se existe associação significativa entre variáveis.
                 
                   - Hipótese Nula: Não há associação significativa entre o tipo de quarto e o grupo de bairro.
                   - Hipótese Alternativa: Existe uma associação significativa entre o tipo de quarto e o grupo de bairro.

                ''')
    
        st.write(f"Estatística Qui²: {chi2:.2f}")
        st.write(f"Valor p: {p:.4f}")
        st.write("Existe associação significativa" if p < 0.05 
                 else "Não há evidência de associação significativa")
        
        st.code('''

        # Cria tabela cruzada das variáveis a serem comparadas
        tabela_cruzada = pd.crosstab(df['room_type'], df['bairro_group'])
        
        # Aplica o teste qui2 
        chi2, p, _, _ = stats.chi2_contingency(tabela_cruzada)
    
        # Exibe os resultados
        print(f"Estatística Qui²: {chi2:.2f}")
        print(f"Valor p: {p:.4f}")
        print("Existe associação significativa" if p < 0.05 
                 else "Não há evidência de associação significativa")
            ''')




streamlit_utils.titulo_personalizado("NOTEBOOK JUPYTER", text_align="left" ,color="#0081BE", size='h2')        
with st.expander('Exibir Notebook'):
    streamlit_utils.load_notebook('./Notebooks/data_understanding.ipynb')



st.markdown("""
             <style>
             .scroll-button {
                 position: fixed;
                 bottom: 20px;
                 right: 20px;
                 background-color: #0081BE;
                 color: white;
                 border: none;
                 padding: 10px 20px;
                 border-radius: 5px;
                 cursor: pointer;
                 font-size: 16px;
                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
             }
             .scroll-button:hover {
                 background-color: #005f8b;
             }
             </style>
             <a href="#inicio">
                 <button class="scroll-button">Voltar ao Início.</button>
             </a>
            """,unsafe_allow_html=True)