print("-----------------------------------------")
print("Ejercicio3 PUNTAJE FINAL")
print("-----------------------------------------")
print("Ingrese el numero de respuestas correctas: ")
RC = int(input())
print("Ingrese el numero de respuestas incorrectas: ")
RI = int(input())
print("Ingrese el numero de respuestas en blanco: ")
RB = int(input())
PRC = RC * 3
PRI = RI * -1
PRB = RB * 0
PF = PRC + PRI + PRB
print("El puntaje final es: " , PF)