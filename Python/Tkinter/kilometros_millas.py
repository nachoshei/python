import tkinter as tk

def convertir_distancia():
    try:
        kilometros = float(entry_kilometros.get())
        millas = kilometros / 1.60934
        label_resultado_millas.config(text=f"La longitud en millas es: {millas:.2f} millas")
    except ValueError:
        label_resultado_millas.config(text="Por favor. ingrese una longitud valida en kilometros.")



ventana = tk.Tk()
ventana.title("Conversor de Longitud")
ventana.geometry("300x150")

label_instrucciones = tk.Label(ventana, text="Ingrese la longitud en kilometros")
label_instrucciones.pack()

entry_kilometros = tk.Entry(ventana)
entry_kilometros.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia)
boton_convertir.pack()

label_resultado_millas = tk.Label(ventana, text="")
label_resultado_millas.pack()

ventana.mainloop() 