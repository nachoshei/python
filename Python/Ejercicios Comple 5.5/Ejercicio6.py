print("-----------------------------------------------------------")
print("Ejercicio 6: INVERTIDO")
print("-----------------------------------------------------------")
aux = 0
aux2 = 0
i = 10
Num = int(input("Ingrese un numero: "))
while i <= Num:
    aux = Num%10
    Num //= 10
    aux2 = aux2 * 10 + aux
aux2 = aux2 * 10 + Num
print("El numero invertido sera: ", aux2)