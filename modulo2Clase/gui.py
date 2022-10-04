import PySimpleGUI as sg
import os

carpeta = sg.popup_get_folder('Elija una carpeta donde crear los archivos')

if not carpeta:
    sg.popup_error('No se seleccionó ninguna carpeta')
    exit(0)

nombre = sg.popup_get_text('Elija un nombre para los archivos')

confirmar = sg.popup_ok_cancel('¿Desea crear los 3 archivos en la carpeta {0} con el nombre {1}?'.format(carpeta, nombre))
if confirmar == 'Cancel':
    sg.popup('Operacion cancelada')
    exit(0)
else:
    # Llama a programa_antiguo.py y le pasa los flags -c y -n con los valores de carpeta y nombre
    os.system('python programa_antiguo.exe -c {0} -n {1}'.format(carpeta, nombre)) 
    sg.popup('Archivos creados exitosamente')

