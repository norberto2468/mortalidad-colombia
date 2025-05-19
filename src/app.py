from dash import Dash, dcc, html
from load_data import cargar_datos
from layout.menu import menu_layout
from callbacks.nav_callbacks import registrar_callbacks
import load_data as load_data


# Paso 1: Inicializar la aplicación
app = Dash(__name__, suppress_callback_exceptions=True)
# Paso 2: Obtener el servidor de la aplicación
server = app.server

# Paso 2: Cargar los datos
mortalidad_df, codigos_df, divipola_df = cargar_datos()

# Paso 3: Layout principal con control de navegación
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='contenido-principal')
    
])

# Paso 4: Registrar los callbacks de navegación
dframes = load_data.cargar_datos()
registrar_callbacks(app,dframes)

# Paso 5: Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
