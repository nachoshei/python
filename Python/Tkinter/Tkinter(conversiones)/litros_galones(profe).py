import tkinter as tk

def convertir_volumen():
    try:
        #convertir litros a galones
        litros = float(entry_litros.get())
        galones = litros * 0.264172
        label_resultado_galones.config(text=f"Litros a galones: {galones:.2f} gal")

        #convertir mililitros a onzas
        mililitros = float(entry_mililitros.get())
        onzas = mililitros * 0.033814
        label_resultado_onzas.config(text=f"Mililitros a onzas: {onzas:.2f} fl oz")
    except ValueError:
        label_resultado_galones.config(text="Por favor, ingrese un valor valido de litros")
        label_resultado_onzas.config(text="Por favor, ingrese un valor valido de onzas")

#crear ventana
ventana = tk.Tk()
ventana.title("Conversor de Volumen")
ventana.geometry("300x200")

#crear y ubicar elementos de la ventana
label_instrucciones_litros = tk.Label(ventana, text="Ingrese el volumen de litros")
label_instrucciones_litros.pack()

entry_litros = tk.Entry(ventana)
entry_litros.pack()

label_instrucciones_mililitros = tk.Label(ventana, text="Ingrese el volumen de mililitros")
label_instrucciones_mililitros.pack()

entry_mililitros = tk.Entry(ventana)
entry_mililitros.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_volumen)
boton_convertir.pack()

label_resultado_galones = tk.Label(ventana, text="")
label_resultado_galones.pack()

label_resultado_onzas = tk.Label(ventana, text="")
label_resultado_onzas.pack()


ventana.mainloop()