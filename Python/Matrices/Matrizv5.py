def mostrarTablas():
    tabla1 = int(input("Hasta que tabla desea multiplicar: "))

    for i in range(1, tabla1 + 1):
        print(f"Tabla del {i}:", end=" ")
        for j in range(1, tabla1 + 1):
            print(f"{i * j}", end=" ") #Otra fomra: [print(f"{i} x {j} = {i * j}")]
        print()

mostrarTablas() 