import sqlite3

def crear_base():
    conectar = sqlite3.connect("mibase.db")
    return conectar

def borrar(conectar, mi_id):
    cursor = conectar.cursor()
    mi_id = int(mi_id)
    data = (mi_id, ) # cuando es un solo elemento, hay que dejar la coma para que lo tome como una tupla
    sql = "DELETE FROM personas WHERE id = ?;"
    cursor.execute(sql, data)
    conectar.commit()

conectar = crear_base()
borrar(conectar, 3)