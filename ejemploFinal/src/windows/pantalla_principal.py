from datetime import date
import PySimpleGUI as sg
from src.consts import font


def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('SystemDefault')

    font16 = ("Calibri Italic", 16)

    layout = [
        [sg.Text(f'Expedientes del día {date.today().strftime("%d/%m/%Y")}', font=(font.font_name, 20), size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expendiente", key='-INGRESAR_EXPEDIENTE-', tooltip='Permite ingresar un expediente nuevo',
                      font=(font.font_name, 11))
        ],
        [sg.Table(values=[["-", "-", "-", "-", "-", "-"]], key="-TABLA_EXPEDIENTE-",
                  justification="c",
                  headings=[" Código ", "     Empresa     ", "   CUIT   ", " Teléfono ", " Categoría "],
                  row_height=20, num_rows=10, header_background_color="#FF8000")],
        [
            sg.Text('Total', font=font16),
            sg.Text('0,00', background_color="#000000", text_color="#ffffff", font=font16, size=(10, 1),
                    justification="right", key="-TEXTO_TOTAL-")]
    ]
    window = sg.Window('Sistema Integral v1.0', layout=layout, resizable=True, finalize=True)

    return window
