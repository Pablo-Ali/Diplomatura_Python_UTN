class Persona():
    
    # constructor
    def __init__(self, nombre): # no tenemos sobrecarga de constructores como en Java
        self.nombre = nombre

    # métodos
    def comer_arroz(self):
        print("Comer arroz desde Persona")

class Cultura():pass

class Argentinos(Persona): # hereda de la clase Persona
    
    # constructor
    def __init__(self, nombre): # no tenemos sobrecarga de constructores como en Java
        self.nombre = nombre

    # métodos
    #def comer_arroz(self):
    #   print("Comer arroz desde Argentinos")

class Chinos(Persona, Cultura):
    
    # constructor
    def __init__(self, nombre): # no tenemos sobrecarga de constructores como en Java
        self.nombre = nombre

    # métodos
    def comer_arroz(self):
        print("Comer arroz desde Chinos")


anna = Persona("Anna Karen")
juan = Persona("Juan Marcelo")
pepe = Argentinos("José Gastón")
josefa = Chinos("Josefa Celeste")

print(anna.nombre)
print(juan.nombre)
anna.comer_arroz()
pepe.comer_arroz() # al haber comentado el método desde Argentinos, usa el que hereda de Personas
josefa.comer_arroz() # por polimorfismo, pisa el método de Personas con el de la clase Chinos
print(Chinos.__mro__) # imprime la estructura de herencia de la clase