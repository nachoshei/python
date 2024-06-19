print("-----------------------------------------------------------")
print("Ejercicio 11: PAR")
print("-----------------------------------------------------------")
i = 1
con = 0
num = 1
#while i <= 100:
for num in range(100 + 1):
    #num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        con = con + 1
    #i = i + 1
print("En 100 numeros enteros hay", con,"numeros pares")