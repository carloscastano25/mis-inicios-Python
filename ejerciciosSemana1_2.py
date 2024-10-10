# """Variables, tipos de datos, y operadores:"""

# # Ejercicio 1: Intercambiar valores de variables}

# a = 5
# b = 10
# c = 12

# print(f"El valor de a es {a}")
# print(f"El valor de b es {b}")
# print(f"El valor de c es {c}")

# a, b, c = c, a, b

# print(f"El valor de a es {a}")
# print(f"El valor de b es {b}")
# print(f"El valor de c es {c}")

# # Ejercicio 2: Cálculo de área y perímetro
# import math

# radio = int(input("Por favor ingrese el valor del radio"))
# perimetro = (2 * math.pi) * radio
# area =  (radio**2) * math.pi

# print(f"El perímetro del cúrculo es {perimetro: .2f}")
# print(f"El área del cúrculo es {area: .2f}")

# # Ejercicio 3: Operaciones con cadenas

# nombre = "Carlos"
# apellido = "Castaño"

# nombre_completo = nombre + " " + apellido

# print(nombre_completo)

# print(nombre_completo.lower())
# print(nombre_completo.upper())


# """Condicionales:"""

# # Ejercicio 4: Par o impar

# numero = int(input("Por favor ingrese un número entero"))
# if numero % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")

# # Ejercicio 5: Comparación de tres números

# print("Por favor ingrese tres números enteros")

# num1 = int(input("Primer número: "))
# num2 = int(input("Segundo número: "))
# num3 = int(input("Tercer número: "))

# if num1 > num2 and num1 > num3:
#     print(f" {num1} es el mayor")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} es el mayor")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} es el mayor")
# else:
#     print("Los números son iguales")
    
# # Ejercicio 6: Calificación de notas

# num = int(input("Ingrese un número del 1 al 100: "))

# if num >= 60:
#     print("Aprobado")
# else:
#     print("Reprobado")

# """Bucles:"""

# #Ejercicio 7: Contador descendente con while

# num = 10
# while num >= 1:
#     print(num)
#     num -=1

# # Ejercicio 8: Sumar todos los números en un rango  

# inicio = int(input("Por favor ingrese un número entero inicial"))
# fin = int(input("Por favor ingrese un número entero final"))

# if inicio > fin:
#     inicio , fin = fin, inicio #!De esta forma se intercambian los valores de una variable

# print(f"Intercambiando los valores, ahora el rango es de {inicio} a {fin}")

# suma_total = 0

# for i in range(inicio, fin + 1):
#     suma_total += i
    
# print(f"La suma de todos los números entre {inicio} y  {fin} es {suma_total}")

# #Ejercicio 9: Multiplicar elementos de una lista

# lista = [1,2,5,6,8,10]

# for i in lista:
#     print(i*2)

# """lista = [1, 2, 5, 6, 8, 10]
# nueva_lista = [i * 2 for i in lista] #!Ojo a esta forma de guardar una lista pasándola por un ciclo for.
# print(nueva_lista"""

# #Ejercicio 10: Tabla de multiplicar

# num = int(input("Por favor ingrese un número entero: "))

# for i in range (1,11):
#     print(f"{num} x {i} = {num * i}")


