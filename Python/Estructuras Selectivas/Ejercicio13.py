print("-----------------------------------------------------------------")
print("Ejercicio13: VERIFICAR SI EL AÑO ES BISIESTO")
print("-----------------------------------------------------------------")
Anio = int(input("Ingrese el año para determinar si es bisiesto: "))
if (Anio % 400 == 0) and (Anio % 4 == 0) or (Anio % 100 != 0):
    print("El año es BISIESTO")
else:
    print("El año no es BISIESTO")