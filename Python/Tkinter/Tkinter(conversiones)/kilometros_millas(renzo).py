import tkinter as tk

def convertirMilla():
    milla = float (entry_dato.get())
    kilometro = milla * 1.60934
    label_resultado.config(text=f"las millas expresadas en kilometros son: {kilometro: .2f} Km")

def convertirKilometro():
    kilometro = float (entry_dato.get())
    milla = kilometro * 0.621371
    label_resultado.config(text=f"los kilometros expresados en millas son: {milla: .2f} Millas")

#Ventana
ventana=tk.Tk()
ventana.title("conversor milla a kilometro")
ventana.geometry("300x200")

#elementos de la ventana
label_instrucciones = tk.Label(ventana, text="Ingrese las millas o kilometros: ")
label_instrucciones.pack()

entry_dato = tk.Entry(ventana)
entry_dato.pack()

boton_millaKilometro = tk.Button(ventana, text="Milla a Km.", command=convertirMilla)
boton_millaKilometro.pack()

boton_kilometroMilla = tk.Button(ventana, text="Km a Milla.", command=convertirKilometro)
boton_kilometroMilla.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

#inicializa bucle
ventana.mainloop()