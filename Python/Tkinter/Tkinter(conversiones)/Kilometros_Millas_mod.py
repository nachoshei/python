import tkinter as tk

def convertir_distancia():
    try:
        kilometros = float(entry_kilometros.get())
        millas = kilometros / 1.609
        label_resultado_millas.config(text=f"La longitud en millas es: {millas:.2f} millas")
    except ValueError:
        label_resultado_millas.config(text="Por favor. ingrese una longitud valida en millas.")

def convertir_distancia2():
    try:
        millas = float(entry_millas.get())
        kilometros = millas * 1.609
        label_resultado_kilometros.config(text=f"La longitud en kilometros es: {kilometros:.2f} km")
    except ValueError:
        label_resultado_kilometros.config(text="Por favor, ingrese una longitud valida en kilometros.")



ventana = tk.Tk()
ventana.title("Conversor de Longitud")
ventana.geometry("300x200")

label_instrucciones = tk.Label(ventana, text="Ingrese la longitud en kilometros")
label_instrucciones.pack()


entry_kilometros = tk.Entry(ventana)
entry_kilometros.pack()


boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia)
boton_convertir.pack()

label_resultado_millas = tk.Label(ventana, text="")
label_resultado_millas.pack()

label_instrucciones = tk.Label(ventana, text="Ingrese la longitud en millas")
label_instrucciones.pack()

entry_millas = tk.Entry(ventana)
entry_millas.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia2)
boton_convertir.pack()

label_resultado_kilometros = tk.Label(ventana, text="")
label_resultado_kilometros.pack()

ventana.mainloop() 