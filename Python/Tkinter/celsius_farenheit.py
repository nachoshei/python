import tkinter as tk

def convertir_temp():
    celsius =float(entry_celsius.get())
    fahrenheit = celsius * 9/5 + 32
    label_resultado.config(text=f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("300x100")

label_instrucciones = tk.Label(ventana, text="Ingrese la temperatura en grados Celsius")
label_instrucciones.pack()

entry_celsius = tk.Entry(ventana)
entry_celsius.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_temp)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()