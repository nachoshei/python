tamano = int(input("Introduce el tamaño del arreglo: "))
numero = int(input("Introduce el numero para generar los multiplos: "))
arreglo = []
for i in range(1, tamano + 1):
    arreglo.append(numero * i)
    print("El arreglo con los multiplos de", numero, "es:", arreglo)