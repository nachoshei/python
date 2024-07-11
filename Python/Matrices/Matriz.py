filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz1 = []
matriz2 = []
sumaMatrices = []

for i in range(filas):
    matriz1.append([])
    matriz2.append([])
    sumaMatrices.append([])
    for j in range(columnas):
        element1 = int(input(f"Ingrese un valor para la posicion [{i}][{j}] en la primera matriz: ".format(i,j)))
        matriz1[i].append(element1)
        element2 = int(input(f"Ingrese un valor para la posición [{i}][{j}] en la segunda matriz: ".format(i,j)))
        matriz2[i].append(element2)
        sumaMatrices[i].append(element1+element2)


print(matriz1)
print(matriz2)
print(sumaMatrices)