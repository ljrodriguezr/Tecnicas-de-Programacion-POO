# Abstracción: Clase base abstracta
from abc import ABC, abstractmethod
class CuentaBancaria(ABC):
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta  # Encapsulamiento: atributo protegido
        self._saldo = saldo  # Encapsulamiento: atributo protegido

    @abstractmethod
    def depositar(self, cantidad):
        pass

    @abstractmethod
    def retirar(self, cantidad):
        pass

    def mostrar_saldo(self):
        return f"Saldo actual de la cuenta {self._numero_cuenta}: {self._saldo}"


# Herencia: Clase derivada para cuenta de ahorros
class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, tasa_interes):
        super().__init__(numero_cuenta, saldo)
        self._tasa_interes = tasa_interes  # Encapsulamiento: atributo protegido

    def depositar(self, cantidad):
        self._saldo += cantidad
        return f"Depósito de {cantidad} realizado. {self.mostrar_saldo()}"

    def retirar(self, cantidad):
        if cantidad > self._saldo:
            return "Fondos insuficientes."
        else:
            self._saldo -= cantidad
            return f"Retiro de {cantidad} realizado. {self.mostrar_saldo()}"

    def aplicar_interes(self):
        self._saldo += self._saldo * self._tasa_interes
        return f"Interés aplicado. {self.mostrar_saldo()}"


# Herencia: Clase derivada para cuenta corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, limite_credito):
        super().__init__(numero_cuenta, saldo)
        self._limite_credito = limite_credito  # Encapsulamiento: atributo protegido

    def depositar(self, cantidad):
        self._saldo += cantidad
        return f"Depósito de {cantidad} realizado. {self.mostrar_saldo()}"

    def retirar(self, cantidad):
        if cantidad > self._saldo + self._limite_credito:
            return "Fondos insuficientes incluso con límite de crédito."
        else:
            self._saldo -= cantidad
            return f"Retiro de {cantidad} realizado. {self.mostrar_saldo()}"


# Uso de polimorfismo
cuentas = [
    CuentaAhorros("001", 1000, 0.05),
    CuentaCorriente("002", 600, 300)
]

for cuenta in cuentas:
    print(cuenta.depositar(200))
    print(cuenta.retirar(100))

# Aplicando interés a la cuenta de ahorros
cuenta_ahorros = cuentas[0]  # Suponiendo que la primera cuenta es una CuentaAhorros
if isinstance(cuenta_ahorros, CuentaAhorros):
    print(cuenta_ahorros.aplicar_interes())