from datetime import datetime

def generar_fecha() -> str:
    '''
    Función que toma la fecha actual y la retorna
    como una cadena formateada como DD/MM/YYYY
    '''
    # Obtengo la fecha actual
    fecha_actual = datetime.now()

    # Formateo
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    return fecha_formateada