print("-----------------------------------------------------------")
print("Ejercicio 2: CUBOS PARES")
print("-----------------------------------------------------------")
#num = int(input("Ingrese 10 numeros pares: "))
num = 0
print("Ingrese 10 numeros pares: ")
for i in range(1, 10):
    num = int(input("Ingrese un numeros: "))
    if num % 2 == 0:
        cubo = num ** 3
        print("El cubo del numero par ",num, "es: ", cubo)
    else:
        print("ERROR: Ingrese un numero par.")