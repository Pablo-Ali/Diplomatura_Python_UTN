class MiMetaClase(type):
    def __new__(meta, nombre_de_clase, superclase, diccionario_de_clase): #primero se ejecuta el __new__
        print("En __new__ de metaclase: ", meta, nombre_de_clase, superclase, diccionario_de_clase, sep="\n...")
        return type.__new__(meta, nombre_de_clase, superclase, diccionario_de_clase)
    
    def __init__(Clase, nombre_de_clase, superclase, diccionario_de_clase):#luego se ejecuta el __init__
        print("En __init__ de metaclase: ", Clase, nombre_de_clase, superclase, diccionario_de_clase, sep="\n...")
        print("..init objeto de clase", list(Clase.__dict__.keys()))



class MiSuperClase: pass

class MiClase(MiSuperClase, metaclass = MiMetaClase): #primero va la super clase y después la metaclase (con la palabra reservada metaclass)
    atributo1 = 1
    def metodo1(self, arg):
        return self.atributo1 + 3 * arg
    

print("Creando una instancia")
x = MiClase()
print("Atributo: ", x.atributo1, x.metodo1(7))
