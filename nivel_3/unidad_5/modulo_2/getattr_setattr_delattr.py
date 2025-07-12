class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def __getattr__(self, atributo):
        print('get: ' + atributo)
        if atributo == 'nombre': # coteja el llamado (línea 25) y retorna el atributo si es lo que se pide
            return self._nombre
        else:
            raise AttributeError(atributo)
    
    def __setattr__(self, atributo, valor):
        print('set: ' + atributo)
        if atributo == 'nombre': # coteja atributo y valor en el llamado (línea 26)
            atributo = '_nombre'
        self.__dict__[atributo] = valor #lo retornamos con el valor del atributo del diccionario para que no vulva a atraparlo y se genere un bucle infinito

    def __delattr__(self, atributo):
        print('del: ' + atributo)
        if atributo == 'nombre': # coteja el atributo en el llamado (línea 27)
            atributo = '_nombre'
        del self.__dict__[atributo]

persona1 = Persona('Anna')
print(persona1.nombre)
persona1.nombre = "Josefa"
del persona1.nombre