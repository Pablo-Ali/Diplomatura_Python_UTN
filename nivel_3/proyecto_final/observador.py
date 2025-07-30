import funciones
from typing import Any

class Subject:
    def __init__(self):
        self.observadores = []

    def agregar(self, obj : 'Observador') -> None: # forward reference en la documentación a la clase Observador, que aún no está declarada en esta línea
        self.observadores.append(obj)

    def notificar(self, *args : any) -> None:
        for observador in self.observadores:
            observador.update(*args)   

class Observador:
    def update(self, *args : any) -> None:
        raise NotImplementedError("Delegación de actualización")
    

class ConcreteObserverA(Observador):
    def __init__(self, obj : Subject) -> None:
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args : any) -> None:
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