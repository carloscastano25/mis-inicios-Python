
#!              ____   __   _____   _____  __   ___   _    _      __      _____   __   ___   _____  
#!             |  _ \ |  | / ____| / ____||  | / _ \ | \  | |    /  \    |  __ \ |  | / _ \ |  ___| 
#!             | | | ||  || |     | |     |  || | | ||  \ | |   / /\ \   | |__) ||  || | | || |___  
#!             | | | ||  || |     | |     |  || | | ||   \| |  / ____ \  |  _  / |  || | | || __  | 
#!             | |_| ||  || |____ | |____ |  || |_| || |\   | / /    \ \ | | \ \ |  || |_| | ___| | 
#!             |____/ |__| \_____| \_____||__| \___/ |_| \__|/_/      \_\|_|  \_\|__| \___/ |_____| 

#TODO: DEFINICIÓN:

#? Un diccionario es una estructura de datos en Python que almacena pares de clave: valor. 
#? Cada clave es única y se utiliza para acceder a su valor asociado. Los diccionarios son mutables, 
#? lo que significa que sus contenidos pueden cambiarse después de su creación.


#TODO: SINTAXIS: 
#! Los diccionarios se definen con llaves

# diccionario = {} #? Puedo crear un diccionario vació para llenar luego

diccionario = {               #? Primero se define el nombre del diccionario, que será igual a lo que hay entre
    "clave1": "valor1",       #? las llaves, se puede ver que el diccionario al igual que un diccionario común
    "clave2": "valor2",       #? consta de una palabra clave y su valor correspondiente, como un diccionario
    "clave3": "valor3"        #? Ingles - Español. La clave a la izquierda, el valor a la derecha después de :
}

#! LAS CLAVES DE UN DICCIONARIO SON ÚNICAS E INMUTABLES:
#? Las claves deben ser String, enteros, números flotantes o tuplas.

#! PERO LOS VALORES SÍ PUEDEN CAMBIAR Y TENER CUALQUIER VALOR QUE QUIERA ASIGNARLES:
#? Los valores sí pueden ser String, números, funciones, tuplas, listas, flotantes y cualquier otro tipo de dato

#TODO: Ejemplo de un diccionario simple:

# mi_diccionario = {
#     "nombre": "Juan",
#     "edad": 25,
#     "ciudad": "Madrid"
# }


#                         #TODO: PARA ACCEDER A LOS VALORES DE UNA CLAVE
# mi_diccionario["nombre"]      #? Para acceder al valor correspondiente a esa clave ---> Juan
# mi_diccionario.get("nombre")  #? Arroja el mismo resultado, acceso al valor de la clave ---> Juan
# print(mi_diccionario.get("universidad", "Dato no guardado"))  #!OJO CON ESTO: 
                                                            #? Ojo aquí, mi diccionario, en realidad, no tiene
                                                            #? una clave llamada universidad, por lo que puedo
                                                            #? darle un valor por defecto, pero, ese valor no queda
                                                            #? guardado, solo se mostrará en esa consulta.

#                                   #TODO: PARA MODIFICAR UN DICCIONARIO
# mi_diccionario["edad"] = 26               #? Cambia el valor correspondiente a la clave edad, pasa de 25 a 26
# mi_diccionario["profesión"] = "Ingeniero" #? Agrega una nueva clave con su respectivo valor a mi diccionario
# del mi_diccionario["ciudad"]              #? Esto borra la clave y su valor correspondiente. 

#                                #TODO: MÉTODOS A USAR CON LOS DICCIONARIOS

#        #! .get(clave)     .get(clave, valor_por_defecto)
#? Este se usa para adquirir el valor correspondiente a una clave que es la que se pone entre los paréntesis
#? Si no existe el resultado es None, pero puedo ponerle un resultado por defecto si no existe ticha clave
#? En el ejemplo, c no existe como clave, pero para que no me diga None, le pongo un valor por defecto

#TODO: Ejemplo práctico:

diccionario = {
    "a": 1,
    "b": 2
    }

print(diccionario.get("a"))  #? Output: 1
print(diccionario.get("b"))  #? Output: 2
print(diccionario.get("c"))  #? Output: None
print(diccionario.get("d", "Clave no encontrada"))  #? Output: Clave no encontrada

