# mortalidadColombia/layout/grafico05.py

from dash import html, dash_table
import pandas as pd

def layout_grafico(df_mortalidad, df_codigos, df_divipola):



    df_codigos = df_codigos.rename(columns={
        "Código de la CIE-10 cuatro caracteres": "COD_MUERTE",
        "Descripcion  de códigos mortalidad a cuatro caracteres": "DESCRIPCION"
    })

    # Agrupar por código de muerte
    top_codigos = df_mortalidad.groupby("COD_MUERTE").size().reset_index(name="TOTAL")

    # Unir con descripciones
    top_merged = pd.merge(top_codigos, df_codigos[['COD_MUERTE', 'DESCRIPCION']], on="COD_MUERTE", how="left")

    # Ordenar por frecuencia y seleccionar top 10
    top_10 = top_merged.sort_values(by="TOTAL", ascending=False).head(10)

    # Formatear tabla para Dash
    table = dash_table.DataTable(
        columns=[
            {"name": "Código", "id": "COD_MUERTE"},
            {"name": "Descripción", "id": "DESCRIPCION"},
            {"name": "Total", "id": "TOTAL"}
        ],
        data=top_10.to_dict('records'),
        style_cell={'textAlign': 'left', 'padding': '8px'},
        style_header={'backgroundColor': 'black', 'color': 'white', 'fontWeight': 'bold'},
        style_table={'overflowX': 'auto'}
    )

    return html.Div([
        html.H3("Gráfico 5: Principales causas de muerte en Colombia (2019)"),
        table,
        html.Br(),
        html.A("⬅️ Volver al menú", href="/", style={"color": "blue", "fontWeight": "bold"})
    ])
