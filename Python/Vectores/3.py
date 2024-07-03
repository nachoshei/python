cantidad = int(input("ingrese cuantos elementos va a ingresar: "))
vector = []

while 1 >= cantidad <=200:
    print ("numero fuera de rango")
    cantidad = int(input("ingrese cuantos elementos va a ingresar: "))

i = 1
while i <= cantidad:
    numero = int(input("ingrese el numero al vector: "))
    vector.append(numero)
    i += 1

vector.sort()
aux = 1

for j in vector:
    comparador = vector [aux]
    if j == comparador:
        vector.remove(j)

    if comparador == len(vector)-1:
        break
    else:
        aux +=1

print (vector)