import tkinter as tk

def convertir_distancia():
    try:
        millas = float(entry_millas.get())
        kilometros = millas * 1.609
        label_resultado_kilometros.config(text=f"La longitud en kilometros es: {kilometros:.2f} km")
    except ValueError:
        label_resultado_kilometros.config(text="Por favor, ingrese una longitud valida en kilometros.")



ventana = tk.Tk()
ventana.title("Conversor de Longitud")
ventana.geometry("300x150")

label_instrucciones = tk.Label(ventana, text="Ingrese la longitud en millas")
label_instrucciones.pack()

entry_millas = tk.Entry(ventana)
entry_millas.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia)
boton_convertir.pack()

label_resultado_kilometros = tk.Label(ventana, text="")
label_resultado_kilometros.pack()

ventana.mainloop()