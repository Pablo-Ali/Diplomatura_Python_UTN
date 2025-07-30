import re

class MisRegex():
    """
    Clase que contiene métodos para validaciones con expresiones regulares.
    """
    def verificar_reg_cadena(self, cadena : str) -> bool:
        """
        Verifica que la cadena contenga solo caracteres válidos (letras, espacios, tildes,
        diéresis, ñ, puntos, comas y guiones).

        :param cadena: Cadena de texto a validar.
        :type cadena: str
        :return: True si la cadena cumple con el patrón, False en caso contrario.
        :rtype: bool
        """
        patron = r"^[a-zA-Z\sáéíóúÁÉÍÓÚäëïöüÄËÏÖÜñÑ\.,\-]+$"
        return bool(re.match(patron, cadena))