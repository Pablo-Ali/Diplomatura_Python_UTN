import sqlite3

def crear_base():
    conectar = sqlite3.connect("mibase.db")
    return conectar

def actualizar(conectar, mi_id, nombre):
    cursor = conectar.cursor()
    mi_id = int(mi_id)
    data = (nombre, mi_id)
    sql = "UPDATE personas SET nombre = ? WHERE id = ?;"
    cursor.execute(sql, data)
    conectar.commit()

conectar = crear_base()
actualizar(conectar, 2, "Josefa")