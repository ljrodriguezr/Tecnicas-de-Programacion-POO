class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.__numero_cuenta = numero_cuenta  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Método público para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de {cantidad} realizado. {self.mostrar_saldo()}"
        else:
            return "La cantidad a depositar debe ser positiva."

    # Método público para retirar dinero
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro de {cantidad} realizado. {self.mostrar_saldo()}"
        else:
            return "Fondos insuficientes o cantidad inválida."

    # Método público para mostrar el saldo
    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"

    # Método público para obtener el número de cuenta
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    # Método público para cambiar el número de cuenta (aunque esto generalmente no se hace)
    def cambiar_numero_cuenta(self, nuevo_numero):
        self.__numero_cuenta = nuevo_numero
        return f"Número de cuenta cambiado a: {self.__numero_cuenta}"

# Uso de la clase
cuenta = CuentaBancaria("1234567890", 1000)

# Acceso controlado a través de métodos
print(cuenta.mostrar_saldo())          # Saldo actual: 8000
print(cuenta.depositar(400))           # Depósito de 400 realizado. Saldo actual: 1600
print(cuenta.retirar(300))             # Retiro de 200 realizado. Saldo actual: 1200
print(cuenta.obtener_numero_cuenta())  # 1234567893
print(cuenta.cambiar_numero_cuenta("0968847138"))  # Número de cuenta cambiado a: 0968847138

# Intentos de acceso directo fallarán porque los atributos son privados
# print(cuenta.__saldo)  # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'
# print(cuenta.__numero_cuenta)  # AttributeError: 'CuentaBancaria' object has no attribute '__numero_cuenta'