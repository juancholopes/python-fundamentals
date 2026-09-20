"""
Las funciones permiten ejecutar tareas repetitivas
cuando se invocan, hacer modificación de datos y retornar resultados.
"""

def saludar():
    print("Hola mundo")

saludar()

# Las funciones reciben parámetros definidos previamente en los argumentos de la función

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Juan")

# Siempre se debe dar los parametros de los argumentos de la función

def sumar(a, b ):
    return a + b
#print(sumar(2)) # Daría error

# Se debe asignar a una variable cuando se retorna un valor
sumar(4, 5) # No se esta asignando el valor que se esta retornando
resultado = sumar(8,3)
print(resultado)
