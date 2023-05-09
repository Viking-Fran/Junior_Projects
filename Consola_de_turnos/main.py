# principal.py

from Generadores_Decoradores import generar_turno_perfumeria, generar_turno_farmacia, generar_turno_cosmeticos

def elegir_area():
    print("Elija el área a la que desea dirigirse:")
    print("1. Perfumería")
    print("2. Farmacia")
    print("3. Cosméticos")
    opcion = input("Ingrese el número de opción: ")
    if opcion == "1":
        return generar_turno_perfumeria()
    elif opcion == "2":
        return generar_turno_farmacia()
    elif opcion == "3":
        return generar_turno_cosmeticos()
    else:
        print("Opción inválida.")
        return None

def tomar_turnos():
    while True:
        turno = elegir_area()
        if turno is not None:
            print(turno)
            nueva_solicitud = input("¿Desea tomar otro turno? (s/n) ")
            if nueva_solicitud.lower() == "n":
                break

if __name__ == "__main__":
    tomar_turnos()
