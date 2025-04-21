# por defecto python busca al archivo __main__.py  por lo tanto, no hace falta aclarar en consola qué archivo deseamos ejecutar


import sys
from . import m_pablo # soluciíon de chat gpt

m_pablo.imprimir(" ".join(sys.argv[1:]))