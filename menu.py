from transacciones import registrar_transaccion, visualizar_datos

def mostrar_menu():
    while True:
        print("\n" + "=" * 50)
        print("UTN-CAPITAL - GESTIÓN DE INVERSIONES VIP")
        print("=" * 50)
        print("1. Registrar una transacción")
        print("2. Visualizar todos los datos")
        print("3. Salir")
        print("=" * 50)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_transaccion()
        elif opcion == "2":
            visualizar_datos()
        elif opcion == "3":
            print("¡Gracias por usar UTN-Capital!")
            break
        else:
            print("Opción no válida.")
