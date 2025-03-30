import pandas as pd 

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    
    """
    Função para salvar um DataFrame em um arquivo CSV.

    Parâmetros:
    df (pd.DataFrame): O DataFrame que será salvo.
    nome_arquivo (str): O nome do arquivo CSV a ser criado.
    separador (str): O caractere usado como separador de colunas no arquivo CSV.
    decimal (str): O caractere usado para separar os valores decimais no arquivo CSV.

    Retorna:
    None: A função apenas salva o arquivo e não retorna nenhum valor.
    """
    
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return