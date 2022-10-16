import PySimpleGUI as sg
from src.windows import nueva_ventana2


def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    

    window = nueva_ventana2.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-CAMBIAR_FECHA-':
            sg.theme('Topanga')
            nueva_fecha = sg.popup_get_date(locale="es")
            sg.theme('SystemDefault')
            if nueva_fecha:
                window['-FECHA_TEXTO-'].update(f'Fecha: {nueva_fecha[1]}/{nueva_fecha[0]}/{nueva_fecha[2]}')

    return window

