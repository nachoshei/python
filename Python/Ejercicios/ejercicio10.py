print("------------------------------------------------")
print("Ejercicio10: CILINDRO")
print("------------------------------------------------")
import math
print("Ingrese el radio: ")
RADIO = float(input())
print("Ingrese la altura: ")
ALTURA = float(input())
VOL = math.pi * (RADIO)**2 * ALTURA
#AREA = 2 * math.pi * RADIO * (RADIO + ALTURA)
AREA = 2 * math.pi * RADIO * ALTURA + 2 * math.pi * (RADIO)**2
print("El volumen es: " , math.ceil(VOL))
print("El area es: " , math.ceil(AREA))