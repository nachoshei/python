def calcular_promedios(estudiantes):
    """
    Calcula el promedio de notas por asignatura para cada estudiante.
    
    :param estudiantes: Diccionario de estudiantes y sus notas.
    :return: Diccionario de promedios.
    """
    promedios = {}
    for estudiante, asignaturas in estudiantes.items():
        promedios[estudiante] = {}
        for asignatura, notas in asignaturas.items():
            promedio = sum(notas) / len(notas) if notas else 0
            promedios[estudiante][asignatura] = promedio
    return promedios

def listar_estudiantes_con_promedio_alto(promedios, umbral):
    """
    Lista los estudiantes con un promedio mayor a un valor dado en al menos una asignatura.
    
    :param promedios: Diccionario de promedios.
    :param umbral: Umbral de promedio.
    """
    print(f"Estudiantes con promedio mayor a {umbral} en alguna asignatura:")
    for estudiante, asignaturas in promedios.items():
        for asignatura, promedio in asignaturas.items():
            if promedio > umbral:
                print(f"{estudiante} en {asignatura} con promedio {promedio:.2f}")

def agregar_nota(estudiantes, estudiante, asignatura, nota):
    """
    Agrega una nueva nota a un estudiante en una asignatura específica.
    
    :param estudiantes: Diccionario de estudiantes y sus notas.
    :param estudiante: Nombre del estudiante.
    :param asignatura: Nombre de la asignatura.
    :param nota: Nota a agregar.
    """
    if estudiante in estudiantes:
        if asignatura in estudiantes[estudiante]:
            estudiantes[estudiante][asignatura].append(nota)
        else:
            estudiantes[estudiante][asignatura] = [nota]
    else:
        estudiantes[estudiante] = {asignatura: [nota]}

# Diccionario inicial de estudiantes y notas
estudiantes = {
    "Juan Perez": {"Matemáticas": [8, 9, 7], "Historia": [6, 7]},
    "Maria Garcia": {"Matemáticas": [10, 9, 8], "Historia": [7, 8]},
    "Ana Lopez": {"Matemáticas": [5, 6], "Historia": [9, 10]}
}

# Ejemplo de uso
promedios = calcular_promedios(estudiantes)
listar_estudiantes_con_promedio_alto(promedios, 8)
agregar_nota(estudiantes, "Juan Perez", "Matemáticas", 10)
print("Nuevas notas de Juan Perez:", estudiantes["Juan Perez"])