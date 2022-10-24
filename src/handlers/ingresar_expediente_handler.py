import json


def agregar_expediente(datos_nuevos):
    """
    Guarda los datos de un nuevo expediente en el archivo de expedientes.json
    """
    with open('files/expedientes.json', 'r') as archivo:
        lista_expedientes = json.load(archivo)  # carga todos los expedientes
    # Obtener el último id, si no hay ningún expediente, el id es 1
    if not lista_expedientes:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_expedientes, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_expedientes.append(datos_nuevos)
    with open('files/expedientes.json', 'w') as archivo:
        json.dump(lista_expedientes, archivo, indent=4)


def leer_archivo():
    """
    Lee todos los datos de expedientes.json y los devuelve como una lista de diccionarios
    """
    with open('files/expedientes.json', 'r') as file:  # r para leer
        datos = json.load(file)  # json.load(file) para leerlo como un diccionario
    # Convierte los datos a una lista de listas para que se pueda mostrar en la tabla
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-CODIGO-"], dato["-EMPRESA-"], dato["-CUIT-"], dato["-TELEFONO-"], dato["-CATEGORIA-"]])
    # Lo mismo pero escrito en una sola linea
    #datos = [[str(dato['id']), dato['empresa'], dato['cuit'], dato['telefono'], dato['categoria']] for dato in datos]
    return datos_para_tabla

