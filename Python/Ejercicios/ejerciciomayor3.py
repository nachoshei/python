num1 = int(input("Ingrese el primero numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if num1>num2 and num1>num3:
    print("El primer numero es mayor")
else:
    if num2>num1 and num2>num3:
        print("El segundo numero es mayor")
    else:
        if num3>num1 and num3>num2:
            print("El tercer numero es mayor")
