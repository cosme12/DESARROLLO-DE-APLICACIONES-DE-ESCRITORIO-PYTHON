import PySimpleGUI as sg

sg.theme("Topanga")

layout = [ 
    [sg.Text('Ingresá un numero'), sg.Spin([i for i in range(1, 100)], size=(5,1))],
    [sg.Text('Ingresá segundo valor'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancelar')]
]

window = sg.Window("Ventana persistente", layout, margins=(200, 150))

while True:
    event, values = window.read()

    #validar que los valores ingresados sean numeros
    if event == "Ok":
        try:
            int(values[0])
        except ValueError:
            sg.popup_error("Ingresá solo números")

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break
    print('Datos ingresados: ', values)

window.close()