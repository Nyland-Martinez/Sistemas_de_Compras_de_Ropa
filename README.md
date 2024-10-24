Sistema de Compra de Ropa

Descripción del Proyecto

Este proyecto implementa un sistema de compra de ropa utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite a los usuarios seleccionar entre diferentes ítems de ropa (camisas, pantalones, zapatos) y procesar la compra. El proyecto demuestra el uso de los cuatro pilares de POO: encapsulamiento, herencia, polimorfismo y abstracción.

Clases Implementadas

Producto

Clase base que representa un producto general.

Atributos:

    _nombre (str): Nombre del producto, privado.
    _precio (float): Precio del producto, privado.

Métodos:

    obtener_precio(): Devuelve el precio del producto.
    mostrar_info(): Muestra la información del producto.

Ropa

Clase que hereda de Producto y añade características específicas de la ropa.

Atributos:

    _cantidad (int): Cantidad de producto disponible, privado.

Métodos:

    mostrar_info(): Muestra la información de la ropa.

Camisa, Pantalon, Zapato

Clases específicas que heredan de Ropa y añaden atributos específicos.

Atributos de Camisa:

    _talla (str): Talla de la camisa, privado.
    _tipo_tela (str): Tipo de tela de la camisa, privado.

Atributos de Pantalon:

    _talla (str): Talla del pantalón, privado.
    _color (str): Color del pantalón, privado.

Atributos de Zapato:

    _calce (str): Talla del zapato, privado.

Métodos:

    mostrar_info(): Muestra la información específica del producto.

Carrito

Clase para manejar el carrito de compras.

Atributos:

    productos (list): Lista de productos en el carrito.

Métodos:

    agregar_producto(producto): Añade un producto al carrito.
    mostrar_resumen(): Muestra el resumen de la compra y el total a pagar.

Tienda

Clase que maneja los productos disponibles y las compras.

Atributos:

    _nombre (str): Nombre de la tienda, privado.
    prendas (list): Lista de productos disponibles en la tienda.
    carrito (Carrito): Carrito de compras del usuario.

Métodos:

    agregar_prenda(prenda): Añade una prenda al inventario.
    mostrar_inventario(): Muestra el inventario de la tienda.
    seleccionar_producto(): Permite al usuario seleccionar productos.
    procesar_compra(): Muestra el resumen de la compra y el total a pagar.

El programa permitirá al usuario seleccionar productos y procesar la compra.

Ejecución del Programa

Para ejecutar el programa, simplemente ejecuta el archivo principal en tu entorno de desarrollo de Python:

    python nombre_del_archivo.py

Autor

Nyland Haidee Martínez Villalba
