

def pedir_cafe():
    print("/n Seleccione una opción ")
    print("1. Capuccino")
    print("2. Latte")
    print("3. Expresso")
    print("4. Mocha")
    print("5. Americano")

    opcion = input("Ingrese su opción: ")
    opciones = {
        "1": "Capuccino",
        "2": "Latte",
        "3": "Expresso",
        "4": "Mocha",
        "5": "Americano",
    }

    if opcion in opciones:
        print(f"Usted eligió {opciones[opcion]}")

        with open("cafe.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{opciones[opcion]}\n")
    else:
        print("Elija correctamente dentro de las opciones disponibles")