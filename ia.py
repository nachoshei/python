def cargar_vector(v, cantidad):
    for indice in range(cantidad):
        v[indice] = int(input(f"Ingrese el valor de la posición {indice}: "))

def multiplicar_vector(v1, v2, cantidad):
    acum = 0
    for indice in range(cantidad):
        acum += v1[indice] * v2[indice]
    return acum

def producto_escalar():
    cantidad = int(input("Cantidad: "))
    v1 = [0] * cantidad
    v2 = [0] * cantidad

    print("Cargando v1")
    cargar_vector(v1, cantidad)

    print("Cargando v2")
    cargar_vector(v2, cantidad)

    print("Multiplicación escalar =", multiplicar_vector(v1, v2, cantidad))

# Ejecutar la función principal
producto_escalar()