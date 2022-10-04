import PySimpleGUI as sg
import os


carpeta = sg.popup_get_folder('Elija una carpeta donde crear los archivos')

nombre = sg.popup_get_text('Elija un nombre para los archivos')

os.system('programa_antiguo.exe -c {0} -n {1}'.format(carpeta, nombre))
#os.system("programa_antiguo.exe -c " + carpeta + " -n " + nombre)

sg.popup('Archivos creados exitosamente')

