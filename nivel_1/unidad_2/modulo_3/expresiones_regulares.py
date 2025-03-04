"""
Hay dos lenguajes de expresiones regulares: POSIX y PCRE. Python permite mezclarlos y, además, utiliza FLAGS para atajos.

"""

import re

patron = re.compile("[p+]")
lista = ["pera", "vfg"]

patron_2 = re.compile("pera" "|manzana" "|limón") # el | es como un or
cadena = "manzana"

print(patron.match(lista[0]))
print(patron.match(lista[1]))
print(patron_2.match(cadena))