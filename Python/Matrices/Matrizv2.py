def primera_matriz():
    num_filas = 3
    num_columnas = 3
    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]

    # Llenar la matriz con los valores ingresados por el usuario
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = int(input(f"Ingrese el valor de {fila},{columna}: "))

    # Imprimir los valores de la matriz
    for fila in range(num_filas):
        for columna in range(num_columnas):
            print(f"El valor de la celda {fila},{columna} es {matriz[fila][columna]}")

# Ejecutar la función principal
primera_matriz()