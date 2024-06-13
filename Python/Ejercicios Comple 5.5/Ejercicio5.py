print("-----------------------------------------------------------")
print("Ejercicio 5: SERIE PT2")
print("-----------------------------------------------------------")
S = 0
Num = int(input("Ingrese numero de terminos: "))
for x in range(1, Num + 1):
    if x % 2 == 0:
        S = S - (1/x)
    else:
        S = S + (1/x)
print("La suma sera: ", S)