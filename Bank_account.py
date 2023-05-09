class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente{self.nombre} {self.apellido} \nCuenta: {self.numero_cuenta} \nBalance: {self.balance}"

    def depositar(self, monto):
        self.balance += monto
        print(f"Se depositaron {monto} dólares. Nuevo balance: {self.balance} dólares.")

    def retirar(self, monto):
        if monto > self.balance:
            print("No tiene suficiente saldo para retirar esa cantidad de dinero.")
        else:
            self.balance -= monto
            print(f"Se retiraron {monto} dólares. Nuevo balance: {self.balance} dólares.")


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta del cliente: ")
    balance = float(input("Ingrese el balance inicial de la cuenta: "))

    return Cliente(nombre, apellido, numero_cuenta, balance)


def inicio():
    cliente = crear_cliente()
    while True:
        print("¿Qué desea hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar balance")
        print("4. Salir")

        opcion = input("Ingrese la opción elegida: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print(f"El balance actual es de {cliente.balance} dólares.")
        elif opcion == "4":
            print("Gracias por utilizar nuestro programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


inicio()
