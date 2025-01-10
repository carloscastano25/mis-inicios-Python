
#!                              __          __  _    _  __  _      _____ 
#!                             |  |        |  || |  | ||  || |    |  ___|
#!                             \  \        /  /| |__| ||  || |    | |___ 
#!                              \  \  /\  /  / |  __  ||  || |    |  ___|
#!                               \  \/  \/  /  | |  | ||  || |___ | |___ 
#!                                \___/\___/   |_|  |_||__||_____||_____|


#! DEFINICIÓN BÁSICA DEL CICLO WHILE 
#? Un ciclo while en Python se utiliza para ejecutar repetidamente un bloque de código mientras una condición 
#? sea verdadera. Se evalúa la condición antes de cada iteración, y el ciclo se detiene cuando 
#? la condición se vuelve falsa.

#! SINTAXIS!!!

# while condicion:
    # Bloque de código a ejecutar
    
#TODO: EJEMPLO BÁSICO:

contador = 1          #?Creo una variable llamada contador y la inicializo en 1
while contador <= 5:  #? Establezco la condición de que mientras el contador sea menor o igual a 5
    print(contador)   #? Muéstrame el contador
    contador += 1     #? Incrementar el contador en cada iteración de uno en uno para que pueda llegar a ser 5
#                     #?-- y así llegar al fin del ciclo, si no lo hago, el ciclo sería infinito. 

# counter = 0   
# while counter <11:
#     if counter % 2 != 0:
#         print(f"{counter}")
#     counter += 1


# n = 3

# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Ya se llegó a:", i, "ese número no hace parte de la lista válida") #! El uso de else aquí, es para decir
         #!que la condición ya no se cumple, por lo que el bucle finaliza. 