def suma_matriz():
    #num_filas = 3
    #num_columnas = 3
    num_filas = int(input("Ingrese el numero de filas: "))
    num_columnas = int(input("Ingrese el numero de columnas: "))

    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = int(input(f"Ingrese el valor de {fila},{columna}: "))

    for fila in range(num_filas):
        int(sumaColumna1 = 0)
        sumacolumna = sumaColumna1 + matriz[fila]
    print("La suma de la columna 1 es: {sumaColumna}")

suma_matriz()