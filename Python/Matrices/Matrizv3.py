def suma_matriz():
    #num_filas = 3
    #num_columnas = 3
    num_filas = int(input("Ingrese el numero de filas: "))
    num_columnas = int(input("Ingrese el numero de columnas: "))

    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = int(input(f"Ingrese el valor de {fila},{columna}: "))

    sumaColumna1 = 0
    for fila in range(num_filas):
        sumaColumna1 += matriz[fila][0]
    print(f"La suma de la columna 1 es: {sumaColumna1}")
suma_matriz()