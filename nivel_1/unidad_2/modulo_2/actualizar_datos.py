import sqlite3

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

def actualizar(conexion, mi_id, nombre):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (nombre, mi_id)
    sql = "UPDATE personas SET nombre = ? WHERE id = ?;"
    cursor.execute(sql, data)
    conexion.commit()

conexion = crear_base()
actualizar(conexion, 2, "Josefa")
conexion.close()