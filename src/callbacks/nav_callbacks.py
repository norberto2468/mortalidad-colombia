from dash import Input, Output
from layout import menu, grafico01,grafico02,grafico03,grafico04,    grafico05, grafico06, grafico07  # Importar los módulos de layout
import load_data as load_data


def registrar_callbacks(app,dframes):
    @app.callback(
        Output('contenido-principal', 'children'),
        Input('url', 'pathname')
    )
    def mostrar_contenido(pathname):
        # Si el usuario ha seleccionado una opción de la barra de navegación
        if pathname == '/grafico01':
            return grafico01.layout_grafico( dframes[0], dframes[1],dframes[2])
        
        elif pathname == '/grafico02':
            return grafico02.layout_grafico( dframes[0], dframes[1],dframes[2])
        elif pathname == '/grafico03':
            return grafico03.layout_grafico( dframes[0], dframes[1],dframes[2])
        elif pathname == '/grafico04':
            return grafico04.layout_grafico( dframes[0], dframes[1],dframes[2])
        elif pathname == '/grafico05':
            return grafico05.layout_grafico( dframes[0], dframes[1],dframes[2])
        elif pathname == '/grafico06':
            return grafico06.layout_grafico( dframes[0], dframes[1],dframes[2])
        elif pathname == '/grafico07':
            return grafico07.layout_grafico( dframes[0], dframes[1],dframes[2])
        else:
            return menu.menu_layout

