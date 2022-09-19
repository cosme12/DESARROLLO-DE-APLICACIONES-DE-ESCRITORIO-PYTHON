import PySimpleGUI as sg                      # Parte 1 - Importamos

# Definimos el contenido de la ventana
layout = [  [sg.Text("Como te llamas?")],     # Parte 2 - El Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Creamos la ventana
window = sg.Window('Titulo de la ventana', layout)  # Parte 3 - Definimos la ventana
                                                
# Dibujamos la ventana y leemos los eventos
event, values = window.read()                 # Parte 4 - Loop de eventos

# Hacemos algo con la información obtenida
print('Hola', values[0], "! Gracias por sumarte al curso de PySimpleGUI")

# Cerramos la ventana
window.close()                                # Parte 5 - Cerramos la ventana
