"""
Operadores de asignación en python

Para asignar un valor a una variable o asignarle un valor con una operación incluida

"""


# Asignación normal
variable = 10

# Asignación y suma

variable += 10 # es igual a variable = variable + 10 es decir 20
print(variable)

# Asignación y resta
variable -= 10 # Le quita 10 es decir queda igual a 10
print(variable)

#Asignación y multiplicacion
variable *= 2
print(variable)

# Asignación y división flotante
variable /= 2
print(variable)

# Asignación y división entera
variable //= 2
print(variable)

# Asignación y potencia
otra_variable = 2
otra_variable **= 2
print(otra_variable)

# Asignación y módulo
otra_variable %= 2
print(otra_variable)

# Walrus operator
print(otra_variable)
print(variable_nueva := "Walrus significa en español morsa")

"""
Este último operador es util cuando se quiere 
asignar un valor a una variable dentro de una función
"""



