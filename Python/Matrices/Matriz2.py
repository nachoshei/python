print("-----------------------------------------------------------")
print("Matriz2: VERIFICAR SI LA MATRIZ ES SIMETRICA")
print("-----------------------------------------------------------")
A = []
D = int(input("Ingrese dimensiones de arreglo: "))
if 1 <= D and D <= 100:
    for i in range(D):
        A.append([])
        for j in range(D):
            elemento = input("A {}{}:".format(i, j))
            A[i].append(int(elemento))
    BAND = True
    i = 0
    while i < D and BAND == True:
        J = 0
        while j < i - 1 and BAND == True:
            if A[i][j] == A[j][i]:
                j = j + 1
            else:
                BAND = False
        i = i + 1
    if BAND:
        print("SI ES SIMETRICA")
    else:
        print("NO ES SIMETRICA")
else:
    print("La dimension de la matriz no es corrrecta.")