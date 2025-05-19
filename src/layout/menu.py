from dash import html, dcc

menu_layout = html.Div([
    html.H2("Menú Principal de Visualización"),
    html.Ul([
        html.Li(dcc.Link("1. Mapa de distribución de muertes por departamento", href="/grafico01")),
        html.Li(dcc.Link("2. Gráfico de líneas de muertes por mes", href="/grafico02")),
        html.Li(dcc.Link("3. Gráfico de barras por ciudades violentas", href="/grafico03")),
        html.Li(dcc.Link("4. Gráfico circular: ciudades con menor índice de mortalidad", href="/grafico04")),
        html.Li(dcc.Link("5. Tabla: 10 principales causas de muerte", href="/grafico05")),
        html.Li(dcc.Link("6. Histograma: distribución de muertes por grupos de edad", href="/grafico06")),
        html.Li(dcc.Link("7. Barras apiladas: muertes por sexo y departamento", href="/grafico07")),
        html.Br(),
        html.Li(dcc.Link("Volver al menú", href="/"))
    ])
])