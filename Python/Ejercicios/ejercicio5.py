print("--------------------------------------------------")
print("Ejercicio5: NUMERO DE MICRO DISCOS 3.5 NECESARIOS")
print("--------------------------------------------------")
import math
print("Ingrese los GB: ")
GB = float(input())
MG = GB * 1024
MD = MG / 1.44
print(MD)
print("Numero de discos necesarios: " , math.ceil(MD))