import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(
    df: pd.DataFrame, 
    nome_arquivo: str, 
    separador: str, 
    decimal: str
):
    """
    **Função para salvar um DataFrame em um arquivo CSV**

    *Parâmetros:*
        - df (pd.DataFrame): DataFrame a ser salvo;
        - nome_arquivo (str): Caminho do arquivo CSV;
        - separador (str): Delimitador dos campos no CSV;
        - decimal (str): Caractere usado para separação decimal;
    
    *Exemplo:* 
        - salvarCsv(dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ";", ".")

    *Saída:*
        - None (A função apenas salva o arquivo e não retorna valor)
    """

    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)

    return


def salvarSQLite(
    df: pd.DataFrame, 
    nome_banco: str, 
    nome_tabela: str
):
    """
    **Função para salvar um DataFrame em um banco de dados SQLite**

    *Parâmetros:*
        - df (pd.DataFrame): DataFrame a ser salvo;
        - nome_banco (str): Caminho do banco de dados SQLite;
        - nome_tabela (str): Nome da tabela onde os dados serão inseridos;

    *Exemplo:*
        - salvarSQLite(dadosBcb, "etlBCB/src/datasets/etlbcb.db", "meios_pagamentos_tri")

    *Saída:*
        - None (A função apenas salva o arquivo e não retorna valor)
    """
    Conn = sqlite3.connect(nome_banco)

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
    **Função para salvar um DataFrame em um banco de dados MySQL**

    *Parâmetros:*
        - df (pd.DataFrame): DataFrame a ser salvo.
        - usuario (str): Nome do usuário do banco de dados.
        - senha (str): Senha do banco de dados.
        - host (str): Endereço do servidor do banco de dados.
        - nome_banco (str): Nome do banco de dados.
        - nome_tabela (str): Nome da tabela onde os dados serão inseridos.
    
    *Exemplo:* 
        - salvarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamentos_tri")

    Saída:
        - None (A função apenas salva o arquivo e não retorna valor)
    """
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return
