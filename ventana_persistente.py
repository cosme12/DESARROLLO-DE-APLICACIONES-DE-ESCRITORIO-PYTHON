import PySimpleGUI as sg

#sg.theme('SystemDefault')   # Tema de la ventana
layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
        [sg.Text('Ingresá segundo valor'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancelar')] 
    ]

window = sg.Window("Ventana persistente", layout, margins=(200, 150))


while True:
    event, values = window.read()

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break

    print('Datos ingresados: ', values)

window.close()
