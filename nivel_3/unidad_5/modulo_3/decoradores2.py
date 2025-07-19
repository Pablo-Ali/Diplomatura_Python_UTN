# decorador para una clase
def decorador(cls):
    # ahora es una clase envoltura en vez de una función
    class Envoltura:
        def __init__(self, *args):
            self.instancia_de_clase = cls(*args)
        
        # definimos el método para recuperar los atributos
        def __getattr__(self, nombre):
            print(self.__class__) #imprimimos la clase (Envoltura)
            print(self.instancia_de_clase.__class__)#imprimimos la instancia de la clase (Auto)
            print("Nombre de atributo de la clase Auto: ", nombre)#imprimimos cada atributo
            return getattr(self.instancia_de_clase, nombre)#retornamos el método

    return Envoltura






@decorador
class Auto:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

x = Auto("Rojo", "Renault")

print(x.color)
print(x.marca)