print("-----------------------------------------------------------")
print("Ejercicio 1: NUMEROS PARES")
print("-----------------------------------------------------------")
c = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 1
#num = int(input("Ingrese 10 numeros: "))
print("Ingrese 10 numeros: ")
for n in range(1, 10):
    num = int(input("Ingrese numero: "))
#for n in nums:
    #print(n)
    if n % 2 == 0:
        c = c + 1
print("Hay " ,c, "numeros pares :")