import os
import pandas as pd

def cargar_datos():
    """
    Carga los archivos Excel desde la carpeta /data (que está al mismo nivel que este script)
    y devuelve los DataFrames correspondientes.
    """

    # Ruta base: carpeta donde está este archivo (src)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta a la carpeta 'data' dentro de 'src'
    ruta_data = os.path.join(base_dir, 'data')

    # Construcción de rutas completas a los archivos Excel
    ruta_mortalidad = os.path.join(ruta_data, 'NoFetal2019.xlsx')
    ruta_codigos = os.path.join(ruta_data, 'CodigosDeMuerte.xlsx')
    ruta_divipola = os.path.join(ruta_data, 'DivipolaCE.xlsx')

    # Carga de archivos Excel en DataFrames
    df_mortalidad = pd.read_excel(ruta_mortalidad)
    df_codigos = pd.read_excel(ruta_codigos)
    df_divipola = pd.read_excel(ruta_divipola)

    # Mensajes de verificación
    print("✅ Datos cargados correctamente:")
    print("📊 Mortalidad:", df_mortalidad.shape)
    print("📊 Códigos:", df_codigos.shape)
    print("📊 Divipola:", df_divipola.shape)

    # Muestra previa de los datos
    print("\n🔍 Primeras filas de Mortalidad:")
    print(df_mortalidad.head())

    print("\n🔍 Primeras filas de Códigos:")
    print(df_codigos.head())

    print("\n🔍 Primeras filas de Divipola:")
    print(df_divipola.head())
    
    # Devuelve los DataFrames como una lista
    return [df_mortalidad, df_codigos, df_divipola]
