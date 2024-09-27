import tkinter as tk
from tkinter import messagebox

def verificar_respuesta(respuesta, solucion):
    if respuesta == solucion:
        messagebox.showInfo("Resultado", "¡Correcto! ¡Felicitaciones!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era '{solucion}'.")
    
#Ejercicio 1: Adivinanza simple
def ejercicio_1():
    ventana = tk.Toplevel()
    ventana.title("Adivinanza")

    adivinanza = "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera."
    solucion = "pera"

    label = tk.Label(ventana, text=adivinanza)
    label.pack()

    respuesta = tk.Entry(ventana)
    respuesta.pack()

    boton = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(respuesta.get().lower(), solucion))
    boton.pack()

#Ejercicio 2: Adivinanza con multiples opciones
def ejercicio_2():
    ventana = tk.Toplevel()
    ventana.title("Adivinanza")

    adivinanza = "Tiene ojos y no puede ver, tiene agua y no puede beber."
    solucion = "a"

    label = tk.Label(ventana, text=adivinanza)
    label.pack()

    opciones = [
        ("a) Un pez", "a"),
        ("b) Un rio", "b"),
        ("c) Un pespejo", "c")
        ]
    
    respuesta = tk.StringVar()

    for opcion, valor in opciones:
        radio = tk.Radiobutton(ventana, text=opcion, variable=respuesta, value=valor)
        radio.pack(anchor="w")

    boton = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(respuesta.get(), solucion))
    boton.pack()

#Ejercicio 3: Adivinanza con pistas
def ejercicio_3():
    ventana = tk.Toplevel()
    ventana.title("Adivinanza")

    adivinanza = "En el dia no puedes verme, en la noche puedes encontrarme. ¿Que soy?"
    solucion = "sol"
    pistas = [

    ]