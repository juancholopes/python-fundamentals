# También son un tipo de dato

verdadero = True
falso = False

print(type(verdadero))

# Casteo de datos con bool()

print(bool(0)) # False porque cero representa falso
print(bool(1)) # True porque uno representa verdadero

# Listas

print(bool([])) # False porque esta vacia
print(bool([1,2,3])) # True porque tiene elementos

# Instancias de clases

entero = 23
print(isinstance(entero, int)) # True porque es un entero

float = 23.5
print(isinstance(float, str)) # En este caso False y la instancia de los strings se escribe str en Python