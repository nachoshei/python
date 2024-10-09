import tkinter as tk

def calcular_tiempo_impacto():
    try:
        # Obtener las velocidades y distancia del usuario
        velocidad_auto1 = float(entry_velocidad_auto1.get())
        velocidad_auto2 = float(entry_velocidad_auto2.get())
        distancia = float(entry_distancia.get())

        # Calcular el tiempo de impacto
        tiempo_impacto = (distancia / (velocidad_auto1 + velocidad_auto2))*3600

        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=f"El tiempo de impacto es: {tiempo_impacto:.2f} segundos")
    except ValueError:
        label_resultado.config(text="Por favor, ingrese valores válidos.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Tiempo de Impacto")

# Crear y ubicar los elementos en la ventana
label_instrucciones_auto1 = tk.Label(ventana, text="Velocidad del Auto 1 (km/h):")
label_instrucciones_auto1.pack()

entry_velocidad_auto1 = tk.Entry(ventana)
entry_velocidad_auto1.pack()

label_instrucciones_auto2 = tk.Label(ventana, text="Velocidad del Auto 2 (km/h):")
label_instrucciones_auto2.pack()

entry_velocidad_auto2 = tk.Entry(ventana)
entry_velocidad_auto2.pack()

label_instrucciones_distancia = tk.Label(ventana, text="Distancia entre los vehículos (km):")
label_instrucciones_distancia.pack()

entry_distancia = tk.Entry(ventana)
entry_distancia.pack()

boton_calcular = tk.Button(ventana, text="Calcular Tiempo de Impacto", command=calcular_tiempo_impacto)
boton_calcular.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciar el bucle principal
ventana.mainloop()