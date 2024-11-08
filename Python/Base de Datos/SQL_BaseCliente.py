import mysql.connector
from tkinter import *
from tkinter import messagebox

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_reparacion"
)
cursor = conn.cursor()

# Función para crear un cliente
def crear_cliente(nombre, contacto):
    cursor.execute("INSERT INTO clientes (nombre, contacto) VALUES (%s, %s)", (nombre, contacto))
    conn.commit()
    messagebox.showinfo("Éxito", "Cliente creado exitosamente.")
    mostrar_clientes()

# Función para actualizar un cliente
def actualizar_cliente(id_cliente, nombre, contacto):
    cursor.execute("UPDATE clientes SET nombre=%s, contacto=%s WHERE id_cliente=%s", (nombre, contacto, id_cliente))
    conn.commit()
    messagebox.showinfo("Éxito", "Cliente actualizado exitosamente.")

# Función para eliminar un cliente
def eliminar_cliente(id_cliente):
    cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
    conn.commit()
    messagebox.showinfo("Éxito", "Cliente eliminado exitosamente.")

# Función para mostrar clientes en una lista
def mostrar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        lista_clientes.insert(END, cliente)

def mostrar_celulares():
    cursor.execute("SELECT * FROM celulares")
    celulares = cursor.fetchall()
    for celulares in celulares:
        lista_celulares.insert(END, celulares)

# Interfaz de Tkinter para gestionar clientes
root = Tk()
root.title("Gestión de Reparación de Celulares")
root.geometry("600x500")

# Frame para el CRUD de clientes
frame_clientes = Frame(root)
frame_clientes.pack()

# Entrada de datos para clientes
Label(frame_clientes, text="Nombre").grid(row=0, column=0)
entry_nombre = Entry(frame_clientes)
entry_nombre.grid(row=0, column=1)

Label(frame_clientes, text="Contacto").grid(row=1, column=0)
entry_contacto = Entry(frame_clientes)
entry_contacto.grid(row=1, column=1)

# Botones de control para clientes
def crear_cliente_callback():
    nombre = entry_nombre.get()
    contacto = entry_contacto.get()
    crear_cliente(nombre, contacto)

Button(frame_clientes, text="Crear Cliente", command=crear_cliente_callback).grid(row=2, column=0, pady=10)
Button(frame_clientes, text="Actualizar Cliente", command=lambda: actualizar_cliente(1, entry_nombre.get(), entry_contacto.get())).grid(row=2, column=1)
Button(frame_clientes, text="Eliminar Cliente", command=lambda: eliminar_cliente(1)).grid(row=2, column=2)

# Lista para mostrar clientes
Label(frame_clientes, text="Clientes").grid(row=3, column=0, columnspan=3)
lista_clientes = Listbox(frame_clientes, width=50)
lista_clientes.grid(row=4, column=0, columnspan=3)
mostrar_clientes()

# Frame para el CRUD de celulares
frame_celulares = Frame(root)
frame_celulares.pack()

Label(frame_celulares, text="Celulares").grid(row=3, column=0, columnspan=3)
lista_clientes = Listbox(frame_clientes, width=50)
lista_clientes.grid(row=4, column=0, columnspan=3)
mostrar_celulares()

Label(frame_celulares, text="Marca").grid(row=0, column=0)
entry_marca = Entry(frame_celulares)
entry_marca.grid(row=0, column=1)

Label(frame_celulares, text="Modelo").grid(row=1, column=0)
entry_modelo = Entry(frame_celulares)
entry_modelo.grid(row=1, column=1)

Button(frame_celulares, text="Crear Celular", command=lambda: registrar_celular(1, entry_marca.get(), entry_modelo.get())).grid(row=2, column=0, pady=10)

# Frame para el CRUD de repuestos
frame_repuestos = Frame(root)
frame_repuestos.pack()

Label(frame_repuestos, text="Descripción del Repuesto").grid(row=0, column=0)
entry_descripcion_repuesto = Entry(frame_repuestos)
entry_descripcion_repuesto.grid(row=0, column=1)

Label(frame_repuestos, text="Costo del Repuesto").grid(row=1, column=0)
entry_costo_repuesto = Entry(frame_repuestos)
entry_costo_repuesto.grid(row=1, column=1)

Button(frame_repuestos, text="Agregar Repuesto", command=lambda: agregar_repuesto(1, entry_descripcion_repuesto.get(), float(entry_costo_repuesto.get()))).grid(row=2, column=0, pady=10)

# Funciones adicionales para manejar reparaciones
def registrar_celular(id_cliente, marca, modelo):
    cursor.execute("INSERT INTO celulares (id_cliente, marca, modelo) VALUES (%s, %s, %s)", (id_cliente, marca, modelo))
    conn.commit()
    messagebox.showinfo("Éxito", "Celular registrado con éxito.")

def agregar_repuesto(id_celular, descripcion, costo):
    cursor.execute("INSERT INTO repuestos (id_celular, descripcion, costo) VALUES (%s, %s, %s)", (id_celular, descripcion, costo))
    conn.commit()
    messagebox.showinfo("Éxito", "Repuesto agregado exitosamente.")

# Finalización de la aplicación
root.mainloop()

# Cierre de conexión
conn.close()