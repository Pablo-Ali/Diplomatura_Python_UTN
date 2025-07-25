class Subject:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update()

class TemaConcreto(Subject):
    def __init__(self, ):
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self, ):
        return self.estado
    

class Observador:
    def uptade(self, ):
        raise NotImplementedError("Delegación de actualización")
    

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de Observador ConcreteObserverA")
        self.estado = self.observado_a.get_estado()
        print("Estado = ", self.estado)


tema1 = TemaConcreto()
observador_a = ConcreteObserverA(tema1)
tema1.set_estado(1)


