import pandas as pd
import sqlite3

from sqlalchemy import create_engine


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


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """
    Função para salvar um DataFrame em um banco de dados SQLite.

    Parâmetros:
    df (pd.DataFrame): O DataFrame que será salvo.
    nome_banco (str): O nome do arquivo do banco de dados SQLite.
    nome_tabela (str): O nome da tabela onde os dados serão salvos.
    Retorna:
    None: A função apenas salva os dados no banco de dados e não retorna nenhum valor.
    Exemplo:
    salvarSQLite(df, 'dados.db', 'tabela_dados')

    """

    Conn = sqlite3.connect(nome_banco)

    # converter o meu df para arquivo sql.
    df.to_sql(nome_tabela, Conn, if_exists="replace", index=False)

    Conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):
    """
    Função para salvar um DataFrame em um banco de dados MySQL.

    Parâmetros:
    df (pd.DataFrame): O DataFrame que será salvo.
    nome_banco (str): O nome do banco de dados MySQL.
    nome_tabela (str): O nome da tabela onde os dados serão salvos.

    Retorna:
    None: A função apenas salva os dados no banco de dados e não retorna nenhum valor.

    Exemplo:
    salvarMySQL(df, 'dados', 'tabela_dados')

    """

    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return
