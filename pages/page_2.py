from utils import streamlit_utils,layout_indicium
from utils import tratamento_de_dados
import streamlit as st
import pandas as pd
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


layout_indicium.layout_custom()
df = streamlit_utils.carrega_dados_cache()


streamlit_utils.titulo_personalizado("Data Preparation", color="#0081BE", anchor='inicio_data_preparation')
st.divider()
streamlit_utils.titulo_personalizado("Abordagem de Experimentação", color="#0081BE", size='h2', text_align='left')
st.write('''
            Esta etapa foi totalmente pensada em experimentação, por este motivo criei features categóricas de variáveis 
            contínuas, visto que algumas transformações podem não fazer tanto sentido.

            O processo de tratamento de dados foi detalhado no arquivo Jupyter Notebook 
            :orange[data_preparation.ipynb]. Além disso, uma classe chamada :orange[TransformData] foi implementada no 
            arquivo :orange[tratamento_de_dados.py], a qual encapsula todas as etapas de 
            tratamento, automatizando todo o processo de preparação dos dados.
         
            Com esta abordagem potencializa a experimentação de diferentes features, visto que posso escolher usar 
            features categorizadas de dados contínuos na etapa da modelagem, verificar a performance e se necessário 
            mudar a abordagem.
         
            Esta abordagem também possibilita a adição de novos tratamentos e criação de novas features de forma mais simples,
            basta adcionar o tratamento adicional a classe como um novo método e incluir no pipeline no método `fit_transform`.
         
            Para instanciar a classe eu preciso fornecer os parâmetros :orange[df] que corresponde ao conjunto de dados,
            :orange[cat_cols] que  corresponde a uma lista das features categóricas que desejo experienciar, 
            e :orange[num_cols] que corresponde as minhas features númericas.

            Assim sendo, tenho disponível as seguintes features para escolher na etapa da modelagem:
         
            **Features_numericas**
            - numero_de_reviews
            - reviews_por_mes
            - calculado_host_listings_count
            - latitude
            - longitude 
            - minimo_noites        

            **features_categoricas**
            - room_type
            - bairro_group
            - bairro
            - minimo_noites_categorico
            - disponibilidade_365_categorico
            - ultima_review_semestre
            - valor_preenchido        

            As demais features, como nome, host_name, id e host_id são descritivas e podem não ser relevantes para o modelo,
          desta forma não utilizei-as nesta etapa.
            ''')
st.divider()

streamlit_utils.titulo_personalizado("1ª experimentação - Abordagem com Features Categóricas", color="#0081BE", size='h2', text_align='left')

st.write('''
            Em minha primeira experimentação decidi por uma abordagem baseda em mais features categoricas assim removendo 
            variáveis contínuas de origem, foram selecionadas as seguintes features: 
           
            
            **Features_numericas**
            - numero_de_reviews
            - reviews_por_mes
            - calculado_host_listings_count
            

            **features_categoricas**
            - room_type
            - bairro_group
            - minimo_noites_categorico
            - disponibilidade_365_categorico
            - ultima_review_semestre
            - valor_preenchido
         ''')

         

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

transformer = tratamento_de_dados.TransformData(df, features_categoricas, features_numericas)
X, y = transformer.fit_transform()

st.write('Após aplicar a classe, os dados foram separados em X e y sendo transformados e organizados da seguinte maneira:')
st.dataframe(X)

with st.expander('Exibir Classe TransformData'):
    st.code("""
            import pandas as pd

    Class TransformData:
       '''
       Classe para realizar pré-processamento de dados para precificação dos imóveis
       '''

       def __init__(self,df, cat_cols, num_cols):
           '''
           Inicializa a classe com os dados e configurações necessárias. 

                  Parâmetros:
           -------------------------------------------------------
           df : pandas.DataFrame - Conjunto de dados de imóveis
           cat_cols : list       - Nomes das colunas categóricas.
           num_cols : list       - Nomes das colunas numéricas.  
           -------------------------------------------------------        
           '''

           self.df = df
           self.cat_cols = cat_cols
           self.num_cols = num_cols


       def _corrige_data(self):
           '''
           Processa a coluna `ultima_review`:
           1. Converte para datetime.
           2. Cria intervalos semestrais (`ultima_review_semestre`).
           3. Trata valores ausentes como 'anuncio_sem_review'.

           '''

           # Converte a coluna 'ultima_review' para datetime
           self.df['ultima_review'] = pd.to_datetime(self.df['ultima_review'])

           # Define a menor e a maior data e ajusta o intervalo de datas
           min_date = self.df['ultima_review'].min()
           max_date = self.df['ultima_review'].max()
           min_date -= pd.DateOffset(months=2)
           max_date += pd.DateOffset(months=5)

           # Cria intervalos de 6 meses
           bins = pd.date_range(start=min_date, end=max_date, freq='6ME')

           # Gera os labels para os intervalos porem exclui o ultimo label da lista
           labels = []
           for b in bins:
               if b.month == 1:
                   labels.append(f'{b.year}-1-semestre')
               else:
                   labels.append(f'{b.year}-2-semestre')
           labels.pop()

           # Cria a coluna categórica 'ultima_review_semestre' e preenche os valores ausentes
           self.df['ultima_review_semestre'] = pd.cut(self.df['ultima_review'], bins=bins, labels=labels)
           self.df['ultima_review_semestre'] = self.df['ultima_review_semestre'].cat.add_categories('anuncio_sem_review')
           self.df[['ultima_review','ultima_review_semestre']] = self.df[['ultima_review','ultima_review_semestre']].fillna('anuncio_sem_review')
           
       
       def _cria_grupos(self):
           '''
             Cria variáveis categóricas a partir de `minimo_noites` e `disponibilidade_365`.
           '''

           # Criei as bins representando o intervalo 
           bins = [0, 3, 7, 14, 30, 60, 180, 365 ,float('inf')]

           # Criei as labels para cada intervalo
           labels = ['Entre_1_a_3_Dias',
                     'Entre_3_a_7_Dias', 
                     'Entre_1_e_2_Semanas', 
                     'Entre_2_Semanas_e_1_Mes',   
                     'Entre_1_Mes_e_2_Meses',
                     'Entre_1_Meses_e_6_Meses',
                     'Entre_6_Meses_e_1_Ano',
                     'Mais_de_1_Ano']

           # Criei a coluna de agrupamento minimo_noites de forma categórica
           self.df['minimo_noites_categorico'] = pd.cut(self.df['minimo_noites'], bins=bins,labels=labels).astype('object')


           # Criei as bins representando o intervalo 
           bins = [-1,0, 3, 7, 14, 30, 60, 180, 364 , float('inf')]

           # Criei as labels para cada intervalo
           labels = ['0_Dias',
                     'Entre_1_a_3_Dias',
                     'Entre_3_a_7_Dias', 
                     'Entre_1 e 2 Semanas', 
                     'Entre_2_Semanas_e_1_Mes',   
                     'Entre_1_Mes_e_2_Meses',
                     'Entre_2_Meses_e_6_Meses',
                     'Entre_6_Meses_e_1_Ano',
                     '1_Ano']

           # Criei a coluna de agrupamento disponibilidade_365 de forma categórica
           self.df['disponibilidade_365_categorico'] = pd.cut(self.df['disponibilidade_365'], bins=bins, labels=labels)

       
       def _corrige_preco_e_qtd_host_listing(self):
           '''
           Corrige dados inconsistentes em `price` e `calculado_host_listings_count`:
           1. Ajusta `calculado_host_listings_count` para `host_ids` específicos.
           2. Remove registros com `price` <= 0.
           '''

           host_ids_com_erros_ou_price_0 = [1641537, 131697576, 8993084, 2787, 101970559, 86327101, 15787004]
           self.df.loc[self.df['host_id'].isin(host_ids_com_erros_ou_price_0), 'calculado_host_listings_count'] -= 1      
           self.df = self.df[self.df['price'] > 0]

       def _fill_na(self):
           '''
           Trata valores ausentes:
           1. Preenche `reviews_por_mes` com 0.
           2. Cria a flag `valor_preenchido` (1 se o valor foi imputado, 0 caso contrário).
           '''
           self.df = self.df.copy()
           self.df.loc[:, 'reviews_por_mes'] = self.df['reviews_por_mes'].fillna(0)
           self.df.loc[:, 'valor_preenchido'] = self.df['reviews_por_mes'].apply(lambda x: 1 if x == 0 else 0)

       def _selecao_de_features(self):
           ''' 
           Seleciona as features finais e o target:
           - Features: Combinação de `num_cols` e `cat_cols`.
           - Target: Coluna `price`.
           '''

           X = self.df[self.num_cols + self.cat_cols]
           y = self.df['price']

           return X, y

       def fit_transform(self):
           '''
           Executa o pipeline completo de pré-processamento:
           1. Correção de datas.
           2. Criação de grupos categóricos.
           3. Correção de outliers.
           4. Tratamento de valores ausentes.
           5. Seleção final de features.
               
               Retorna:
           --------------------------------------------------------
           X : pandas.DataFrame - Features prontas para modelagem.
           y : pandas.Series    - Target (`price`).
           --------------------------------------------------------
           '''
           
           self._corrige_data()
           self._cria_grupos()
           self._corrige_preco_e_qtd_host_listing()
           self._fill_na()
           X, y = self._selecao_de_features()
           return X, y
        """)



streamlit_utils.titulo_personalizado("Divisão dos Dados Para Treino, Teste e Calibração", 
                                     text_align='left',
                                     color="#0081BE", 
                                     size='h2')

st.write('''

        A divisão de dados será feita em 2 conjuntos, treino e teste com a seguinte divisão:
         
         - **Treino**: 70\% dos dados
         - **Teste** : 30\% dos dados
         
        ''')
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)


streamlit_utils.titulo_personalizado("Enconding e Padronização", 
                                     text_align='left', 
                                     color="#0081BE", 
                                     size='h2')

transformer = ColumnTransformer(
    transformers=[
        # Padronização features numéricas com RobustScaler
        ('num', RobustScaler(), features_numericas),
        # Encondingg das features categóricas com OneHotEncoder
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), features_categoricas)
    ])

transformer.fit(X_train)

st.write('''
           O algoritmo escolhido para a padronização dos dados numéricos foi o :green[RobustScaler], 
         devido à sua abordagem de padronização ter capacidade de atuar em conjuntos de dados com outliers.
         Para Enconding das variáveis categóricas, optei pelo :green[OneHotEncoder].

         Para facilitar a implementação, também foi utilizado o ColumnTransformer, padronizando o preprocessamento de dados.
        ''')

st.write(f'''
            Resultando nas seguintes dimensões dos dados:
            - Treino: {transformer.transform(X_train).shape[0]} linhas {transformer.transform(X_train).shape[1]} features
            - Teste: {transformer.transform(X_test).shape[0]} linhas {transformer.transform(X_test).shape[1]} features.
         ''')

st.divider()
st.write('**Dados após as transformações**')
st.dataframe(pd.DataFrame(transformer.transform(X_train).toarray(), columns=transformer.get_feature_names_out()))

with st.expander('Exibir o código da implementação:'):
    st.code('''
                # Leitura dos dados originais
                df = df_copia.copy()

                # Definição das features numericas
                features_numericas = ['numero_de_reviews',
                                      'reviews_por_mes',
                                      'calculado_host_listings_count']

                # Definição das features categoricas 
                features_categoricas = [
                    'room_type',
                    'bairro_group',
                    'minimo_noites_categorico',
                    'disponibilidade_365_categorico',
                    'ultima_review_semestre',
                    'valor_preenchido']

                # Instaciamento e execução da classe para limpeza dos dados e divisão em X e y
                cleaner_data = TransformData(df, features_categoricas, features_numericas)
                X, y  = cleaner_data.fit_transform()

                # Divisão dos dados para treino, calibração e teste
                X_train, X_temp, y_train, y_temp = train_test_split(X, y, train_size=0.6, random_state=42)
                X_calib, X_test, y_calib, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

                # Criação do pipeline de encoding e padronização
                transformer = ColumnTransformer(
                    transformers=[
                        # Padronização features numéricas com RobustScaler
                        ('num', RobustScaler(), features_numericas),
                        # Encondingg das features categóricas com OneHotEncoder
                        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), features_categoricas)
                    ])

                # Treinando o pipeline de enconding e padronização
                transformer.fit(X_train)

                # Aplicando as transformações ao conjunto de dados.    
                X_train = transformer.transform(X_train)
                X_test = transformer.transform(X_test)
                X_calib = transformer.transform(X_calib)

                            ''')
    
streamlit_utils.titulo_personalizado("Jupyter Notebook", 
                                    text_align='left',
                                     color="#0081BE", 
                                     size='h2')

st.write('A baixo você pode conferir o Jupyter Notebook que detalha o processo de desenvolvimento da etada Data Preparation.')

with st.expander('**Notebook Jupyter**'):
    streamlit_utils.titulo_personalizado("Data Preparation Notebook", 
                                         size="h3", 
                                         text_align='left',
                                         color="#F7A600")

    streamlit_utils.load_notebook('./Notebooks/data_preparation.ipynb')

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
             <a href="#inicio_data_preparation">
                 <button class="scroll-button">Voltar ao Início.</button>
             </a>
            """,unsafe_allow_html=True)