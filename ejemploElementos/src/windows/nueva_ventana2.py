import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('SystemDefault')

def build():

    layout1 = [
        [sg.Text('Formulario generico',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('Fecha: --/--/--', size=(15,1), key="-FECHA_TEXTO-"), sg.Button('Cambiar fecha', key="-CAMBIAR_FECHA-")],
        [sg.Text('Campo 2', size=(15,1)), sg.Input(size=(30,1),key='-EMPRESA-')],
        [sg.Text('Campo 3', size=(15,1)), sg.Input(size=(30,1),key='-CUIT-')],
        [sg.Text('Campo 4', size=(15,1)), sg.Input(size=(30,1),key='-TELEFONO-')],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    layout2 = [
        [sg.Text('Sección de ayuda',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Multiline("""1. Presione en el boton cambiar fecha.
2. Seleccione la fecha deseada.
3. Confirme la operación""",size=(50,10))]
    ]

    layout = [
        [sg.Text('Sección organizada usando columnas')],
        [sg.HorizontalSeparator()],
        # Columnas
        [sg.Column(layout1, element_justification='c'), sg.Column(layout2, element_justification='c')],
        [sg.HorizontalSeparator()],
        [sg.Text('Mensaje debajo de las columnas')],
        [sg.Sizegrip()]
    ]

    window = sg.Window('Ventana con columnas', layout, font=(font_name,font_size), modal=True, resizable=True)
    return window