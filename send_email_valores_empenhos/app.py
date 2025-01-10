import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
pd.options.display.float_format = lambda x: f"R${x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

caminho_csv = r"S:\NCD\Projetos 2024\Projeto Pajuçara\execucao_secretarias\Valores_empenhos.csv"
df = pd.read_csv(caminho_csv,delimiter =';', low_memory = False)

agora = datetime.now()
mes = agora.month
ano = agora.year
ano_anterior = ano-1
ano_retrasado = ano-2

df['Liquidado'] = df['Liquidado'].str.replace(",", ".", regex=False).astype(float)

dfano1 = df.query("Ano == @ano_anterior and Mês <= @mes").groupby(['Emp_Credor_Nome_Fantasia','Ano'])['Liquidado'].sum().reset_index()
dfano2 = df.query("Ano == @ano_retrasado and Mês <= @mes").groupby(['Emp_Credor_Nome_Fantasia','Ano'])['Liquidado'].sum().reset_index()

top_20_ano1 = dfano1.sort_values(by='Liquidado', ascending=False).head(20)
top_20_ano2 = dfano2.sort_values(by='Liquidado', ascending=False).head(20)


# Criando o gráfico
fig = go.Figure(data=[
    go.Bar(
        name='Ano 2024',
        x=top_20_ano1['Liquidado'],  # Valores do ano de 2024
        y=top_20_ano1['Emp_Credor_Nome_Fantasia'],
        orientation='h',  # Barras horizontais
        marker=dict(line=dict(width=2, color='DarkSlateGrey'))
    ),
    go.Bar(
        name='Ano 2023',
        x=top_20_ano2['Liquidado'],  # Valores do ano de 2023
        y=top_20_ano2['Emp_Credor_Nome_Fantasia'],
        orientation='h',
        marker=dict(line=dict(width=2, color='DarkSlateGrey'))
    )
])

fig.update_layout(
    title='Top 20 Credores por Valor Liquidado',
    barmode='group',
    xaxis=dict(title='Valores Liquidado'),
    yaxis=dict(title='Credores', automargin=True),  # Ajusta margens automaticamente
    height=1000  # Aumenta altura para mais espaço
)

fig.write_image("Grafico_top_20_credores_por_valor_liquidado.png")
fig.show()


