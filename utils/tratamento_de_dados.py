import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import re


class TransformData:
    """
    Classe para realizar pré-processamento de dados para precificação dos imóveis
    """

    def __init__(self,df, cat_cols, num_cols, treino=True):
        """
        Inicializa a classe com os dados e configurações necessárias. 

               Parâmetros:
        -------------------------------------------------------
        df : pandas.DataFrame - Conjunto de dados de imóveis
        cat_cols : list       - Nomes das colunas categóricas.
        num_cols : list       - Nomes das colunas numéricas.  
        -------------------------------------------------------        
        """

        self.df = df
        self.cat_cols = cat_cols
        self.num_cols = num_cols
        self.treino = treino
        


    def _corrige_data(self):
        """
        Processa a coluna `ultima_review`:
        1. Converte para datetime.
        2. Cria intervalos semestrais (`ultima_review_semestre`).
        3. Trata valores ausentes como 'anuncio_sem_review'.

        """

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

        # Seleciona host_ids que possuem incossitencias identificadas na etapa de business understanding
        host_ids_com_erros_ou_price_0 = [1641537, 131697576, 8993084, 2787, 101970559, 86327101, 15787004]

        # Subtrai a contagem de 'calculado_host_listings_count'
        self.df.loc[self.df['host_id'].isin(host_ids_com_erros_ou_price_0), 'calculado_host_listings_count'] -= 1 
         
        if self.treino:
            # Seleciona apenas os dados onde price é maior que 0
            self.df = self.df[self.df['price'] > 0]


    def _fill_na(self):
        '''
        Trata valores ausentes:
        1. Preenche `reviews_por_mes` com 0.
        2. Cria a flag `valor_preenchido` (1 se o valor foi imputado, 0 caso contrário).
        '''

        self.df = self.df.copy()
        self.df.loc[:, 'reviews_por_mes'] = self.df['reviews_por_mes'].fillna(0)
        # Cria coluna valor_preenchido para  
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
       

def obtem_palavras_comuns(df: pd.DataFrame, column: str='nome', top:int=20, stopwords:list=None):
    text = ' '.join(df[column].dropna().values)
    words = re.findall(r'\w+', text.lower())
    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]
    return Counter(filtered_words).most_common(top)