print("------------------------------------------------")
print("Ejercicio10: DISTANCIA")
print("------------------------------------------------")
x1 = float(input("Ingrese el valor del punto x1: "))
y1 = float(input("Ingrese el valor del punto y1: "))
z1 = float(input("Ingrese el valor del punto z1: "))
print("------------------------------------------------")
x2 = float(input("Ingrese el valor del punto x2: "))
y2 = float(input("Ingrese el valor del punto y2: "))
z2 = float(input("Ingrese el valor del punto z2: "))
dis =  ((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5
print("La distancia es: " , dis)