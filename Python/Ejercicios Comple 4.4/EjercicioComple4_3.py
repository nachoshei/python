print("----------------------------------------------------------------------")
print("Ejercicio3: COSTO DE ARTICULO")
print("----------------------------------------------------------------------")
producto = float(input("Indique el precio de su compra: "))
ConIGV = producto * 0.20
IGV = producto + ConIGV
print("Su precio con IGV agregado es: " , IGV)
if  IGV >= 2000:
    descuento = IGV * 0.10
    descuentoFinal = IGV - descuento
    print("Usted obtiene un descuento del 10%.")
    print("Precio Final: " , descuentoFinal)
Marca = input("Ingrese la marca: ")

if Marca == "Nosy":
    descuentoN = descuentoFinal * 0.05
    descuentoNosy = descuentoFinal - descuentoN
    print("Usted obtiene un descuento adicional del 5%.")
    print("Su precio final seria: " , descuentoNosy)