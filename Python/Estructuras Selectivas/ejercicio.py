def obtener_nombre_mes(numero_mes):
    meses = {
        1:"enero",
        2:"febrero",
        3:"marzo",
        4:"abril",
        5:"mayo",
        6:"junio",
        7:"julio",
        8:"agosto",
        9:"septiembre",
        10:"octubre",
        11:"noviembre",
        12:"diciembre"
    }
    return meses.get(numero_mes, "Mes no valido")

def main():
    #try:
        numero_mes = int(input("Ingrese numero de mes (1-12): "))
        if numero_mes < 13:
            nombre_mes = obtener_nombre_mes(numero_mes)
            print(f"El numero {numero_mes} corresponde al mes de {nombre_mes}.")
    #except ValueError:
        else:
            print("Error: Por favor, ingrese un numero valido")

if __name__ == "__main__":
    main()