from dash import html, dcc
import plotly.express as px
import pandas as pd

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    # Total de muertes por municipio
    total_muertes = df_mortalidad.groupby("COD_MUNICIPIO").size().reset_index(name="Total_Muertes")

    # Unir con divipola para obtener nombres
    df_merged = pd.merge(total_muertes, df_divipola, how="left", on="COD_MUNICIPIO")

    # Eliminar filas sin nombre de municipio
    df_merged = df_merged.dropna(subset=["MUNICIPIO"])

    # Seleccionar 10 con menor cantidad
    df_10_menor = df_merged.sort_values(by="Total_Muertes").head(10)

    fig = px.pie(
        df_10_menor,
        values="Total_Muertes",
        names="MUNICIPIO",
        title="10 ciudades con menor índice de mortalidad"
    )

    return html.Div([
        html.H3("Gráfico 4: Ciudades con menor mortalidad (2019)"),
        dcc.Graph(figure=fig),
        html.Br(),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
