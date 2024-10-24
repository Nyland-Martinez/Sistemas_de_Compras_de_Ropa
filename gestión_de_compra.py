# Clase padre para productos
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo privado
        self._precio = precio  #        ""   

    def obtener_precio(self):
        return self._precio

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: ${self._precio}")

# Clase Ropa que hereda de producto
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase padre
        self._cantidad = cantidad # Atributo específico de Ropa

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Cantidad: {self._cantidad}")

# Clases específicas que heredan de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase Ropa
        self._talla = talla  # Atributo específico de Camisa
        self._tipo_tela = tipo_tela 

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo de tela: {self._tipo_tela}")

class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, color):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase Ropa
        self._talla = talla # Atributo específico de Pantalon
        self._color = color

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}, Color: {self._color}")

class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, calce):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase Ropa
        self._calce = calce # Atributo específico de Zapatos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Calce: {self._calce}")

# Clase para manejar el carrito de compras
class Carrito:
    def __init__(self):
        self.productos = [] # Lista para almacenar los productos del carrito
        
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        for producto in self.productos:
            print(f"Nombre: {producto._nombre}, Precio: ${producto.obtener_precio()}")
            total += producto.obtener_precio()
        print(f"Total a pagar: ${total}")

# Clase para la tienda
class Tienda:
    def __init__(self, nombre):
        self._nombre = nombre
        self.prendas = [] # Lista para almacenar los productos del inventario
        self.carrito = Carrito()

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print(f"Inventario de la tienda {self._nombre}:")
        for prenda in self.prendas:
            prenda.mostrar_info()

    def seleccionar_producto(self):
        while True:
            nombre_producto = input("Introduce el nombre del producto (o 'fin' para terminar): ")
            if nombre_producto.lower() == 'fin':
                break
            for prenda in self.prendas:
                if prenda._nombre.lower() == nombre_producto.lower():
                    self.carrito.agregar_producto(prenda)
                    print(f"{prenda._nombre} agregado al carrito")
                    break
            else:
                print("Producto no encontrado")

    def procesar_compra(self):
        print("Resumen de la compra:")
        self.carrito.mostrar_resumen()


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda("Magic Shop")

    # Crear instancias de productos
    camisa = Camisa("Camisa de Hombre", 40.5, 15, "M", "Algodón")
    pantalon = Pantalon("Pantalón de Mujer", 85.99, 10, "L", "Azul")
    zapatos = Zapato("Zapatos Nike", 90.90, 5, "42")

    # Agregar productos al inventario
    tienda.agregar_prenda(camisa)
    tienda.agregar_prenda(pantalon)
    tienda.agregar_prenda(zapatos)

    # Mostrar inventario y procesar la compra
    tienda.mostrar_inventario()
    tienda.seleccionar_producto()
    tienda.procesar_compra()
