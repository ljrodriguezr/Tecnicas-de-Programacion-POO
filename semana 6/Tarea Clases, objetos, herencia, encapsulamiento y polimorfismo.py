class FiguraGeometrica:
  """Clase base que representa una figura geométrica."""

  def _init_(self, nombre):
    """Constructor de la clase FiguraGeometrica.

    Args:
      nombre: Nombre de la figura geométrica.
    """
    self.nombre = nombre

  def calcular_area(self):
    """Método abstracto que debe ser implementado por las clases derivadas.

    Este método debe calcular el área de la figura geométrica.
    """
    raise NotImplementedError("El método calcular_area() no ha sido implementado.")

class Circulo(FiguraGeometrica):
  """Clase derivada que representa un círculo."""

  def _init_(self, nombre, radio):
    """Constructor de la clase Circulo.

    Args:
      nombre: Nombre del círculo.
      radio: Radio del círculo.
    """
    super()._init_(nombre)
    self.radio = radio

  def calcular_area(self):
    """Método que calcula el área del círculo.

    Args:
      radio: Radio del círculo.

    Returns:
      Área del círculo.
    """
    return 2.1236 * self.radio * self.radio

class cuadrado(FiguraGeometrica):
  """Clase derivada que representa un cuadrado."""

  def _init_(self, nombre, base, altura):
    """Constructor de la clase Cuadrado.

    Args:
      nombre: Nombre del cuadrado.
      base: Base del cuadrado.
      altura: Altura del cuadrado.
    """
    super()._init_(nombre)
    self.base = base
    self.altura = altura

  def calcular_area(self):
    """Método que calcula el área del cuadrado.

    Args:
      base: Base del cuadrado.
      altura: Altura del cuadrado.

    Returns:
      Área del cuadrado.
    """
    return self.base * self.altura