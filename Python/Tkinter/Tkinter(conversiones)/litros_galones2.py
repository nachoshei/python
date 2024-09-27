import tkinter as tk

def convertir_litros():
    litros = float(entry_dato.get())
    galones = litros / 3.785
    label_resultado.config(text=f"La cantidad es de {galones:.2f} galones")

def convertir_galones():
    galones = float(entry_dato.get())
    litros = galones * 3.785
    label_resultado.config(text=f"La cantidad es de {litros:.2f} litros")


ventana = tk.Tk()
ventana.title("Conversor de volumen")
ventana.geometry("300x150")

label_instrucciones = tk.Label(ventana, text="Ingrese la cantidad de volumen")
label_instrucciones.pack()

entry_dato = tk.Entry(ventana)
entry_dato.pack()

boton_convertir = tk.Button(ventana, text="Litros a Galones", command=convertir_litros)
boton_convertir.pack()

boton_convertir = tk.Button(ventana, text="Galones a Litros", command=convertir_galones)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()