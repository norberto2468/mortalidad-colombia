PROYECTO: Mortalidad Colombia - Visualización Interactiva con Dash

Este proyecto permite visualizar y analizar datos de mortalidad en Colombia por departamento y municipio, utilizando Dash y Plotly para una experiencia interactiva y profesional.

REQUISITOS:
- Python 3.8 o superior
- Las librerías listadas en requirements.txt

INSTALACIÓN:
1. Clona o descarga este repositorio en tu equipo.
2. Instala las dependencias ejecutando:
   pip install -r requirements.txt

EJECUCIÓN:
1. Ejecuta el archivo principal de la aplicación:
   python app.py
2. Abre tu navegador y accede a la dirección:
   http://127.0.0.1:8050/

ESTRUCTURA DEL PROYECTO:

- app.py  
  Archivo principal que inicializa y ejecuta la aplicación Dash.

- data/
  Carpeta que contiene todos los archivos de datos necesarios para la visualización:
  - CodigosDeMuerte.xlsx: Códigos y descripciones de causas de muerte.
  - Colombia.geo.json: GeoJSON con la geometría de los departamentos de Colombia.
  - Divipola.xlsx: Tabla de códigos DANE y nombres de departamentos y municipios.
  - DivipolaCE.xlsx: Información complementaria de códigos DANE.
  - NoFetal2019.xlsx: Datos de mortalidad no fetal para el año 2019.

- src/
  Carpeta principal del código fuente de la aplicación.
  - layout/
    Componentes de layout y gráficos de la aplicación:
    - grafico01.py: Mapa coroplético de muertes por departamento.
    - (otros archivos de visualización y layout)
  - utils/
    Funciones utilitarias para la carga y procesamiento de datos:
    - load_data.py: Funciones para cargar y preparar los datos desde los archivos fuente.
  - callbacks/
    Definición de callbacks de Dash para la navegación y lógica interactiva de la app.

- requirements.txt  
  Archivo con la lista de dependencias necesarias para ejecutar la aplicación.

NOTAS IMPORTANTES:
- Todos los archivos de datos deben estar ubicados en la carpeta `data/` para el correcto funcionamiento de la aplicación.
- El archivo `Colombia.geo.json` es utilizado localmente para la visualización geográfica, no requiere conexión a internet.
- Si experimentas problemas con la visualización de mapas, revisa la correspondencia entre los códigos DANE en tus archivos de datos y el GeoJSON.
- Para personalizar los gráficos o agregar nuevas visualizaciones, edita o agrega archivos en la carpeta `src/layout/`.

##  Despliegue  en Render

Haz clic aquí para desplegar la aplicación en tu cuenta de Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)]
(https://render.com/deploy?repo=https://github.com/norberto2468/actividad4_aplicaciones)

1. Haz clic en el botón "Deploy to Render" de arriba.
2. Inicia sesión o crea una cuenta gratuita en [Render](https://render.com/).
3. Render detectará automáticamente el archivo `render.yaml` y configurará el entorno necesario.
4. Confirma la creación del servicio y espera a que Render instale las dependencias y despliegue la aplicación.
5. Una vez finalizado el proceso, Render te proporcionará una URL pública para acceder a la aplicación.

Enlace de la aplicación desplegada de ejemplo:  
[https://desplegar-dash-render-9cjy.onrender.com](https://desplegar-dash-render-9cjy.onrender.com)

Puedes monitorear y administrar el despliegue desde el panel de control de Render:  
[https://dashboard.render.com/web/srv-d0lbbdogjchc73eu7gk0](https://dashboard.render.com/web/srv-d0lbbdogjchc73eu7gk0)

> Nota: Si deseas desplegar tu propia instancia, solo necesitas tener acceso a este repositorio y 
seguir los pasos anteriores. El proceso es automático y no requiere configuración adicional.



AUTORES:
- Norberto Guerrero
- William Ruiz

Contacto:  
Para dudas o soporte, contacta a los autores a través del repositorio o correo institucional.