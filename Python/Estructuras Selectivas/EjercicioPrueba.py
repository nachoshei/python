switcher = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}
argument = int(input("Ingrese el numero del mes: "))
nombreDeMes = switcher.get(argument, "Mes invalido")
print(nombreDeMes)