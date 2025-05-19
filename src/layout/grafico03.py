from dash import html, dcc
import plotly.express as px
import pandas as pd

def layout_grafico(df_mortalidad, df_codigos, df_divipola):
    """
    Gráfico 3: Visualiza las 5 ciudades más violentas por homicidios y agresión con armas de fuego en 2019.
    """

    # 1. Normalizar los códigos de muerte a mayúsculas y sin espacios
    df_mortalidad["COD_MUERTE"] = df_mortalidad["COD_MUERTE"].astype(str).str.upper().str.strip()

    # 2. Mostrar en consola los códigos únicos para depuración
    print("Códigos únicos en COD_MUERTE:", df_mortalidad["COD_MUERTE"].unique())

    # 3. Definir los códigos de homicidio y agresión con armas de fuego (en mayúsculas)
    codigos_violentos = ['X95', 'X93', 'X94']

    # 4. Filtrar solo los registros con esos códigos
    df_violentas = df_mortalidad[df_mortalidad["COD_MUERTE"].isin(codigos_violentos)]

    # 5. Mostrar shape y algunos datos para depuración
    print("df_violentas shape:", df_violentas.shape)
    print(df_violentas[["COD_MUERTE", "COD_MUNICIPIO"]].head())

    # 6. Agrupar por municipio y contar el total de muertes violentas
    df_ciudades_violentas = df_violentas.groupby("COD_MUNICIPIO").size().reset_index(name="Total_Violentas")

    # 7. Unir con el dataframe divipola para obtener nombres de municipio
    df_ciudades_violentas = pd.merge(
        df_ciudades_violentas,
        df_divipola[["COD_MUNICIPIO", "MUNICIPIO"]],
        on="COD_MUNICIPIO",
        how="left"
    )

    # 8. Si no hay nombres de municipio, usar el código como nombre
    df_ciudades_violentas["MUNICIPIO"] = df_ciudades_violentas["MUNICIPIO"].fillna(df_ciudades_violentas["COD_MUNICIPIO"].astype(str))

    # 9. Eliminar duplicados por código de municipio
    df_ciudades_violentas = df_ciudades_violentas.drop_duplicates(subset=["COD_MUNICIPIO"])

    # 10. Tomar las 5 ciudades con más casos (aunque haya menos de 5)
    top5 = df_ciudades_violentas.sort_values(by="Total_Violentas", ascending=False).head(5)

    # 11. Mostrar en consola los datos del top 5 para depuración
    print("Top 5 ciudades violentas:\n", top5)

    # 12. Si no hay datos, mostrar mensaje claro en la app
    if top5.empty or top5["Total_Violentas"].sum() == 0:
        return html.Div([
            html.H3("Gráfico 3: Ciudades más violentas por homicidios (2019)"),
            html.P("⚠️ No hay datos de homicidios con los códigos seleccionados (X95, X93, X94)."),
            html.Br(),
            dcc.Link("⬅️ Volver al menú", href="/")
        ])

    # 13. Crear gráfico de barras con Plotly Express
    fig = px.bar(
        top5,
        x="MUNICIPIO",
        y="Total_Violentas",
        color="Total_Violentas",
        text="Total_Violentas",
        title="Top 5 Ciudades más Violentas de Colombia por Homicidios (2019)",
        labels={"MUNICIPIO": "Ciudad", "Total_Violentas": "Muertes Violentas"}
    )

    # 14. Mejorar presentación del gráfico
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis_title="Número de Muertes Violentas",
        xaxis_title="Ciudad",
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )

    # 15. Devolver el layout de Dash con el gráfico y un enlace para volver al menú
    return html.Div([
        html.H3("Gráfico 3: Ciudades más violentas por homicidios (2019)"),
        dcc.Graph(figure=fig),
        html.Br(),
        dcc.Link("⬅️ Volver al menú", href="/")
    ])
