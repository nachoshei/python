cuantos = int(input("ingrese la cantidad de numeros a ingresar: "))
count = 0
suma = 0
i = 1
lista = []

while i <= cuantos:
    temp = int(input("ingrese la temperatura: "))
    lista.append (temp) 
    i += 1
    suma = suma + temp

promedio = suma/cuantos

for j in lista: 
    if j >= promedio:
        count += 1

print (f"el promedio es {promedio} y hay {count} mayores o iguales al promedio")