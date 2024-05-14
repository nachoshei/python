print("-----------------------------------------------------------------")
print("Ejercicio14: FUNCION")
print("-----------------------------------------------------------------")
print("Ingrese valores: ")
NUM = int(input("Tipo de calculo: "))
V = int(input("Ingrese V: "))
funcion = {
    1: 100*V,
    2: 100**V,
    3: 100/V
}
VAL = funcion.get(NUM, 0)
print(VAL)