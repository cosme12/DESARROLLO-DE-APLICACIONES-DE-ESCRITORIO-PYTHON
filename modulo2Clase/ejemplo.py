import PySimpleGUI as sg                      # Parte 1 - Importamos

# Definimos el contenido de la ventana
layout = [  
        [sg.Text("Como te llamas?                    "), sg.InputText()],
        [sg.Text("Cual es tu edad?                    "), sg.InputText()],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]

# Creamos la ventana
window = sg.Window('Titulo de la ventana', layout)  # Parte 3 - Definimos la ventana
                                                
# Dibujamos la ventana y leemos los eventos
event, values = window.read()                 # Parte 4 - Loop de eventos


# Cerramos la ventana
window.close()