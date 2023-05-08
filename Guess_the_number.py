from random import randint

estimado = 0
nombre = input("Cual es tu nombre: ")
numero_secreto = randint(1, 100)
vidas = 0

print(f"ok {nombre}, he pensado un numero entre 1 y 100\ntienes 8 intentos para adivinarlo.")

while vidas < 8:
    estimado = int(input("Ingresa el numero: "))
    vidas += 1
    if estimado not in range(1,100):
        print("Numero fuera de rango, debes ingresar un numero entre 1 y 100")

    elif estimado < numero_secreto:
        print("Incorrecto ,has ingresado un numero menor")

    elif estimado > numero_secreto:
        print("Incorrecto ,has ingresado un numero mayor")

    else:
        print(f"Correcto {nombre}!! Has ganado :)")
        print(f"Lo has logrado en {vidas} intentos")
        break

if estimado != numero_secreto:
    print(f"Game over, el numero correcto era {numero_secreto}")








