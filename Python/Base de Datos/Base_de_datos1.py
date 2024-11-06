import mysql.connector

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="puntodigital"
)

# Crear un cursor
cursor = conexion.cursor()

# Función para crear un estudiante
def crear_estudiante(estudiante):
    sql = "INSERT INTO estudiantes (nombre, apellido, Fecha_Nacimiento, DNI, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, estudiante)
    conexion.commit()
    return cursor.lastrowid

# Función para obtener un estudiante por ID
def obtener_estudiante(id_estudiante):
    sql = "SELECT * FROM estudiantes WHERE idestudiantes = %s"
    cursor.execute(sql, (id_estudiante,))
    return cursor.fetchone()

# Función para actualizar un estudiante
def actualizar_estudiante(id_estudiante, datos_estudiante):
    sql = "UPDATE estudiantes SET nombre = %s, apellido = %s, Fecha_Nacimiento = %s, DNI = %s, Telefono = %s, Direccion = %s WHERE idestudiantes = %s"
    cursor.execute(sql, (*datos_estudiante, id_estudiante))
    conexion.commit()

# Función para eliminar un estudiante
def eliminar_estudiante(id_estudiante):
    sql = "DELETE FROM estudiantes WHERE idestudiantes = %s"
    cursor.execute(sql, (id_estudiante,))
    conexion.commit()

# Ejemplos de uso
if _name_ == "_main_":
    # Crear un estudiante
    nuevo_estudiante = ("Nombre", "Apellido", "1990-01-01", "12345678", "1234567890", "Dirección")
    estudiante_id = crear_estudiante(nuevo_estudiante)
    print(f"Estudiante creado con ID: {estudiante_id}")

    # Obtener un estudiante por ID
    estudiante = obtener_estudiante(estudiante_id)
    print("Estudiante obtenido:")
    print(estudiante)

    # Actualizar el estudiante
    datos_actualizados = ("NuevoNombre", "NuevoApellido", "1995-02-02", "87654321", "9876543210", "NuevaDirección")
    actualizar_estudiante(estudiante_id, datos_actualizados)
    print("Estudiante actualizado:")

    # Eliminar el estudiante
    eliminar_estudiante(estudiante_id)
    print("Estudiante eliminado")

# Cerrar la conexión
conexion.close()