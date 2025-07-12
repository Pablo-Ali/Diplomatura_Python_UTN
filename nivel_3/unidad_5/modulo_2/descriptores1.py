# Descriptores

class DescriptorUsuario:
    "Documentación para el descriptor"

    def __get__(self, instance, owner): #podemos acceder a la instancia del descriptor, a la instancia de la clase y a la clase dentro de la cual se usa el descriptor
        print('Recuperar el usuario...')
        return instance._usuario.upper()
    
    def __set__(self, instance, valor):
        print('Modificar usuario...')
        instance._usuario = valor

    def __delete__(self, instance):
        print('Remover el usuario...')
        del instance._usuario

class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario

    usuario = DescriptorUsuario() #llamo a la clase descriptora en vez de a property

cliente1 = Cliente("Anna")
print(cliente1.usuario)
cliente1.usuario = "Ana"
print(cliente1.usuario)
#print(Cliente.usuario.__doc__) #esta línea no anda, INVESTIGAR