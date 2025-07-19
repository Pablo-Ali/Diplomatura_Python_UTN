def metodo_instancia_1(obj):
    return obj.valor*4

def metodo_instancia_2(obj, valor):
    return "Estoy en método de instancia creado desde metaclase " + valor


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['met_inst_1']=metodo_instancia_1
        classdict['met_inst_2']=metodo_instancia_2
        return type.__new__(meta, classname, supers, classdict)


class Usuarios(metaclass=Extender):
    def __init__(self, valor):
        self.valor=valor

    def imprimir(self,):
        return self.valor*2
    
class Usuarios2(metaclass=Extender):
    valor='3'

x=Usuarios('8')
y=Usuarios2()

print(x.imprimir())
print(x.met_inst_1())
print(x.met_inst_2('4'))

print(y.met_inst_1())
print(y.met_inst_2('5'))