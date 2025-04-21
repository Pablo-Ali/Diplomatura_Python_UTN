import sys
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import N 
from tkinter import E
from tkinter import W

from PIL import Image
from PIL import ImageTk

from modelo import actualizar
from modelo import buscar_libro
from modelo import eliminar
from modelo import guardar
from modelo import imprimir_registros
from modelo import conexion

def vista_principal(root):
    # ruta de la imagen según sistema operativo
    ruta_script = sys.path[0]

    if sys.platform == "win32": # método de sys robado de chat gpt para poder usar el script en mi notebok con fedora y en mi pc de escritorio con windows
        ruta_imagen = ruta_script + "\\" + "libros.png"
    else:
        ruta_imagen = ruta_script + "/" + "libros.png"
        
    # variables de tkinter
    var_titulo = StringVar()
    var_autor = StringVar()
    var_genero = StringVar()
    var_stock = IntVar()

    # pongo el fondo en negro
    root.configure(bg="black")

    # carga y redimensión de la imagen
    imagen_original = Image.open(ruta_imagen)
    imagen_redimensionada = imagen_original.resize((100, 100))
    imagen = ImageTk.PhotoImage(imagen_redimensionada)

    label_imagen_izq = Label(root, image=imagen, bg="black")
    label_imagen_izq.grid(row=0, column=2, sticky=N)
    label_imagen_der = Label(root, image=imagen, bg="black")
    label_imagen_der.grid(row=0, column=0, sticky=N)

    # título app
    titulo_app = Label(root, text="Stock Librería", bg="black", fg="white", font=('', 30, 'bold'))
    titulo_app.grid(row=0, column=1, pady=25, sticky=N)

    # etiquetas de los entry

    titulo = Label(root, text="Título", bg="black", fg="white", font=('', 10, 'bold'))
    titulo.grid(row=1, column=0, pady=2, sticky=E)
    autor = Label(root, text="Autor", bg="black", fg="white", font=('', 10, 'bold'))
    autor.grid(row=2, column=0, pady=2, sticky=E)
    genero = Label(root, text="Género", bg="black", fg="white", font=('', 10, 'bold'))
    genero.grid(row=3, column=0, pady=2, sticky=E)
    stock = Label(root, text="Stock", bg="black", fg="white", font=('', 10, 'bold'))
    stock.grid(row=4, column=0, pady=2, sticky=E)

    # entrys
    entry_titulo = Entry(root, textvariable=var_titulo, width=25, bg="gray", fg="white", font=('', 10, 'bold'))
    entry_titulo.grid(row=1, column=1, pady=2)
    entry_autor = Entry(root, textvariable=var_autor, width=25, bg="gray", fg="white", font=('', 10, 'bold'))
    entry_autor.grid(row=2, column=1, pady=2)
    entry_genero = Entry(root, textvariable=var_genero, width=25, bg="gray", fg="white", font=('', 10, 'bold'))
    entry_genero.grid(row=3, column=1, pady=2)
    entry_stock = Entry(root, textvariable=var_stock, width=10, bg="gray", fg="white", font=('', 10, 'bold'))
    entry_stock.grid(row=4, column=1, pady=2)

    # botones
    boton_guardar = Button(root, text="Guardar", width=10, bg="gray", fg="white", font=('', 10, 'bold'), command=lambda: guardar(conexion, var_titulo, var_autor, var_genero, var_stock, tree))
    boton_guardar.grid(row=5, column=1, pady=2, sticky=W)

    boton_borrar = Button(root, text="Eliminar", width=10, bg="gray", fg="white", font=('', 10, 'bold'), command=lambda : eliminar(conexion, tree))
    boton_borrar.grid(row=5, column=1, pady=2, sticky=E)

    boton_actualizar_stock = Button(root, text="Actualizar\nStock", width=10, bg="gray", fg="white", font=('', 10, 'bold'), command=lambda: actualizar(conexion, tree, var_stock))
    boton_actualizar_stock.grid(row=6, column=1, pady=2, sticky=W)

    boton_buscar = Button(root, text="Buscar\npor ID", width=10, bg="gray", fg="white", font=('', 10, 'bold'), command=lambda: buscar_libro(conexion))
    boton_buscar.grid(row=6, column=1, pady=2, sticky=E)

    # tree
    tree = ttk.Treeview(root)

    tree["columns"] = ("col1", "col2", "col3", "col4")
    tree.column("#0", width=50, minwidth=50, anchor=W)
    tree.column("col1", width=300, minwidth=300, anchor=W)
    tree.column("col2", width=150, minwidth=150, anchor=W)
    tree.column("col3", width=100, minwidth=100, anchor=W)
    tree.column("col4", width=50, minwidth=50, anchor=W)

    tree.heading("#0", text="ID")
    tree.heading("col1", text="Título")
    tree.heading("col2", text="Autor")
    tree.heading("col3", text="Género")
    tree.heading("col4", text="Stock")

    tree.grid(column=0, row=7, columnspan=5)

    # cargar registros
    imprimir_registros(conexion, tree)