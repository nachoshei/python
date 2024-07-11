A = []
B = []
C = []

print("Ingrese dimension de la matriz, maximo 100")
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
for i in range(filas):
    A.append([])
    B.append([])
    C.append([])
    for j in range(columnas):
        A[i].append( int(input("A{}{}: ".format(i + 1, j + 1))))

        B[i].append( int(input("B{}{}: ".format(i + 1, j + 1))))
        C[i].append( A[i][j] + B[i][j])
print("Matriz A: ", A[i])
print("Matriz B: ", B[i])
print("Matriz C: ", C[i])