print("------------------------------------------------")
print("Ejercicio9: GASOLINERA")
print("------------------------------------------------")
import math
LITROXG = 3.785
PRECIOXL = 4.50
CONSU = float(input("Cantidad surtida: "))
LITROS = CONSU * LITROXG
print("En litros: " , LITROS)
TOTAL = CONSU * LITROXG * PRECIOXL
print("Lo que debera pagar seran: " , math.ceil(TOTAL))
