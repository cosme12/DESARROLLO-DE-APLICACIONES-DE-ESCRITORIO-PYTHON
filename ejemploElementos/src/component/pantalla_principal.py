import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_expediente, nueva_ventana1, nueva_ventana2
from src.handlers import ingresar_expediente_handler


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
    sg.theme('SystemDefault')

    window = pantalla_principal.build()
    # Actualizamos la tabla al iniciar el sistema
    window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente_handler.leer_archivo())

    while True:
        event, values = window.read()
        print(event)

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_EXPEDIENTE-':
            ingresar_expediente.start()
            window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente_handler.leer_archivo())

        elif event == 'Ventana 1':
            nueva_ventana1.start()

        elif event == 'Ventana 2':
            nueva_ventana2.start()
        
        # Las tablas tambien tienen values que se muestran cuando se selecciona algun elemento
        # Si se selecciona una opcion de la tabla, se hace click derecho y se presiona eliminar
        elif event == "Eliminar seleccion" and window["-TABLA_EXPEDIENTE-"].get():
            if values["-TABLA_EXPEDIENTE-"]:
                print(f'Fila selecciona de la tabla: {values["-TABLA_EXPEDIENTE-"][0]}')
                expediente_seleccionado = window["-TABLA_EXPEDIENTE-"].get()[values["-TABLA_EXPEDIENTE-"][0]]
                print(expediente_seleccionado)
        
        else:
            sg.popup_error("Este evento aún no hace nada. Pruebe las Ventanas nuevas", title="Error")

    return window

