import sqlite3

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

def borrar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id, ) # cuando es un solo elemento, hay que dejar la coma para que lo tome como una tupla
    sql = "DELETE FROM personas WHERE id = ?;"
    cursor.execute(sql, data)
    conexion.commit()

conexion = crear_base()
borrar(conexion, 3)
conexion.close()