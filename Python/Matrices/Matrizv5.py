def mostrarTablas():
    tabla1 = int(input("Hasta que tabla desea multiplicar: "))

    for i in range(1, tabla1 + 1):
        #print(f"Tabla del {i}: ")
        for j in range(tabla1 + 1):
            print(f"Tabla del {i}: {i * j}", end=" ") #Otra fomra: [print(f"{i} x {j} = {i * j}")]
        print()

mostrarTablas() 