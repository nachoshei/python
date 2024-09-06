import random
def completar_boliche(personas, capacidad):
    for i in range(capacidad):
        personas[i] = random.randint(18, 40)

def contar_menores(personas, capacidad):
    menores = 0
    for i in range(capacidad):
        if personas[i] < 21:
            menores += 1
    return menores

def mostrar_personas(personas, capacidad):
    for i in range(capacidad):
        print(f"Persona {i + 1}: Edad {personas[i]}")

def disco():
    capacidad = 270
    personas = [0] * capacidad

    completar_boliche(personas, capacidad)

    menores21 = contar_menores(personas, capacidad)

    mostrar_personas(personas, capacidad)


    print("Los menores de 21 son:", menores21)
    print("Los mayores de 21 son:", capacidad - menores21)
    print("En total hay", capacidad, "personas")

disco()