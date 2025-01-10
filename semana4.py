# # Ejercicio 1: Calcular el área de un rectángulo

# def calcular_area (base, altura):
    
#     return base * altura

# def pedir_valores():
#     while True:
#         try:
#             base = int(input("Por favor ingrese la base (entero positivo) "))
#             altura = int(input("Por favor ingrese la altura (entero positivo) "))
#             if base <= 0 or altura <=0:
#                 print(f"ERROR: La base o la altura deben ser valores positivos diferentes a cero, intente de nuevo")
#                 print(f"\nNUEVO INTENTO")
#                 continue
#             return base, altura
#         except ValueError:
#             print(f"Error: debe ingresar valores con las condiciones especificadas")
#             continue

# def ejecutar ():
#     print(f"CALCULADORA DE ÁREA DE UN RECTÁNGULO")

#     base, altura = pedir_valores ()

#     area = calcular_area(base,altura)

#     print(f"El área del rectángulo es {area}")
#     print(f"\n")
    
# ejecutar()

# # Ejercicio 2: Calcular el promedio de una lista de números

# def calcular_prometio(lista):
#     return sum(lista) / len(lista) if lista else 0

# lista = [5,2,6,5,4,5,6]

# promedio = calcular_prometio(lista)
    
# print(f"{promedio: .2f}")

# Ejercicio 3: Determinar si un número es primo

