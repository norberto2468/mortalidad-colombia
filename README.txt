PROYECTO: Mortalidad Colombia - Visualización Dash

Este proyecto permite visualizar datos de mortalidad en Colombia por departamento y municipio, usando Dash y Plotly.

REQUISITOS:
- Python 3.8 o superior
- Las librerías listadas en requirements.txt

INSTALACIÓN:
1. Clona o descarga este repositorio.
2. Instala las dependencias:
   pip install -r requirements.txt

EJECUCIÓN:
1. Ejecuta el archivo principal:
   python app.py
2. Abre tu navegador y ve a http://127.0.0.1:8050/

ESTRUCTURA DEL PROYECTO:
- app.py: Archivo principal de la aplicación Dash.
- mortalidadColombia/utils/load_data.py: Funciones para cargar los datos.
- mortalidadColombia/layout/: Layouts y gráficos de la app.
- mortalidadColombia/callbacks/: Callbacks de navegación y lógica.
- requirements.txt: Dependencias del proyecto.

NOTAS:
- Asegúrate de tener los archivos de datos requeridos en la carpeta correspondiente.
- Si tienes problemas con los geojson, revisa tu conexión a internet.

Autor: Norberto Guerrrero y WIlliam ruiz