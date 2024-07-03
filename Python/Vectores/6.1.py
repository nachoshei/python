cuantos = int(input("ingrese la cantidad de numeros a ingresar: "))
numeros = []
i = 1

while i <= cuantos:
    numero = int(input("ingrese los numeros: "))
    numeros.append(numero)
    i += 1

print (numeros)