from tkinter import *
from tkinter.messagebox import *

root = Tk()

# lanzar ventanas emergentes:

###
def funcion_e():
    showerror("Titulo del mensaje", "Contenido del mensaje") # permite mostrar mensajes de error

def funcion_s():
    if askyesno("Titulo de la consulta", "Contenido de la consulta"): # permite que el ususario tome una decisión
        showinfo("Si", "Mensaje de información")
    else:
        showinfo("No", "Está a punto de salir")
###

boton_error = Button(root, text="Error", command=funcion_e)
boton_error.grid(row=2, column=1)

boton_show = Button(root, text="Show", command=funcion_s)
boton_show.grid(row=3, column=1)

root.mainloop()