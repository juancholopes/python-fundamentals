x = "Esta es una variable en python"

print(x)

array = ["Hola", "Mundo", "Python"]
copy = array
copy.append("Hola Mundo")

print(array)
print(copy)


array2 = ["Hola", "Mundo", "Python", ["Elemento1", "Elemento2"]]
copy2 = array2.copy()
copy2.append("Nuevo Elemento")
print(array2)
print(copy2)

print(type(array2))


# También esta el casteo de datos


entero = 34
print(type(entero))

flotante = float(entero)
print(flotante)