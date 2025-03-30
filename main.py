import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv

dadosBcb = requestApiBcb('20191')

salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";", ".")
#print(dadosBcb)
#dadosBcb.to_csv("meiosPagamentosTri.csv", sep=';', decimal='.')