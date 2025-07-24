import json
import os
from datetime import datetime

#########################################################################################################################################
# AHORA HAY QUE TOMAR TODO ESTO Y GENERAR UNO O MÁS DECORADORES PARA QUE, CADA VEZ QUE SE INGRESE AL SERVIDOR, SE REGISTRE EN UN ARCHIVO.
# LUEGO, REALIZAR UN DECORADOR QUE REGISTRE CADA VEZ QUE SE CARGUE UN LIBRO NUEVO EN LA BASE DE DATOS DEL PROGRAMA.
# SOLO QUEDA VER CÓMO IMPLEMENTAR EL PATRÓN OBSERVADOR, QUIZÁS PARA MODIFICACIONES DE STOCK, O ALGO.
#########################################################################################################################################

def generar_fecha() -> str:
    '''
    Función que toma la fecha actual y la retorna
    como una cadena formateada como DD/MM/YYYY
    '''
    # Obtén la fecha actual
    fecha_actual = datetime.now()

    # Formateo
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    return fecha_formateada


def leer_json(nombre_archivo : str) -> list:
    '''
    Función que lee un archivo json y retorna una lista con su contenido.
    En caso de no existir, retorna una lista vacía.
    '''
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            lista = json.load(archivo)
        return lista
    else:
        return []


def registrar_ingreso_json(nombre_archivo: str) -> bool:
    '''
    Función que registra los datos de ingreso al sistema en un archivo JSON.
    Si el archivo ya contiene datos, agrega el nuevo registro sin eliminar los existentes.
    '''
    nuevo_registro = ["Ingreso registrado", generar_fecha()]

    datos = leer_json(nombre_archivo)

    # Agregamos el nuevo ingreso
    datos.append(nuevo_registro)

    # Sobrescribimos el archivo con la lista actualizada
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return True