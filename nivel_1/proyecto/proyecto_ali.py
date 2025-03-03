import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo

############################################################
# FUNCIONES
############################################################

def crear_base():
    conexion = sqlite3.connect("base_libreria.db")
    return conexion

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sql = "CREATE TABLE libros(id integer PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT NOT NULL, genero TEXT NOT NULL, stock integer NOT NULL)"
    cursor.execute(sql)
    conexion.commit()

def guardar(conexion, titulo, autor, genero, stock, mi_treeview):
    cursor = conexion.cursor()
    data = (titulo.get(), autor.get(), genero.get(),stock.get())
    
    if titulo.get() == "":
        showinfo("Error", "Debe añadir un título")
    elif autor.get() == "":
        showinfo("Error", "Debe añadir un autor")
    elif genero.get() == "":
        showinfo("Error", "Debe añadir un género")
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


def eliminar(conexion, mi_treeview, ):
    valor = mi_treeview.selection()

    if not valor:  # Si no hay nada seleccionado, salir de la función
        showinfo("Error", "Debe seleccionar un registro para eliminar")
        return 
    
    item = mi_treeview.item(valor)
    
    alerta = confirmar_borrar()

    if alerta:
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


def actualizar(conexion, mi_treeview, stock):
    valor = mi_treeview.selection()

    if not valor:  # Si no hay nada seleccionado, salir de la función
        showinfo("Error", "Debe seleccionar un registro para actualizar")
        return 
    
    item = mi_treeview.item(valor)
    
    alerta = confirmar_actualizar()
    
    if alerta:
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

def confirmar_borrar():
    if askyesno("Precaución", "¿Está seguro que desea borrar el registro?"):
        return True
        
    else:
        return False

def confirmar_actualizar():
    if askyesno("Precaución", "¿Está seguro que desea cambiar el stock?"):
        return True
        
    else:
        return False

############################################################
# PERSISTENCIA Y LÓGICA
############################################################

# apertura / creación de la base
conexion = crear_base()

try:
    crear_tabla(conexion)
except:
    print("Tabla ya creada")

############################################################
# IGU
############################################################

# apertura del bucle principal
root = Tk()

# variables de tkinter
var_titulo = StringVar()
var_autor = StringVar()
var_genero = StringVar()
var_stock = IntVar()

# etiquetas
titulo_app = Label(root, text="Stock Librería")
titulo_app.grid(row=0, column=1, sticky=N)

titulo = Label(root, text="Título")
titulo.grid(row=1, column=0, sticky=W)
autor = Label(root, text="Autor")
autor.grid(row=2, column=0, sticky=W)
genero = Label(root, text="Género")
genero.grid(row=3, column=0, sticky=W)
stock = Label(root, text="Stock")
stock.grid(row=4, column=0, sticky=W)


# entrys
entry_titulo = Entry(root, textvariable=var_titulo, width=25)
entry_titulo.grid(row=1, column=1, sticky=W)
entry_autor = Entry(root, textvariable=var_autor, width=25)
entry_autor.grid(row=2, column=1, sticky=W)
entry_genero = Entry(root, textvariable=var_genero, width=25)
entry_genero.grid(row=3, column=1, sticky=W)
entry_stock = Entry(root, textvariable=var_stock, width=10)
entry_stock.grid(row=4, column=1, sticky=W)

# botones
boton_guardar = Button(root, text="Guardar", command=lambda: guardar(conexion, var_titulo, var_autor, var_genero, var_stock, tree))
boton_guardar.grid(row=5, column=1, sticky=W)

boton_borrar = Button(root, text="Eliminar", command=lambda : eliminar(conexion, tree))
boton_borrar.grid(row=6, column=1, sticky=W)

boton_actualizar_stock = Button(root, text="Actualizar Stock", command=lambda: actualizar(conexion, tree, var_stock))
boton_actualizar_stock.grid(row=7, column=1, sticky=W)

# tree
tree = ttk.Treeview(root)

tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=200, anchor=W)
tree.column("col2", width=150, minwidth=150, anchor=W)
tree.column("col3", width=100, minwidth=100, anchor=W)
tree.column("col4", width=50, minwidth=50, anchor=W)

tree.heading("#0", text="ID")
tree.heading("col1", text="Título")
tree.heading("col2", text="Autor")
tree.heading("col3", text="Género")
tree.heading("col4", text="Stock")

tree.grid(column=0, row=8, columnspan=5)

# cargar registros
imprimir_registros(conexion, tree)

# cierre del bucle principal
root.mainloop() 

#cierre de la base
conexion.close()

