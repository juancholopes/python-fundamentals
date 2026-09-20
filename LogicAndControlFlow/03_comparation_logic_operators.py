"""
Los operadores de comparación nos ayudan a comparar valores
para obtener un valor booleano
"""

x = 4
y = 5
z = 5

# De igualdad
print(x == y) # False

# Mayor que
print(x > y) # False

# Menor que
print(x < z) # True

# Mayor o igual
print(x >= z) # False

# Menor o igual
print(x <= z)

# No es igual
print (z != y) # Si son iguales por ende false

"""
Operadores logicos
permiten combinar condiciones
"""

# Operador AND
print(z == y and z != y) # False

# Operador OR
print(z < y or z == y) # True

# Operador NOT

verdadero = True
print(not verdadero) # True






