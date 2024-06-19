print("-----------------------------------------------------------")
print("Ejercicio 9: MayorMenor")
print("-----------------------------------------------------------")
limite = int(input("Ingrese la cantidad de numeros a comparar: "))
Num = int(input("Ingrese un numero: "))
may = Num
men = Num
for i in range(1, limite):
    Num = int(input("Ingrese un numero: "))
    if Num < men:
        men = Num
    else:
        if Num > may:
            may = Num
print("El mayor es:", may)
print("El menor es: ", men)