print("-----------------------------------------------")
print("Ejercicio2: DIVISORES")
print("-----------------------------------------------")
print("Introduce un numero y para acabar uno negativo: ")
num = int(input("Num: "))
while num > 0:
    suma = 0
    for i in range(1,num+1):
        if num % i == 0:
            suma = suma + i
#suma = suma + num
    print("La suma de los divisores del numero:", num, "es", suma)
    print("Introduce un numero y para acabar uno negativo: ")
    num = int(input("Num: "))