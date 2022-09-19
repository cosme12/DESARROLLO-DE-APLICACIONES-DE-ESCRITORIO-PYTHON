import PySimpleGUI as sg                      # Parte 1 - Importamos

# Definimos el contenido de la ventana
layout = [  [sg.Text("Bienvenidos al curso de intefaz gráfica con Python.\n\n🚧 Cualquier duda podés escribir en el foro.")],     # Parte 2 - El Layout
        ]

# Creamos la ventana
window = sg.Window('Titulo de la ventana', layout)  # Parte 2 - Definimos la ventana
                                                
# Dibujamos la ventana y leemos los eventos
event, values = window.read()                 # Parte 3 - Loop de eventos

# Cerramos la ventana
window.close()                                # Parte 4 - Cerramos la ventana
