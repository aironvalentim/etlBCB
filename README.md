# etlBCB

# 📊 Dados sobre Estabelecimentos, Transações e Tarifas de Cartões de Pagamento

## 📌 Visão Geral
Este repositório contém informações detalhadas sobre a aceitação de cartões de pagamento, incluindo estabelecimentos credenciados, tarifas de intercâmbio, taxas de desconto, terminais de autoatendimento (ATM), volumetria de operações e programas de recompensa.

Os dados são atualizados trimestralmente e ficam disponíveis 90 dias após o final de cada trimestre.

---

## 📂 Estrutura dos Dados

### 🏬 **Quantidade de Estabelecimentos Credenciados**
- Total e ativos
- Segmentação por bandeira e função do cartão

### 💳 **Tarifas de Intercâmbio (TIC) e Volumetria**
- Taxas cobradas nas transações
- Formas de captura
- Parcelamento
- Quantidade e valor das transações

### 📉 **Taxas de Desconto (MDR) e Volumetria**
- Média das taxas cobradas
- Quantidade de transações
- Valor total das transações

### 🏧 **Terminais de Autoatendimento (ATM)**
- Quantidade instalada
- Localização (UF)
- Tipo de compartilhamento

### 🔄 **Volumetria das Operações Intrabancárias**
- Operações realizadas entre clientes da mesma instituição
- Exclusão de transferências Pix intrabancárias

### 📡 **Volumetria por Canal de Acesso e Produto**
- Transações por tipo de canal
- Detalhamento de operações em ATMs

### 🏪 **Quantidade de Terminais POS e PDV**
- Número de terminais POS e PDV
- Distribuição por UF
- POS com leitora de chip e compartilhados

### 🎁 **Tarifas, Programas de Recompensa e Fidelidade**
- Tarifas cobradas por emissão e uso do cartão
- Estoque, aquisição e conversão de pontos
- Gastos com programas de recompensa

---

## 📥 Acesso aos Dados
Os dados podem ser consultados e filtrados com os seguintes parâmetros:
- `trimestre` (AAAAT) → trimestre de referência
- `$format` → tipo de conteúdo retornado
- `$select` → propriedades retornadas
- `$filter` → filtros aplicáveis
- `$orderby` → ordenação dos dados
- `$skip` → índice inicial dos dados
- `$top` → limite de registros retornados

---

## 📜 Licença
Os dados são disponibilizados conforme as diretrizes e regulamentos aplicáveis.
