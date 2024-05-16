num1 = int(input("Ingrese el tipo de calculo a realizar: "))
V = int(input("Ingrese V: "))
calculo = {
    1: 100 * V,
    2: 100 ** V,
    3: 100 / V
}
Resultado = calculo.get(num1)#"Numero invalido"
print("El resultado es: " , Resultado)