import requests
import pandas as pd


def requestApiBcb(data: str) -> pd.DataFrame:
    """
    Função para extrair os dados dos meios de pagamentos trimestrais do banco central

    Parâmetros:
    data - string - aaaat (Exemplo: 20191)

    Saída:
    DataFrame - Estrutura de dados do pandas
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"

    req = requests.get(url)
    # print(req.status_code)
    # print(req.json())
    dados = req.json()

    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])
    return df


# dadosBCB = requestApiBcb('20191')
# print(dadosBCB.info())

print(requestApiBcb("20191"))
