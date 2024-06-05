print("-----------------------------------------------")
print("Ejercicio1: INTERES")
print("-----------------------------------------------")
C = 0
I = 0
M = 0
while (C < 0) or (I <= 0) or (I >= 100) or (M <= 0):
    C = float(input("Ingrese el capital: "))
    I = float(input("Ingrese el interes: "))
    M = int(input("Ingrese los años: "))
for i in range(M):
    C = C * (1 + I / 100)
print("Tienes ", C , "pesos")