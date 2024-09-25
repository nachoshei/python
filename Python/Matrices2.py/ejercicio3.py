def calcular_inventario_total(inventario):
    total_por_producto = [sum(producto) for producto in inventario]
    return total_por_producto

# Ejemplo de uso:
inventario = [
    [50, 30, 20],  # Producto 1
    [40, 25, 35],  # Producto 2
    [30, 45, 25],  # Producto 3
]

print(calcular_inventario_total(inventario))  # [100, 100, 100]