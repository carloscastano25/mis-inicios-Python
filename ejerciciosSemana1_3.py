"""Variables, tipos de datos, y operadores:"""

# # Ejercicio 1: Operaciones con cadenas

# nombre_completo = input("Por favor ingrese su nombre y apellido: ")

# nombre = len(nombre_completo.replace(" ",""))
# print(f"Su nombre es {nombre_completo} y tiene {nombre} caracteres")

# print(f"{nombre_completo.title()}")
# print("")

# # Ejercicio 2: Conversión de temperatura

# temp_celsius = int(input("Por favor ingrese la temperatura en grados celsius: "))
# conversion_farenheit = ((9/5)*temp_celsius) + 32
# print(f"La temperatura en farenheit es: {conversion_farenheit}")

# # Ejercicio 3: Operaciones combinadas con números

# import math

# print(f"Ingrese dos números enteros")
# try:
#     a = int(input("Primer número: "))
#     b = int(input("segundo número: "))
# except ValueError:
#     print(f"Los valores deben ser números enteros:")
    
# print(f"El resultado de la suma de los números {a} y {b} es {a+b}")
# print(f"El resultado de la resta de los números {a} y {b} es {a-b}")
# print(f"El resultado de la multiplicación de los números {a} y {b} es {a*b}")
# if b != 0:
#     print(f"El resultado de {a} dividido {b} es {math.floor(a/b)}")
# else:
#     print(f"Error, no es posible dividir entre cero")
# print(f"El resultado de elevar {a} a la {b} es {a**b}")
# print(f"El modulo de la division entre {a} y {b} es {a%b}")

"""Condicionales:"""

# Ejercicio 4: Clasificación de edad


try:
    edad = int(input("Por favor ingrese su edad:  "))
except ValueError:
    print(f"El número debe ser un entero:")

if edad < 18:
    print(f"Menor de edad")
elif edad >= 18 and edad < 65:
    print(f"Adulto")
else:
    print(f"Adulto mayor")



