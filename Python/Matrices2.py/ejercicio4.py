def calcular_reservas_por_mes(reservas):
    total_por_mes = [sum(mes) for mes in reservas]
    return total_por_mes

# Ejemplo de uso:
reservas = [
    [3, 5, 8, 2],  # Enero
    [6, 3, 9, 4],  # Febrero
    [7, 8, 5, 6],  # Marzo
]

print(calcular_reservas_por_mes(reservas))  # [18, 22, 26]