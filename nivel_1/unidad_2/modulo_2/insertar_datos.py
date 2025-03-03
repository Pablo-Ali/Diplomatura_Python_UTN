import sqlite3

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

def insertar(conexion, mi_id, nombre):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id, nombre)
    sql = "INSERT INTO personas(id, nombre) VALUES (?, ?);"
    cursor.execute(sql, data)
    conexion.commit()

conexion = crear_base()
insertar(conexion, 3, "Anna3")
conexion.close()