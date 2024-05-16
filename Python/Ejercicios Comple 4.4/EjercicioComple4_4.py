print("----------------------------------------------------------------------")
print("Ejercicio4: FECHA")
print("----------------------------------------------------------------------")
print("Ingrese la fecha: ")
anio = int(input("El año: "))
mes = int(input("El mes en numero: "))
dia = int(input("El dia: "))
if dia > 0 and dia < 30:
    print("Mañana es: " , dia + 1, 1, 1)
else:
    if mes > 0 and mes < 12:
        print("Mañana sera: " ,1 , mes + 1, 1)
    else:
        print("Mañana sera: " , 1, 1, anio + 1)