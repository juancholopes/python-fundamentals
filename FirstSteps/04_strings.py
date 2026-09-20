# Metodos de Strings

string = "Hola mundo"

print(len(string)) # Cuenta los espacios también como un caracter

# Metodo para poner todo en mayúsculas

print(string.upper())

# Metodo para poner todo el string en minusculas
print(string.lower())

# Forma de saber si un caracter esta en la cadena

frase = "Esta es una frase y tiene muchas palabras"

print("frase" in frase)

poema = """
Ya no seré feliz. Tal vez no importa. 
Hay tantas otras cosas en el mundo; 
un instante cualquiera es más profundo 
y diverso que el mar.
"""

print("FELIZ" in poema) # False porque no se esta normalizando

# Normalizar una cadena
print("FELIZ".lower() in poema.lower())

# Index en las cadenas

mi_cadena = "Esto es una cadena"
print(mi_cadena[0])

# Slice de cadenas
print(mi_cadena[:]) # Toda la cadena
print(mi_cadena[0:5])

# Split de cadenas
print(mi_cadena.split(" ")) # Devuelve una lista con las palabras separadas por el caracter que se le pase al metodo

print(mi_cadena.split("e")) # Dividido por la letra e

