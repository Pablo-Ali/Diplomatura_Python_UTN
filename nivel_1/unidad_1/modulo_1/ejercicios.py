import sys

# Constantes

PI = 3.1416

"""
Ejercicio 1

Cree un programa que tome tres valores por consola multiplique el primero por el segundo
y le sume el tercero. Presente el resultado en la terminal del editor
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

print("Resultado:", numero_1 * numero_2 + numero_3)

"""
Ejercicio 2

Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos.
"""

# comando: python3 ejercicios.py 2 3 4

print("Si el resto de dividir por dos el 0, el número es múltiplo de 2.")
print("El número es:", sys.argv[1], "y el resto de su división por 2 es:", int(sys.argv[1]) % 2)
print("El número es:", sys.argv[2], "y el resto de su división por 2 es:", int(sys.argv[2]) % 2)
print("El número es:", sys.argv[3], "y el resto de su división por 2 es:", int(sys.argv[3]) % 2)

"""
Ejercicio 3

Escriba un programa que solicite el radio de una circunferencia y permita calcular el
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio 
"""

radio = float(input("Ingrese el radio: "))

longitud = 2 * PI * radio

print("La longitud del perímetro es:", longitud)

"""
Ejercicio 4

Escriba un programa que solicite el radio de una circunferencia y permita calcular su
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
A = 𝜋. 𝑟²
A = Área 
π = Número pi igual a 3.1416
r = Radio
"""

radio = float(input("Ingrese el radio: "))

area = PI * (radio * radio)

print("El área del círculo es:", area)

"""
Ejercicio 5

Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
editor el valor incrementado en un 10%.
"""

valor = int(input("Ingrese un núemero entero: "))

print("Este es su número con un incremento del 10%:", valor * 1.1)