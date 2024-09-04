def suma_columna_matriz():
# Leer la cantidad de filas y columnas
    num_filas = int(input("Indique cantidad de filas: "))
    num_columnas = int(input("Indique cantidad de columnas: "))

    # Inicializar la matriz con ceros
    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]

    # Llenar la matriz con los valores ingresados por el usuario
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = int(input(f"Valor en {fila},{columna}: "))

    # Calcular la suma de la primera columna (columna 0)
    suma_columna1 = 0
    for fila in range(num_filas):
        suma_columna1 += matriz[fila][0]

    # Mostrar el resultado
    print(f"La suma de la columna 1 es: {suma_columna1}")

# Ejecutar la función principal
suma_columna_matriz()