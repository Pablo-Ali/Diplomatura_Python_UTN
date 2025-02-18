from tkinter import *

# iniciamos el bucle principal de la ventana emergente
root = Tk()
e = Entry(root) # Entry es un widget de ingreso de datos. Lo ponemos dentro de root
e.pack() # maquetamos con pack

#################
c = 4
d = "Mi número es: " + str(c)

#var = IntVar() # entero en Tkinter
var = StringVar() # Str en Tkinter
e.config(textvariable=var) # la variable puede poner o sacar información del campo de entrada
var.set(d) # ponemos el valor de d en el campo de entrada


root.mainloop() # cierre del bucle principal