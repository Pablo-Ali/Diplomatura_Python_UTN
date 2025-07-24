import socket

"""
PASO 1 - Creamos el objeto socket
PASO 2 (opcional) - El método bind() se utiliza p
"""

clientesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.100.29'
# host = socket.gethostname() # Esta es la dirección IP del servidor
puerto = 456
clientesocket.connect((host, puerto))
mensaje = clientesocket.recv(1024)
clientesocket.close()
print(mensaje.decode('ascii'))