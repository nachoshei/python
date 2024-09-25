def calcular_gasto_total(gastos):
    total_por_tipo_gasto = [sum(gasto) for gasto in gastos]
    return total_por_tipo_gasto

# Ejemplo de uso:
gastos = [
    [200, 250, 300],  # Alimentación
    [150, 200, 180],  # Transporte
    [100, 120, 130],  # Servicios
]

print(calcular_gasto_total(gastos))  # [750, 530, 350]