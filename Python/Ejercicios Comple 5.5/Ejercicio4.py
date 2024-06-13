print("-----------------------------------------------------------")
print("Ejercicio 4: SERIE")
print("-----------------------------------------------------------")
num = int(input("Ingrese el numero de terminos: "))
s = 5
ser = 0
a = 1
for a in range(num):
    s = s + 5
    ser = ser + s
print("La suma de la serie es: ", ser)