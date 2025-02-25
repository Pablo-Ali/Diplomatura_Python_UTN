import sqlite3

def crear_base():
    conectar = sqlite3.connect("mibase.db")
    return conectar

def seleccionar(conectar, mi_id):
    cursor = conectar.cursor()
    mi_id = int(mi_id)
    data = (mi_id, )
    sql = "SELECT * FROM personas WHERE id = ?;"
    cursor.execute(sql, data)
    conectar.commit()

    # imprimir el resultado
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

conectar = crear_base()
seleccionar(conectar, 2)
conectar.close()