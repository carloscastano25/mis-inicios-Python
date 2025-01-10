# """Calculadora"""
# def sumar (a,b):
#     return a + b

# def restar (a,b):
#     return a - b

# def multiplicar (a,b):
#     return a * b

# def dividir (a,b):
#     if b != 0:
#         return a /b
#     else:
#         return "Error, no es posible dividir entre cero"

# def deifinir_operaciones ():
#     return {
#         1: sumar,
#         2: restar,
#         3: multiplicar,
#         4: dividir
#     }

# def opciones ():
#     print("MENÚ DE OPERACIONES")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")

# def ejecutar ():
#     while True:
#         opciones()
#         try:
#             opcion = int(input("Por favor ingrese el número correspondiente a la operación que desea realizar: "))
#         except ValueError:
#             print("El número debe ser un número entero y debe estar dentro de la lista dada")
#             continue
        
#         if opcion == 5:
#             print("Adios")
#             break
        
#         operaciones = deifinir_operaciones()
        
#         if opcion in operaciones:
#             try:
#                 a = int(input("Por favor ingrese el primer número entero: "))
#                 b = int(input("Por favor ingrese el segundo número entero: "))
#             except ValueError:
#                 print("Debe ingresar un número entero")
#                 continue
        
#             resultado = operaciones[opcion](a,b)
        
#             print(f"El resultado es {resultado}")
        
#         else:
#             print("El valor es debe estar dentro de las opciones dadas")
        

# ejecutar()