# ejemplos de const y dest
class Persona:
    """
    Clase que representa a una persona.

    Atributos:
        nombre (str): El nombre de la persona.
        edad (int): La edad de la persona.

    Métodos:
        __init__(self, nombre, edad): Constructor de la clase.
        __del__(self): Destructor de la clase.
        presentarse(self): Presenta a la persona.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Inicializa los atributos nombre y edad de la persona.

        Args:
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Creando persona: {self.nombre} ({self.edad} años)")

    def __del__(self):
        """
        Destructor de la clase Persona.

        Se llama automáticamente cuando se elimina la instancia de la persona.
        Imprime un mensaje de despedida.
        """
        print(f"Despidiendo a la  persona: {self.nombre} ({self.edad} años)")

    def presentarse(self):
        """
        Presenta a la persona.

        Imprime el nombre y la edad de la persona.
        """
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Ejemplo de uso
persona1 = Persona("Paul Chanaluisa", 3)
persona1.presentarse()

# Se elimina la variable 'persona1', lo que desencadena el destructor
del persona1

persona2 = Persona("Lucia Rodriguez", 28)
persona2.presentarse()

# Se elimina la variable 'persona2', lo que desencadena el destructor
del persona2
