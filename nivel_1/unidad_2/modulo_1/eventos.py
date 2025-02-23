from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *


root = Tk()

###
def funcion_ruta():
    ruta = askopenfilename()
    print(ruta)

def funcion_color():
    resultado = askcolor(color="#00ff00", title="El título")
    print(resultado)
    print(resultado[1])

###

boton_ruta = Button(root, text="Ruta", command=funcion_ruta)
boton_ruta.grid(row=2, column=1)

boton_color = Button(root, text="Color", command=funcion_color)
boton_color.grid(row=3, column=1)

root.mainloop()