print("----------------------------------------------------------------------")
print("Ejercicio5: RAICES")
print("----------------------------------------------------------------------")
print("Valores de la ecuacion cuadratica: ")
a = float(input("Ingrese A: "))
b = float(input("Ingrese B: "))
c = float(input("Ingrese C: "))
d = b**2-4*a*c
if d > 0:
    x1 = ((-b)+d**0.5)/2*a
    x2 = ((-b)-d**0.5)/2*a
    print("Raices Reales: " , x1, x2)
else:
    print("Raices Irracionales")