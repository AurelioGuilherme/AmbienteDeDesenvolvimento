import pandas as pd
import numpy as np
import streamlit as st


def retorna_quartis(coluna: pd.Series):
    q1 = coluna.quantile(0.25)
    q2 = coluna.quantile(0.50)
    q3 = coluna.quantile(0.75)
    q4 = coluna.max()
    
    return q1, q2, q3, q4

def retorna_limites_outliers(coluna: pd.Series):
    q1, q2, q3, q4 = retorna_quartis(coluna)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return lower_bound, upper_bound, q1, q2, q3, q4

def exibe_analise_q3_outliers(df: pd.DataFrame, coluna: pd.Series):
    
    lower_bound, upper_bound, q1, q2, q3, q4 = retorna_limites_outliers(coluna)
    st.write('**Dados no terceiro quartil (Q3)**')
    st.write(f'O ponto de corte do terceiro quartil é {q3}')

    st.dataframe(df[df[coluna.name] > q3])
    qtd_q3 = len(df[df[coluna.name] > q3])
    st.write(f'- Há {qtd_q3} registros no terceiro quartil (Q3) da coluna :orange[{coluna.name}].')
    st.divider()

    st.write('**Outliers**')
    st.dataframe(df[df[coluna.name] > upper_bound])

    qtd_outliers = len(df[df[coluna.name] > upper_bound])
    st.write(f'''
             - O ponto de corte do valor mínimo da coluna :orange[{coluna.name}] considerado outlier  é {lower_bound}
             - O ponto de corte do valor máximo da coluna :orange[{coluna.name}] considerado outlier  é {upper_bound}
             - Há {qtd_outliers} registros considerados outliers :orange[{coluna.name}].
             ''')


