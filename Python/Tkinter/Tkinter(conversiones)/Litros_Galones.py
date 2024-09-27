import tkinter as tk

def convertir_liquido():
    litros = float(entry_galones.get())
    galones = litros / 3.785
    label_resultado_galones.config(text=f"La cantidad es de {galones:.2f} galones")

ventana = tk.Tk()
ventana.title("Conversor de Litros a Galones")
ventana.geometry("300x150")

label_instrucciones = tk.Label(ventana, text="Ingrese la cantidad de litros")
label_instrucciones.pack()

entry_galones = tk.Entry(ventana)
entry_galones.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_liquido)
boton_convertir.pack()

label_resultado_galones = tk.Label(ventana, text="")
label_resultado_galones.pack()

ventana.mainloop()