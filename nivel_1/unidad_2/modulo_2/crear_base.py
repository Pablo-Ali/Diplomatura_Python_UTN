import sqlite3

# crear base de datos

# conectar = sqlite3.connect("mibase.db") # si la base no existe, la crea. Si no, la abre
# conectar.close() # cierra la base

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

conexion = crear_base()
conexion.close()
