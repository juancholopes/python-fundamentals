
def ver_historial():

    try:
        with open("cafe.txt", "r", encoding="utf-8") as archivo:
            pedidos = archivo.read()
            if pedidos:
                for i, pedido in enumerate(pedidos.splitlines(), start=1):
                    print(str(i) + ". " + pedido.strip() + "\n")
            else:
                print("No hay historial de cafés aún.")
    except FileNotFoundError:
        print("Todavía no se han registrado cafés.")