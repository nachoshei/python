import random  # Para generar edades aleatorias

def completar_boliche(personas, capacidad):
    # Completa la lista de personas con edades aleatorias entre 18 y 40
    for indice in range(capacidad):
        personas[indice] = random.randint(18, 40)

def contar_menores(personas, capacidad):
    # Cuenta cuántas personas son menores de 21 años
    menores = 0
    for indice in range(capacidad):
        if personas[indice] < 21:
            menores += 1
    return menores

def mostrar_personas(personas, capacidad):
    # Muestra la edad de cada persona
    for indice in range(capacidad):
        print(f"Persona {indice + 1}: Edad {personas[indice]}")

def disco():
    # Capacidad máxima del boliche
    capacidad = 270  
    personas = [0] * capacidad  # Lista para almacenar las edades de las personas

    # Llenar el boliche con edades aleatorias
    completar_boliche(personas, capacidad)

    # Contar cuántas personas son menores de 21 años
    menores21 = contar_menores(personas, capacidad)

    # Mostrar las edades de todas las personas en el boliche
    mostrar_personas(personas, capacidad)

    # Mostrar los resultados
    print("Los menores de 21 son:", menores21)
    print("Los mayores de 21 son:", capacidad - menores21)
    print("En total hay", capacidad, "personas")

# Ejecutar el programa
disco()