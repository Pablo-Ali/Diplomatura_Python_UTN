# Descriptores

class AccederInstanciaMail():
    def __get__(self, instance, owner):
        print('Recuperar el mail...')
        return instance._mail + '.ar'

    def __set__(self, instance, valor):
        print('Modificar el mail...')
        instance._mail = valor

class Cliente:
    def __init__(self, usuario, mail):
        self._usuario = usuario
        self._mail = mail

    # el descriptor también puede estar dentro de la clase si es propio de esta y no lo va a usar otra clase
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

    usuario = DescriptorUsuario() #llamo a la clase descriptora en vez de a property
    mail = AccederInstanciaMail()

cliente1 = Cliente("Anna", "anna@gmail.com")
print(cliente1.usuario)
print(cliente1._mail) # accede al atributo
print(cliente1.mail) # accede al descriptor (__get__)
