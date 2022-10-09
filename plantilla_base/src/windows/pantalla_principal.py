from datetime import date
import PySimpleGUI as sg
from src.consts import font


def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('SystemDefault')

    layout = [
        [sg.Text(f'Expedientes del día', font=(font.font_name, 20), size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expendiente", key='-INGRESAR_EXPEDIENTE-', font=(font.font_name, 11))],
        [sg.Table(values=[["-", "-", "-", "-", "-", "-"]], key="-TABLA_VENTAS_CAJA-", justification="c",
                  headings=[" Código ", "     Empresa     ", "   CUIT   ", " Teléfono ", " Categoría "],
                  row_height=20, num_rows=10, header_background_color="#FF8000")],
        [sg.Text('Total')]
    ]
    
    window = sg.Window(f'Sistema Integral v1.0', layout=layout, resizable=True)

    return window
