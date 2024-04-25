print("------------------------------------------------")
print("Ejercicio7: CALCULAR EL TERCER LADO DEL TRIANGULO")
print("------------------------------------------------")
import math
b = float(input("Ingrese lado B del triangulo: "))
c = float(input("Ingrese lado C del triangulo: "))
alfa = float(input("Ingrese el angulo en grados sexagesimales: "))
a = (b**2+c**2-2*b*c*math.cos(alfa*math.pi/180))**0.5
print("El lado A es: " , a)
