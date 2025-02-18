from tkinter import *
from tkinter import ttk

mi_id = 0

root = Tk()

var_nombre = StringVar()
var_apellido = StringVar()

nombre = Label(root, text="Nombre")
nombre.grid(row=0, column=0, sticky=W)
apellido = Label(root, text="Apellido") 
apellido.grid(row=1, column=0, sticky=W) 

entry_nombre = Entry(root, textvariable=var_nombre, width=25)
entry_nombre.grid(row=0, column=1)
entry_apellido = Entry(root, textvariable=var_apellido, width=25) 
entry_apellido.grid(row=1, column=1) 

###
def funcion_g():
    global mi_id
    mi_id += 1
    tree.insert("", "end", text=str(mi_id), values=(var_nombre.get(), var_apellido.get()))

def funcion_f():
    global mi_id
    item = tree.focus()
    tree.delete(item)
    mi_id -= 1
###


tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)

tree.grid(column=0, row=4, columnspan=4)


boton_guardar = Button(root, text="Guardar", command=funcion_g)
boton_guardar.grid(row=2, column=1)

boton_borrar = Button(root, text="Eliminar", command=funcion_f)
boton_borrar.grid(row=3, column=1)

root.mainloop() 