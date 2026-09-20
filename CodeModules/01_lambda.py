"""
Las funciones lambda son funciones anónimas
utilizadas para realizar funciones simples y cortas

Primero se define una variable y luego se asigna la función lambda
"""

lambda_sumar = lambda x, y : x + y

lambda_sumar(2, 3) # No devuelve nada porque no la estamos asignando a una variable

resultado = lambda_sumar(2, 3)
print(resultado)

# Generador de funciones

def funcion_generadora(n):
    return lambda x : x * n

# Creamos la función

multiplicador_por_2 = funcion_generadora(2)
multiplicador_por_5 = funcion_generadora(5)

print(multiplicador_por_2(2))

print(multiplicador_por_5(2))

