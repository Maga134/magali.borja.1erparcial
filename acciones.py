ACCIONES_NOMBRES = ["APPLE", "TESLA", "NVIDIA"]
ACCIONES_PRECIOS = [10.41, 7.71, 8.50]

from utils import normalizar_accion

def validar_accion(accion):
    accion_norm = normalizar_accion(accion)
    for i in range(len(ACCIONES_NOMBRES)):
        if accion_norm == ACCIONES_NOMBRES[i]:
            return True, accion_norm, ACCIONES_PRECIOS[i]
    return False, "", 0.0
