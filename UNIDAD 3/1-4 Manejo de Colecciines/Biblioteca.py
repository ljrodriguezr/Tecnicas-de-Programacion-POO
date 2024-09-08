# class libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f'ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}'


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f'El libro {libro.titulo} ya existe.')
        else:
            self.libros[libro.isbn] = libro
            print(f'El libro {libro.titulo} fue añadido.')

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f'El libro con ISBN {isbn} fue eliminado.')
        else:
            print(f'El libro con ISBN {isbn} no existe.')

    def agregar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f'El usuario {usuario.nombre} ya existe.')
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f'Usuario {usuario.nombre} agregado.')

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f'El usuario con ID {id_usuario} fue dado de baja.')
        else:
            print(f'El usuario con ID {id_usuario} no existe.')

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f'El usuario con ID {id_usuario} no existe.')
        elif isbn not in self.libros:
            print(f'El libro con ISBN {isbn} no existe.')
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f'Al usuario {usuario.nombre} le fue prestado el libro {libro.titulo}.')

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f'Libros prestados a {usuario.nombre}:')
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f'El usuario {usuario.nombre} no tiene libros prestados.')
        else:
            print(f'El usuario con ID {id_usuario} no existe.')


def menu():
    mi_biblioteca = Biblioteca()
    while True:
        print('\n--- Menú ---')
        print('1. Agregar libro')
        print('2. Quitar libro')
        print('3. Prestar libro')
        print('4. Agregar usuario')
        print('5. Dar de baja usuario')
        print('6. Listar libros prestados')
        print('7. SALIR')

        opcion = input('Selecciona una opción: ')
        if opcion == '1':
            titulo = input('Ingrese el título del libro: ')
            autor = input('Ingrese el autor del libro: ')
            categoria = input('Ingrese la categoría del libro: ')
            isbn = input('Ingrese el ISBN del libro: ')
            libro = Libro(titulo, autor, categoria, isbn)
            mi_biblioteca.agregar_libro(libro)
        elif opcion == '2':
            isbn = input('Ingrese el ISBN del libro a eliminar: ')
            mi_biblioteca.quitar_libro(isbn)
        elif opcion == '3':
            id_usuario = input('Ingrese el ID del usuario: ')
            isbn = input('Ingrese el ISBN del libro: ')
            mi_biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == '4':
            nombre = input('Ingrese el nombre del usuario: ')
            id_usuario = input('Ingrese el ID del usuario: ')
            usuario = Usuario(nombre, id_usuario)
            mi_biblioteca.agregar_usuario(usuario)
        elif opcion == '5':
            id_usuario = input('Ingrese el ID del usuario a dar de baja: ')
            mi_biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == '6':
            id_usuario = input('Ingrese el ID del usuario para ver libros prestados: ')
            mi_biblioteca.listar_libros_prestados(id_usuario)
        elif opcion == '7':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción inválida. Intenta de nuevo.')


if __name__ == '__main__':
    menu()






