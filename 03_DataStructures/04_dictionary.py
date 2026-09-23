"""
Los diccionarios son un tipo de estructura de dato que permite almacenar datos con clave
y valor, en otros lenguajes son llamados objetos.
"""

familia = {
    "padre": "Juan",
    "madre": "Maria",
    "hijo" : "Pedro"
}

print(familia)

# Se pueden añadir elementos a un diccionario

familia["hija"] = "Ana"
print(familia)

# Se puede cambiar el valor de un elemento
familia["padre"] = "Jose"
print(familia)

# Se puede eliminar un elemento
familia.pop("hijo")
print(familia)

# Eliminar el último  par insertado en el diccionario
familia.popitem()
print(familia)

# Actualizar con update o añadir en la misma linea
familia.update({"hijo": "Pedro", "abuelo": "Lucas"})
print(familia)

# Para imprimir solo las claves de el diccionario
print(familia.keys())

# Para imprimir solo los valores del diccionario
print(familia.values())

# Recorrer el diccionario por keys
for key in familia.keys():
    print(key)

# Recorrer el diccionario por values
for value in familia.values():
    print(value)

# Recorrer tanto la llave como el valor
for key, value in familia.items():
    print(key, value)