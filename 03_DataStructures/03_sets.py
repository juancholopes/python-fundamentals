"""
Los conjuntos en python son estructuras de datos que son mutables pero cuyos valores
no se pueden repetir, es decir no puede haber el mismo valor repetido más de una
vez, ya que generalmente se ignora

Además de que en los conjuntos no se puede acceder a sus elementos por medio de un índice
ya que no tienen un orden predefinido
"""

frutas = {"Pera", "Manzana", "Naranja", "Papaya", "Papaya" }
print(frutas)
print(len(frutas))

# Añadir datos a las colecciones
frutas.add("Mango")
print(frutas)

# Update, permite añadir otro set al otro conjunto y ademas permite añadir otros tipos de datos como listas o tuplas
frutasDeLaPasion = {"Fresa", "Kiwi"}
frutas.update(frutasDeLaPasion)
print(frutas)

# Eliminar elementos del conjunto

# Remove ==> En este caso lanza un error si no existe el elemento
frutas.remove("Kiwi")
print(frutas)

# Discard ==> No lanza un error sino existe el elemento
frutas.discard("Maracuya")
print(frutas)

# Pop ==> Elimina un elmento aleatorio
frutas.pop()
print(frutas)

# Clear que vacía el conjunto
frutas.clear()
print(frutas)

"""
En matemáticas se pueden hacer conjunciones entre conjuntos
En python se pueden hacer conjunciones para saber las intersecciones, uniones y diferencia entre conjuntos
"""

transportesA = {"Bicicleta", "Moto", "Coche"}
transportesB = {"Avion", "Helicoptero", "Coche"}

union = transportesA.union(transportesB)
print(union) # Ninguno se repite

interseccion = transportesA.intersection(transportesB)
print(interseccion)

diferencia = transportesA.difference(transportesB)
print(diferencia)


# Recorrer los conjuntos
lenguajes = {"Python", "Java", "C++"}

for lenguaje in lenguajes:
    print(lenguaje) # Se imprime de manera aleatoria
