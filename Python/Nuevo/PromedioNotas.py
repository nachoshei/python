def calcularPromedio(nota1, nota2, nota3):
    prom3 = (nota1 + nota2 + nota3)/3

def buscar(alumBuscado, alumnos, cantidadA):
    indAlum = -1
    indice = 0
    while indice < cantidadA and indAlum == -1:
        if alumnos[indice] == alumBuscado:
            indAlum = indice

def promedioEscolar():
    cantidadA = int(input("Ingrese la cantidad de alumnos: "))
    for indice in range(cantidadA):
        alumnos[indice] = int(input(""))