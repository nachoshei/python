import random
def matriz_azar():
    #num_filas = 3
    #num_columnas = 3
    num_filas = int(input("Ingrese el numero de filas: "))
    num_columnas = int(input("Ingrese el numero de columnas: "))

    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = random.randint(0,9)
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            print(f"matriz[{fila},{columna}] = {matriz[fila][columna]}")

matriz_azar()