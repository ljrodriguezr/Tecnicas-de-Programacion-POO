from abc import ABC, abstractmethod
import math

# Clase base abstracta
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

# Clase derivada para círculos
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

# Clase derivada para rectángulos
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Clase derivada para triángulos
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura

# Uso del polimorfismo
formas = [
    Circulo(6),
    Rectangulo(5, 7),
    Triangulo(5, 7)
]

for forma in formas:
    print(f"Área: {forma.area()}")