# Relatórios de Execução Orçamentária - Automação 2024

Este projeto é uma aplicação completa para o **processamento, análise, geração de gráficos e envio automatizado** de relatórios de execução orçamentária. Ele processa dados provenientes de arquivos Excel e CSV, gera relatórios diários detalhados com tabelas e gráficos, e os envia automaticamente por e-mail com formatação personalizada em HTML.

## Funcionalidades

### 1. Processamento de Dados
- Filtragem de dados para o ano de **2024**.
- Agrupamento por `UGC_Sigla_Ação` com cálculos como:
  - **Dotação Autorizada**
  - **Empenhado**
  - **Liquidado**
  - **Percentuais de execução** (ex.: Liquidado %).
- Análise e comparação dos valores liquidados entre os anos **2023 e 2024**.
- Suporte à formatação de valores em moeda brasileira (**R$**) e percentuais.

### 2. Geração de Relatórios
- **Tabelas em formato HTML**:
  - Exibição dos **10 melhores** e **10 piores** resultados de execução orçamentária.
- **Gráficos automáticos**:
  - Top 10 Melhores e Top 10 Piores percentuais de execução por `UGC_Sigla_Ação`.
  - Top 20 Credores por Valor Liquidado, comparando **2023 e 2024**.
- Exportação de gráficos no formato **PNG** para uso nos relatórios.

### 3. Automação de E-mails
- Configuração de envio via servidor SMTP utilizando **variáveis de ambiente**.
- Relatórios enviados diariamente (**de segunda a sexta-feira**) contendo:
  - Tabelas HTML personalizadas.
  - Gráficos integrados.
  - Imagens de cabeçalho e rodapé.

## Requisitos

### Ambiente
- **Python**: >= 3.8

### Bibliotecas
As principais bibliotecas utilizadas no projeto são:
- `pandas`
- `plotly`
- `dotenv`
- `smtplib`
- `email`
- `openpyxl`

### Arquivos Necessários
- **Dados orçamentários**:
  - Exemplo: `valores_gerais.parquet.gzip`, `Valores_empenhos.csv`.
- **Imagens para e-mails**:
  - Cabeçalho: `header.png`
  - Rodapé: `footer.png`
