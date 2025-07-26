import socket
import funciones

def iniciar_servidor():
    '''
    Función que permite abrir un servidor desde un hilo de ejecución
    creado en el controlador. Toma la fecha actual y la IP y genera
    un registro con los datos. Se cierra al finalizar.
    '''
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname() # Esta es la IP del servidor
    puerto = 456 # Puerto en el cual estoy escuchando
    print(host)

    try:
        serversocket.bind((host, puerto))
        serversocket.listen(1) # solo se conecta una vez

        clientesocket,address = serversocket.accept()

        try:
            # Obtengo la fecha actual
            fecha_formateada = funciones.generar_fecha()

            # Creo la cadena a registrar
            log = f"{fecha_formateada} - Inicio de sesión desde IP: {address[0]}\n"

            # Realizo el registro
            with open("log_servidor.txt", "a", encoding="utf-8") as archivo:
                archivo.write(log)

        except Exception as e:
            # Genero un registro con el error
            with open("log_errores.txt", "a", encoding="utf-8") as archivo_e:
                archivo_e.write(f"ERROR: No se pudo añadir entrada al log: {e}\n")
            # Cierro la conexión
            clientesocket.close()
    
    finally:    
        # Cierro la conexión
        clientesocket.close()