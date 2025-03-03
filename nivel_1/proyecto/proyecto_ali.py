import sqlite3
from tkinter import *
from tkinter import ttk


# Funciones
def crear_base():
    conexion = sqlite3.connect("mibase.db")
    return conexion

conectar = crear_base()

def guardar():
    pass

def eliminar():
    pass

def actualizar():
    pass

def crear_base():
    pass

# apertura / creación de la base
conexion = crear_base()

# apertura del bucle principal
root = Tk()

# variables de tkinter

var_titulo = StringVar()
var_autor = StringVar()
var_genero = StringVar()
var_stock = IntVar()

# maquetación

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
entry_titulo.grid(row=1, column=1)
entry_autor = Entry(root, textvariable=var_autor, width=25)
entry_autor.grid(row=2, column=1)
entry_genero = Entry(root, textvariable=var_genero, width=25)
entry_genero.grid(row=3, column=1)
entry_stock = Entry(root, textvariable=var_stock, width=10)
entry_stock.grid(row=4, column=1)

# botones
boton_guardar = Button(root, text="Guardar", command=guardar)
boton_guardar.grid(row=5, column=1)

boton_borrar = Button(root, text="Eliminar", command=eliminar)
boton_borrar.grid(row=6, column=1)

# tree
tree = ttk.Treeview(root)

tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=100, anchor=W)
tree.column("col2", width=100, minwidth=100, anchor=W)
tree.column("col3", width=100, minwidth=100, anchor=W)
tree.column("col4", width=50, minwidth=50, anchor=W)

tree.heading("#0", text="ID")
tree.heading("col1", text="Título")
tree.heading("col2", text="Autor")
tree.heading("col3", text="Género")
tree.heading("col4", text="Stock")

tree.grid(column=0, row=7, columnspan=5)


# cierre del bucle
root.mainloop() 

#cierre de la base
conexion.close()
