# clase producto
class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        # Usamos una tupla para garantizar que ID no sea modificable
        self.datos_producto = (producto_id, nombre)
        # Cantidad y precio pueden cambiar, así que los dejamos como valores individuales
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.datos_producto[0]}, Nombre: {self.datos_producto[1]}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    # Métodos para obtener y establecer atributos
    def get_id(self):
        return self.datos_producto[0]

    def get_nombre(self):
        return self.datos_producto[1]

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


import json


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos
        self.nombres_productos = set()  # Conjunto para evitar nombres duplicados

    def añadir_producto(self, producto):
        # Si el nombre del producto ya está en el inventario, no lo añadimos
        if producto.get_nombre() not in self.nombres_productos:
            self.productos[producto.get_id()] = producto
            self.nombres_productos.add(producto.get_nombre())
        else:
            print("El producto ya existe en el inventario.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            # Eliminamos también el nombre del producto del conjunto
            self.nombres_productos.remove(self.productos[producto_id].get_nombre())
            del self.productos[producto_id]
        else:
            print("Producto no encontrado")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print("Producto no encontrado")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre() == nombre:
                print(producto)
                return
        print("Producto no encontrado")

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_a_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({pid: {"id": p.get_id(), "nombre": p.get_nombre(), "cantidad": p.get_cantidad(), "precio": p.get_precio()}
                       for pid, p in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            self.productos = {pid: Producto(pid, info["nombre"], info["cantidad"], info["precio"]) for pid, info in data.items()}
            # También volvemos a llenar el conjunto con los nombres de los productos
            self.nombres_productos = {info["nombre"] for info in data.values()}


def menu():
    inventario = Inventario()

    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            if nombre in inventario.nombres_productos:
                print(f"El producto '{nombre}' ya existe en el inventario.")
            else:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_a_archivo(archivo)
        elif opcion == '7':
            archivo = input("Nombre del archivo para cargar el inventario: ")
            inventario.cargar_desde_archivo(archivo)
        elif opcion == '8':
            break
        else:
            print("Opción no válida")

