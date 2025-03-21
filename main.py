import requests
import pandas as pd


def requestApiBcb(data):
    
    """
    funcao para extrair os dados dos meios de pagamentos trismestral do Banco Central
    Paramentos data - string
    """
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"

    req  = requests.get(url)

    dados = req.json()

    df = pd.json_normalize(dados['value'])

    return print(df)

requestApiBcb('20191')


