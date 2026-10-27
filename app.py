from src.cafeteria import Cafeteria


def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un número mayor que 0.")
        except ValueError:
            print("Ingresa un número válido.")


def registrar(cafeteria):
    print("\n--- REGISTRAR PEDIDO ---")
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    cantidad = leer_entero("Cantidad: ")

    while True:
        tipo = input("Tipo (1 = Normal, 2 = Prioritario): ")
        if tipo == "1":
            tipo = "Normal"
            break
        elif tipo == "2":
            tipo = "Prioritario"
            break
        print("Opción inválida.")

    tiempo = leer_entero("Tiempo de preparación (minutos): ")
    pedido = cafeteria.registrar_pedido(cliente, producto, cantidad, tipo, tiempo)
    print("Pedido registrado:", pedido)


def preparar(cafeteria):
    pedido = cafeteria.preparar_siguiente()
    if pedido:
        print("\nPreparando ->", pedido)
    else:
        print("\nNo hay pedidos pendientes.")


def consultar(cafeteria):
    pedido = cafeteria.consultar_siguiente()
    if pedido:
        print("\nSiguiente pedido ->", pedido)
    else:
        print("\nNo hay pedidos pendientes.")


def mostrar_pendientes(cafeteria):
    prioritarios, normales = cafeteria.pedidos_pendientes()
    print("\n--- PEDIDOS PRIORITARIOS ---")
    if prioritarios:
        for p in prioritarios:
            print(p)
    else:
        print("(vacía)")

    print("\n--- PEDIDOS NORMALES ---")
    if normales:
        for p in normales:
            print(p)
    else:
        print("(vacía)")


def mostrar_estadisticas(cafeteria):
    e = cafeteria.estadisticas()
    print("\n--- ESTADÍSTICAS ---")
    print("Pedidos registrados:", e["registrados"])
    print("Pedidos preparados:", e["preparados"])
    print("Pedidos cancelados:", e["cancelados"])
    print("Pendientes prioritarios:", e["pendientes_prioritarios"])
    print("Pendientes normales:", e["pendientes_normales"])
    print("Tiempo total de preparación:", e["tiempo_total"], "min")
    print("Tiempo promedio por pedido:", round(e["tiempo_promedio"], 2), "min")


def cancelar(cafeteria):
    numero = leer_entero("Número de pedido a cancelar: ")
    pedido = cafeteria.cancelar_pedido(numero)
    if pedido:
        print("Pedido cancelado:", pedido)
    else:
        print("No se encontró ese pedido en las filas pendientes.")


def main():
    cafeteria = Cafeteria()

    while True:
        print("\n===== CAFETERÍA UTEC =====")
        print("1. Registrar pedido")
        print("2. Preparar el siguiente pedido")
        print("3. Consultar el siguiente pedido")
        print("4. Mostrar pedidos pendientes")
        print("5. Consultar estadísticas")
        print("6. Cancelar pedido")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar(cafeteria)
        elif opcion == "2":
            preparar(cafeteria)
        elif opcion == "3":
            consultar(cafeteria)
        elif opcion == "4":
            mostrar_pendientes(cafeteria)
        elif opcion == "5":
            mostrar_estadisticas(cafeteria)
        elif opcion == "6":
            cancelar(cafeteria)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()