import funciones
from typing import Callable, Any # robado a ChatGPT para poder documentar mejor el código


def decorador_registrar_libro(funcion : callable) -> callable:
    '''
    Decorador que registra la fecha y hora en la que son agregados
    nuevos libros a la base de datos.
    '''   
    def envoltura(*args : any, **kwargs : any) -> any:

        try:
            # Obtengo el título antes de ejecutar el método original para que no se borre el campo
            # Guardo la referencia al objeto StringVar
            titulo_var = args[1]

            # Genero el String del título
            titulo_str = titulo_var.get()
            
            # Llamo al método original
            resultado = funcion(*args, **kwargs)

            if resultado is True:
                # Obtengo la fecha actual
                fecha_formateada = funciones.generar_fecha()

                # Creo la cadena a registrar
                log = f"{fecha_formateada} - Nuevo libro añadido: {titulo_str}\n"

                # Realizo el registro
                with open("log_registro_libros.txt", "a", encoding="utf-8") as archivo:
                    archivo.write(log)

                # Retorno el método
                return resultado

        except Exception as e:
            # Genero un registro con el error
            with open("log_errores.txt", "a", encoding="utf-8") as archivo_e:
                archivo_e.write(f"ERROR: No se pudo añadir entrada al log: {e}\n")
       
    return envoltura