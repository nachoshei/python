def calcular_promedio_calificaciones(calificaciones):
    promedios = [sum(estudiante) / len(estudiante) for estudiante in calificaciones]
    return promedios

# Ejemplo de uso:
calificaciones = [
    [85, 90, 78],  # Estudiante 1
    [92, 88, 94],  # Estudiante 2
    [70, 85, 80],  # Estudiante 3
    [90, 92, 88]   # Estudiante 4
]

print(calcular_promedio_calificaciones(calificaciones))  # [84.33, 91.33, 78.33, 90.0]