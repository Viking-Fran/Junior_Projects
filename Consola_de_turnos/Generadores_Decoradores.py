# Generadores_Decoradores

def mensaje_turno(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            numero = func(*args, **kwargs)
            return f"{mensaje} {numero}. Aguarde y será atendido."
        return wrapper
    return decorador


@mensaje_turno("Su turno es (Perfumería):")
def generar_turno_perfumeria(contador=[0]):
    contador[0] += 1
    return f"P-{contador[0]:03}"


@mensaje_turno("Su turno es (Farmacia):")
def generar_turno_farmacia(contador=[0]):
    contador[0] += 1
    return f"F-{contador[0]:03}"


@mensaje_turno("Su turno es (Cosméticos):")
def generar_turno_cosmeticos(contador=[0]):
    contador[0] += 1
    return f"C-{contador[0]:03}"
