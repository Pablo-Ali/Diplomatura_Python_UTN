def extender_clase(self, arg):
    print(arg)

class MiClase():pass

MiClase.extender_clase = extender_clase #esto luego lo hacemos con metaclases, pero así es como extendemos métodos

objeto = MiClase()
objeto.extender_clase("Este método se ha agregado a la clase")