from datetime import datetime
import socket


def generar_fecha() -> str:
    '''
    Función que toma la fecha y hora actuales y las retorna
    como una cadena con formato ISO 8601 extendido
    '''
    # Obtengo la fecha actual
    fecha_actual = datetime.now()

    # Formateo
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    return fecha_formateada

# Robada a ChatGPT porque me fallaba el socket.gethostname() cuando intentaba ejecutar el código en mi máquina de Linux
def obtener_ip_local():
    """
    Devuelve la IP local de la máquina (por ejemplo, 192.168.x.x o 127.0.0.1).
    Funciona en Windows, Linux y macOS.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # No se envía nada, esto es solo para obtener la IP local
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"  # Fallback


def conectar_servidor() -> None:
    '''
    Función que permite conectar al cliente con el servidor.
    '''
    # Declaro la variable para poder cerrarla en el finally en caso de error
    clientesocket = None
    try:
        clientesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #host = socket.gethostname()  # IP del servidor (en local)
        host = obtener_ip_local()
        puerto = 65432 # Puerto en el cual está escuchando el servidor (número alto para que no lance error en Linux)

        clientesocket.connect((host, puerto))  # Conexión

    except Exception as e:
        with open("log_errores.txt", "a", encoding="utf-8") as archivo_e:
            archivo_e.write(f"ERROR: No se pudo añadir entrada al log: {e}\n")

    finally:
        clientesocket.close()