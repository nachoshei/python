print("-----------------------------------------------------------")
print("Ejercicio 12: SUELDO")
print("-----------------------------------------------------------")
can = int(input("Ingrese la cantidad de empleados: "))
i = 1
sueMayor = 0
while i <= can:
    sueldo = int(input("Ingrese sueldo: "))
    if sueldo > sueMayor:
        sueMayor = sueldo
        c = i
    i = i + 1
print("El empleado numero", c,"tiene el mayor sueldo que es: ",sueMayor)