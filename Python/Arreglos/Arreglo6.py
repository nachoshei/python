contadorN = 0
tam = int(input("Ingrese tamaño del arreglo: "))
for i in range(tam - 1):
    num = int(input("Ingrese un numero: "))
    if num < 0:
        contadorN += 1
print("Numero de elementos negativos:", contadorN)