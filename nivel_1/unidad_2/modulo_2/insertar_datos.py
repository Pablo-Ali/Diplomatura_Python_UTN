import sqlite3

def crear_base():
    conectar = sqlite3.connect("mibase.db")
    return conectar

def insertar(conectar, mi_id, nombre):
    cursor = conectar.cursor()
    mi_id = int(mi_id)
    data = (mi_id, nombre)
    sql = "INSERT INTO personas(id, nombre) VALUES (?, ?);"
    cursor.execute(sql, data)
    conectar.commit()

conectar = crear_base()
insertar(conectar, 3, "Anna3")