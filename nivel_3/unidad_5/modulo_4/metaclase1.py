class Material:pass

class Auto(Material):
    color = "azul"

    def retornar_color(self, ):
        return self.color
    
objeto = Auto()
print(objeto.retornar_color())
print(type(Auto.__class__)) # vemos de qué clase es la clase Auto (va a decir type)

print("---"*23)

# declaración de una clase de forma explícita
Auto2 = type("Auto2", (Material, ), {"color":"azul", "retornar_color":(lambda x:x.color)}) 

objeto2 = Auto2()
print(objeto2.retornar_color())
print(type(Auto2.__class__))

# en Python, todas las clases son objetos de type. No es una superclase, sino una metaclase a partir de la cual genero otras