def dia_mayor_produccion(produccion):
    mayor_por_producto = [dia.index(max(dia)) + 1 for dia in produccion]
    return mayor_por_producto

# Ejemplo de uso:
produccion = [
    [100, 120, 90, 110],  # Producto 1
    [80, 95, 85, 90],     # Producto 2
    [150, 130, 160, 140], # Producto 3
]

print(dia_mayor_produccion(produccion))  # [2, 2, 3]