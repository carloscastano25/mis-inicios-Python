
# """Variables, tipos de datos, y operadores:"""

# #Ejercicio 1: Definir variables

# numero_entero = 1
# numero_decimal = 2.5 #!Recomendación, en python el decimal es con punto, no con coma.
# nombre = "Carlos"

# print(f"El valor de la variable numero_entero es {numero_entero}")
# print(f"El valor de la variable numero_decimal es {numero_decimal}")
# print(f"El valor de la variable nombre es {nombre}")

# #Ejercicio 2: Operaciones con números

# var1 = 5
# var2 = 2

# suma = var1 + var2
# resta = var1 - var2
# multiplicacion = var1 * var2
# division = var1 / var2
# modulo = var1 % var2

# print(f"Los números ingresados son {var1} y  {var2}")
# print(f"La suma de ellos es {suma}")
# print(f"La resta de ellos es {resta}")
# print(f"La multiplicacion de ellos es {multiplicacion}")
# print(f"La division entre ellos es {division}")
# print(f"El módulo ente ellos es {modulo}")

# #!Recomendación: Cuando mis datos no van a ser utilizados posteriormente, puedo hacer la operación directamente en el
# #!print, así print(f"La suma de {var1} y {var2} es {var1 + var2}")

# # Ejercicio 3: Conversión de tipos

# entero = 565
# entero_a_cadena = str(entero)

# cadena = "565"
# cadena_a_entero = int(cadena)

# operacion = entero * cadena_a_entero

# print(f"El resultado  de la multiplcacion es {operacion}")


# """Condicionales:"""

# #Ejercicio 4: Condicional simple

# numero = int(input("Por favor ingrese un número entero"))

# if numero == 10:
#     print("El número es igual a 10")
# elif numero < 10:
#     print("El número es menor a 10")
# else:
#     print("El número es mayor a 10")
    
# """Bucles:
# """
    
# #Ejercicio 5: Bucle while

# tope = 1

# while tope <= 10:
#     print(tope)
#     tope = tope + 1

# # Ejercicio 6: Bucle for con una lista

# lista = ["Jorge", "Mariana", "Miguel"]

# for nombre in lista:
#     print(f"Hola {nombre}")
