tamano = int(input("Introduce el tamaño de los arreglos: "))
nombres = []
longitudes = []
for i in range(tamano):
    nombre = input(f"Introduce el nombre {i+1}: ")
    nombres.append(nombre)
    longitudes.append(len(nombre))
for i in range(tamano):
    print(f"Nombre: {nombres[i]}, Longitud: {longitudes[i]}")