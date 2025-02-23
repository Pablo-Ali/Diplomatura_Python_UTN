from tkinter import *


root = Tk()


###
def hola():
    print("Hola")
###

menubar = Menu(root)

menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir", command=hola)
menu_archivo.add_command(label="Guardar", command=hola)
menu_archivo.add_separator() # agrego un separador
menu_archivo.add_command(label="salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo) # agrego los comandos anteriores en modo cascada


menu_edicion = Menu(menubar, tearoff=0)
menu_edicion.add_command(label="Abrir", command=hola)
menu_edicion.add_command(label="Guardar", command=hola)
menu_edicion.add_separator()
menu_edicion.add_command(label="salir", command=root.quit)
menubar.add_cascade(label="Editar", menu=menu_edicion)
# Agregamos un submenú

submenu = Menu(menu_edicion, tearoff=True)
submenu.add_command(label="Cambiar color", command=hola)
submenu.add_command(label="Rotar imagen", command=hola)
menu_edicion.add_cascade(label="Otros", menu=submenu)

root.config(menu=menubar) # muestro en pantalla el menú
root.mainloop()