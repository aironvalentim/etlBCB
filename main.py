import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL


dadosBcb = requestApiBcb("20191")

#print(dadosBcb) #Exibe o DataFrame retornado pela API do Banco Central (extraxão e transformação)

#salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";", ".") #Salva o DataFrame em um arquivo CSV;

salvarSQLite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri") #Salva o DataFrame em um banco de dados SQLite;

#salvarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamentos_tri")
