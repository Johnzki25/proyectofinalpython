print('Proyecto Final de John Denrick')

#str es string, int de integer ,float 
class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, cantidad: int):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self) -> str:
        return self.__nombre

    def get_categoria(self) -> str:
        return self.__categoria

    def get_precio(self) -> float:
        return self.__precio

    def get_cantidad(self) -> int:
        return self.__cantidad

    # Setters
    def set_precio(self, precio: float):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self) -> str:
        return f"Producto: {self.__nombre}, Categoría: {self.__categoria}, Precio: €{self.__precio:.2f}, Cantidad: {self.__cantidad}"


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto: Producto):
        if any(p.get_nombre().lower() == producto.get_nombre().lower() for p in self.__productos):
            raise ValueError("El producto ya existe en el inventario.")
        self.__productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado con éxito.")

    def actualizar_producto(self, nombre: str, precio: float = None, cantidad: int = None):
        producto = self.__buscar_producto_por_nombre(nombre)
        if producto:
            if precio is not None:
                producto.set_precio(precio)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            print(f"Producto '{nombre}' actualizado con éxito.")
        else:
            print(f"No se encontró el producto con nombre '{nombre}'.")

    def eliminar_producto(self, nombre: str):
        producto = self.__buscar_producto_por_nombre(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
        else:
            print(f"No se encontró el producto con nombre '{nombre}'.")

    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario:")
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre: str):
        producto = self.__buscar_producto_por_nombre(nombre)
        if producto:
            print(producto)
        else:
            print(f"No se encontró el producto con nombre '{nombre}'.")

    def __buscar_producto_por_nombre(self, nombre: str) -> Producto:
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None


def menu():
    inventario = Inventario()

    # Ejemplo de productos predefinidos para gym
    print ("Ejemplos de los productos predeterminados para gym")

    inventario.agregar_producto(Producto("Mancuernas", "Pesas", 69, 20))
    inventario.agregar_producto(Producto("Esterilla", "Accesorios", 10, 50))
    inventario.agregar_producto(Producto("Cinturón de levantamiento", "Accesorios", 25, 10))
    inventario.agregar_producto(Producto("Kettlebell", "Pesas", 40, 15))
    inventario.agregar_producto(Producto("Banda elástica", "Accesorios", 10, 100))

    while True:
        print("\n=== Gestión de Inventario de Gimnasio ===")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad en stock: "))
                producto = Producto(nombre, categoria, precio, cantidad)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                nombre = input("Nombre del producto a actualizar: ")
                precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
                cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
                precio = float(precio) if precio else None
                cantidad = int(cantidad) if cantidad else None
                inventario.actualizar_producto(nombre, precio, cantidad)

            elif opcion == "3":
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == "4":
                inventario.mostrar_inventario()

            elif opcion == "5":
                nombre = input("Nombre del producto a buscar: ")
                inventario.buscar_producto(nombre)

            elif opcion == "6":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    menu()
