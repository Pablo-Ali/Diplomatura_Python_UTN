class Personas():

    def __init__(self, nombre, edad, salario, trabajo=None):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.trabajo = trabajo
    
    def dar_aumento(self, porcentaje):
        self.salario *= 1 + porcentaje
