import sqlite3

def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

def seleccionar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id, )
    sql = "SELECT * FROM personas WHERE id = ?;"
    cursor.execute(sql, data)
    conexion.commit()

    # imprimir el resultado
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

conexion = crear_base()
seleccionar(conexion, 2)
conexion.close()