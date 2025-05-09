# etlBCB

# Introdução

A turma 34 em Análise e Desenvolvimento de Sistemas do SENAC está aprendendo, na disciplina de Data Science, os conceitos de ETL (Extract/extrair, transform/transformar e load/carregar). 

Nas últimas 2 semanas pudemos desenvolver práticas em sala para adquirir consistência de conhecimento, conseguindo criar as funções extactTransform (ET) e load (L) com o auxílio do professor Marcos Mialaret. Estas, por sua vez, possuem docstring para elucidação de execução.

## Dicionário de Dados

### Meios de Pagamentos Trimestrais
Conjunto de informações sobre operações com cartões de pagamento e de transferências de crédito (boletos bancários, cartões de crédito e débito, transferências bancárias). Dados ficam disponíveis 90 dias após o final do trimestre.

### Parâmetros

| Nome         | Tipo     | Título   | Descrição                                                                 |
|--------------|----------|----------|---------------------------------------------------------------------------|
| trimestre    | texto    | Trimestre| Os dados serão trazidos a partir do tri forn como parâmetro no form AAAAT. |
| $format      | texto    | $format  | Tipo de conteúdo que será retornado.                                      |
| $select      | texto    | $select  | Propriedades que serão retornadas.                                        |
| $filter      | texto    | $filter  | Filtro de seleção de entidades. Exemplo: Nome eq 'João'.                  |
| $orderby     | texto    | $orderby | Propriedades para ordenação das entidades. Exemplo: Nome asc, Idade desc. |
| $skip        | inteiro  | $skip    | Índice (maior ou igual a zero) da primeira entidade que será retornada.   |
| $top         | inteiro  | $top     | Número máximo (maior que zero) de entidades que serão retornadas.        |


### Resultado

| Nome                         | Tipo     | Título                        | Descrição                                                                                                           |
|------------------------------|----------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|
| datatrimestre                | texto    | Trimestre                     |                                                                                                                     |
| valorPix                     | decimal  | Valor Pix                     | Volume financeiro (R$ milhões) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. |
| valorTED                     | decimal  | Valor TED                     | Montante financeiro (R$ milhões) trimestral transferido por meio de TED.                                           |
| valorTEC                     | decimal  | Valor TEC                     | Montante financeiro (R$ milhões) trimestral transferido por meio de TEC.                                           |
| valorCheque                  | decimal  | Valor Cheque                  | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente.           |
| valorBoleto                  | decimal  | Valor Boleto                  | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente.           |
| valorDOC                     | decimal  | Valor DOC                     | Montante financeiro (R$ milhões) trimestral transferido por meio de DOC.                                           |
| valorCartaoCredito           | decimal  | Valor Cartão de Crédito       | Valor (R$ milhões) de transações realizadas com cartão de crédito.                                                 |
| valorCartaoDebito            | decimal  | Valor Cartão de Débito        | Valor (R$ milhões) de transações realizadas com cartão de débito trimestralmente.                                  |
| valorCartaoPrePago           | decimal  | Valor Cartão Pré-pago         | Valor (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente.                                    |
| valorTransIntrabancaria      | decimal  | Valor Transferência Intrabancária | Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes da Instituição. |
| valorConvenios               | decimal  | Valor Convênio                | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais e não-governamentais.          |
| valorDebitoDireto            | decimal  | Valor Débito Direto           | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente em sua conta corrente. |
| valorSaques                  | decimal  | Valor Saque                   | Montante sacado (R$ milhões) nos caixas eletrônicos trimestralmente.                                                |
| quantidadePix                | decimal  | Quantidade Pix                | Quantidade (em milhares) de transações Pix liquidadas trimestralmente no SPI e fora do SPI.                        |
| quantidadeTED                | decimal  | Quantidade TED                | Quantidade (em milhares) de TED realizadas trimestralmente.                                                        |
| quantidadeTEC                | decimal  | Quantidade TEC                | Quantidade (em milhares) de TEC realizadas trimestralmente.                                                        |
| quantidadeCheque             | decimal  | Quantidade Cheque             | Quantidade (em milhares) de cheques interbancários e de cheques intrabancários compensados trimestralmente.        |
| quantidadeBoleto             | decimal  | Quantidade Boleto             | Quantidade (em milhares) de cheques interbancários e intrabancários compensados trimestralmente.                   |
| quantidadeDOC                | decimal  | Quantidade DOC                | Quantidade (em milhares) de DOC realizados trimestralmente.                                                        |
| quantidadeCartaoCredito      | decimal  | Quantidade Cartão de Crédito  | Quantidade (em milhares) de transações realizadas com cartão de crédito trimestralmente.                           |
| quantidadeCartaoDebito       | decimal  | Quantidade Cartão de Débito   | Quantidade (em milhares) de transações realizadas com cartão de débito trimestralmente.                            |
| quantidadeCartaoPrePago      | decimal  | Quantidade Cartão Pré-pago    | Quantidade (em milhares) de transações realizadas com cartão pré-pago trimestralmente.                             |
| quantidadeTransIntrabancaria | decimal  | Quantidade de Transferência Intrabancária | Quantidade (em milhares) de transferências realizadas trimestralmente entre contas de clientes da Instituição.    |
| quantidadeConvenios          | decimal  | Quantidade Convênio           | Quantidade (em milhares) de transações realizadas referentes a arrecadações trimestrais governamentais e não-governamentais. |
| quantidadeDebitoDireto       | decimal  | Quantidade Débito Direto      | Quantidade (em milhares) de transações trimestrais referente a débitos previamente autorizados pelo cliente.       |
| quantidadeSaques             | decimal  | Quantidade de Saque           | Quantidade (em milhares) de saques realizados nos caixas eletrônicos trimestralmente.                              |



