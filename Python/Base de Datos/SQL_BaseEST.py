import mysql.connector
import tkinter as tk
from tkinter import messagebox

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
def crear_estudiante():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nacimiento = fecha_entry.get()
    dni = dni_entry.get()
    telefono = telefono_entry.get()
    direccion = direccion_entry.get()
    
    sql = "INSERT INTO estudiantes (nombre, apellido, Fecha_Nacimiento, DNI, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, fecha_nacimiento, dni, telefono, direccion))
    conexion.commit()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Estudiante creado con éxito.")

# Función para obtener un estudiante por ID
def obtener_estudiante():
    id_estudiante = id_entry.get()
    sql = "SELECT * FROM estudiantes WHERE idestudiantes = %s"
    cursor.execute(sql, (id_estudiante,))
    estudiante = cursor.fetchone()
    if estudiante:
        limpiar_campos()
        nombre_entry.insert(0, estudiante[1])
        apellido_entry.insert(0, estudiante[2])
        fecha_entry.insert(0, estudiante[3])
        dni_entry.insert(0, estudiante[4])
        telefono_entry.insert(0, estudiante[5])
        direccion_entry.insert(0, estudiante[6])
    else:
        messagebox.showerror("Error", "Estudiante no encontrado.")

# Función para actualizar un estudiante
def actualizar_estudiante():
    id_estudiante = id_entry.get()
    datos_actualizados = (
        nombre_entry.get(),
        apellido_entry.get(),
        fecha_entry.get(),
        dni_entry.get(),
        telefono_entry.get(),
        direccion_entry.get()
    )
    sql = "UPDATE estudiantes SET nombre = %s, apellido = %s, Fecha_Nacimiento = %s, DNI = %s, Telefono = %s, Direccion = %s WHERE idestudiantes = %s"
    cursor.execute(sql, (*datos_actualizados, id_estudiante))
    conexion.commit()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Estudiante actualizado con éxito.")

# Función para eliminar un estudiante
def eliminar_estudiante():
    id_estudiante = id_entry.get()
    sql = "DELETE FROM estudiantes WHERE idestudiantes = %s"
    cursor.execute(sql, (id_estudiante,))
    conexion.commit()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Estudiante eliminado con éxito.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    fecha_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)

# Configuración de la ventana tkinter
root = tk.Tk()
root.title("Gestión de Estudiantes")

# Crear etiquetas y campos de entrada
id_label = tk.Label(root, text="ID del Estudiante:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack()

apellido_label = tk.Label(root, text="Apellido:")
apellido_label.pack()
apellido_entry = tk.Entry(root)
apellido_entry.pack()

fecha_label = tk.Label(root, text="Fecha de Nacimiento:")
fecha_label.pack()
fecha_entry = tk.Entry(root)
fecha_entry.pack()

dni_label = tk.Label(root, text="DNI:")
dni_label.pack()
dni_entry = tk.Entry(root)
dni_entry.pack()

telefono_label = tk.Label(root, text="Teléfono:")
telefono_label.pack()
telefono_entry = tk.Entry(root)
telefono_entry.pack()

direccion_label = tk.Label(root, text="Dirección:")
direccion_label.pack()
direccion_entry = tk.Entry(root)
direccion_entry.pack()

# Botones para realizar las operaciones CRUD
crear_button = tk.Button(root, text="Crear Estudiante", command=crear_estudiante)
crear_button.pack()

obtener_button = tk.Button(root, text="Obtener Estudiante", command=obtener_estudiante)
obtener_button.pack()

actualizar_button = tk.Button(root, text="Actualizar Estudiante", command=actualizar_estudiante)
actualizar_button.pack()

eliminar_button = tk.Button(root, text="Eliminar Estudiante", command=eliminar_estudiante)
eliminar_button.pack()

# Iniciar la ventana tkinter
root.mainloop()

# Cerrar la conexión
conexion.close()