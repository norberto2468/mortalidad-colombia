# grafico07.py
from dash import html, dcc
import plotly.express as px
import pandas as pd

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    df_mortalidad = pd.merge(df_mortalidad, df_divipola, how="left", on="COD_DEPARTAMENTO")
    df_mortalidad["SEXO"] = df_mortalidad["SEXO"].map({1: "Masculino", 2: "Femenino"})

    df_pivot = df_mortalidad.groupby(["DEPARTAMENTO", "SEXO"]).size().reset_index(name="TOTAL")

    fig = px.bar(
        df_pivot,
        x="DEPARTAMENTO",
        y="TOTAL",
        color="SEXO",
        barmode="group",
        title="Muertes por Sexo y Departamento (2019)",
        labels={"TOTAL": "Muertes", "DEPARTAMENTO": "Departamento"}
    )
    fig.update_layout(xaxis_tickangle=-45)

    return html.Div([
        html.H3("Gráfico 7: Muertes por Sexo y Departamento (2019)"),
        dcc.Graph(figure=fig),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
