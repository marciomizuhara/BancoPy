from datetime import date
from datetime import datetime


# Definir formatação da data para string
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


# Definir formatação da string para data
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


# Definir formatação de float para o formato da currency
def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'







