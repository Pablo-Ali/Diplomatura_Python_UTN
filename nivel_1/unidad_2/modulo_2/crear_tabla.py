import sqlite3

def crear_base():
    conectar = sqlite3.connect("mibase.db")
    return conectar

def crear_tabla(conectar):
    cursor = conectar.cursor()
    sql = "CREATE TABLE personas(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    conectar.commit()

conectar = crear_base()
crear_tabla(conectar)
conectar.close()