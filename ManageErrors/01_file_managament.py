try:
    with open("file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    open("file.txt", "x")
    print("El archivo no existe")

try:
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write("Hola mundo desde el with")
    with open("file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("El archivo no existe")