# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def moverse(self):
        return f"{self.nombre} está moviéndose."


# Clase derivada que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"


# Clase derivada que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"


# Uso de las clases
mi_perro = Perro("Rocky")
mi_gato = Gato("Garfiel")

print(mi_perro.nombre)  # Rocky
print(mi_perro.hacer_sonido())  # Guau!
print(mi_perro.moverse())  # Rocky está moviéndose.

print(mi_gato.nombre)  # Garfiel
print(mi_gato.hacer_sonido())  # Miau!
print(mi_gato.moverse())  # Whiskers está moviéndose.