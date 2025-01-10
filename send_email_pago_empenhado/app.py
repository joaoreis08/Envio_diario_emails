import pandas as pd
import plotly.graph_objects as go


caminho = r"S:\NCD\Projetos 2024\Projeto Pajuçara\envia-emails\dados\valores_gerais.parquet.gzip"

df = pd.read_parquet(caminho)
df = df.query('Ano == "2024"').groupby(['Ano', 'UGC_Sigla_Ação'])[['Empenhado', 'Pago']].sum().reset_index()

# Calculate the percentage and format it correctly
df['%'] = df['Pago'] / df['Empenhado'] * 100
df['%'] = df['%'].apply(lambda x: f"{x:,.2f}%")

# Format "Pago" and "Empenhado" columns with Brazilian currency formatting
df['Pago'] = df['Pago'].apply(lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
df['Empenhado'] = df['Empenhado'].apply(lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))


df_top10 = df[['Ano', 'UGC_Sigla_Ação', 'Pago', 'Empenhado', '%']].sort_values('%', ascending=False)
df_top10 = df_top10[df_top10['%'] != 'nan%'].head(10)
df_worst10 = df[['Ano', 'UGC_Sigla_Ação', 'Pago', 'Empenhado', '%']].sort_values('%', ascending=True)
df_worst10 = df_worst10[df_worst10['%'] != 'nan%'].head(10)


fig = go.Figure()

# Adicionar a série "%" usando valores numéricos para o tamanho das barras
fig.add_trace(
    go.Bar(
        x=df_top10['%'].str.replace('%', '').astype(float),  # Converter para numérico
        y=df_top10['UGC_Sigla_Ação'],
        orientation='h',
        name='%',
        text=df_top10['%'],  # Exibir valores formatados nas barras
        textposition='outside'
    )
)

# Ajustar layout
fig.update_layout(
    height=500,  # Ajuste para um tamanho adequado
    title='Valores por Sigla',
    xaxis=dict(title='Porcentagem', showticklabels=True),
    yaxis_title='Siglas',
    showlegend=False
)
fig.write_image("Top 10.png")
# Mostrar o gráfico
fig.show()


# Criar o gráfico para os 10 piores valores
fig = go.Figure()

# Adicionar a série "%" usando valores numéricos para o tamanho das barras
fig.add_trace(
    go.Bar(
        x=df_worst10['%'].str.replace('%', '').astype(float),  # Converter para numérico
        y=df_worst10['UGC_Sigla_Ação'],
        orientation='h',
        name='%',
        text=df_worst10['%'],  # Exibir valores formatados nas barras
        textposition='outside'
    )
)

# Ajustar layout
fig.update_layout(
    height=500,  # Ajuste conforme necessário
    title='Piores 10 Valores por Sigla',
    xaxis=dict(title='Porcentagem', showticklabels=True),
    yaxis_title='Siglas',
    showlegend=False
)

fig.write_image("Worse 10.png")

# Mostrar o gráfico
fig.show()

