import sqlite3
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

from mis_regex import MisRegex
from alertas import MisAlertas

class MiBase():
    def crear_base(self, ):
        conexion = sqlite3.connect("base_libreria.db")
        return conexion

    def crear_tabla(self, conexion):
        cursor = conexion.cursor()
        sql = "CREATE TABLE libros(id integer PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT NOT NULL, genero TEXT NOT NULL, stock integer NOT NULL)"
        cursor.execute(sql)
        conexion.commit()

class MiCRUD():
    def guardar(self, conexion, titulo, autor, genero, stock, mi_treeview):
        cursor = conexion.cursor()
        data = (titulo.get(), autor.get(), genero.get(),stock.get())
        reg_cadena = MisRegex()
        
        if titulo.get() == "":
            showinfo("Error", "Debe añadir un título")
        elif not reg_cadena.verificar_reg_cadena(autor.get()):
            showinfo("Error", "Debe añadir un autor con caracteres válidos")
        elif not reg_cadena.verificar_reg_cadena(genero.get()):
            showinfo("Error", "Debe añadir un género con caracteres válidos")
        elif stock.get() < 0:
            showinfo("Error", "El stock no puede ser negativo")
        else:
            sql = "INSERT INTO libros(titulo, autor, genero, stock) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, data)
            conexion.commit()
            
            titulo.set("")
            autor.set("")
            genero.set("")
            stock.set(0)

        imprimir_registros(conexion, mi_treeview)


    def eliminar(self, conexion, mi_treeview):
        valor = mi_treeview.selection()

        if not valor:  # Si no hay nada seleccionado, salir de la función
            showinfo("Error", "Debe seleccionar un registro para eliminar")
            return 
        
        item = mi_treeview.item(valor)
        
        alerta = MisAlertas()

        if alerta.confirmar_borrar():
            showinfo("Confirmar", "Registro eliminado")
            cursor = conexion.cursor()
            id = item['text']
            data = (id, )
            sql = "DELETE FROM libros WHERE id = ?;"
            cursor.execute(sql, data)
            conexion.commit()
            mi_treeview.delete(valor)
        else:
            showinfo("Cancelar", "Acción cancelada")


    def actualizar(self, conexion, mi_treeview, stock):
        valor = mi_treeview.selection()

        if not valor:  # Si no hay nada seleccionado, salir de la función
            showinfo("Error", "Debe seleccionar un registro para actualizar")
            return 
        
        item = mi_treeview.item(valor)
        
        alerta = MisAlertas()
        
        if alerta.confirmar_actualizar():
            nuevo_stock = stock.get()
            if nuevo_stock >= 0:
                showinfo("Confirmar", "Stock actualizado")
                cursor = conexion.cursor()
                id = item['text']
                data = (nuevo_stock, id)
                sql = "UPDATE libros SET stock = ? WHERE id = ?;"
                cursor.execute(sql, data)
                conexion.commit()
                imprimir_registros(conexion, mi_treeview)
            else:
                showinfo("Error", "El stock no puede ser negativo")
        else:
            showinfo("Cancelar", "Acción cancelada")

        stock.set(0)

    def buscar_libro(self, conexion):
        id_libro = askstring("Búsqueda", "Ingrese el ID del libro a buscar")

        # corroboro que ingrese datos correctos
        if (id_libro is None) or (id_libro.isdigit() == False):
            showinfo("Error", "Debe ingresar un número válido")
            return

        cursor = conexion.cursor()
        data = (id_libro, )
        sql = "SELECT * FROM libros WHERE id = ?;"
        cursor.execute(sql, data)
        conexion.commit()

        ##############################################################################################################
        # esta parte se la robé a chat gpt
        libro = cursor.fetchone()

        if libro:
            mensaje = f"ID: {libro[0]}\nTítulo: {libro[1]}\nAutor: {libro[2]}\nGénero: {libro[3]}\nStock: {libro[4]}"
            showinfo("Libro encontrado", mensaje)
        else:
            showinfo("No encontrado", "No existe un libro con ese ID.")
        ##############################################################################################################

def imprimir_registros(conexion, mi_treeview):
    # limpiar tree
    for item in mi_treeview.get_children():
        mi_treeview.delete(item)

    # recuperar registros con SELECT *
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    registros = cursor.fetchall()

    # Insertar los datos en el Treeview
    for registro in registros:
        mi_treeview.insert("", "end", text=registro[0], values=(registro[1], registro[2], registro[3], registro[4]))


############################################################
# PERSISTENCIA
############################################################

# apertura / creación de la base y la tabla
base = MiBase()
conexion = base.crear_base()

try:
    base.crear_tabla(conexion)
except:
    print("Tabla ya creada")
