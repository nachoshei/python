print("-----------------------------------------------------------")
print("Ejercicio 7: N PRIMOS")
print("-----------------------------------------------------------")
con = 0
Num = int(input("Ingrese un numero: "))
for i in range(2, Num):
    if Num % i == 0:
        con = con + 1
if con == 0:
    print(Num, "es un numero primo")
else:
    print(Num, "no es un numero primo")