print("-------------------------------------------------")
print("Ejercicio 5: DETERMINAR EL VALOR DE X")
print("-------------------------------------------------")
x = int(input("Introduce el valor de X: "))
e = 1
num = 1
den = 1
i = 1

num = x ** num
den = den * i
i = i + 1
e = e + num / den
while not (num/den < 0.000001):
    num = x ** i
    den = den * i
    i = i + 1
    e = e + num / den
print("e elevado a:",x, "es ", e)