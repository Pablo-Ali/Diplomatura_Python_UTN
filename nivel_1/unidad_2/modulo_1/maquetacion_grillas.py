from tkinter import *

"""
No puede haber más de una forma de maquetar a la vez, o usamos grid o usamos pack,
pero no ambas a la vez.
----------------------------------------------------------
Al trabajar con grillas, el .grid debe colocarse aparte de la creación del propio wigdet, de
forma tal que luego pueda editarse la propia grilla, para cambiar el color, por ejemplo, y
no cause problemas con el widget. Ejemplo:
entry_nombre = Entry(root)
entry_nombre.grid(row=1, column=1)
----------------------------------------------------------
sticky nos permite anclar elementos usando puntos cardinales (N, W, E, S) en una parte de la pantalla
"""

root = Tk()

el_id = Label(root, text="id") # coloco el widget de título dentro de la ventana root y con el texto "id"
el_id.grid(row=0, column=0, sticky=W) # metemos el elemento en la grilla
el_nombre = Label(root, text="Nombre")
el_nombre.grid(row=1, column=0, sticky=W) # pegamos a la izquierda el widget con sticky

entry_id = Entry(root) # agregamos los widgets de campo de entrada
entry_id.grid(row=0, column=1) # se lo ubica en la grilla
entry_nombre = Entry(root)
entry_nombre.grid(row=1, column=1)

###
def funcion():
    print("Datos Guardados")
###

boton_guardar = Button(root, text="Guardar", command=funcion)
boton_guardar.grid(row=2, column=1)

root.mainloop()