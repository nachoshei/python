def matrizVentas():
    dias = 7
    categoria = 5
    for i in range(dias):
        for j in range(categoria):
            matrizVentas[i, j] = int(input(f"Ingrese las ventas para la categoria {j}"))
