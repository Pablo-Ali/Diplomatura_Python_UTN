from datetime import datetime
import socket


def generar_fecha() -> str:
    '''
    Función que toma la fecha actual y la retorna
    como una cadena formateada como DD/MM/YYYY
    '''
    # Obtengo la fecha actual
    fecha_actual = datetime.now()

    # Formateo
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    return fecha_formateada

def conectar_servidor() -> None:
    '''
    Función que permite conectar al cliente con el servidor.
    '''
    try:
        clientesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()  # IP del servidor (en local)
        puerto = 456

        clientesocket.connect((host, puerto))  # Conexión

    except Exception as e:
        with open("log_errores.txt", "a", encoding="utf-8") as archivo_e:
            archivo_e.write(f"ERROR: No se pudo añadir entrada al log: {e}\n")

    finally:
        clientesocket.close()