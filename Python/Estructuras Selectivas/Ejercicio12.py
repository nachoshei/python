print("-----------------------------------------------------------------")
print("Ejercicio12: SUELDO A PERCIBIR")
print("-----------------------------------------------------------------")
Sueldo = float(input("Ingrese su sueldo: "))
if Sueldo <= 1000:
    Aumento = Sueldo * 0.15
    Sue = Sueldo + Aumento
print("Usted tiene un aumento del 15%: " , Sue)
