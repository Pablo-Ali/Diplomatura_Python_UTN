# decorador que toma parámetros

def modo_de_trabajo(valor=False): # toma los parámetros del decorador
    def _modo_de_trabajo(funcion): # toma la función
        def interna(*args, **kwargs): # toma los parámetros de la función
            if valor:
                print("Estoy en producción")
            else:
                print("Estoy en desarrollo")
            for id, argumento in enumerate(args): # INVESTIGAR LÍNEA 10 A 12
                print("argumento %d:%s " %(id, argumento))
            funcion(*args, **kwargs)
        return interna
    return _modo_de_trabajo

@modo_de_trabajo(False)
def registro_usuario(nombre, apellido):
    print("Registro de %s " %nombre)

registro_usuario("Anna", "Rodriguez")