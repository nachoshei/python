#ejemplo de conexión a base de datos Test Y Grabado de datos
import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="test"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejemplo: Insertar un estudiante n la tabla de estudiantes
idestudiantes =  1
nombre = "Juan Perez"
edad = 20
curso = "Matemáticas"

# Consulta SQL para la inserción
consulta = "INSERT INTO estudiantes (idestudiantes, nombre, edad, curso) VALUES (%s, %s, %s, %s)"
datos = (idestudiantes, nombre, edad, curso)

# Ejecutar la consulta
cursor.execute(consulta, datos)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

#aca un ejemplo de las distintas consultas a realizar sobre una tabla, el CRUD en ingles del ABM