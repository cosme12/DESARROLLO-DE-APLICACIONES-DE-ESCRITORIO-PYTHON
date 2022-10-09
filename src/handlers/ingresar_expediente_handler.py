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