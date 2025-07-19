# Decoradores

# defino la función que va a decorar a la otra
def decorador_multiplicar_por10(funcion):
    # acá se procesa lo retornado por la función decorada y se retorna
    def envoltura(*args):
        print(funcion(*args) * 10)
    return envoltura

# defino una clase decoradora
class DecoradorDividirPor10:
    def __init__(self, func) -> None:
        self.func = func
    # atrapa la función con sus parámetros y ejecuta la lógica
    def __call__(self, *args):
        print(self.func(*args) / 10)


# tomo el retorno de la suma y lo mando al decorador
@decorador_multiplicar_por10
def sumar(a, b):
    c = a + b
    return c

@DecoradorDividirPor10
def restar(a, b):
    c = a - b
    return c

sumar(2, 3) # la función sumar toma los parámetros y los suma, ahí los manda al decorador donde se aplica la lógica adicional. Esto se aplica tanto para funciones como para métodos
restar(50, 20) # si uso una clase decoradora, ahí solo se puede sobre funciones, no sobre métodos

