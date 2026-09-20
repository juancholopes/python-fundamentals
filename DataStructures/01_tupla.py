"""
Las tuplas a diferencia de las listas son inmutables
es decir no se pueden modificar directamente
"""

tecnologias = ("Python", "Java", "C++")
print(type(tecnologias))
print(tecnologias)

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

tuplaString = ("Tupla",) # Se añade la coma al final para que se covierta a tupla sino queda como string
print(type(tuplaString))

# Para añadir a una tupla se tiene que convertir a lista y luego a tupla
colores = ("Rojo", "Amarillo", "Naranja")
print(colores)

coloresLista = list(colores) # Se convierte a lista
coloresLista.append("Azul")
colores = tuple(coloresLista)
print(colores)

# Se pueden recorrer las tuplas
for color in colores:
    print(color)

# Multiplicar la tuplas
print(colores * 2)

# Se pueden repetir elementos en la tupla

numeros1 = (1, 2, 3)
numeros2 = numeros1 * 2
print(numeros2)

