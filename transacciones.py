MAX_TRANSACCIONES = 1000
transacciones = [None] * MAX_TRANSACCIONES
total_transacciones = 0

from usuarios import validar_usuario
from acciones import validar_accion
from validaciones import validar_cantidad

def registrar_transaccion():
    global total_transacciones, transacciones

    print("\n" + "=" * 50)
    print("REGISTRAR NUEVA TRANSACCIÓN")
    print("=" * 50)

    # Usuario
    while True:
        usuario = input("Ingrese nombre de usuario: ")
        valido, usuario_norm = validar_usuario(usuario)
        if valido:
            break
        print("Usuario no válido. Intente nuevamente.")

    # Acción
    while True:
        accion = input("Ingrese acción (APPLE, TESLA, NVIDIA): ")
        valido, accion_norm, precio = validar_accion(accion)
        if valido:
            break
        print("Acción no válida. Intente nuevamente.")

    # Cantidad
    while True:
        cantidad_str = input("Ingrese cantidad de acciones (0-500): ")
        valido, cantidad = validar_cantidad(cantidad_str)
        if valido:
            break
        print("Cantidad no válida. Intente nuevamente.")

    total = precio * cantidad

    if total_transacciones < MAX_TRANSACCIONES:
        transacciones[total_transacciones] = [usuario_norm, accion_norm, precio, cantidad, total]
        total_transacciones += 1

    print("\n¡Transacción registrada con éxito!")
    print(f"Usuario: {usuario_norm}, Acción: {accion_norm}, Cantidad: {cantidad}, Total: ${total:.2f}")


def visualizar_datos():
    if total_transacciones == 0:
        print("No hay transacciones registradas.")
        return
    print("\n" + "=" * 70)
    print("LISTADO COMPLETO DE TRANSACCIONES (ORDENADO)")
    print("=" * 70)
    print("Usuario\t\tAcción\tPrecio\tCantidad\tTotal")
    print("-" * 70)
    
