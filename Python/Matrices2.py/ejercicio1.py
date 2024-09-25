def calcular_ventas_totales(ventas):
    total_por_categoria = [sum(col) for col in zip(*ventas)]
    return total_por_categoria

# Ejemplo de uso:
ventas = [
    [100, 200, 150],  # Lunes
    [90, 180, 120],   # Martes
    [80, 220, 130],   # Miércoles
    [110, 210, 140],  # Jueves
    [95, 205, 160],   # Viernes
    [85, 190, 170],   # Sábado
    [100, 230, 175]   # Domingo
]

print(calcular_ventas_totales(ventas))  # [660, 1435, 1045]