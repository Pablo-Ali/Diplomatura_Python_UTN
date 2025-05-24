import sqlite3
from peewee import *

# declaro qué base voy a usar
db = SqliteDatabase("mi_base_peewee.db")

# indico que use la base de datos declarada
class BaseModel(Model):
    class Meta:
        database = db

# creo una clase para cada tabla a crear
class Noticia(BaseModel):
    titulo = CharField(unique=True)
    descripcion = CharField()

# conecto la base
db.connect()

# creo la tabla de la clase
db.create_tables([Noticia])

# alta
def alta (self, titulo, descripcion, mitreeview):
    # instancio la clase
    noticia = Noticia()
    
    # tomo los atributos
    noticia.titulo = titulo.get()
    noticia.descripcion = descripcion.get()
    
    # lo guardo con peewee
    noticia.save()

    # actualizamos el treeview
    self.actualizar_treeview(mitreeview)

# actualizar el treeview
def actualizar_treeview(self, mitreeview):
    # limpieaza de tabla
    records = mitreeview.get_children()
    for element in records:
        mitreeview.delete(element)

    #imprimir los nuevos datos
    for fila in Noticia.select():
        mitreeview.insert("", 0, text=fila.id, values=(fila.titulo, fila.descripcion))

# baja
def baja(self, mitreeview):
    # selecciono el campo
    item_seleccionado = mitreeview.focus()
    valor_id = mitreeview.item(item_seleccionado)
    
    # borrola fila con el id seleccionado
    borrar = Noticia.get(Noticia.id==valor_id["text"])
    borrar.delete_instance()
    
    # actualizo el treeview
    self.actualizar_treeview(mitreeview)

# modificacion
def modificar(self, titulo, descripcion, mitreeview):
    # selecciono el campo
    item_seleccionado = mitreeview.focus()
    valor_id = mitreeview.item(item_seleccionado)
    
    # actualizo la fila seleccionada en cada uno de sus valores
    actualizar = Noticia.update(titulo=titulo.get(), descripcion=descripcion.get()).where(Noticia.id==valor_id["text"])
    actualizar.execute()

    # actualizo el treeview
    self.actualizar_treeview(mitreeview)

