# Clase padre para el producto
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  #         ""
        self._cantidad = cantidad  # Atributo privado

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self._cantidad}")

    def actualizar_stock(self, cantidad):
        self._cantidad = cantidad


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


# Clase para inventario
class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda al inventario

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda


# Clase para la tienda
class Tienda:
    def __init__(self, nombre, inventario):
        self.nombre = nombre
        self.inventario = inventario
        self.carrito = []  # Lista para almacenar el carrito de compras

    def mostrar_inventario(self):
        print(f"Inventario de la tienda {self.nombre}:")
        self.inventario.mostrar_inventario()

    def seleccionar_prenda(self):
        while True:
            nombre_prenda = input("Introduce el nombre de la prenda (o 'fin' para terminar): ")
            if nombre_prenda.lower() == 'fin':
                break
            for prenda in self.inventario.prendas:
                if prenda.nombre.lower() == nombre_prenda.lower():
                    self.carrito.append(prenda)  # Agrega la prenda al carrito
                    print(f"{prenda.nombre} agregado al carrito")
                    break
            else:
                print("Prenda no encontrada")

    def procesar_compra(self):
        total = 0
        for prenda in self.carrito:
            total += prenda.precio
        print(f"Total a pagar: ${total}")
        self.carrito.clear()


# Ejemplo de uso
inventario = Inventario()

# Crear instancias de RopaHombre y RopaMujer
camisa = RopaHombre("Camisa de Hombre", 40.5, 10, "M")
pantalon = RopaMujer("Pantalón de Mujer", 80.99, 12, "L")
zapatos = RopaHombre("Zapatos de Hombre", 90.95, 2, "42")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")

# Crear el inventario y agregar las prendas
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(zapatos)
inventario.agregar_prenda(falda)

# Crear la tienda y asignarle el inventario
tienda = Tienda("Magic Shop", inventario)

# Mostrar inventario
tienda.mostrar_inventario()

# Llamada al método para seleccionar producto y procesar la compra
tienda.seleccionar_prenda()
tienda.procesar_compra()
