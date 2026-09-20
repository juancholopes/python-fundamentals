"""
Permiten manejar errores dentro del sistema y manejar dichas excepciones
sin que se bloquee la ejecución del programa
"""

try:
    print(x)
except NameError: # Se debe o debería pasar el nombre de la excepción
    print("Error de variable no definida")
finally:
    print("Se ejecuta siempre no importa el bloque de código")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error de división por cero")