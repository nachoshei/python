import math
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def buscar(alum_buscado, alumnos, alum_num):
    for indice in range(alum_num):
        if alumnos[indice] == alum_buscado.casefold():
            return indice
    return -1

def promedio_notas_estudiantes():
    alum_num = int(input("Ingrese el número de alumnos: "))
    alumnos = [None] * alum_num
    nota1 = [0] * alum_num
    nota2 = [0] * alum_num
    nota3 = [0] * alum_num

    for indice in range(alum_num):
        alumnos[indice] = input("Nombre: ").lower()
        nota1[indice] = int(input("Nota 1er trimestre: "))
        nota2[indice] = int(input("Nota 2do trimestre: "))
        nota3[indice] = int(input("Nota 3er trimestre: "))

    alum_buscado = input("A quien busca: ").lower()
    ind_alum = buscar(alum_buscado, alumnos, alum_num)

    if ind_alum != -1:
        promedio = calcular_promedio(nota1[ind_alum], nota2[ind_alum], nota3[ind_alum])
        print(f"El promedio de {alum_buscado.title()} es {math.ceil(promedio)}")
    else:
        print(f"No se pudo encontrar a {alum_buscado.title()}")

# Ejecutar la función principal
promedio_notas_estudiantes()