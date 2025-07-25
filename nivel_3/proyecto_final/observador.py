import funciones

class Subject:
    def __init__(self):
        self.observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)   

class Observador:
    def update(self, *args):
        raise NotImplementedError("Delegación de actualización")
    

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        try:
            titulo = args[0]
            # Obtengo la fecha actual
            fecha_formateada = funciones.generar_fecha()

            # Creo la cadena a registrar
            log = f"{fecha_formateada} - Libro buscado en la base: {titulo}\n"

            # Realizo el registro
            with open("log_busqueda_libros.txt", "a", encoding="utf-8") as archivo:
                archivo.write(log)

        except Exception as e:
            # Genero un registro con el error
            with open("log_errores.txt", "a", encoding="utf-8") as archivo_e:
                archivo_e.write(f"ERROR: No se pudo añadir entrada al log: {e}\n")




