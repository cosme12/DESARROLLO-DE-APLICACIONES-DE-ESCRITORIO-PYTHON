import PySimpleGUI as sg
from src.windows import nueva_ventana1


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
    

    window = nueva_ventana1.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

    return window

