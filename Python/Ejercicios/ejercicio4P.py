print("Ingrese el primero numero: ")
num1 = int(input())
print("Ingrese el segundo numero: ")
num2 = int(input())
print("Ingrese el tercer numero: ")
num3 = int(input())
if num1 >= num2 and num1 >= num3:
    print("El primer numero es mayor")
else:
    if num2 >= num1 and num2 >= num3:
        print("El segundo numero es mayor")
    else:
        if num3 >= num1 and num3 >= num2:
            print("El tercer numero es mayor")
            