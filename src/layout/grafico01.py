# mortalidadColombia/layout/grafico01.py

from dash import html, dcc
import plotly.express as px
import pandas as pd
import json
import os

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    """
    Mapa: Visualización de la distribución total de muertes por departamento en Colombia para el año 2019.
    """

    # Agrupar los datos por departamento y contar el total de muertes
    df_total = df_mortalidad.groupby("COD_DEPARTAMENTO").size().reset_index(name="TOTAL")

    # Unir con df_divipola para obtener nombres y códigos DANE
    df_merged = pd.merge(df_total, df_divipola, how="left", on="COD_DEPARTAMENTO")

    # Leer el GeoJSON local de departamentos de Colombia
    geojson_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Colombia.geo.json')
    try:
        with open(geojson_path, encoding='utf-8') as f:
            geojson_data = json.load(f)
    except Exception as e:
        return html.Div([
            html.H3("Error: No se pudo cargar el archivo local Colombia.geo.json."),
            html.Code(str(e))
        ])

    # DEPURACIÓN: imprime los valores únicos para comparar
    print("DF COD_DANE únicos:", df_merged['COD_DANE'].unique())
    print("GeoJSON keys:", geojson_data['features'][0]['properties'].keys())
    print("GeoJSON DPTO únicos:", set([feature['properties']['DPTO'] for feature in geojson_data['features']]))

    # Asegura que los códigos DANE sean string y tengan dos dígitos
    df_merged['COD_DANE'] = df_merged['COD_DANE'].astype(str).str.zfill(2)
    # Si tienes códigos de municipio, toma solo los dos primeros dígitos
    df_merged['COD_DANE'] = df_merged['COD_DANE'].str[:2]
    for feature in geojson_data['features']:
        feature['properties']['DPTO'] = str(feature['properties']['DPTO']).zfill(2)

    # FILTRA SOLO LOS DEPARTAMENTOS QUE EXISTEN EN EL GEOJSON
    geojson_dptos = set([feature['properties']['DPTO'] for feature in geojson_data['features']])
    df_merged = df_merged[df_merged['COD_DANE'].isin(geojson_dptos)]

    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_merged,
        geojson=geojson_data,
        locations='COD_DANE',
        featureidkey='properties.DPTO',
        color='TOTAL',
        color_continuous_scale='Reds',
        labels={'TOTAL': 'Muertes'},
        title='Mapa: Visualización de la distribución total de muertes por departamento en Colombia para el año 2019'
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        showcountries=True,
        lataxis_range=[-5, 15],
        lonaxis_range=[-82, -66]
    )
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})

    return html.Div([
        html.H3("Mapa: Visualización de la distribución total de muertes por departamento en Colombia para el año 2019"),
        dcc.Graph(figure=fig),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
