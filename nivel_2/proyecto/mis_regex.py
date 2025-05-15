import re

class MisRegex():
    def verificar_reg_cadena(self, cadena):
        patron = r"^[a-zA-Z\sáéíóúÁÉÍÓÚäëïöüÄËÏÖÜñÑ\.,\-]+$"
        return bool(re.match(patron, cadena))