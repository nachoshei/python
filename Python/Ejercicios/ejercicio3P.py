print("Ingrese al primer numero: ")
numero1=int(input())
print("Ingrese al segundo numero: ")
numero2=int(input())
if numero1 > numero2 and numero2 < numero1:
    print("El primer numero es mayor") 
else: 
    if numero1 == numero2 and numero2 == numero1:
        print("Son iguales")
if numero2 > numero1 and numero1 < numero2:
    print ("El segundo numero es mayor")

