def agregar_paciente(pacientes, nombre, diagnostico, costo):
    """
    Agrega un nuevo paciente a la lista de pacientes.
    
    :param pacientes: Lista de pacientes.
    :param nombre: Nombre del paciente.
    :param diagnostico: Diagnóstico del paciente.
    :param costo: Costo del tratamiento del paciente.
    """
    pacientes.append([nombre, diagnostico, costo])

def calcular_costo_total(pacientes):
    """
    Calcula el costo total de tratamiento para todos los pacientes.
    
    :param pacientes: Lista de pacientes.
    :return: Costo total.
    """
    return sum(paciente[2] for paciente in pacientes)

def listar_pacientes_costosos(pacientes, umbral):
    """
    Lista los pacientes con un costo de tratamiento mayor a un valor dado.
    
    :param pacientes: Lista de pacientes.
    :param umbral: Umbral de costo.
    """
    print(f"Pacientes con un costo de tratamiento mayor a {umbral}:")
    for paciente in pacientes:
        if paciente[2] > umbral:
            print(f"Nombre: {paciente[0]}, Diagnóstico: {paciente[1]}, Costo: {paciente[2]}")

# Lista inicial de pacientes
pacientes = [
    ["Juan Perez", "Gripe", 200],
    ["Maria Garcia", "Fractura", 1500],
    ["Ana Lopez", "Diabetes", 3000]
]

# Ejemplo de uso
agregar_paciente(pacientes, "Carlos Diaz", "Alergia", 500)
costo_total = calcular_costo_total(pacientes)
print(f"Costo total de tratamiento: {costo_total}")
listar_pacientes_costosos(pacientes, 1000)