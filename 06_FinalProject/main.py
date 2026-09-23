
from menu import mostrar_menu
from pedir_cafe import pedir_cafe
from ver_historial import ver_historial

def main():
    while True:
        # Mostrar menú
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Muchas gracias por haberse tomado un cafe con nosotros")
            break
        else:
            print("Opción invalida por favor seleccione una opción correcta")

if __name__ == "__main__":
    main()
