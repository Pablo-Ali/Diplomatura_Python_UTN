# apilar decoradores

def cambio_estado(func):
    def envoltura(*args, **kargs):
        if args[0]:
            func(*args, **kargs)
            print("El motor se ha encendido")
        else:
            func(*args, **kargs)
            print("El motor se ha apagado")

    return envoltura


def aviso_cambio_estado(func):
    def envoltura(*args, **kargs):
        print("Se envía un mensaje al celular")
        func(*args, **kargs)
        print("Se ejecutó %s" %func.__name__)# me imprime qué función se ejecutó
    return envoltura


@cambio_estado # este toma lo que retorna @aviso_cambio_estado
@aviso_cambio_estado # primero pasa por acá tomando a la función y sus parámetros y lo procesa y manda al siguiente
def estado_motor(estado):
    print(estado)

estado_motor(True)
print("---"*23)
estado_motor(False)