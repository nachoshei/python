arreglo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mayor = float('-inf')
segundoMayor = float('-inf')
for elemento in arreglo:
    if elemento > mayor:
        segundoMayor = mayor
        mayor = elemento
    elif elemento > segundoMayor and elemento != mayor:
        segundoMayor = elemento
print("El segundo mayor es: ", segundoMayor)