from peewee import *

from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

from mis_regex import MisRegex
from alertas import MisAlertas

import decoradores

# declaro qué base voy a usar
db = SqliteDatabase("base_libreria_final.db")

# indico que use la base de datos declarada
class BaseModel(Model):
    """
    Clase base que conecta los modelos a la base de datos SQLite.
    """
    class Meta:
        database = db

# creo una clase para cada tabla a crear
class Libros(BaseModel):
    """
    Modelo que representa la tabla 'Libros' en la base de datos.

    Atributos
    ----------
    titulo : CharField
        Título del libro.
    autor : CharField
        Autor del libro.
    genero : CharField
        Género literario del libro.
    stock : IntegerField
        Cantidad de ejemplares disponibles.
    """
    titulo = CharField()
    autor = CharField()
    genero = CharField()
    stock = IntegerField()

# conecto la base
db.connect()

try:
    # creo la tabla de la clase
    db.create_tables([Libros])
except:
    print("Tabla ya creada")

class MiCRUD():
    """
    Clase que encapsula las operaciones CRUD | ABMC sobre el modelo Libros.
    """
    @decoradores.decorador_registrar_libro
    def guardar (self, titulo, autor, genero, stock, mitreeview):
        """
        Guarda un nuevo libro en la base de datos, validando los campos.

        Parámetros
        ----------
        titulo : StringVar
            Título del libro (vía Tkinter).
        autor : StringVar
            Autor del libro.
        genero : StringVar
            Género del libro.
        stock : StringVar
            Cantidad de ejemplares como texto.
        mitreeview : ttk.Treeview
            Tabla de visualización de libros.
        """
        # instancio la clase
        libro = Libros()
        reg_cadena = MisRegex()
        
        # tomo los atributos
        if titulo.get() == "":
            showinfo("Error", "Debe añadir un título")
            return False
        elif not reg_cadena.verificar_reg_cadena(autor.get()):
            showinfo("Error", "Debe añadir un autor con caracteres válidos")
            return False
        elif not reg_cadena.verificar_reg_cadena(genero.get()):
            showinfo("Error", "Debe añadir un género con caracteres válidos")
            return False
        
        try:
            stock_num = int(stock.get())
        except ValueError:
            showinfo("Error", "Debe ingresar un número entero válido para el stock")
            return False
        
        libro.titulo = titulo.get()
        libro.autor = autor.get()
        libro.genero = genero.get()
        libro.stock = stock_num
        
        # lo guardo con peewee
        try:
            libro.save()
        except Exception as e:
            showinfo("Error", f"No se pudo guardar el libro:\n{e}")
            return False

        # pongo los campos en blanco
        titulo.set("")
        autor.set("")
        genero.set("")
        stock.set(0)
        
        # actualizamos el treeview
        self.imprimir_registros(mitreeview)
        
        # retorno para que se ejecute el decorador correctamente
        return True

    def eliminar(self, mitreeview):
        """
        Elimina un libro seleccionado del Treeview y de la base de datos.

        Parámetros
        ----------
        mitreeview : ttk.Treeview
            Tabla de visualización de libros.
        """
        alerta = MisAlertas()

        # selecciono el campo
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        
        if not item_seleccionado:  # Si no hay nada seleccionado, salir de la función
            showinfo("Error", "Debe seleccionar un registro para eliminar")
            return 

        if alerta.confirmar_borrar():
            showinfo("Confirmar", "Registro eliminado")
            # borro la fila con el id seleccionado
            borrar = Libros.get(Libros.id==valor_id["text"])
            borrar.delete_instance()
        else:
            showinfo("Cancelar", "Acción cancelada")
        
        # actualizo el treeview
        self.imprimir_registros(mitreeview)

    def actualizar(self, stock, mitreeview):
        """
        Actualiza el stock del libro seleccionado en el Treeview.

        Parámetros
        ----------
        stock : StringVar
            Nuevo stock a establecer.
        mitreeview : ttk.Treeview
            Tabla de visualización de libros.
        """
        alerta = MisAlertas()
        
        # selecciono el campo
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)

        if not item_seleccionado:  # Si no hay nada seleccionado, salir de la función
            showinfo("Error", "Debe seleccionar un registro para actualizar")
            return
        
        if alerta.confirmar_actualizar():
            try:
                nuevo_stock = int(stock.get())
            except ValueError:
                showinfo("Error", "Debe ingresar un número entero válido para el stock")
                return
            if nuevo_stock >= 0:
                showinfo("Confirmar", "Stock actualizado")
                # actualizo la fila seleccionada en cada uno de sus valores
                actualizar = Libros.update(stock=stock.get()).where(Libros.id==valor_id["text"])
                try:
                    actualizar.execute()
                except Exception as e:
                    showinfo("Error", f"No se pudo actualizar el libro:\n{e}")
                    return
            else:
                showinfo("Error", "El stock no puede ser negativo")
        else:
            showinfo("Cancelar", "Acción cancelada")

        # actualizo el treeview
        self.imprimir_registros(mitreeview)
        stock.set(0)

    def buscar_libro(self):
        """
        Solicita al usuario un ID de libro y muestra la información correspondiente si existe.
        """
        id_libro = askstring("Búsqueda", "Ingrese el ID del libro a buscar")

        # Validación de entrada
        if (id_libro is None) or (not id_libro.isdigit()):
            showinfo("Error", "Debe ingresar un número válido")
            return

        try:
            libro = Libros.get_or_none(Libros.id == int(id_libro))
        except Exception as e:
            showinfo("Error", f"Ocurrió un error al buscar el libro: {e}")
            return

        if libro:
            mensaje = (
                f"ID: {libro.id}\n"
                f"Título: {libro.titulo}\n"
                f"Autor: {libro.autor}\n"
                f"Género: {libro.genero}\n"
                f"Stock: {libro.stock}"
            )
            showinfo("Libro encontrado", mensaje)
        else:
            showinfo("No encontrado", "No existe un libro con ese ID.")



    def imprimir_registros(self, mitreeview):
        """
        Limpia el Treeview y lo repuebla con todos los registros actuales de libros.

        Parámetros
        ----------
        mitreeview : ttk.Treeview
            Tabla donde se muestran los registros.
        """
        # limpieaza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        #imprimir los nuevos datos
        for fila in Libros.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.titulo, fila.autor, fila.genero, fila.stock))


