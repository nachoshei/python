print("-----------------------------------------------------------")
print("Ejercicio 3: CUBOS PRIMOS")
print("-----------------------------------------------------------")
b = 2
for i in range(1, 29):
    co = 0
    for a in range(2, b):
        if b % a == 0:
            co = co + 1
            a = b
    if co == 0:
        print("El cubo de ", b, "es: ", b**3)
    b = b + 1