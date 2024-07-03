arreglo = [3, -1, 4, -1, 5, 9, -2, 6, 5, -3, 5]
contador_negativos = 0
for elemento in arreglo:
    if elemento < 0:
        contador_negativos += 1
print("Numero de elementos negativos:", contador_negativos)
