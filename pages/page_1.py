import streamlit as st
from streamlit_option_menu import option_menu
from utils import streamlit_utils, layout_indicium, stats_utils
import pandas as pd
import plotly.express as px


layout_indicium.layout_custom()
df = streamlit_utils.carrega_dados_cache()
streamlit_utils.titulo_personalizado("Data Understanding", color="#0081BE")
st.divider()

# Menu horizontal
selected = option_menu(menu_title=None,
                       options=["Descrição dos Dados",
                                "Análise Descritiva",
                                "Análise Inferencial",
                                "Resumo"],
                       icons=["list-task", "list-task", "list-task", "list-task"],
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
    streamlit_utils.titulo_personalizado("Dados Faltantes", text_align="left" ,color="#0081BE", size='h2')
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


    streamlit_utils.titulo_personalizado("Dados Duplicados", text_align="left" ,color="#0081BE", size='h2')
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


    streamlit_utils.titulo_personalizado("Análise de Dados Contínuos", text_align="left" ,color="#0081BE", size='h2')
    st.write('''
             Para analisar os dados contínuos, selecionarei as seguintes colunas:
              :orange[price], :orange[minimo_noites], :orange[numero_de_reviews], :orange[reviews_por_mes], 
              :orange[calculado_host_listings_count], :orange[disponibilidade_365].
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


    streamlit_utils.titulo_personalizado("Valores Discrepantes", text_align="left" ,color="#0081BE", size='h3')
    with st.expander('Gráficos Boxplot'):
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                streamlit_utils.titulo_personalizado("price", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='price')
                st.plotly_chart(fig)

            with col_2:
                streamlit_utils.titulo_personalizado("minimo_noites", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='minimo_noites')
                st.plotly_chart(fig)
            with col_3:
                
                streamlit_utils.titulo_personalizado("numero_de_reviews", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='numero_de_reviews')
                st.plotly_chart(fig)

            col_4, col_5, col_6 = st.columns(3)
            with col_4:
                streamlit_utils.titulo_personalizado("reviews_por_mes", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='reviews_por_mes')
                st.plotly_chart(fig)

            with col_5:
                streamlit_utils.titulo_personalizado("calculado_host_listings_count", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='calculado_host_listings_count')
                st.plotly_chart(fig)

            with col_6:
                streamlit_utils.titulo_personalizado("disponibilidade_365", text_align="left" ,color="#0081BE", size='h3')
                fig = px.box(df, y='disponibilidade_365')
                st.plotly_chart(fig)

    with st.expander('Gráficos Histograma'):
            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                streamlit_utils.titulo_personalizado("price", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='price', nbins=50)
                st.plotly_chart(fig)

            with col_2:
                streamlit_utils.titulo_personalizado("minimo_noites", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='minimo_noites', nbins=50 )
                st.plotly_chart(fig)
            with col_3:
                
                streamlit_utils.titulo_personalizado("numero_de_reviews", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='numero_de_reviews', nbins=50)
                st.plotly_chart(fig)

            col_4, col_5, col_6 = st.columns(3)
            with col_4:
                streamlit_utils.titulo_personalizado("reviews_por_mes", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='reviews_por_mes', nbins=50)
                st.plotly_chart(fig)

            with col_5:
                streamlit_utils.titulo_personalizado("calculado_host_listings_count", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='calculado_host_listings_count', nbins=50)
                st.plotly_chart(fig)
                
            with col_6:
                streamlit_utils.titulo_personalizado("disponibilidade_365", text_align="left" ,color="#0081BE", size='h3')
                fig = px.histogram(df, x='disponibilidade_365')
                st.plotly_chart(fig)
        
    st.write('''
                Ao analisar os gráficos apresentados acima, é possível comprovar a presença de 
                outliers nos dados. Para compreender melhor essas discrepâncias, será realizada 
                uma análise detalhada de cada coluna individualmente.
             ''')
    st.divider()
    
    
    streamlit_utils.titulo_personalizado("Exploração Individual das Variáveis ", text_align="left" ,color="#0081BE", size='h3')        
    
    
    st.write('''
                 :blue-background[**price**]
            ''')
    with st.expander('Exibir Análise'):
        st.write('**price menor do que 1**')
        st.dataframe(df.query('price < 1'))
        st.write('''
                 - São imóveis diferentes de acordo com a latitude e longitude.
                 - Há imóveis que pertencem ao mesmo proprietário neste grupo de dados.

                 :red[**Esses valores serão tratados na etapa de Data Preparation, podendo ser removidos ou preenchidos**]
             
                 ''')
        st.divider()


        stats_utils.exibe_analise_q3_outliers(df, df.price)


    st.write('''
                :blue-background[**minimo_noites**]
            ''')
    with st.expander('Exibir Análise'):
        stats_utils.exibe_analise_q3_outliers(df, df.minimo_noites)


    st.write('''
                :blue-background[**numero_de_reviews**]
            ''')
    with st.expander('Exibir Análise'):
        stats_utils.exibe_analise_q3_outliers(df,df.numero_de_reviews)
    
    
    st.write('''
                :blue-background[**reviews_por_mes**]
            ''')
    with st.expander('Exibir Análise'):
        stats_utils.exibe_analise_q3_outliers(df, df.reviews_por_mes)


    st.write('''
                :blue-background[**calculado_host_listings_count**]
            ''')
    with st.expander('Exibir Análise'):
        stats_utils.exibe_analise_q3_outliers(df, df.calculado_host_listings_count)
    
    
    st.write('''
                :blue-background[**disponibilidade_365**]
            ''')
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

             - :red[**Neste momento**] Caso seja constado que a performance do modelo é insulficiente 
             na etapa de evaluation, pode ser considerado algum tratamento de dados adicional nos valores outliers
             para a melhoria do modelo. 
             ''')
    st.divider()

    streamlit_utils.titulo_personalizado("Análise de Dados Categóricos", text_align="left" ,color="#0081BE", size='h2')







if selected =="Resumo":
    streamlit_utils.titulo_personalizado("Resumo", text_align="left" ,color="#0081BE", size='h1')        


    streamlit_utils.titulo_personalizado("NOTEBOOK JUPYTER", text_align="left" ,color="#0081BE", size='h2')        
    with st.expander('Exibir Notebook'):
        streamlit_utils.load_notebook('./Notebooks/data_understanding.ipynb')