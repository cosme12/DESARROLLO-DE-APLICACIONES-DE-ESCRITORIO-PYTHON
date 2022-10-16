import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('SystemDefault')

def build():

    layout1 = [
        [sg.Text('Formulario generico',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('Campo 1', size=(15,1)), sg.Spin(list(range(99999)), size=(10, 1), key="-CODIGO-")],
        [sg.Text('Checkbox', size=(15,1)), sg.Checkbox('Ya se encuentra inscripto', key="-CHECKBOX-")],
        [sg.Text('Radio', size=(15,1)), sg.Radio('Local', "RADIO1", default=True, key="-RADIO1-"), sg.Radio('Visitante', "RADIO1", key="-RADIO2-")],
        [sg.Text('Campo 4', size=(15,1)), sg.Input(size=(30,1),key='-TELEFONO-')],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    layout2 = [
        [sg.Text('Sección de ayuda',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Image("src/resources/images/provincia.png")],
        [sg.Text("""El elemento Tab es otro contenedor de elementos que permite organizar la ventana en pestañas.
Para agregar un elemento Tab a la ventana, se debe agregar un elemento TabGroup al layout de la ventana.
El elemento TabGroup recibe como parámetro un listado de elementos Tab.
Cada elemento Tab recibe como parámetro un listado de elementos que se mostrarán en la pestaña.
El elemento Image permite mostrar una imagen en la ventana.""")]
    ]

    layout = [
        [sg.Text('Ejemplo de uso de Tabs')],
        [sg.HorizontalSeparator()],
        [sg.TabGroup([[sg.Tab('Tab 1', layout1), sg.Tab('Tab 2', layout2)]])],
        [sg.Text('Mensaje debajo de los tabs')]
    ]

    window = sg.Window('Ejemplo de elemento tabs', layout, font=(font_name,font_size), modal=True)
    return window