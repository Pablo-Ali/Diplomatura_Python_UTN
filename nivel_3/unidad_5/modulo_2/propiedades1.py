class Empresa:
    def __init__(self, usuario):
        self._usuario = usuario # el '_' es como el private

    def get_usuario(self, ):
        print('Recuperar el usuario...')
        return self._usuario
    
    def set_usuario(self, valor):
        print('Modificar usuario...')
        self._usuario = valor

    def del_usuario(self, ):
        print('Remover el usuario...')
        del self._usuario
    
    usuario = property(get_usuario, set_usuario, del_usuario, "Datos adicionales")
    # cada vez que el cliente llama a usuario se activa la propiedad y me permite agregar una lógica nueva

# las propiedades pueden ser heredadas
class Cliente(Empresa): pass


cliente1 = Cliente("Anna")
print(cliente1.usuario)
cliente1.usuario = "Ana"
print(cliente1.usuario)
print(Cliente.usuario.__doc__) # me trae lo que puse en el propertry ("Datos adicionales")