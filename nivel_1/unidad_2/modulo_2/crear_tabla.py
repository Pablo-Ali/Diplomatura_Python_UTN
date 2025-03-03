import sqlite3

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sql = "CREATE TABLE personas(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    conexion.commit()

conexion = crear_base()
crear_tabla(conexion)
conexion.close()