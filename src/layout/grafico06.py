from dash import html, dcc
import plotly.express as px

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    # Agrupar por grupo de edad
    df_edad = df_mortalidad["GRUPO_EDAD1"].value_counts().reset_index()
    df_edad.columns = ["Grupo_Edad", "Total_Muertes"]
    df_edad = df_edad.sort_values(by="Grupo_Edad")  # Ordenar si es necesario

    # Crear histograma
    fig = px.bar(
        df_edad,
        x="Grupo_Edad",
        y="Total_Muertes",
        title="Distribución de muertes por grupos de edad (2019)",
        labels={"Grupo_Edad": "Grupo de Edad", "Total_Muertes": "Número de Muertes"},
        color="Total_Muertes",
        color_continuous_scale="plasma"
    )

    return html.Div([
        html.H3("Gráfico 6: Muertes por Grupo de Edad (2019)"),
        dcc.Graph(figure=fig),
        html.Br(),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
