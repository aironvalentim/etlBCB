# etlBCB

# Estrutura do Projeto
## A estrutura do projeto é organizada da seguinte maneira:


├── src/
│   ├── extractTransform.py  		  # Função para extrair dados da API do Banco Central
│   ├── load.py            			  # Função para salvar os dados extraídos em CSV
│   └── main.py             			# Arquivo principal que executa a extração e carga dos dados
├── datasets/
│   └── meiosPagamentosTri.csv  	# Arquivo CSV gerado com os dados extraídos
└── README.md               		  # Documentação do projeto



# Dependências
O projeto requer as seguintes bibliotecas:

requests: Para fazer requisições à API do Banco Central.

pandas: Para manipulação de dados e exportação para CSV.

# 📊 Dados sobre Estabelecimentos, Transações e Tarifas de Cartões de Pagamento

## 📌 Visão Geral
Este repositório contém informações detalhadas sobre a aceitação de cartões de pagamento, incluindo estabelecimentos credenciados, tarifas de intercâmbio, taxas de desconto, terminais de autoatendimento (ATM), volumetria de operações e programas de recompensa.

Os dados são atualizados trimestralmente e ficam disponíveis 90 dias após o final de cada trimestre.

---
| **Coluna**                        | **Tipo**   | **Descrição**    | **Exemplo**              |                                                                                                                                                                                             
|-----------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| **trimestre**                     | texto      | Data-base de referência no formato AAAAT (Ano e Trimestre).                                                                                                                                                 | "202503"                 |
| **funcaoCartao**                  | texto      | Função do cartão de pagamento, especificando a forma de pagamento escolhida pelo portador e aceita pelo estabelecimento credenciado.                                                                         | "Crédito"                |
| **bandeira**                      | texto      | Bandeira que detém os direitos e deveres da marca estampada no cartão, incluindo as bandeiras pertencentes aos emissores.                                                                                     | "Visa"                   |
| **produto**                       | texto      | Categoria atribuída a um cartão de pagamento, com um conjunto de vantagens que o diferenciam, conforme o perfil do portador.                                                                                  | "Premium"                |
| **modalidade**                    | texto      | Define se o cartão de crédito é emitido em parceria com comerciante ou entidade.                                                                                                                             | "Convênio"               |
| **tarifaAnuidadeMedia**           | decimal    | Média das tarifas de anuidade praticadas pelo emissor, calculada pela receita trimestral das tarifas de anuidade dividida pelo número de cartões com cobrança de tarifa.                                           | 120.50                   |
| **qtdPontosAcumulados**           | decimal    | Estoque de pontos creditados nas contas dos portadores no final do trimestre, considerando pontos adquiridos no trimestre, menos os pontos transferidos ou expirados.                                           | 1,250.00                 |
| **qtdPontosAdquiridos**           | decimal    | Quantidade de pontos acumulados pelos portadores de cartões no âmbito dos programas de recompensa, no decorrer do trimestre.                                                                                   | 500.00                   |
| **qtdPontosConvertidos**          | decimal    | Quantidade de pontos transferidos para programas de fidelidade/recompensa de terceiros no decorrer do trimestre.                                                                                             | 150.00                   |
| **qtdPontosExpirados**            | decimal    | Quantidade de pontos expirados no decorrer do trimestre, no âmbito dos programas de recompensa do emissor.                                                                                                     | 50.00                    |
| **valorGastoProgramaRecompra**    | decimal    | Valor total gasto no trimestre pelo emissor para repasses em programas de fidelidade/recompensa de terceiros, com aquisição de bens ou serviços pelos portadores de cartões.                                      | 100,000.00               |

---

