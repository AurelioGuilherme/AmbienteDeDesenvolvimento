import re
from datetime import datetime
import datetime

def texto_valido(texto):
    """
    Valida se o texto contém apenas letras, espaços e caracteres básicos.
    """
    if texto and re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s]+", texto):
        return True
    return False

def numero_valido(numero, minimo=None, maximo=None):
    """
    Valida se o número é inteiro e opcionalmente se está dentro de um intervalo.
    """
    try:
        valor = int(numero)
        if minimo is not None and valor < minimo:
            return False
        if maximo is not None and valor > maximo:
            return False
        return True
    except ValueError:
        return False

def numero_decimal_valido(numero):
    """
    Valida se o número é decimal ou inteiro.
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False

def data_valida(data, formato="%Y-%m-%d"):
    """
    Valida se a data está no formato especificado (padrão: YYYY-MM-DD).
    """
    try:
        datetime.strptime(data, formato)
        return True
    except ValueError:
        return False