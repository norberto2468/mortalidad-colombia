# mortalidadColombia/layout/grafico01.py

from dash import html, dcc
import plotly.express as px
import pandas as pd
import requests

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    """
    Gráfico 1: Mapa coroplético de mortalidad por departamento en Colombia.
    """

    # 1. Agrupar los datos por departamento y contar el total de muertes
    df_total = df_mortalidad.groupby("COD_DEPARTAMENTO").size().reset_index(name="TOTAL")

    # 2. Unir con df_divipola para obtener nombres y códigos DANE
    df_merged = pd.merge(df_total, df_divipola, how="left", on="COD_DEPARTAMENTO")

    # 3. Descargar el GeoJSON oficial de departamentos de Colombia (DANE)
    # Este GeoJSON es confiable y compatible con Plotly
    url_geojson = "https://gist.github.com/john-guerra/43c7656821069d00dcbc.js"
    try:
        geojson_data = requests.get(url_geojson).json()
    except Exception as e:
        # Si falla la descarga, mostrar mensaje de error
        return html.Div([
            html.H3("Error: No se pudo descargar el GeoJSON de departamentos de Colombia."),
            html.Code(str(e))
        ])

    # 4. Asegurar que los códigos DANE sean string para el cruce
    df_merged['COD_DANE'] = df_merged['COD_DANE'].astype(str)
    for feature in geojson_data['features']:
        feature['properties']['DPTO'] = str(feature['properties']['DPTO'])

    # 5. Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_merged,
        geojson=geojson_data,
        locations='COD_DANE',  # Columna de tu DataFrame con el código DANE
        featureidkey='properties.DPTO',  # Propiedad del GeoJSON con el código DANE
        color='TOTAL',  # Columna con el valor a mostrar
        color_continuous_scale='Reds',
        labels={'TOTAL': 'Muertes'},
        title='Mapa de Mortalidad por Departamento en Colombia - 2019'
    )

    # 6. Ajustar el mapa para que se centre en Colombia y no muestre el fondo gris
    fig.update_geos(fitbounds="locations", visible=False)

    # 7. Devolver el layout de Dash con el gráfico y un enlace para volver al menú
    return html.Div([
        html.H3("Gráfico 1: Mapa de Mortalidad por Departamento (2019)"),
        dcc.Graph(figure=fig),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
