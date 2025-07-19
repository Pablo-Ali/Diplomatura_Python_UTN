class ControlMotor(type): #heredar de type es lo que la convierte en metaclase
    encendido = False

    def recuperar_hora(cls):
        return "Hora del evento"
    

class Material:
    material = "plástico"


class Auto(Material, metaclass=ControlMotor):
    marca ="renault"

    def __init__(self, color):
        self.color = color

    def retornar_color(self, valor):
        return self.color + str(valor)
    
# una instancia de auto no va a tener acceso ni al atributo ni al método de la metalcase, aunque sí la propia clase

print(Auto.encendido)
print(Auto.recuperar_hora())
print("----")
objeto = Auto("rojo")
try:
    objeto.encendido
except:
    print("El objeto de la clase no puede acceder al atributo")

try:
    objeto.recuperar_hora()
except:
    print("El objeto de la clase no puede acceder al método")