# sobrecarga de operadores con metaclases


class ControlMotor(type):
    def __getitem__(cls, indice): #sobrecarga#
        return cls.color[indice]*5

class Auto(metaclass=ControlMotor):
    color="Azul"

    def __getitem__(self, indice): #sobrecarga#
        return indice**0.5
    
objeto=Auto()
print(objeto[64])

print(Auto[1])