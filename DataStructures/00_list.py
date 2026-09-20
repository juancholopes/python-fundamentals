"""
Las listas son un tipo de almacenamiento de dato
también conocidos en otros lenguajes como arreglos o arrays
"""

lista = ["Manzana", "Pera", "Naranja"] # Empiezan con índice 0
print(type(lista))
print(lista)

# Cambiar alguno de sus elementos
lista[0] = "Sandía"
print(lista)

# Buscar dentro de una lista por el valor del campo en el que ocupa

if "Sandía" in lista:
    print("La sandía esta incluida en la lista")
else:
    pass

# Contar cuantos elementos existen en la lista
print(len(lista))

# Añadir elementos de la lista
lista.append("Mango") # Lo incluye al final
print(lista)

# Para incluir en una posición especifica de la lista, se utiliza insert()

lista.insert(0, "Mandarina") # En la primera posición
print(lista)

# Eliminar un elemento por su valor
lista.remove("Mandarina")
print(lista)

# Eliminar por el indice de la posición
lista.pop(0)
print(lista)

# Ordenar una lista alfabeticamente
lista.sort()
print(lista)

# Ordenar alfabeticamente a la inversa
lista.reverse()
print(lista)

# Eliminar todos los elementos de la lista
lista.clear()
print(lista)

# Unir dos listas

coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion1.extend(coleccion2)
print(coleccion1)

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

# Si no se quiere crear una nueva lista se utiliza append

