def validar_cantidad(cantidad_str):
    es_numero = True
    for char in cantidad_str:
        if char < '0' or char > '9':
            es_numero = False
            break
    if not es_numero:
        return False, 0
    cantidad = 0
    for char in cantidad_str:
        cantidad = cantidad * 10 + (ord(char) - 48)
    if 0 <= cantidad <= 500:
        return True, cantidad
    return False, 0
