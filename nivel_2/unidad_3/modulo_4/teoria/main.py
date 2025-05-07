class Personas():

    def __init__(self, nombre, edad, salario, trabajo=None):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.trabajo = trabajo



if __name__=="__main__": # lo que viene a continuación solo se ejecuta si lo lanzamos desde el main. Se usa para poder probar cosas sin que se ejecute toda la app cuando estamos en otro archivo
    juan = Personas("Juan Marcelo Barreto", 7, 500)
    susana = Personas("Susana Anna Perez", 6, 300)
    print(juan.nombre.split()[-1])
    print(juan.nombre)
    print(susana.edad)
    susana.salario*=1.1
    print(susana.salario)

    base_personas = [juan, susana]
    for persona in base_personas:
        print(persona.nombre, persona.salario)