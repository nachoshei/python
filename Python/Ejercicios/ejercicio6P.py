print("Ingrese un numero: ")
num1 = float(input())
if num1 <= 0:
    print("Ha ocurrido un error")
else:
    if num1 > 0:
        num2 = (num1)**2
        print("El cuadrado del numero es: " , num2)
        num3 = (num1)**0.5
        print("Y la raiz del numero es: " , num3)
