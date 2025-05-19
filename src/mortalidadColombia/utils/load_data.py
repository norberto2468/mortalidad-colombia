import os
import pandas as pd

def cargar_datos():
    """
    Carga los archivos Excel desde la carpeta /data y devuelve los DataFrames.
    """

    # Ruta base al directorio raíz del proyecto (actividad4/)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    ruta_data = os.path.join(base_dir, 'data')

    # Construcción segura de rutas
    ruta_mortalidad = os.path.join(ruta_data, 'NoFetal2019.xlsx')
    ruta_codigos = os.path.join(ruta_data, 'CodigosDeMuerte.xlsx')
    ruta_divipola = os.path.join(ruta_data, 'Divipola.xlsx')

    # Carga de archivos
    df_mortalidad = pd.read_excel(ruta_mortalidad)
    df_codigos = pd.read_excel(ruta_codigos)
    df_divipola = pd.read_excel(ruta_divipola)

    # Verificación
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
