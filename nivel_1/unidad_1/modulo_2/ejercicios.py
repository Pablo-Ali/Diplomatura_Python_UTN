import sys

# Constantes

PI = 3.1416

"""
Ejercicio 1

Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. Utilice la estructura if / else
"""

# comando: python3 ejercicios.py 2 3 4

if int(sys.argv[1]) % 2 == 0:
    print("Es múltiplo de 2")
else:
    print(("No es múltiplo de 2"))

if int(sys.argv[2]) % 2 == 0:
    print("Es múltiplo de 2")
else:
    print(("No es múltiplo de 2"))

if int(sys.argv[3]) % 2 == 0:
    print("Es múltiplo de 2")
else:
    print(("No es múltiplo de 2"))

"""
Ejercicio 2

Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración
conteniendo los dos elementos de la lista concatenándolos con texto para formar una
oración con sentido. Presente el resultado en la terminal del editor
"""

frutas = ["manzanas", "peras"]

print("Fui a la verdulería y compré dos " + frutas[0] + " y tres " + frutas[1])

"""
Ejercicio 3

Tome dos valores por consola, y guarde en una lista
[primer_valor, segundo_valor, la_suma_de_los_valores] 
"""

primer_valor = int(input("Ingrese el primer entero: "))
segundo_valor = int(input("Ingrese el segundo entero: "))
suma = primer_valor + segundo_valor

lista = [primer_valor, segundo_valor, suma]

print(lista)

"""
Ejercicio 4

Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
fecha de jubilación, presente en la terminal el mensaje “Ya está en edad de jubilarse" en
caso contrario que presente “Aún está en edad de trabajar”
"""

edad = int(input("Ingrese la edad: "))

if edad >= 65:
    print("Ya está en edad de jubilarse")
else:
    print("Aun está en edad de trabajar")

"""
Ejercicio 5

Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
función, de forma que la operación se realice dentro de la misma.
Presente el resultado en la terminal del editor.
"""

def calcular_longitud_perimetro():
    
    radio = float(input("Ingrese el radio: "))
    longitud = 2 * PI * radio

    return longitud

def calcular_area_circulo():
    
    radio = float(input("Ingrese el radio: "))
    area = PI * (radio * radio)

    return area

def incrementar_10_porciento():
    
    valor = int(input("Ingrese un núemero entero: "))
    resultado = valor * 1.1

    return resultado

perimetro = calcular_longitud_perimetro()
area = calcular_area_circulo()
numero_incrementado = incrementar_10_porciento()

print("La longitud del perímetro es:", perimetro)
print("El área del círculo es:", area)
print("Este es su número con un incremento del 10%:", numero_incrementado)