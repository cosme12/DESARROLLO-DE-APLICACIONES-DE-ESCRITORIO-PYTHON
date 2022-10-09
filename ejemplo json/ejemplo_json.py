import json

def leer_archivo():
    """
    Lee todos los datos de compras.json y los devuelve como una lista de diccionarios
    """
    with open('compras.json', 'r') as file:  # r para leer
        datos = json.load(file)  # json.load(file) para leerlo como un diccionario
    return datos


def guardar_datos_en_archivo(datos):
    """
    Guarda un diccionario en el archivo nuevo_archivo.json
    """
    with open('nuevo_archivo.json', 'w') as file:  # w para escribir
        json.dump(datos, file, indent=4)  # indent=4 para que se vea mejor


if __name__ == '__main__':
    datos = leer_archivo()
    print(datos)
    datos = {'nombre': 'Juan', 'edad': 20}
    guardar_datos_en_archivo(datos)

