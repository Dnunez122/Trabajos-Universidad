# Importar solo las funciones necesarias de re
from re import match, search

# Listas de productos y sus precios/códigos usando diccionarios de python 
productos_precio = {"Cartón de huevos": 2500, "Caja de leche": 1850, "Botella de agua": 2000}
productos_codigo = {"Cartón de huevos": 28289, "Caja de leche": 13523, "Botella de agua": 98982}

# Solicitar el nombre o código del producto deseado
Orden = input("Nombre o código de producto que desea: ")

# Verificar si el producto está en la lista por nombre o código
if Orden in productos_codigo:
    print(f"Precio de {Orden}: {productos_precio[Orden]}")
    cantidad = int(input("¿Cuántas unidades desea comprar? "))
    total = productos_precio[Orden] * cantidad
    print(f"El total a pagar es: {total}")
else:
    print("Producto no encontrado en la lista.")
