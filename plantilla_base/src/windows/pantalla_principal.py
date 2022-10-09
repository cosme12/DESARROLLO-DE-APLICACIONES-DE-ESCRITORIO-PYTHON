import PySimpleGUI as sg


def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('SystemDefault')

    layout = [
        [sg.Text("Expedientes del dia")],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expendiente", key="-INGRESAR_EXPEDIENTE-")],
        [sg.Table(values=[["-", "-", "-", "-", "-", "-"]], key="-TABLA_EXPEDIENTES-", justification="c",
            headings=[" Código ", "     Empresa     ", "   CUIT   ", " Teléfono ", " Categoría "],
            row_height=20, num_rows=10, header_background_color="#FF8000")],
    ]

    window = sg.Window("Sistema Integral v1.0", layout=layout, resizable=True)

    return window
