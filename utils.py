def normalizar_usuario(usuario):
    resultado = ""
    for i in range(len(usuario)):
        ascii_val = ord(usuario[i])
        if i == 0 and 97 <= ascii_val <= 122:
            resultado += chr(ascii_val - 32)
        elif i > 0 and 65 <= ascii_val <= 90:
            resultado += chr(ascii_val + 32)
        else:
            resultado += usuario[i]
    return resultado

def normalizar_accion(accion):
    resultado = ""
    for char in accion:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            resultado += chr(ascii_val - 32)
        else:
            resultado += char
    return resultado
