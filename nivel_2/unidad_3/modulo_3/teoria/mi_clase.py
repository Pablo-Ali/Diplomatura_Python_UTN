# utilicamos upper cammel case para nombrar a las clases en Python
class OperacionesMatematicas():
    # métodos (hay de instancia, de clase y estático)

    def sumar(self, a, b): # self es como this de Java
        return a + b
    

# creamos un objeto de la clase para lanzar la rutina

mi_objeto = OperacionesMatematicas()

print(mi_objeto.sumar(2,3))