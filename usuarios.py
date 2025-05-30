USUARIOS = [
    "Lunatico_pixel", "Sombra_cristal", "Ecoerrante", "Navefantasma", "Bytesdelabahia",
    "Tintaenelviento", "Relojoxidado", "Miradacodificada", "Circuitoazul", "Fuego_niebla",
    "Teclaerrante", "Nebulosa_urbana", "Sueno_binario", "Saltofantasma", "Claveoculta"
]

from utils import normalizar_usuario

def validar_usuario(usuario):
    usuario_norm = normalizar_usuario(usuario)
    for u in USUARIOS:
        if usuario_norm == normalizar_usuario(u):
            return True, usuario_norm
    return False, ""
