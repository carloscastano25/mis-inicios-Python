"""Variables, tipos de datos, y operadores:"""

# Ejercicio 1: Operaciones con cadenas

nombre_completo = input("Por favor ingrese su nombre y apellido: ")

nombre = len(nombre_completo.replace(" ",""))
print(f"Su nombre es {nombre_completo} y tiene {nombre} caracteres")

print(f"{nombre_completo.title()}")
print("")

# Ejercicio 2: Conversión de temperatura

temp_celsius = int(input("Por favor ingrese la temperatura en grados celsius: "))
conversion_farenheit = ((9/5)*temp_celsius) + 32
print(f"La temperatura en farenheit es: {conversion_farenheit}")

# Ejercicio 3: Operaciones combinadas con números

import math

print(f"Ingrese dos números enteros")
try:
    a = int(input("Primer número: "))
    b = int(input("segundo número: "))
except ValueError:
    print(f"Los valores deben ser números enteros:")
    
print(f"El resultado de la suma de los números {a} y {b} es {a+b}")
print(f"El resultado de la resta de los números {a} y {b} es {a-b}")
print(f"El resultado de la multiplicación de los números {a} y {b} es {a*b}")
if b != 0:
    print(f"El resultado de {a} dividido {b} es {math.floor(a/b)}")
else:
    print(f"Error, no es posible dividir entre cero")
print(f"El resultado de elevar {a} a la {b} es {a**b}")
print(f"El modulo de la division entre {a} y {b} es {a%b}")

"""Condicionales:"""

# Ejercicio 4: Clasificación de edad


try:
    edad = int(input("Por favor ingrese su edad:  "))
except ValueError:
    print(f"El número debe ser un entero:")

if edad < 18:
    print(f"Menor de edad")
elif edad >= 18 and edad <= 65:
    print(f"Adulto")
else:
    print(f"Adulto mayor")

# Ejercicio 5: Calculadora básica con condicionales

print(f"LISTA DE OPERADORES")

print(f"1. SUMA")
print(f"2. RESTA")
print(f"3. MULTIPLICACIÓN")
print(f"4. DIVISIÓN")

try:
    operador = int (input("Por favor indique el número correspondiente a la operación que desea realizar: "))
except ValueError:
    print(f"Debe ingresar un número entero de 1 a 4")

print(f"Ingrese dos números a operar:")
try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
except ValueError:
    print(f"Los valor debe ser números enteros:")
    
if operador == 1:
    print(f"La suma de los números ingresados es {a+b}")
elif operador == 2:
    print(f"La resta de los números ingresados es {a-b}")
elif operador == 3:
    print(f"La multiplicación de los números ingresados es {a*b}")
elif operador == 4:
    if b != 0:
        print(f"La división de los números ingresados es {a/b}")
    else:
        print(f"No es posible dividir entre cero")
else:
    print(f"Ese número no corresponde a ninguna operación en la lista")

#Ejercicio 6: Determinar si un año es bisiesto


anio = int(input("Por favor ingrese un año"))

if anio % 4 == 0:
    print(f"El año es bisiesto")
elif anio % 100 == 0 and anio % 400 != 0:
        print(f"El año no es bisiesto")
else:
    print(f"El año no es bisiesto")

"""Bucles:"""

# Ejercicio 7: Suma de dígitos


numero = int(input("Por favor ingrese un número entero positivo: "))

while numero < 0:
    numero = int(input("Por favor ingrese un entero positivo: "))
    
suma_digitos = 0

while numero > 0:
    digito = numero % 10 #! Con esta funcionalidad en digito guardo el último dígito del número
    suma_digitos += digito
    numero //= 10 # !Con esta funcionalidad // se divide con resultado entero, osea que se elimina el último digito

print(f"La suma de los dígitos es {suma_digitos}")

#Ejercicio 8: Encontrar el número más pequeño en una lista

lista = [8,2,3,4,5,6]

menor_numero = lista[0]

for numero in lista:
    if numero < menor_numero:
        menor_numero = numero

print(f"El número más pequeño es {menor_numero}")
    

#Ejercicio 9: Contar letras en una frase

frase = input("Por favor ingrese una frase: ")

contador = 0

for letra in frase:
    if letra.isalpha():
        contador += 1
    
print(f"{contador}")

# Ejercicio 10: Factorial de un número

while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print(f"Por favor ingrese un número positivo")
            continue
        break
    except ValueError:
        print(f"El dígito ingresado no cumple con las condiciones dadas:")
        continue

factorial = 1

for i in range(1, numero+1):
    factorial *= i

print(f"El factorial del {numero} es {factorial}")


# Ejercicio 11: Números pares en un rango

print(f"Debe ingresar dos números (Inicio de rango y fin de rango), ambos deben ser enteros y positivos")

while True:
    try:
        inicio = int(input("Ingrese el primer número aquí: "))
        fin = int(input("Ingrese el segundo número aquí"))
        if inicio < 0 or fin < 0:
            print(f"Todos los número ingresados deben ser POSITIVOS")
            continue
        break
    except ValueError:
        print(f"El dígito ingresado debe ser un número entero; ejemplo: 5")
        continue
    
for numero in range(inicio, fin+1):
    if numero % 2 == 0:
        print(f"{numero}")

# Ejercicio 12: Multiplicación acumulativa

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero == 0:
            print(f"EL número debe ser diferente de cero")
            continue
        break
    except ValueError:
        print(f"El número no es un entero")
        continue

contador = 0
base = 1
while base < 1000:
    base = base * numero
    contador += 1
    
print(f"{base} y {contador}")
