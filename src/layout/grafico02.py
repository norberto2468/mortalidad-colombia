from dash import html, dcc
import plotly.express as px
import pandas as pd

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    # Agrupar por mes y contar muertes
    df_muertes_mes = df_mortalidad.groupby("MES").size().reset_index(name="Total_Muertes")

    # Ordenar por número de mes
    df_muertes_mes = df_muertes_mes.sort_values(by="MES")

    # Crear gráfico de líneas
    fig = px.line(
        df_muertes_mes,
        x="MES",
        y="Total_Muertes",
        markers=True,
        title="Muertes por mes en Colombia (2019)",
        labels={"MES": "Mes", "Total_Muertes": "Número de Muertes"}
    )
    fig.update_traces(line=dict(color="firebrick", width=3))

    return html.Div([
        html.H3("Gráfico 2: Variación mensual de muertes en Colombia (2019)"),
        dcc.Graph(figure=fig),
        html.Br(),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
