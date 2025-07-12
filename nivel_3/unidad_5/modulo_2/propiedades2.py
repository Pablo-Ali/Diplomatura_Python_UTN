# Decoradores

class Empresa:
    def __init__(self, usuario):
        self._usuario = usuario # el '_' es como el private

    @property #declaro la función como una propiedad
    def usuario(self, ):
        """Datos adicionales"""
        print('Recuperar el usuario...')
        return self._usuario
    
    @usuario.setter
    def usuario(self, valor):
        print('Modificar usuario...')
        self._usuario = valor

    @usuario.deleter
    def usuario(self, ):
        print('Remover el usuario...')
        del self._usuario
    

class Cliente(Empresa): pass


cliente1 = Cliente("Anna")
print(cliente1.usuario)
cliente1.usuario = "Ana"
print(cliente1.usuario)
print(Cliente.usuario.__doc__) # me trae lo que puse en el propertry con """ """