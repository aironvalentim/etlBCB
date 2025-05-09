import requests
import pandas as pd


def requestApiBcb(
    data: str
) -> pd.DataFrame:
    """
    **Função para extrair os dados dos meios de pagamentos trimestrais do Banco Central**

    *Parâmetros:*
        - data (str): Trimestre desejado no formato 'aaaat' (ano e trimestre);
    
    *Exemplo:* 
        - requestApiBcb("20221") - primeiro trimestre de 2022

    *Saída:*
        - pd.DataFrame: Estrutura de dados do pandas, contendo os registros retornados pela API, já com a coluna 'datatrimestre' convertida para datetime.
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"

    req = requests.get(url) #Faz a requisição GET para a URL da API do Banco Central

    #print(req.status_code) #Retorna o código de status da requisição (200 = sucesso, 404 = não encontrado, etc.)
    
    #print(req.json()) #Retorna o conteúdo da resposta em formato JSON (dados crus)
    
    dados = req.json() #Converte o conteúdo JSON em um dicionário Python

    #print(dados) #Exibe o dicionário Python

    df = pd.json_normalize(dados["value"]) #Converte o dicionário em um DataFrame do pandas, normalizando os dados aninhados
    
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"]) #Converte a coluna 'datatrimestre' para o formato datetime do pandas
    
    return df




