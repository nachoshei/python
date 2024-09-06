import random

def cargar_habitantes(nro_pisos, nro_deptos, edificio):
    # Llenar el edificio con habitantes generados aleatoriamente
    for indice_piso in range(nro_pisos):
        for indice_depto in range(nro_deptos):
            edificio[indice_piso][indice_depto] = random.randint(0, 10)

def calcular_habitantes_por_piso(nro_pisos, nro_deptos, edificio, habitantes_por_piso):
    # Calcular el total de habitantes por piso
    for indice_piso in range(nro_pisos):
        habitantes_piso = 0
        for indice_depto in range(nro_deptos):
            habitantes_piso += edificio[indice_piso][indice_depto]
        habitantes_por_piso[indice_piso] = habitantes_piso

def habitantes_edificio():
    # Definición de número de pisos y departamentos por piso
    nro_pisos = 10
    nro_deptos = 2

    # Inicializar el edificio y los habitantes por piso
    edificio = [[0 for _ in range(nro_deptos)] for _ in range(nro_pisos)]
    habitantes_por_piso = [0 for _ in range(nro_pisos)]

    # Cargar habitantes aleatoriamente en el edificio
    cargar_habitantes(nro_pisos, nro_deptos, edificio)

    # Calcular el número de habitantes por piso
    calcular_habitantes_por_piso(nro_pisos, nro_deptos, edificio, habitantes_por_piso)

    # Calcular el total de habitantes en el edificio
    total_habitantes = 0
    print("Habitantes por piso:")
    for indice in range(nro_pisos):
        total_habitantes += habitantes_por_piso[indice]
        print(f"Piso {indice + 1}: {habitantes_por_piso[indice]}")

    # Mostrar el total de habitantes
    print(f"La cantidad total de habitantes es: {total_habitantes}")

# Ejecutar la función principal
habitantes_edificio()