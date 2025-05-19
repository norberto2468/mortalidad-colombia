from mortalidadColombia.utils.load_data import cargar_datos

df_mortalidad, df_codigos, df_divipola = cargar_datos()
print(df_mortalidad.columns)
