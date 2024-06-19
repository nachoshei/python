print("-----------------------------------------------------------")
print("Ejercicio 8: CEROS")
print("-----------------------------------------------------------")
con = 0
Num = 0
while not Num == -1:
    Num = int(input("Ingrese un numero: "))
    if Num == 0:
        con = con + 1
print("Hay", con, "ceros")  